from main import *

event_request = requests.get("http://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple".format(event_key="2018orwil"), params=authkey)

event = event_request.json()

for team in event:
    print(team["nickname"] + " : " + str(team["team_number"]))
    