from functions import *

TEAM = 5450
TEAM = "frc" + str(TEAM)

# 2018orwil 2018orlak
EVENT = "2018orlak"
    
if __name__ == "__main__":   
    
    print("SERT")
    print("Scale:  ",average_teleop_ownership("frc2521", "scale", True))
    print("Switch:  ",average_teleop_ownership("frc2521", "switch", True))
    print("==============================================")
    print(TEAM)
    print("Scale:  ",average_teleop_ownership(TEAM, "scale", True))
    print("Switch:  ",average_teleop_ownership(TEAM, "switch", True))




    # for key, value in average_teleop_ownership_eventleaderboard(EVENT, "scale"):
    #     print("{team} : {time}s".format(team=key,time=value))
    # print("=====================================================================")
    # for key, value in average_teleop_ownership_eventleaderboard(EVENT, "switch"):
    #     print("{team} : {time}s".format(team=key,time=value))