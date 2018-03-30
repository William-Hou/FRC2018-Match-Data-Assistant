from collections import OrderedDict
from handlers import *
from utils import *

# Average scale/switch ownership for robot's alliance
def average_teleop_ownership(team_key, structure, exclude_playoffs):
    matches = match_request_handler(team_key)
    structure = structure.title()
    total = []
    for match in matches:
        try:
            if exclude_playoffs and match_exists(matches,match["key"],team_key) and 'qm' in match["key"]:
                    total.append(match["score_breakdown"][alliance_color(matches,match["key"],team_key)]["teleop{}OwnershipSec".format(structure)])
            elif not exclude_playoffs and match_exists(matches, match["key"], team_key):
                    total.append(match["score_breakdown"][alliance_color(matches,match["key"],team_key)]["teleop{}OwnershipSec".format(structure)])
        except KeyError:
                    print("That's not a valid game structure!")
                    quit()
    return round(sum(total)/len(total),2)
    
# Average scale/switch ownership for all the teams at an event
def average_teleop_ownership_eventleaderboard(event, structure):
    event = event_request_handler(event)
    leaderboard = {}
    for team in event:
        leaderboard[team["nickname"]] = average_teleop_ownership("frc" + str(team["team_number"]), structure, True)
    leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return leaderboard
    
    

