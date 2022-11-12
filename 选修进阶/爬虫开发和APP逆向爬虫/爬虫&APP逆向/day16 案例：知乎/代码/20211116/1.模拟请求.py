import requests

res = requests.get(
    url="https://www.zhihu.com/api/v4/search_v3?q=%E5%93%88%E5%93%88%E5%93%88%E5%93%88&t=general&lc_idx=0&correction=1&offset=0&advert_count=0&limit=20&is_real_time=0&show_all_topics=0&search_source=Normal&filter_fields=&raw_query=",
    headers={
        "x-udid": "AIDQoejlCRRLBXqaH0Zjw4S5gqeSRdBIlEE=",
        "x-ac-udid": "AIDQoejlCRRLBXqaH0Zjw4S5gqeSRdBIlEE=",
        "x-hd": "bdf95f1eb35b1db1386535cff3adb645",
        "x-zse-96": "2.0_aTFBo4XyrLNXHhtBzwtyNgU8bH2fNhFBGMF0gvH0k_Of",

        "user-agent": "ZhihuHybrid com.zhihu.android/Futureve/5.32.1 Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
        'x-app-version': "5.32.1",
        "x-zse-93": "101_4_2.0",
    }
)

print(res.text)
