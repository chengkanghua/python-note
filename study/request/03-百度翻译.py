import requests,json

if __name__ == '__main__':
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
    }
    url = 'https://fanyi.baidu.com/sug'
    strans_word = input('enter a word: ')
    param = {
        'kw':strans_word
    }

    response = requests.get(url=url,params=param, headers=header)
    print(response.json())

    fp = open(strans_word+'.json','w',encoding='utf-8')
    json.dump(obj=response.json(),fp=fp,ensure_ascii=False)


