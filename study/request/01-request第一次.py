import requests
if __name__ == "__main__":
    url = 'https://www.mi.com/'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)

    with open('./mi.html','w',encoding='utf-8') as f:
        f.write(page_text)

    print('game over')