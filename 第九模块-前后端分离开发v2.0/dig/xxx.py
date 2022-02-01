info  = {
            11:{"reply": 2, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 1, "create_datetime": "2021-09-01 22:32:22"},
            12:{"reply": 2, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 1, "create_datetime": "2021-09-01 22:32:22"},
            13:{"reply": 11, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 2, "create_datetime": "2021-09-01 22:32:22"},
            14:{"reply": 12, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 2, "create_datetime": "2021-09-01 22:32:22"},
            15:{"reply": 13, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 3, "create_datetime": "2021-09-01 22:32:22"},
            16:{"reply": 15, "children":[],"content": "oooadfa;skdjf;akjsd;flkjasdf","depth": 4, "create_datetime": "2021-09-01 22:32:22"}
        }


data_list = []

data_list.append(info[11])
data_list.append(info[12])

info[11]['children'].append(666)

print(data_list)
