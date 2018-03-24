from handlers import *
from utils import *

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