import re
import json
import requests
import subprocess
import os



def download_bilibili_video(url):
    session = requests.session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
        'Referer': 'https://www.bilibili.com'
    }

    resp = session.get(url, headers=headers)

    # 提取视频标题
    title = re.findall(r'<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili', resp.text)[0]

    # 提取视频播放信息
    play_info = re.findall(r'<script>window.__playinfo__=(.*?)</script>', resp.text)[0]
    json_data = json.loads(play_info)

    # 获取音频和视频下载链接
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]

    # 下载音频和视频
    audio_content = session.get(audio_url, headers=headers).content
    video_content = session.get(video_url, headers=headers).content

    # 保存音频和视频文件
    audio_file = title + '.mp3'
    video_file = title + '_temp.mp4'
    with open(audio_file, 'wb') as f:
        f.write(audio_content)
    with open(video_file, 'wb') as f:
        f.write(video_content)

    # 使用ffmpeg将音频合并到视频中
    output_file = title + '.mp4'
    merge_command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -strict experimental "{output_file}"'
    subprocess.call(merge_command, shell=True)

    # 删除临时的音频和视频文件
    # os.remove(audio_file)
    os.remove(video_file)

    print(f"视频已下载：{title}")


# 示例用法
video_url = "https://www.bilibili.com/video/BV1Gg4y1W7Zj/?spm_id_from=333.999.0.0&vd_source=a4a0c20ca464b5d861d4a2871ce0d9f4"
download_bilibili_video(video_url)
