from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

load_dotenv()

class Message(BaseModel):
    name: str
    age: int
    profession: str
    IsMarried: bool


client = MongoClient(os.getenv("MONGODB"))
try:
    # La commande 'ping' renvoie {'ok': 1.0} si la connexion est établie
    client.admin.command('ping')
    print("✅ Connexion à MongoDB réussie !")
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
    
db = client["hackathon"]
collection = db["messages"]





@app.patch("/update")
def update_data(msg: Message):
    

    filter = {"name": msg.name}
    new_values = {"$set": {
        "age": msg.age,
        "profession": msg.profession,
        "IsMarried": msg.IsMarried
    }}
    
    result = collection.update_one(filter, new_values, upsert=True)


    return {
        "message": f"User: {msg.name} Age: {msg.age} Profession: {msg.profession} IsMarried: {msg.IsMarried}",
        "status": "successfully updated",
        "result": f"Matched {result.matched_count} document(s), Modified {result.modified_count} document(s)"
    }
    
    

@app.post("/save")
def save(msg: Message):

    document = {  
                "name": msg.name,
                "age": msg.age,
                "profession": msg.profession, 
                "IsMarried": msg.IsMarried
            }

    result= collection.insert_one(document)
        
    
    print(db.list_collection_names)
    return {
        "message": f"Updated - User: {msg.name} Age: {msg.age} Profession: {msg.profession} IsMarried: {msg.IsMarried}",
        "status": "successfully Saved",
        "result": f"New id : {result.inserted_id}" 
        }


@app.get("/users")
async def get_all_users():
    
    all_users = collection.find({}).to_list(length=None)
    
    for users in all_users:
        users["_id"] = str(users["_id"])

    # return all_users
    return {
        "message": all_users,
        "status": "successfull"
    }
    
