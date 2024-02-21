from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.z5g2xnh.mongodb.net/")

db = client["ytmanager"]

video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"Id: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,name,time):
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name":name,"time":time}})

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})

def main():
    while True:
        print('\n Youtube Video Manager')
        print('1. List all Videos')
        print('2. Add new Video')
        print('3. Update Video')
        print('4. Delete Video')
        print('5. Exit the prompt')
        choice = input("Enter You Choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input('Enter the Video name: ')
            time = input('Enter the Video Duration: ')
            add_video(name,time)
        elif choice == "3":
            list_videos()
            video_id = input("Enter the VideoId you want to change: ")
            name = input("Enter the new name for video: ")
            time = input("Enter the new Duration of the video: ")
            update_video(video_id,name,time)
        elif choice == "4":
            list_videos()
            video_id = input("Enter the VideoId you want to delete")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("You Enter The Wrong Choice")
                  
if __name__ == "__main__":
    main()