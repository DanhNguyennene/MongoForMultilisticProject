from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')  # Change URI if needed

database = input("your database: ")
collection = input("your collection: ")
db = client[f'{database}']  # Replace 'yourDatabase' with your database name

collection = db[f'{collection}']  # Replace 'users' with your collection name

# Get a sample of documents to infer the schema
documents = collection.find().limit(5)  # Get the first 5 documents

# Function to get the schema from the sample documents
def print_schema(documents):
    schema = {}
    for doc in documents:
        for key, value in doc.items():
            if key not in schema:
                schema[key] = type(value).__name__  # Store the type of the field
    return schema

# Print the schema
schema = print_schema(documents)
print("Schema Skeleton:")
for field, field_type in schema.items():
    print(f"{field}: {field_type}")

# Close the connection
client.close()

