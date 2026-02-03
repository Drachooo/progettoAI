from envs.obsgrid_env import ObsGrid


class AquaticEnv(ObsGrid):

    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        #(O) Open Water: Normal movement; no additional challenges.  
        #(C) Currents: Areas where the drone's movement is influenced by ocean currents, potentially pushing it off course.  
        #(F) Seaweed Forests: Dense vegetation that slows the drone, incurring extra energy costs per move.    
        #(R) Rocky Areas: Impassable zones the drone must navigate around.  
        #(E) Energy Stations: Specific points where the drone can recharge its battery, adding a small reward to encourage efficient navigation.

        grid = [
            ['S', 'O', 'O', 'F', 'F', 'F', 'F', 'O', 'O', 'O'],
            ['O', 'F', 'C', 'C', 'C', 'O', 'F', 'E', 'F', 'O'],
            ['O', 'O', 'F', 'F', 'F', 'O', 'F', 'F', 'F', 'C'],
            ['F', 'C', 'F', 'F', 'E', 'C', 'F', 'O', 'F', 'C'],
            ['F', 'C', 'F', 'F', 'F', 'C', 'F', 'O', 'F', 'C'],
            ['F', 'E', 'F', 'O', 'O', 'O', 'F', 'E', 'F', 'C'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'F', 'F', 'F', 'C'],
            ['O', 'F', 'F', 'F', 'O', 'O', 'O', 'F', 'F', 'C'],
            ['O', 'O', 'O', 'O', 'F', 'F', 'F', 'F', 'F', 'C'],
            ['F', 'F', 'F', 'O', 'O', 'O', 'O', 'G', 'O', 'F']
        ]

        rewards = {"S": -0.04, "O": -0.04, "F": -0.2, "C": -0.04, "E": 1.0,  "G": 20.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)

