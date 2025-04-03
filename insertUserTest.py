from pymongo import MongoClient
from faker import Faker
import random
from bson import ObjectId

fake = Faker()

client = MongoClient('mongodb://localhost:27017')
db = client['yourDatabase']  
users_collection = db['users']  

def generate_user():
    user = {
        "userId": str(ObjectId()),  
        "username": fake.user_name(),
        "email": fake.email(),
        "role": random.choice(["admin", "user", "guest"]),
        "faceID": fake.sha256()
        "password": fake.password(),
        "authorizedDevices": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "createdAt": fake.date_this_decade()
    }
    return user

users = [generate_user() for _ in range(50)]

users_collection.insert_many(users)

print("50 users have been inserted into MongoDB.")
