import datetime
from pymongo import MongoClient
client = MongoClient()
# optional following line above line will connect on default ports
client = MongoClient('localhost',27017)
#or MongoDb URI format
#  client = MongoClient('mongodb://localhost:27017/')
db = client.test
#or use Directory Style if above syntax is heaving problamatic
#db = client['School-database']
collection = db.School
# or collection = db['StudentDetails-collection']

post = {"author": "Akhilesh",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

posts = db.posts
post_id = posts.insert(post)

