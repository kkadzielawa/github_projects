from robots import *
from test import print_board

class World:
    def __init__(self):
        # initialize a grid of 20 by 20.
        # grid is a double list
        # all elements on the grid are none
        self.grid= []
        self.maxX = 20
        self.maxY = 20
        self.numRobots = {1:0,2:0}
        
        for irow in range(self.maxY):
            row=[]
            for icol in range(self.maxX):
                row.append(None)
            self.grid.append(row)

    def test_position(self,x,y):
        # return none if (x,y) is out of the board
        # return element at (x,y) on the grid
		return self.grid[x][y]

    def add_attack_robot(self, team, x, y, direction):
        # initialize an attack robot, 
        # and put it at (x,y) on the grid
		self.grid[x][y] = AttackRobot(team, x, y, direction)
        self.numRobots[team] += 1
 
    def add_medic_robot(self, team, x, y, direction, filename):
        # initialize an medic robot, 
        # and put it at (x,y) on the grid
		self.grid[x][y] = MedicRobot(team, x, y, direction, filename)
        self.numRobots[team] +=1


    def move_robot(self,oldx, oldy, newx, newy):
        # move robot from (oldx,oldy) to (newx,newy)
        # make (oldx,oldy) None
		self.grid[newx][newy] = self.grid[oldx][oldy]
        self.grid[oldx][oldy] = None

    def run_turn(self):
        # make every robots to move on the board
        # Trick is make sure if a robot has been 
        # moved into your new location, you don't
        # move this robot any more.

        # you can use tmp array to record
        # tmp = [[0 for i in range(self.maxX)] for j in range(self.maxY)]
		tmp= [[0 for i in range(self.maxX)] for j in range(self.maxY)]
        for i in range(self.maxY):
            for j in range(self.maxX):
                if tmp[i][j]==0 and self.grid[i][j] != None:
                    self.grid[i][j].run_turn(self,tmp)


    def kill_robot(self,x,y):
        # set (x,y) on grid None
		robot = self.grid[x][y]
        self.grid[x][y] = None
        self.numRobots[robot.team] -= 1

    def game_over(self):
        # initialize two counters
        # count how many members of team 1 and team 2
        # if counter of team 1 is 0, return 2
        # if counter of team 2 is 0, return 1
        # else return None
        if self.numRobots[1] == 0:
            if self.numRobots[2] > 0:
                return 2
        if self.numRobots[2] == 0:
            if self.numRobots[1] > 0:
                return 1
        return None

if __name__ == "__main__":
    from test import print_board
    import os
    import time
    world = World()
    world.add_attack_robot(1, 2, 3, "N")
    world.add_attack_robot(2,2,4,"S")
    world.add_medic_robot(2,2,5,"N", "C:\Users\Conrad\Desktop\MCS 260 Projects\mcs260\project2\Move_Medic.txt")
    
    os.system("CLEAR")
    print_board(world)
    
    for i in range(100):
        world.run_turn()
        
        time.sleep(.2)
        print_board(world)		

		