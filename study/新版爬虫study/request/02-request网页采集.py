import requests
if __name__ == '__main__':
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"
    }

    url = 'https://www.sogou.com/web'
    search_word = input('enter word: ')
    param = {
        'query': search_word
    }

    response = requests.get(url=url,params=param,headers=header)
    print(response.text)
    file_name = search_word+'.html'
    print(file_name)
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(response.text)

    print(file_name,'game over')