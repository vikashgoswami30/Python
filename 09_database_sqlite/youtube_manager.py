import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
     CREATE TABLE IF NOT EXISTS videos(
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
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name= ?,time = ? WHERE id= ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtune manager app with db")
        print("1 List All Video")
        print("2 Add videos")
        print("3 Update videos")
        print("4 Delete Videos")
        print("5 Exit App")
        choice = input("Enter Your choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
           name= input("Enter the video name: ")
           time= input("Enter the video Time: ")
           add_video(name,time)
        elif choice == '3':
           video_id=input("Enter Video ID to update")
           name= input("Enter the video name: ")
           time= input("Enter the video Time: ")
           update_video(video_id,name ,time)
        elif choice == '4':
           video_id=input("Enter Video ID to Delete")
           delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
    
    conn.close()
        
if __name__ == "__main__":
    main()
