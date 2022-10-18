#Developer: Ashish Gavshinde
#Database: MongoDB
#FrameWork: FastAPI
#Upwork Profile: Link
#Hourly Rate:
#Daily Possible Working Hours: 9 hrs
#Timezone[Country]: IST[India]

from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user)