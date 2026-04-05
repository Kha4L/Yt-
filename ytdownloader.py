import os 
import subprocess

def download_video(url, output_path):
    try:
        print(f"Memulai Download video dari url {url}.")
        os.makedirs(output_path, exist_ok=True)
        command = [
            'yt-dlp',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            url
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Download selesai")
    except subprocess.CalledProcessError as e:
        print(f"Gagal pas mendownload video: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def download_playlist(url, output_path):
    try:
        print(f"Memulai mendownload playlist {url}")
        os.makedirs(output_path, exist_ok=True)
        command = [
            'yt-dlp',
            '-o', os.path.join(output_path, '%(playlist)s/%(title)s.%(ext)s'),
            url
        ]
       
        subprocess.run(command, check=True)
        print("Download Selesai")
    except subprocess.CalledProcessError:
        print("Gagal mendownload")
    except Exception as e:
        print(f'terjadi kesalahan: {e}')

def main():

    print("Masukan Link Video atau playlist")

    while True:
        #Tanya user mau download apaan
        mode = input('pilih Mode download (Video/Playlist) q= buat keluar: ').strip().lower()

        if mode.lower() == 'q':
            print("Ddah")
            break
        elif mode == '1':
            video_url = input("Masukan link")
            download_video(video_url, "Video")
        elif mode == '2':
            playlist_url = input("Masukan link playlist")
            download_playlist(playlist_url, "Playlist")
        else:
            print("Ga ada opsi buat itu")

if __name__ == '__main__':
    main()
    
    


    
    
   
   



 