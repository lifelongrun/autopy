import requests

# 视频的 URL
video_url = "https://play.vidyard.com/eQZU7c9vMcWsExv6z61Sr4"

# 发送 GET 请求获取视频数据
response = requests.get(video_url)

# 检查请求是否成功
if response.status_code == 200:
    # 获取视频的文件名
    filename = video_url.split("/")[-1]

    # 将视频数据写入本地文件
    with open(filename, "wb") as file:
        file.write(response.content)

    print("视频下载完成！")
else:
    print("视频下载失败。")
