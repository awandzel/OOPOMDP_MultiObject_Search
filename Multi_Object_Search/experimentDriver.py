'''
    Created by awandzel on 10/29/18.
'''

import random
import copy
import click  # Command Line Interface Creation Kit
import Multi_Object_Search.Core.Environment as envMap
import Multi_Object_Search.Core.RRT as RRT
import Multi_Object_Search.Core.mapUtilities as Util
import Multi_Object_Search.OOPOMCP.belief as Belief
import Multi_Object_Search.Core.LanguageCommand as LanguageCommand

@click.command()
@click.option('--exp', required=True, type=str, help='Name of experiment')
@click.option('--mem', required=True, type=str, help='Class-object membership (e.g. \'1,2,1\' 3 classes of 1,2,1 objects)')
@click.option('--cmd', required=True, type=str, help='Language command e.g. "Please find the mugs in the kitchen and books in the library or kitchen"')
@click.option('--sam', required=True, type=int, help='Number of Monte-Carlo samples')
@click.option('--act', required=True, type=int, help='Max number of actions')
@click.option('--map', required=True, type=str, help='Name of map')
@click.option('--obs', required=True, type=float, help='Accuracy of observation model')
@click.option('--sdv', required=True, type=float, help='Standard deviation of event A in observation model')
@click.option('--dep', required=True, type=int, help='Vision cone depth')
@click.option('--adv', required=True, type=bool, help='Adversarial command')
@click.option('--psi', required=True, type=float, help='Psi language error')
@click.option('--itr', required=True, type=int, help='Number of experiment iterations')

#Example: experimentDriver.py --exp=test --mem=2 --mem2=0 --sam=10000 --act=10 --map=arthur --obs=1.0 --sdv=.0001 --dep=2 --adv=False --psi=0 --itr=1

def experimentDriver(exp, mem, cmd, sam, act, map, obs, sdv, dep, adv, psi, itr):
    fileName = exp + "__" + "Mo-" + mem + "_Mc-" + cmd + "_S-" + str(sam) + "_A-" + str(act) \
               + "_M-" + map + "_Oa-" + str(obs) + "_Os-" + str(sdv) + "_D-" + str(dep) + "_Ad-" + str(adv) \
               + "_P-" + str(psi) + ".txt";
    #omit itr for aggregating over iterations
    print(fileName)

    # //////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////// PARAMETERS ////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////

    #POMCP parameters
    pomcpHeight = 25
    pomcpReinvigorate = True
    pomcpReinvigorateSamples = 1000
    pomcpExploration = 999
    pomcpDiscount = .95

    #POMDP parameters
    objectReward = 1000
    actionReward = -10

    #Observation model parameters (V in visionCone / NV not in visionCone
    betaV = (1.0 - obs) / 2.0
    gammaV = (1.0 - obs) / 2.0
    alphaV = obs
    betaNV = (1.0 - obs) / 2.0
    gammaNV = obs
    alphaNV = (1.0 - obs) / 2.0

    #-----------Program------------
    #set true if manually specifying goal location via map
    manualMapSpecification = True
    ROBOTEXPERIMENT = False

    #-----------RRT------------
    numberOfSecondsForRRTSamples = 0

    #-----------Debug----------
    debugPrintOuts = 4 #{0:none, 1:env steps, 2:belief, 3:RRT, 4:other}
    issuePomdpVisualizer = True

    #sets random seed constant for goal placement & RRT nodes.
    preprocessingConsistency = True

    #sets random seed constant for POMDP algorithm (sampling / action selection)
    algorithmConsistency = True

    #No uncertianity POMCP for checking if agent can reach goals with RRT nodes
    issueNoUncertainityPOMCP = False;

    # //////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////// EXPERIMENT ////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////////////////
    #//----------------------------Set Randomness------------------------------------
    POMCPRn = random.Random(0) if algorithmConsistency else random.Random()
    observationRn = random.Random(0) if algorithmConsistency else random.Random()
    beliefRn = random.Random(0) if algorithmConsistency else random.Random()

    objectRn = random.Random(0) if preprocessingConsistency else random.Random()
    languageRn = random.Random(0) if preprocessingConsistency else random.Random()
    RRTRn = random.Random(0) if preprocessingConsistency else random.Random()

    # //----------------------------Set Maps & Rooms-----------------------------
    Maps = envMap.selectMap(map)

    Rooms = envMap.roomsInMap()
    Rooms.setTransitionMatrix(Maps)
    Rooms.setAdjacencyMatrix(Maps)
    Rooms.setMappings(Maps)

    if debugPrintOuts > 3:
        Maps.debugPrint()
        Rooms.debugPrint()

    #start in center
    startState = Rooms.transitionMatrix[Rooms.numberOfRooms] #8,13 ROBOT EXPERIMENT

    # //----------------------------Parse Classes------------------------------------
    objectClasses = [int(s) for s in mem.split(",")]
    numberOfObjects = sum(objectClasses)

    #TODO: reobotexperiment should be uniform for language
    #TODO: python map starts at 0 for object/rooms

    #//////////////////////////////RRT///////////////////////////////////
    #//
    #//////////////////////////////RRT///////////////////////////////////
    rrtGraph = RRT.RRT(Maps, RRTRn)
    utilities = Util.mapUtilities(Maps)
    for i in range(Rooms.numberOfRooms):

        locationsInRoom = []
        #extra careful with move locations for live robot experiments
        if ROBOTEXPERIMENT:
            for l in Rooms.roomToLocationsMapping[i]:
                if not utilities.isConflictInCardinalDirections(l):
                    locationsInRoom.append(l)
        else:
            locationsInRoom = Rooms.roomToLocationsMapping[i]

        centerOfRoom = Rooms.transitionMatrix[i]
        rrtGraph.buildGraph(centerOfRoom, locationsInRoom, dep, numberOfSecondsForRRTSamples)

    if debugPrintOuts > 2:
        rrtGraph.debugPrint()

    #//////////////////////////////EXPERIMENT DRIVER///////////////////////////////////
    #//
    #//////////////////////////////EXPERIMENT DRIVER///////////////////////////////////
    for e in range(itr):
        print("\n===============================================\n" +
              "-----------------Experiment:" + str(e) + "------------------" +
              "\n===============================================\n")

        # //////////////////////////////LANGUAGE COMMAND///////////////////////////////////
        # //
        # //////////////////////////////LANGUAGE COMMAND///////////////////////////////////
        belief = Belief.belief(Maps, numberOfObjects, beliefRn)
        beliefPrior = belief.makeUniformBelief()

        belief.debugPrint(beliefPrior)

        languageCommand = LanguageCommand.LanguageCommand(Rooms, objectClasses)
        languageCommand.parseLanguageCommand(cmd, languageRn)
        languageCommand.translateToObservation(psi)

        belief.b = languageCommand.beliefUpdate(beliefPrior)
        #Adversarial: object distribution is anti-belief
        if adv:
            languageCommand.translateToObservation(1.0 - psi)
            belief.objectDistribution = languageCommand.beliefUpdate(beliefPrior)
        else:
            belief.objectDistribution = copy.deepcopy(belief.b)

        if debugPrintOuts > 1:
            print("\n////////////////////////////////////////////////////////" +
                  "\n////////////////////BeliefDistribution////////////////////" +
                  "\n////////////////////////////////////////////////////////")
            belief.debugPrint(belief.b)
            print("\n//////////////////////////////////////////////////////////" +
                  "\n////////////////////ObjectDistribution////////////////////" +
                  "\n////////////////////////////////////////////////////////")
            belief.debugPrint(belief.objectDistribution)














if __name__ == '__main__':
    experimentDriver()



