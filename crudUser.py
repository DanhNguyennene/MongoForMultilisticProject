
# -------------------
# CREATE operation
# -------------------
def create_user(user_data):
    user_data["createdAt"] = datetime.now()  # Set the current date and time for 'createdAt'
    try:
        db.users.insert_one(user_data)
        print("User created successfully!")
    except DuplicateKeyError:
        print("Error: Duplicate user ID!")

# -------------------
# READ operation
# -------------------

# Find a user by their userId
def find_user_by_userId(user_id):
    user = db.users.find_one({"userId": user_id})
    return user

# Find a user by their email
def find_user_by_email(email):
    user = db.users.find_one({"email": email})
    return user

# -------------------
# UPDATE operation
# -------------------

# Update a user's role by their userId
def update_user_role(user_id, new_role):
    result = db.users.update_one(
        {"userId": user_id},
        {"$set": {"role": new_role}}
    )
    if result.matched_count > 0:
        print(f"User {user_id}'s role updated successfully!")
    else:
        print(f"No user found with userId {user_id}")

# -------------------
# DELETE operation
# -------------------

# Delete a user by userId
def delete_user(user_id):
    result = db.users.delete_one({"userId": user_id})
    if result.deleted_count > 0:
        print(f"User {user_id} deleted successfully!")
    else:
        print(f"No user found with userId {user_id}")



