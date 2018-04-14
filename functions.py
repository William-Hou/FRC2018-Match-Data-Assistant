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
def average_teleop_ownership_eventleaderboard(event, structure, byname=False):
    event = event_request_handler(event)
    leaderboard = {}
    if not byname:
        for team in event:
            leaderboard[team["nickname"]] = average_teleop_ownership("frc" + str(team["team_number"]), structure, True)
        leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    else:
        for team in event:
            leaderboard[team["team_number"]] = average_teleop_ownership("frc" + str(team["team_number"]), structure, True)
            leaderboard = OrderedDict(sorted(leaderboard.items()))
    return leaderboard

# How often a team's robot climbs
def average_climb(team_key):
    matches = match_request_handler(team_key)
    climb_statuses = []
    for match in matches:
        robot_position = match["alliances"][alliance_color(matches,match["key"],team_key)]["team_keys"].index(team_key) + 1
        climb_statuses.append(match["score_breakdown"][alliance_color(matches,match["key"],team_key)]["endgameRobot{}".format(robot_position)])
    return round(climb_statuses.count("Climbing")/len(climb_statuses) * 100, 2)

# Returns the climb percentage of all the robots at an event
def get_event_climbs(event):
    team_climbs = {}
    events = event_request_handler(event)
    for team in events:
        team_climbs[team["team_number"]] = average_climb(team["key"])
    return OrderedDict(sorted(team_climbs.items()))