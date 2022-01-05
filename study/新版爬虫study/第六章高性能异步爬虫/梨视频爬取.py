import requests

video_id = "1747247"
cont_id = f"cont-{video_id}"
url = "https://www.pearvideo.com/video_1747247"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    'Referer': f'https://www.pearvideo.com/video_{video_id}'
}
res = requests.get(url=f'https://www.pearvideo.com/videoStatus.jsp?contId={video_id}', headers=headers)
srcUrl = res.json()['videoInfo']["videos"]['srcUrl']
srcUrl = srcUrl.replace(srcUrl.split("-")[0].split("/")[-1], cont_id)

with open('a.mp4', mode='wb') as f:
    response = requests.get(url=srcUrl, headers=headers, stream=True)  # 1639051186936 替换成 cont-1747247
    for i in response.iter_content(1024):
        f.write(i)