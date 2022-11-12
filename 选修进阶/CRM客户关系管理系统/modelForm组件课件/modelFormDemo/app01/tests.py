from django.test import TestCase

# Create your tests here.




import requests

res = requests.post("http://127.0.0.1:8000/addStu/",data={
    "name":"xxxxxxxxxxxx",
})

print(res.text)