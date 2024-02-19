import json

file_name = "youtube_videos.txt"

def load_data():
    try:
        with open(file_name,'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name,"w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print("*" * 77)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.Video Name = {video['name']} , video duration = {video['time']}")
    print('\n')
    print("*" * 77)

def add_youtube_video(videos):
    name = input("Enter Video name: ")
    time = input("Enter Video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_youtube_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number you want to update: "))
    if 1 <= index <= len (videos):
        name = input("Enter the new Video Name: ")
        time = input("Enter the new Video time: ")
        videos[index - 1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def delete_youtube_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number you want to update: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | Choose An Option')
        print('1. List All youtube Videos')
        print('2. Add a Youtube Video')
        print('3. Update a Youtube Video Details')
        print('4. Delete a Youtube Video')
        print('5. Exit Prompt')
        choice = input("Enter Your Choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_youtube_video(videos)
            case "3":
                update_youtube_video(videos)
            case "4":
                delete_youtube_video(videos)
            case "5":
                break
            case _:
                print("Wrong Choice")

if __name__ == "__main__":
    main()