import os

import moviepy.editor as mp
from pytube import Playlist, YouTube
from pytube.cli import on_progress


def download_playlist_videos(play_list_url, folder):
    playlist = Playlist(play_list_url)
    os.mkdir(folder)
    i = 1
    for url in playlist:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            video = yt.streams.filter(only_audio=True).first()
            print(
                f"downloading {i}/{len(playlist)}, size {round(video.filesize/(1024*1024))}MB, inside {folder}, '{yt.title}'")
            video.download(folder, filename=f"{i}-{yt.title}.mp4")
            i += 1
        except Exception as e:
            print(f"Error downloading '{url}': {e}")


def convert_videos_to_mp3(video_folder, audio_folder):
    files = os.listdir(video_folder)
    os.mkdir(audio_folder)
    i = 1
    for filename in files:
        if filename.endswith(".mp4"):
            try:
                mp4_file = os.path.join(video_folder, filename)
                mp3_file = os.path.join(
                    audio_folder, filename.replace('.mp4', ".mp3"))
                print(f"converting {i}/{len(files)}, '{filename}'")
                # print(
                #     f"converting {i}/{len(files)}, '{filename}', path: {mp4_file}, new path: {mp3_file}")

                clip = mp.AudioFileClip(mp4_file)
                clip.write_audiofile(mp3_file)
                clip.close()
            except Exception as e:
                print(f"Error converting '{filename}': {e}")
            i += 1


def main():
    videos_folder = "./download/videos"
    audios_folder = "./download/audio"
    download_playlist_videos(
        "https://www.youtube.com/playlist?list=PLrvKqne9ixu3bBt_z1gPIei11KaWRcGwU", videos_folder)
    convert_videos_to_mp3(videos_folder, audios_folder)


if __name__ == '__main__':
    main()
