from functions import *

TEAM = 2521
TEAM = "frc" + str(TEAM)

# 2018orwil 2018orlak
EVENT = "2018orlak"
    
if __name__ == "__main__":    
    print(average_teleop_ownership(TEAM, "scale", True))
    for key, value in average_teleop_ownership_eventleaderboard(EVENT, "scale"):
        print("{team} : {time}s".format(team=key,time=value))
    print("=====================================================================")
    for key, value in average_teleop_ownership_eventleaderboard(EVENT, "switch"):
        print("{team} : {time}s".format(team=key,time=value))