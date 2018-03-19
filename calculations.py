import requests
import json

from handlers import *
from utils import *

TEAM = 2521
TEAM = "frc" + str(TEAM)

def average_teleop_ownership(team_key, structure):
    matches = match_request_handler(team_key)
    structure = structure.title()
    total = []
    for match in matches:
        if match_exists(matches,match["key"],team_key):
            # print(match["score_breakdown"][alliance_color(match["key"])]["teleopSwitchOwnershipSec"])
            try:
                total.append(match["score_breakdown"][alliance_color(matches,match["key"],team_key)]["teleop{}OwnershipSec".format(structure)])
            except KeyError:
                print("That's not a valid game structure!")
                break
    return round(sum(total)/len(total),2)
    
    
    
    
    
if __name__ == "__main__":    
    print(average_teleop_ownership(TEAM, "scale"))
    