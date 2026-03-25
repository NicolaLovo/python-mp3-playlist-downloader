import os
import shutil

import yt_dlp
from pydub import AudioSegment
from moviepy import AudioFileClip


# def parse_file_name(index, title):
#     name = f"{index}-{title}.mp4"
#     name = name.replace("|", "-").replace("/", "-").replace("\\", "-")
#     name = name.replace("'", "").replace('"', "")
#     name = name.replace(":", "-").replace("*", "-").replace("?", "-")
#     name = name.strip()
#     return name


def download_playlist_audio(playlist_url, output_folder):
    print("Fetching playlist...")

    # ? Video + audio download and merge kept here for reference
    # ydl_opts = {
    #     # Download audio+video
    #     # Some videos may not have mp4, so we use a fallback here for higher compatibility
    #     "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/best",
    #     # "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",

    #     # Output filename
    #     # https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#output-template
    #     "outtmpl": os.path.join(
    #         output_folder,
    #         "%(playlist_index)s-%(title)s.%(ext)s"
    #     ),

    #     # Download playlist
    #     "noplaylist": False,

    #     "quiet": False,
    #     "ignoreerrors": True,

    #     # Force mp4 container
    #     "postprocessors": [
    #         {
    #             "key": "FFmpegVideoRemuxer",
    #             "preferedformat": "mp4",
    #         }
    #     ],
    # }


    # ? Audio-only download 
    ydl_opts = {
        # Download audio only
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        # Output filename
        "outtmpl": os.path.join(
            output_folder,
            "%(playlist_index)s-%(title)s.%(ext)s"
        ),

        # Download playlist
        "noplaylist": False,

        "quiet": False,
        "ignoreerrors": True,

        # Force mp4 container
        "postprocessors": [
            {
                "key": "FFmpegVideoRemuxer",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])



def convert_videos_to_mp3(video_folder, audio_folder):
    files = os.listdir(video_folder)

    i = 1
    print("Converting mp4 to mp3")
    for filename in files:
        if filename.endswith(".mp4"):
            try:
                mp4_file = os.path.join(video_folder, filename)
                mp3_file = os.path.join(audio_folder, filename.replace(".mp4", ".mp3"))
                print(f"    ->converting mp4 to mp3 {i}/{len(files)}, '{filename}'")
                print(
                    f"converting {i}/{len(files)}, '{filename}', path: {mp4_file}, new path: {mp3_file}")

                clip = AudioFileClip(mp4_file)
                clip.write_audiofile(mp3_file)
                clip.close()
            except Exception as e:
                print(f"Error converting mp4 to mp3 '{filename}'", e)
            i += 1


def convert_mp3_to_wav(audio_folder, wav_folder):
    files = os.listdir(audio_folder)

    i = 1
    print("Converting mp3 to wav")
    for filename in files:
        if filename.endswith(".mp3"):
            try:
                mp3_file = os.path.join(audio_folder, filename)
                wav_file = os.path.join(wav_folder, filename.replace(".mp3", ".wav"))
                print(f"    ->converting mp3 to wav {i}/{len(files)}, '{filename}'")
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
        os.makedirs(videos_folder)
    except:
        pass
    try:
        os.makedirs(audios_folder)
    except:
        pass
    try:
        os.makedirs(wav_folder)
    except:
        pass

    print("Python mp3 downloader. By Nicola Lovo https://github.com/NicolaLovo\n\n")
    print("NOTE: the playlist must be public and not private.")
    # playlist_url = "https://www.youtube.com/playlist?list=PLrvKqne9ixu2VC3MCxH6SsAABXQ-FzXi4"
    playlist_url = input("Insert the youtube playlist url to convert: ")
    print(f"\nStart downloading playlist '{playlist_url}'")

    # Nicola playlist
    # video nuovi https://www.youtube.com/playlist?list=PLrvKqne9ixu2VC3MCxH6SsAABXQ-FzXi4
    # playlist totale https://www.youtube.com/playlist?list=PLrvKqne9ixu1FZTt6afGX3Q8-s0ol1fLs
    # video list ["https://youtu.be/5IWS7Y5KRhk?list=PLrvKqne9ixu2VC3MCxH6SsAABXQ-FzXi4"]

    download_playlist_audio(playlist_url, videos_folder)

    print("\n\n")
    # ! convert videos to mp3
    convert_videos_to_mp3(videos_folder, audios_folder)

    print("\n\n")

    playlist_url = input("Do you also want to convert the mp3 files to wav? (y/n):")

    if playlist_url.lower() == "y":
        convert_mp3_to_wav(audios_folder, wav_folder)


if __name__ == "__main__":
    main()
