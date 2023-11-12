from video_utils import extract_audio, extract_video_without_audio, replace_audio, replace_audio_fast, \
    replace_audio_ffmpeg, extract_audio_ffmpeg, extract_audio_ffmpeg_start_from, convert_wav_to_aac


def test_extract_audio():
    source = "E:/temp/testVideo/sourceVideo.mp4"
    dest = "E:/temp/testVideo/audio.aac"
    extract_audio(source, dest)


def test_extract_video_without_audio():
    source = "E:/temp/testVideo/sourceVideo.mp4"
    dest = "E:/temp/testVideo/pure.mp4"
    extract_video_without_audio(source, dest)


def test_replace_audio():
    source_video = "E:/temp/testVideo/sourceVideo.mp4"
    source_audio = "E:/temp/testVideo/audio.aac"
    dest_video = "E:/temp/testVideo/output.mp4"
    replace_audio(source_video, source_audio, dest_video)

def test_replace_audio_fast():
    source_video = "E:/temp/testVideo/sourceVideo.mp4"
    source_audio = "E:/temp/testVideo/audio.aac"
    dest_video = "E:/temp/testVideo/output.mp4"
    replace_audio_fast(source_video, source_audio, dest_video)


def test_replace_audio_ffmpeg():
    source_video = "E:/temp/testVideo/sourceVideo.mp4"
    source_audio = "E:/temp/testVideo/audio.aac"
    dest_video = "E:/temp/testVideo/output.mp4"
    # video_duration = "02:15:01.23"

    replace_audio_ffmpeg(source_video, source_audio, dest_video)


def test_extract_audio_ffmpeg():
    source_video = "E:/temp/testVideo/sourceVideo.mp4"
    dest = "E:/temp/testVideo/audio.aac"
    extract_audio_ffmpeg(source_video, dest)


def test_extract_audio_ffmpeg_start_from():
    source_video = "E:/temp/testVideo/sourceVideo.mp4"
    output_noise_audio = "E:/temp/testVideo/keyboard_noise_audio.aac"
    start_time = "00:46:27.5"
    video_duration = "00:00:02.2"
    extract_audio_ffmpeg_start_from(source_video, output_noise_audio, start_time, video_duration)

def test_convert_wav_to_aac():
    source = 'D:/code/pycharm/videoNoiseReducer/assets/audio/keyboard_noise_audio_manual.wav'
    dest = 'D:/code/pycharm/videoNoiseReducer/assets/audio/keyboard_noise_audio_manual.aac'
    convert_wav_to_aac(source,dest)


if __name__ == '__main__':
    test_extract_audio_ffmpeg_start_from()
