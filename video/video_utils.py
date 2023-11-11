import subprocess

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import VideoFileClip

# todo fill the ffmpeg bin path
ffmpeg_bin = "D:/devsoft/FFmpeg/ffmpeg-6.0-essentials_build/bin/"
default_audio_codec = "aac"

def extract_audio(video_path, output_path):
    # 加载视频剪辑
    video_clip = VideoFileClip(video_path)

    # 提取音频
    audio_clip = video_clip.audio

    # 保存音频
    audio_clip.write_audiofile(output_path,  codec=default_audio_codec)

    # 关闭视频和音频剪辑
    video_clip.close()
    audio_clip.close()




def extract_audio_ffmpeg(video_path, output_audio_path):
    command = [
        ffmpeg_bin + 'ffmpeg',
        '-i', video_path,
        '-vn',  # 禁用视频流
        '-acodec', 'copy',  # 拷贝音频流
        output_audio_path
    ]

    subprocess.run(command, check=True)


def extract_video_without_audio(video_path, output_path):
    # 加载视频剪辑
    video_clip = VideoFileClip(video_path)

    # 获取没有音频的视频剪辑
    video_without_audio = video_clip.set_audio(None)

    # 保存没有音频的视频
    video_without_audio.write_videofile(output_path, codec="libx264")

    # 关闭视频剪辑
    video_clip.close()
    video_without_audio.close()


def replace_audio(video_path, new_audio_path, output_path):
    # 加载视频剪辑
    video_clip = VideoFileClip(video_path)

    # 加载新的音频剪辑
    new_audio_clip = AudioFileClip(new_audio_path)

    # 将视频剪辑的音频替换为新的音频
    video_clip = video_clip.set_audio(new_audio_clip)

    # 保存带有新音频的视频
    video_clip.write_videofile(output_path, codec="libx264", audio_codec=default_audio_codec)

    # 关闭视频和音频剪辑
    video_clip.close()
    new_audio_clip.close()


def replace_audio_fast(video_path, new_audio_path, output_path):
    # 加载视频剪辑
    video_clip = VideoFileClip(video_path)

    # 加载新音频
    new_audio_clip = AudioFileClip(new_audio_path)

    # 将视频剪辑的音频替换为新音频，保持时长不变
    video_clip = video_clip.set_audio(new_audio_clip.set_duration(video_clip.duration))

    # 保存新视频，不重新渲染
    video_clip.write_videofile(output_path, codec="mpeg4", audio_codec="aac", threads=4)

    # 关闭视频剪辑
    video_clip.close()
    new_audio_clip.close()


def replace_audio_ffmpeg(video_path, new_audio_path, output_path):
    # 使用ffmpeg命令合并视频和音频，不重新渲染
    command = f'{ffmpeg_bin}ffmpeg -i "{video_path}" -i "{new_audio_path}" -c copy -map 0:v -map 1:a  "{output_path}"'

    # 执行命令
    subprocess.call(command, shell=True)