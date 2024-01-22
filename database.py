#Alif's Database ᕦ ε ᕥ

# def insertkey():
#     return input("Enter your name: ")

# def insertvalue():
#     return int(input("Enter your score: "))

# # Call the functions to get user input
# name = insertkey()
# score = insertvalue()

# # Create the database dictionary using the obtained values
# database = {'Name': name, 'Score': score}

# # Function to insert new key-value pair
# def insert_new_data():
#     new_key = input("Enter your name (or type 'close' to stop): ")

#     # Check if the user wants to stop
#     if new_key.lower() == 'close':
#         return False

#     new_value = input("Enter your score: ")
#     database[new_key] = new_value
#     print(f"Data inserted: {new_key}: {new_value}")
#     return True

# # Continuously insert new data
# while insert_new_data():
#     pass

# print(database)




# def show_leaderboard():
#     print("Leaderboard:")
#     print("-------------")
#     for name, score in sorted(database.items(), key=lambda x: x[1], reverse=True):
#         print(f"{name}: {score}")

# def insert_new_data():
#     new_key = input("Enter your name (or type 'close' to stop): ")

#     # Check if the user wants to stop
#     if new_key.lower() == 'close':
#         return False

#     new_value = int(input("Enter your score: "))
#     database[new_key] = new_value
#     print(f"Data inserted: {new_key}: {new_value}")
#     return True

# # Database initialization
# database = {}

# # Continuously insert new data
# while insert_new_data():
#     pass

# # Show the leaderboard
# show_leaderboard()

def get_name():
    pass