from functions import *

TEAM = 2521
TEAM = "frc" + str(TEAM)

# 2018orwil 2018orlak
EVENT = "2018roe"
    


print("SERT")
print("Scale:  ",average_teleop_ownership("frc2521", "scale", True))
print("Switch:  ",average_teleop_ownership("frc2521", "switch", True))
print("==============================================")
# print(TEAM)
# print("Scale:  ",average_teleop_ownership(TEAM, "scale", True))
# print("Switch:  ",average_teleop_ownership(TEAM, "switch", True))
# print("==============================================")
# print("Event Leaderboard")
# for team, time in average_teleop_ownership_eventleaderboard(EVENT, "scale", byname=False):
#     print("{} : {}s".format(team, time))
# print("By Name")
# for team, time in average_teleop_ownership_eventleaderboard(EVENT, "scale", byname=True).items():
#     print("{} : {}s".format(team, time))
for team, climb_percent in get_event_climbs(EVENT).items():
    print("{} : {}".format(team, climb_percent))

