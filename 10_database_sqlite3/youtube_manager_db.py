import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute(" INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ? , time = ? where id = ?",(name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List All Youtube Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit Prompt")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter Video Name: ")
            time = input('Enter Video Time: ')
            add_video(name,time)                
        elif choice == "3":
            list_videos()
            video_id = input("Enter Video ID to Update: ")
            name = input("Enter Video Name: ")
            time = input('Enter Video Time: ')
            update_video(video_id,name,time)
        elif choice == "4":
            list_videos()
            video_id = input("Enter Video ID to Delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print('Invalid Choice')


    conn.close()



if __name__ == "__main__":
    main()