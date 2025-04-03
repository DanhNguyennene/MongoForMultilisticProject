from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

client = MongoClient('mongodb://localhost:27017/')
db = client['aiot_database']  # Database name

user_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["userId", "username","email","role", "faceID", "password", "createdAt"],
        "properties": {
            "userId": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "gender": {
                "bsonType": "string",
                "description": "must be a string and is not required"
            },
            "username": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "email": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "role": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "faceID": {
                "bsonType": "string",
                "description": "must be a string (hash or encoded) and is required"
            },
            "password": {
                "bsonType": "string",
                "description": "must be a string (hash or profile data) and is required"
            },
            "authorizedDevices": {
                "bsonType": "array",
                "items": {"bsonType": "string"},
                "description": "must be an array of device IDs (strings)"
            },
            "createdAt": {
                "bsonType": "date",
                "description": "must be a date and is required"
            }
        }
    }
}

try:
    db.create_collection('user', validator=user_schema)
    print("Users collection created with schema validation.")
except CollectionInvalid:
    print("Users collection already exists with schema validation.")
