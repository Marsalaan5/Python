from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://Id:Password@youtube.qr8zk9u.mongodb.net/",tlsAllowInvalidCertificates=True)


print(client)
db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_video():
     for video in video_collection.find():
         print(f"ID: {video['_id']}, Name: {video['name']}, and Time{video['time']}")
   


def add_video(name,time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set':{"name": new_name, "time": new_time}}
        )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List Video")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your Choice: ")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
        elif choice == "3":
            video_id = input("Enter vidoe ID: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id,name,time)
        elif choice == "4":
            video_id = input("Enter vidoe ID: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
            
        

    

if __name__ == "__main__":
    main()
