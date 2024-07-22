import re
from pytube import YouTube
import moviepy.editor as mp

# 阶段1：音频提取
# YouTube视频的URL
video_url = "https://www.youtube.com/watch?v=b4vbS4mJfRY"

# 从YouTube下载视频并提取音频
youtube = YouTube(video_url)
video_title = youtube.title

# 将视频标题中的特殊字符替换为下划线
video_title = re.sub(r'[^\w\-_\. ]', '_', video_title)

# 使用视频标题作为文件名
audio_file = f"{video_title}.mp4"
video = youtube.streams.filter(only_audio=True).first()
video.download(filename=audio_file)

# 阶段2：音频转换
# 将下载的音频转换为wav格式
clip = mp.AudioFileClip(audio_file)
wav_file = f"{video_title}.wav"
clip.write_audiofile(wav_file)