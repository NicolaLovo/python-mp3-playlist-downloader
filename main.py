import os
import shutil

import moviepy.editor as mp
from pydub import AudioSegment
from pytube import Playlist, YouTube
from pytube.cli import on_progress


def parse_file_name(index, title):
    name = f"{index}-{title}.mp4"
    name = name.replace("|", "-").replace("/", "-").replace("\\", "-")
    name = name.replace("'", "").replace('"', "")
    name = name.replace(":", "-").replace("*", "-").replace("?", "-")
    name = name.strip()
    return name


def download_playlist_videos(play_list_url, folder):
    playlist = Playlist(play_list_url)
    i = 1
    for url in playlist:
        try:
            yt = YouTube(url, on_progress_callback=on_progress,
                         use_oauth=True, allow_oauth_cache=True)
            video = yt.streams.filter(only_audio=True).first()

            name = parse_file_name(i, yt.title)
            print(
                f"downloading {i}/{len(playlist)}, size {round(video.filesize/(1024*1024))}MB, inside {folder}, '{name}'")
            video.download(folder, filename=name)
            i += 1
        except Exception as e:
            print(f"Error downloading '{url}': {e}")


def download_list_videos(videos_urls, folder):
    i = 1
    for url in videos_urls:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            video = yt.streams.filter(only_audio=True).first()
            print(
                f"downloading {i}/{len(videos_urls)}, size {round(video.filesize/(1024*1024))}MB, inside {folder}, '{yt.title}'")
            name = parse_file_name(i, yt.title)
            video.download(folder, filename=name)
            i += 1
        except Exception as e:
            print(f"Error downloading '{url}': {e}")


def convert_videos_to_mp3(video_folder, audio_folder):
    files = os.listdir(video_folder)

    i = 1
    for filename in files:
        if filename.endswith(".mp4"):
            try:
                mp4_file = os.path.join(video_folder, filename)
                mp3_file = os.path.join(
                    audio_folder, filename.replace('.mp4', ".mp3"))
                print(f"converting mp4 to mp3 {i}/{len(files)}, '{filename}'")
                # print(
                #     f"converting {i}/{len(files)}, '{filename}', path: {mp4_file}, new path: {mp3_file}")

                clip = mp.AudioFileClip(mp4_file)
                clip.write_audiofile(mp3_file)
                clip.close()
            except Exception as e:
                print(f"Error converting mp4 to mp3 '{filename}': {e}")
            i += 1


def convert_mp3_to_wav(audio_folder, wav_folder):
    files = os.listdir(audio_folder)

    i = 1
    for filename in files:
        if filename.endswith(".mp3"):
            try:
                mp3_file = os.path.join(audio_folder, filename)
                wav_file = os.path.join(
                    wav_folder, filename.replace('.mp3', ".wav"))
                print(f"converting mp3 to wav {i}/{len(files)}, '{filename}'")
                # print(
                #     f"converting {i}/{len(files)}, '{filename}', path: {mp3_file}, new path: {wav_file}")
                sound = AudioSegment.from_mp3(mp3_file)
                sound.export(wav_file, format="wav")
            except Exception as e:
                print(f"Error converting mp3 to wav '{filename}': {e}")
            i += 1


def main():
    videos_folder = "./download/videos"
    audios_folder = "./download/audio"
    wav_folder = "./download/wav"
    shutil.rmtree(videos_folder, ignore_errors=True)
    shutil.rmtree(audios_folder, ignore_errors=True)
    shutil.rmtree(wav_folder, ignore_errors=True)
    try:
        os.mkdir(videos_folder)
    except:
        pass
    try:
        os.mkdir(audios_folder)
    except:
        pass
    try:
        os.mkdir(wav_folder)
    except:
        pass

    # ! videos list
    # videos_list = [
    #     "https://youtu.be/5IWS7Y5KRhk?list=PLrvKqne9ixu2VC3MCxH6SsAABXQ-FzXi4"]
    # download_list_videos(videos_list, videos_folder)

    # ! playlist
    # playlist totale
    # playlist_url = "https://www.youtube.com/playlist?list=PLrvKqne9ixu1FZTt6afGX3Q8-s0ol1fLs"
    playlist_url = "https://www.youtube.com/playlist?list=PLrvKqne9ixu2VC3MCxH6SsAABXQ-FzXi4"  # video nuovi
    download_playlist_videos(playlist_url, videos_folder)

    print("\n\n")
    # ! convert videos to mp3
    convert_videos_to_mp3(videos_folder, audios_folder)

    print("\n\n")

    # ! convert mp3 to wav: decomment if needed!!!
    # convert_mp3_to_wav(audios_folder, wav_folder)


if __name__ == '__main__':
    main()
