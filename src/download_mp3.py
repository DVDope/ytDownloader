import os

from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, PytubeFixError
from pydub import AudioSegment
from pydub.exceptions import CouldntEncodeError


def m4a_to_mp3(input_file: str, output_file: str) -> None:
    """
    This function takes in two file paths, one for the input and one for the output. The input file should be a M4A
    file. The output file will be a MP3 file. The M4A file will be deleted after the conversion.

    :param input_file: Filepath to M4A file which should be converted. Different file formats **could** work.
    :param output_file: Filepath where the converted file should be saved. Will be MP3 file.
    :return: Void
    """

    try:
        m4a_file = AudioSegment.from_file(input_file)

        m4a_file.export(output_file, format="mp3")
    except FileNotFoundError:
        print("File not found")
    except AttributeError:
        print("Wrong file format")
    except CouldntEncodeError:
        print("Couldn't encode the file")
    finally:
        os.remove(f"output/currentSong.m4a")


def download_using_pytube(link: str):
    yt = YouTube(link)

    # Check if the YouTube link is valid
    try:
        is_valid = True

        if not yt.watch_url:
            is_valid = False

        if not yt.title:
            is_valid = False
    except VideoUnavailable:
        print("Video is unavailable!")
        return 1
    except PytubeFixError:
        print("There is an error with PyTube!")
        return 1

    if not is_valid:
        print("URL is not valid or unavailable!")
        return 2

    # Get first result from search query. The search query should only find one result anyway!
    try:
        video = yt.streams.filter(only_audio=True).first()
    except VideoUnavailable:
        print("This video is not available! Might be a YouTube-Kids error...")
        return -1

    # Resulting files will be placed within the current session id folder
    destination = f"output/"

    out_file = video.download(output_path=destination, filename='currentSong.m4a')  # Save file to "output/currentSong.m4a"

    # Transform the m4a file to a mp3 file
    m4a_to_mp3(f"output/currentSong.m4a", f"output/currentSong.mp3")

    print(yt.title + " has been downloaded to " + destination)


def download_mp3_from_youtube(youtube_link: str) -> str:
    try:
        download_using_pytube(youtube_link)
    except PermissionError:
        print("Failed")

    pass
