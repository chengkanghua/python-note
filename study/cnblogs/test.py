column_display = ["nickname", "read_count", "comment_count", "support_count", "step_count"]
# for k in column_display:
#     print(k)
fields = {
    'title': '标题',
    'text': '内容',
    'read_count': '阅读数',
    'comment_count': '评论数',
    'support_count': '点赞数',
    'step_count': '踩数',
    'nickname': '作者'
}

text = ','.join([k for k in fields.keys()])
print(text)
