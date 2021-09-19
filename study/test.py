import pymysql
import re


def into_db(num, title, url):
    conn = pymysql.connect(host='localhost', user='root', password='root123', port=3306, db='db1', charset='utf8')
    cursor = conn.cursor()
    # sql = 'insert into new(num,title,url) values(%s,%s,%s)'
    cursor.execute('insert into new(num,title,url) values(%s,%s,%s)', [num, title, url])
    conn.commit()
    cursor.close()
    conn.close()


def run():
    file_object = open(file='info.csv', mode='r', encoding='utf-8')
    for line in file_object:
        # num ,title ,url = re.findall('(\d),(.*),(http.*.mp4)',line) #返回格式[(数据1，数据2，数据3)]
        # _, num, title, url, _ = re.split('(\d),(.*),(http.*.mp4)', line.strip())
        num,title,url = re.match('(\d+),(.*),(http.*.mp4)', line.strip()).groups()
        into_db(num, title, url)

    file_object.close()


# result = cursor.fetchall()
# print(result)

if __name__ == '__main__':
    run()
