'''
    Created by awandzel on 03/04/18.
'''
import Multi_Object_Search.Pomdp.Domain.ParameterizedActions as Action
import Multi_Object_Search.Pomdp.Domain.FactoredModel as FactoredModel
import Multi_Object_Search.Pomdp.Domain.StaticConstants as Constants
import Multi_Object_Search.Pomdp.ObservationFunction.FanShapedSensor as FanShapedSensor

class SearchDomain:
    #Domain general data members
    ActionTypes = [] #list of parameterized actions
    FactoredModel = None
    ObservationModel = None

    def __init__(self, util, PomdpParameters, ObservationModelParameters, observationRn):
        self.util = util
        self.PomdpParameters = PomdpParameters
        self.ObservationModelParameters = ObservationModelParameters
        self.observationRn = observationRn

    def generateDomain(self):
        #Add action types for enumeration
        self.ActionTypes.append(Action.MoveRoom(self.util, Constants.ACTION_MOVE_ROOM))
        self.ActionTypes.append(Action.Move(self.util, Constants.ACTION_MOVE))
        self.ActionTypes.append(Action.Look(self.util, Constants.ACTION_LOOK))
        self.ActionTypes.append(Action.Find(self.util, Constants.ACTION_FIND))

        self.FactoredModel = FactoredModel.FactoredModel(self.util, self.PomdpParameters)
        self.ObservationModel = FanShapedSensor.FanShapedSensor(self.util, self.ObservationModelParameters, self.observationRn)


    def applicableActions(self, s):
        applicableActions = []
        for action in self.ActionTypes:
            applicableActions += action.applicableActions(s)
        return applicableActions

    def selectRandomAction(self, state, random):
        applicableActions = self.applicableActions(state)
        return random.choice(applicableActions)







