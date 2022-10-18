#Developer: Ashish Gavshinde
#Database: MongoDB
#FrameWork: FastAPI
#Upwork Profile: Link
#Hourly Rate:
#Daily Possible Working Hours: 9 hrs
#Timezone[Country]: IST[India]

import datetime
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.db import conn
from models.user import Users
from schemas.user import usersEntity, eventsEntity, feedsEntity, eventInvitationsEntity, advertismentsEntity

user = APIRouter()

users = usersEntity(conn.TeamUp["Users"].find())
events = eventsEntity(conn.TeamUp["Events"].find())
feeds = feedsEntity(conn.TeamUp["Feeds"].find())
event_invitation = eventInvitationsEntity(conn.TeamUp["EventInvitations"].find())

#get all urser with there IDs
@user.get('/users')
async def all_users():
    return users

#get possible events for the specific user by ID
@user.get('/possible_events/{id}')
async def possible_events(id):
    upcoming_event = []
    liked_event = []
    played_event = []
    unplayed_event = []
    events_data = []
    now = datetime.date.today()
    today = f'{now}T00:00:00.000+00:00'

    for user_check in users:
        if(user_check["id"] == id):
            logged_in_user = user_check
    
    #check possible new events 
    for z in events:
        if(str(z["date_of_event"]) > today ):
            upcoming_event.append(z)
    
    #check past liked events
    for z in events:
        for y in feeds:
            if((y["user_id"] == logged_in_user["id"]) and (str(z["date_of_event"]) < today)):
                liked_event.append(y["event_id"])
    
    #check played or unplayed events of login user
    for x in event_invitation:
        if(x["invited_by"] == logged_in_user["id"] or x["invited_user"] == logged_in_user["id"]):
            if(x["status"] == "played"):
                played_event.append(x["event_id"])
            if(x["status"] == "unplayed"):
                unplayed_event.append(x["event_id"])

    for i in upcoming_event:
        if((logged_in_user["location"]["address"] == i["location"]["address"]) and ((i["id"] in liked_event) or (i["id"] in played_event) or (i["id"] in unplayed_event))):
            time_of_event = str(i["time_of_event"]).split(" ")[1].split(".")[0]
            events_data.append(
                {
                    "title":i["title"],
                    "game_name":i["game_name"],
                    "date_of_event":str(i["date_of_event"]).split(" ")[0],
                    "time_of_event":time_of_event
                })
    return events_data