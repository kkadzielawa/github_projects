from world import *
from robots import *

def print_board(w):
    print "-" * 60
    for y in range(19,-1,-1):
        line = ""
        for x in range(0,20):
            r = w.test_position(x, y)
            if r == None:
                line += ".... "
            else:
                if isinstance(r, AttackRobot):
                    rtype = "A"
                elif isinstance(r, MedicRobot):
                    rtype = "M"
                else:
                    rtype = "!"
                if r.get_team() == 1:
                    line += "%s%02i%s " % (rtype, r.get_health(), r.get_direction())
                else:
                    line += "%s%02i%s " % (rtype.lower(), r.get_health(), r.get_direction())
        print line
    print "-" * 60
