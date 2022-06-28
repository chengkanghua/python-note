import requests

res = requests.get(
    url="https://app.api.lianjia.com/Rentplat/v2/house/list",
    params={
        "city_id": "110000",
        "condition": "shahe2%2F",
        "offset": "0",
        "limit": "30",
        "scene": "list",
        "isMyCompany": "0",
        "is_second_filter": "0",
        "request_ts": "1632724797"
    }
)

print(res.json())
