from functions import *
from handlers import *



event = event_request_handler(EVENT)

# Average scale ownership for robot's alliance
for team in event:
    leaderboard = {}
    leaderboard = [team["nickname"]] = str(average_teleop_ownership("frc" + str(team["team_number"]), "scale", True)) + "s"
    # print(team["nickname"] + " : " + str(average_teleop_ownership("frc" + str(team["team_number"]), "scale", True)) + "s")
    # print((team["nickname"],str(average_teleop_scale_ownership("frc" + str(team["team_number"])))))
    
    