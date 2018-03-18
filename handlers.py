import requests

base_url = "http://www.thebluealliance.com/api/v3/"
authkey = {"X-TBA-Auth-Key" : "KuyisSfG5mADtkhd2h0ebKbiCtE40vqwN5fX6voJq8i4IYr9STai3PpqLHT1z3kR"}

def match_request_handler(team):
    return requests.get("http://www.thebluealliance.com/api/v3/team/{team_key}/matches/2018".format(team_key=team), params = authkey).json()

def event_request_handler(event):
    return requests.get("http://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple".format(event_key=event), params=authkey).json()

    