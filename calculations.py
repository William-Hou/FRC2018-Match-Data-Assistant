import requests
import json

from handlers import *

TEAM = 2521
team_key = "frc" + str(TEAM)

matches = match_request_handler(team_key)

def alliance_color(matchkey, team=team_key):
    for match in matches:
        if match["key"] == matchkey:
            if team_key in match["alliances"]["blue"]["team_keys"]:
                return "blue"
            elif team_key in match["alliances"]["red"]["team_keys"]:
                return "red"

def match_exists(matchkey):
    for match in matches:
        if match["key"] == matchkey:
            if match["score_breakdown"] is None:
                return False
    return True
                
def average_teleop_scale_ownership():
    total = []
    for match in matches:
        if match_exists(match["key"]):
            # print(match["score_breakdown"][alliance_color(match["key"])]["teleopSwitchOwnershipSec"])
            total.append(match["score_breakdown"][alliance_color(match["key"])]["teleopScaleOwnershipSec"])
    return sum(total)/len(total)
    
    
if __name__ == "__main__":    
    print(average_teleop_scale_ownership())
    