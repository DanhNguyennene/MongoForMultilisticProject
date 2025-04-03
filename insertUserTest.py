from faker import Faker
import random
from bson import ObjectId

fake = Faker()

def generate_user():
    user = {
        "userId": str(ObjectId()),
        "username": fake.user_name(),
        "email": fake.email(),
        "role": random.choice(["admin", "user", "guest"]),
        "faceID": fake.sha256(),
        "password": fake.password(),
        "authorizedDevices": [fake.uuid4() for _ in range(random.randint(1, 3))],
        "createdAt": fake.date_this_decade()  
    }
    return user

users = [generate_user() for _ in range(50)]

for user in users:
    print(user)
