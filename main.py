from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Get the database
db = client.mydb

# Create collection
todo = db.todo

print(db)

# Insert a document
# todo_1 = {
#    'title': 'Buy milk',
#    'description': 'Milk is needed for the baby',
#    'done': False
# }

# todo.insert_one(todo_1)

# Get a document
# todo_1 = todo.find()

# print(list(todo_1))

# Update a document
# todo.update_one({"title": "Buy milk"}, {"$set": {"done": True}})
# todo_1 = todo.find()

# print(list(todo_1))

# Delete a document
todo.delete_many({"title": "Buy milk"})
todo_1 = todo.find()
print(list(todo_1))