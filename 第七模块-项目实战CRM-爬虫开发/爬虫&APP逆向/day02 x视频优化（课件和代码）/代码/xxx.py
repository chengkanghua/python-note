data = """{'k1':123,'k2':456}"""

# import json
# v = json.loads(data)
# print(v)


v = eval(data)
print(v, type(v))
