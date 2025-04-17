from pymongo import MongoClient
from bson import ObjectId 

client = MongoClient("mongodb+srv://youtubepy:youtubepy@youtube.ndbrbk7.mongodb.net/ytmanager",tlsAllowInvalidCertificates=True)

print(client)
db = client["ytmanager"] 
video_collection = db["videos"]

print(video_collection)

def list_video():
     for video in video_collection.find():
         print(f"Id:{video['_id']},Name: {video['name']} and Time: {video['time']}")

def add_video(name,time):
     video_collection.insert_one({"name": name, "time": time})

def update_video(video_id,newname,newtime):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": newname, "time": newtime}}
        )

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})



def main():
    while True:
        print("\n Youtube Manager APP")
        print("1. List All Videos")
        print("2. Add New Video")
        print("3. Update Video")
        print("4. Delete a Video")
        print("5. Exit the App")
        choice = input("Enter your choice:  ")
        if choice=='1':
            list_video()
        elif choice =='2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
            
        elif choice =='3':
            video_id=input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id,name,time)
        
        elif choice =='4':
            video_id=input("Enter the video id to update: ")
            delete_video(video_id)

        elif choice=='5':
            break    
        else:
            print("Invalid choice")
            
                  



if __name__ == "__main__":
    main()