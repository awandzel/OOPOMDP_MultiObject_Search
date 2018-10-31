import numpy as np

#Environment Constants
E = -1 #empty
W = -2 #wall
X = -3 #room center
Y = -4 #map center
U = -5 #uncertain

class environmentMaps():
    def __init__(self, occupancy, semantic):
        self.occupancyMap = occupancy
        self.semanticMap = semantic
        self.beliefMap = np.zeros([len(occupancy), len(occupancy[0])])

def printMap(map):
    print(np.matrix(map))

def printMaps(maps):
    print("\nOccupancy Map: \n", np.matrix(maps.occupancyMap))
    print("\nSemantic Map: \n", np.matrix(maps.semanticMap))
    print("\nBelief Map: \n", np.matrix(maps.beliefMap))

def selectMap(mapRef):
    if mapRef == "small":
        return environmentMaps(smallOccupancy, smallSemantic)

smallOccupancy = [
          [E, E, 1, E, E, E, E, E, E, E, E],
          [0, X, E, E, E, E, E, E, E, X, E],
          [E, E, E, W, W, W, W, W, E, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, Y, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, E, W, W, W, W, W, E, E, E],
          [E, X, E, E, E, E, E, E, E, X, E],
          [E, E, E, E, E, E, E, E, E, E, E],
  ]
smallSemantic = [
          [1, 1, 1, E, E, E, E, E, 2, 2, 2],
          [1, 1, 1, E, E, E, E, E, 2, 2, 2],
          [1, 1, 1, W, W, W, W, W, 2, 2, 2],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, 4, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [E, E, W, W, W, W, W, W, W, E, E],
          [0, 0, 0, W, W, W, W, W, 3, 3, 3],
          [0, 0, 0, E, E, E, E, E, 3, 3, 3],
          [0, 0, 0, E, E, E, E, E, 3, 3, 3],
  ]

'''
Original domains from paper
  public static int[][] robotDomain = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, 0, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W},
          {0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, W, W, W, 0, 0, 0, W},
          {0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, W, W, 0, 0, X, 0, W},
          {0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W},
          {0, 0, 0, W, W, W, 0, 0, Y, 0, W, W, W, 0, 0, 0, W, 0, 0, W},
          {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, W, W, W, W, W, W},
          {W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, W, W, W, W, W},
          {W, W, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };
  public static int[][] roomsInRobotDomain = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, 2, 2, 2, 2, 0, W, W, W, W, W, W, W, W, W, W, W},
          {1, 1, 1, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, W, W, W, 5, 5, 5, W},
          {1, 1, 1, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, W, W, 0, 5, 5, 5, W},
          {1, 1, 1, W, 2, 2, 2, 2, 0, 3, 3, 3, 3, W, 0, 0, 5, 5, 5, W},
          {1, 1, 1, W, W, W, 0, 0, 6, 0, W, W, W, 0, 0, W, W, 0, 0, W},
          {1, 1, 1, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, W, W, W, W, W, W},
          {W, W, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, W, W, W, W, W, W, W, W},
          {W, W, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };
  
    public static int[][] A = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, W, W, 0, 0, 0, X, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Y, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, X, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, W, W, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, W, W, 0, 0, 0, X, 0, 0, 0, W, W, 0, 0, 0, X, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, X, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };

  public static int[][] roomsInA = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W},
          {W, 8, 8, 8, 8, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, 0, 0, 4, 4, 4, 4, 4, 4, W},
          {W, 8, 8, 8, 8, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, 0, 0, 4, 4, 4, 4, 4, 4, W},
          {W, 8, 8, 8, 8, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 8, 8, 8, 8, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 0, 0, W, W, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 0, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 0, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, W, 5, 5, 5, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };

  public static int[][] B = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, X, 0, 0, 0, W, W, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 5, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, X, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, Y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, W, W, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, 0, 0, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, W, 0, 7, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, X, 0, 0, 0, W, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, W, 0, 0, 6, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, X, 0, W, 0, X, 0, 0, W, W, 0, 0, 0, 0, X, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, W, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };

  public static int[][] roomsInB = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, 1, 1, 1, 1, 1, 1, 1, W, W, 0, 0, 0, W, W, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W},
          {W, 8, 8, 8, 8, 8, 8, 8, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 3, 3, 3, 3, 3, 3, W},
          {W, 8, 8, 8, 8, 8, 8, 8, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 3, 3, 3, 3, 3, 3, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, W, W, W, W, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, 0, 0, W, W, W, W, W, W, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, 7, 7, 7, 7, 7, 7, 7, W, W, 6, 6, 6, 6, W, 5, 5, 5, 5, W, W, 4, 4, 4, 4, 4, 4, 4, 4, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };


  //2L, 2M, 3S
    public static int[][] C = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W, W, W, 0, 0, 0, X, 0, 0, W},
          {W, W, W, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W, W, W, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, X, 0, 0, 0, 0, W, 0, Y, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };


  public static int[][] roomsInC = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, 2, 2, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, W, W, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, W, W, 0, 0, W, W, W, W, W, W, W, W, W, W, W, W, 0, 0, W, W, W, W, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W, W},
          {W, W, W, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, 0, 0, 0, 0, W, W, W, W, W, W, W, W, W, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, W, W, W, W, W, W, W, W, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 9, 0, W, 4, 4, 4, 4, 4, 4, 4, 0, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, 0, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, 0, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, 8, 8, W, 0, 0, 0, W, 4, 4, 4, 4, 4, 4, 4, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, W, W, W, W, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, W, W, 0, 0, 0, W, W, W, W, 0, 0, 0, W, W, W, W, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 6, 6, 6, 6, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 6, 6, 6, 6, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 6, 6, 6, 6, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 7, 7, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };

  public static int[][] D = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, X, 0, 0, 0, 0, W, 0, 0, X, 0, 0, W, W, W, 0, 0, W, W, W, W, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, W, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, W},
          {W, W, W, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W},
          {W, W, W, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, 0, 0, W, W, W, W},
          {W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, 0, 0, W, W, W, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, X, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, W, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, X, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };


  public static int[][] roomsInD = new int[][]{
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, W, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, W, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, W, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, W, W, 0, 0, W, W, W, W, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, 4, 4, 4, 4, 4, 4, 4, W, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, 0, 4, 4, 4, 4, 4, 4, 4, W, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, 0, 4, 4, 4, 4, 4, 4, 4, W, 3, 3, 3, 3, W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, 4, 4, 4, 4, 4, 4, 4, W, 3, 3, 3, 3,W},
          {W, 1, 1, 1, 1, 1, 1, 1, 1, 1, W, 2, 2, 2, 2, 2, W, 4, 4, 4, 4, 4, 4, 4, W, 3, 3, 3, 3,W},
          {W, W, W, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W},
          {W, W, W, 0, 0, 0, 0, W, W, W, W, W, 0, 0, 0, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W},
          {W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, 0, 0, W, W, W, W},
          {W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, 0, 0, W, W, W, W, W, W, 0, 0, W, W, W, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, 8, 8, 8, 8, 8, 8, W, 7, 7, 7, 7, 7, 7, W, 6, 6, 6, 6, 6, 6, W, 5, 5, 5, 5, 5, 5, 5, W},
          {W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W},
  };
}
'''



