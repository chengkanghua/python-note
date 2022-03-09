def message_sort(message_list):
    """冒泡排序"""
    for key1, item1_bytes in enumerate(message_list):
        list2 = len(message_list) - key1 - 1
        for key2 in range(0, list2):
            message1 = message_list[key2].decode().split("_")[-1]
            message2 = message_list[key2 + 1].decode().split("_")[-1]
            if int(message1) > int(message2):
                message_list[key2], message_list[key2 + 1] = message_list[key2 + 1], message_list[key2]

    return message_list