import subprocess

ffmpeg_bin = "D:/devsoft/FFmpeg/ffmpeg-6.0-essentials_build/bin/"


def py_ffmpeg(command):
    command = ffmpeg_bin + command
    return subprocess.run(command, check=True)