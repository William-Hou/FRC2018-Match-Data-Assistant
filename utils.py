
def alliance_color(matches, matchkey, team_key):
    for match in matches:
        if match["key"] == matchkey:
            if team_key in match["alliances"]["blue"]["team_keys"]:
                return "blue"
            elif team_key in match["alliances"]["red"]["team_keys"]:
                return "red"

def match_exists(matches, matchkey, team_key):
    for match in matches:
        if match["key"] == matchkey:
            if match["score_breakdown"] is None:
                return False
    return True
                