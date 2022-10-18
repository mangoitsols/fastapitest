#Developer: Ashish Gavshinde
#Database: MongoDB
#FrameWork: FastAPI
#Upwork Profile: Link
#Hourly Rate:
#Daily Possible Working Hours: 9 hrs
#Timezone[Country]: IST[India]

from tokenize import Double
from pydantic import BaseModel

#Users Table Model
class Users(BaseModel):
    user_name: str
    email: str
    password: str
    profile: str
    Boi: str
    location: dict
    isvisble_other: str
    achivements: str
    phone_number: str

#Events Table Model
class Events(BaseModel):
    title: str
    image: str
    description: str
    location: dict
    date_of_event: str
    create_by: str
    game_name: str
    number_of_player: int
    time_of_event: str

#Feeds Table Model
class Feeds(BaseModel):
    event_id: str
    is_like: bool
    comments: list
    share_with: list
    user_id: str
    ads_id: str

#EventInvitations Table Model
class EventInvitations(BaseModel):
    invited_user: str
    invited_by: str
    event_id: str
    status: str
    achiver_id: str

#Advertisments Table Model
class Advertisments(BaseModel):
    poster: str
    created_by: str
    title: str