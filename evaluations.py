from calculations import *
from handlers import *

# 2018orwil 2018orlak
EVENT = "2018orwil"

event = event_request_handler(EVENT)

for team in event:
    print(team["nickname"] + " : " + str(team["team_number"]))
    