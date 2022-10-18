#Developer: Ashish Gavshinde
#Database: MongoDB
#FrameWork: FastAPI
#Upwork Profile: Link
#Hourly Rate:
#Daily Possible Working Hours: 9 hrs
#Timezone[Country]: IST[India]

#User Data
def userEntity(userItem) -> dict:
    return{
        "id":str(userItem["_id"]),
        "user_name":userItem["user_name"],
        "email":userItem["email"],
        "password":userItem["password"],
        "profile":userItem["profile"],
        "Boi":userItem["Boi"],
        "location":{
            "longitude":userItem["location"]["longitude"],
            "latitude":userItem["location"]["latitude"],
            "address":userItem["location"]["address"]
        },
        "isvisble_other":userItem["isvisble_other"],
        "achivements":userItem["achivements"],
        "phone_number":userItem["phone_number"]
    }

def usersEntity(entity) -> list:
    return [userEntity(userItem) for userItem in entity]

#Event Data
def eventEntity(eventItem) -> dict:
    return{
        "id":str(eventItem["_id"]),
        "title":eventItem["title"],
        "image":eventItem["image"],
        "description":eventItem["description"],
        "location":{
            "longitude":eventItem["location"]["longitude"],
            "latitude":eventItem["location"]["latitude"],
            "address":eventItem["location"]["address"]
        },
        "date_of_event":eventItem["date_of_event"],
        "create_by":str(eventItem["create_by"]),
        "game_name":eventItem["game_name"],
        "number_of_player":eventItem["number_of_player"],
        "time_of_event":eventItem["time_of_event"]
    }

def eventsEntity(entity) -> list:
    return [eventEntity(eventItem) for eventItem in entity]

#Feeds Data
def feedEntity(feedItem) -> dict:
    return{
        "id":str(feedItem["_id"]),
        "event_id":str(feedItem["event_id"]),
        "is_like":bool(feedItem["is_like"]),
        "comments":list(feedItem["comments"]),
        "share_with":str(feedItem["share_with"]),
        "user_id":str(feedItem["user_id"]),
        "ads_id":str(feedItem["ads_id"]),
    }

def feedsEntity(entity) -> list:
    return [feedEntity(feedItem) for feedItem in entity]

#EventInvitations Data
def eventInvitationEntity(eventInvitationItem) -> dict:
    return{
        "id":str(eventInvitationItem["_id"]),
        "invited_user":str(eventInvitationItem["invited_user"]),
        "invited_by":str(eventInvitationItem["invited_by"]),
        "event_id":str(eventInvitationItem["event_id"]),
        "status":str(eventInvitationItem["status"]),
        "achiver_id":str(eventInvitationItem["achiver_id"]),
    }

def eventInvitationsEntity(entity) -> list:
    return [eventInvitationEntity(eventInvitationItem) for eventInvitationItem in entity]


#Advertisments Data
def advertismentEntity(advertismentItem) -> dict:
    return{
        "id":str(advertismentItem["_id"]),
        "poster":str(advertismentItem["poster"]),
        "created_by":str(advertismentItem["created_by"]),
        "title":str(advertismentItem["title"]),
    }

def advertismentsEntity(entity) -> list:
    return [advertismentEntity(advertismentItem) for advertismentItem in entity]