import random

left_dict = {"N":"W", "W":"S", "S":"E", "E":"N"}
right_dict= {"W":"N", "S":"W", "E":"S", "N":"E"}
rotate_dict= {"N":"S", "S":"N", "W":"E", "E":"W"}
forward_dict={"N":"N", "S":"S", "W":"W", "E":"E"}



class Robot:
    def __init__(self, team, x, y, direction):
        self.team = team
        self.health = 50
        self.x = x    
        self.y = y
        self.direction = direction

    def get_team(self):
        # return team value
		return self.team

    def get_health(self):
        # return health value
		return self.health

    def get_direction(self):
        # return direction
		return self.direction

    def left90(self):
        # use left_dict
		self.direction = left_dict[self.direction]

    def right90(self):
        # use right_dict
		self.direction = right_dict[self.direction]

    def turn180(self):
        # use turn_dict
		self.direction = rotate_dict[self.direction]

    def board_position_in_direction(self, direction=None):
        # by default, use the direction of this robot
        # return the next position (x,y) in the direction
		if direction == None:
			direction = self.direction
		x = self.x
		y = self.y
		if self.direction == "N":
			y += 1
		elif self.direction == "S":
			y -= 1
		elif self.direction == "E":
			x += 1
		elif self.direction == "W":
			x -= 1
		return x,y

    def forward(self,world,tmp):
        # use board_position_in_direction to find next position
        # if new position is out of board, rotate
        # if new position is on the board, check the following
        # if no robot is there, use world.move_robot
        # else, a robot is there, return False
        # return True
        x,y = self.board_position_in_direction()
        if x < 0 or x > 19 or y < 0 or y > 19:
            print "ROTATE"
            self.rotate()
            return True
        else:
            if world.grid[x][y] == None:
                print "MOVE", self.x, self.y, x, y
                world.move_robot(self.x, self.y, x,y)
                tmp[x][y] = 1
                self.x = x
                self.y = y
                return True
            else:
                return False

    def healthchange(self, change):
        # increase health by the amount of change
        # if health > 50, make it equal to 50

class AttackRobot(Robot):
    def __init__(self,team,x,y,direction):
        Robot.__init__(self,team,x,y,direction)

    def run_turn(self, world, tmp):
        # 1. call try_attack, try to attack enemy robot in front,
        #    if success return 0
        # 2. call try_turn, try to enemy robot on the right or left,
        #    if success, return 0
        # 3. call move, move by chance to forward, left, right
        # return 0
        if self.try_attack(world):
            return 0
        if self.try_turn(world):
            return 0

        new_direction = random.choice(["F", "F", "L", "R"])
 
        print "new_direction= ", new_direction
        if new_direction == "F":
            self.forward(world, tmp)
        elif new_direction == "L":
            self.left90()
        elif new_direction == "R":
            self.right90()
        return 0

    def move(self,world, tmp):
        # move by chance to forward, left, right
        # use random.choice(["F", "F", "L", "R"])
        # you will call left90, right90, turn180


    def try_attack(self, world):
        # attack front enemy robot
        # call board_position_in_direction to get the front position
        # check if there is a robot and robot is an enemy robot
        # then attack, and check if this robot is alive
        # if not alive call world.kill_robot to remove it
        # return True, if attack happens
        # return False
        x, y = self.board_position_in_direction()

        if x >= 0 and x <= 19 and y >= 0 and y <= 19:
            robot = world.test_position(x,y)
            
            if (robot != None) and (self.get_team() != robot.get_team()):
                print "attack"
                self.attack(robot)
                
                if robot.get_health() <= 0:
                    world.kill_robot(x,y)
                    
                return True
            
        #no attack happened
        return False

    def try_turn(self,world):
        # try right
        # use right_dict to get direction on the right
        # use board_position_indirection to get right position
        # if there is a robot and it is an enemy robot,
        # turn right, return True
        # try left, the same as try right, return True if success
        # return False by default

    def attack(self, robot):
        # generate a random damage by random.randrange(1,7)
		damage = random.randrange(1,7)
        # robot's health will decrease by amount
        robot.health -= damage
        
class MedicRobot(Robot):
    def __init__(self,team,x,y,direction,filename):
        Robot.__init__(self,team,x,y,direction)
        
		with open(filename, 'r') as f:
            self.L = []
            for line in f:
                self.L.append(line.strip())
        self.nextmovement = 0
        
        # record number of commands
        self.n_commands = len(self.commands)
        # record current index of commands
        self.command_ind = 0

        # use a variable to store if any forward movement is pending
        self.forward_done = True

    def next_command(self):
        # read next command from self.commands
        # increase current index of commands by 1
        # if index == number of commands, make it 0,
        # back to beginning
        # return command

    def run_turn(self, world, tmp):
	
	
        for direction_dict in [right_dict, forward_dict, left_dict]:
           x,y = self.board_position_in_direction(direction_dict[self.direction])
           if x >= 0 and x <= 19 and y >= 0 and y <= 19:
               robot = world.test_position(x,y)
               if (robot != None) and (self.get_team() == robot.get_team()):
                   heal = random.randrange(0,4)
                   robot.health += heal
                   if robot.health > 50:
                       robot.health = 50
        if self.L[self.nextmovement] == "Forward":
            self.forward(world, tmp)
        if self.L[self.nextmovement] == "Left90":
            self.left90()
        if self.L[self.nextmovement] == "Right90":
            self.right90()
        if self.L[self.nextmovement] == "Turn180":
            self.left90()
            self.left90()
        self.nextmovement = (self.nextmovement + 1) % len(self.L)  

    def move(self,world,tmp):
        # check forward_done to see if any forward movement is pending
        # if yes, try to move forward
        # else call next_command and finish the move
        # make sure to update the status of forward_done
        # self.forward_done = self.forward(world,tmp)


    def heal(self,world):
        # use right_dict, left_dict to find the direction
        # use board_position_in_direction to find the poistion
        # if there is a team robot in right center or left,
        # heal it by random.randrange(0,4)
        # call healthchange   
		
if __name__ == "__main__":
    r= Robot(1, 2, 3, "N")
    r2 = AttackRobot(2,2,4,"N")
    print r.get_health()
    r2.attack(r)
    print r.get_team()
    print r.get_health()
    print r.get_direction()
    print_board(world)
