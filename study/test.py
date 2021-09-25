from db import db

# db.exec('select * from student where sid=%(sid)s ',sid=5) # 执行语句
#
# result = db.fetch_one('select * from student where sid=%(sid)s ', sid=5)
# print(result)
#
# result = db.fetch_all('select * from student',)
# print(result)

fields = {
    "title": "标题",
    "text": "内容",
    "read_count": "阅读数",
    "comment_count": "评论数",
    "support_count": "赞数",
    "step_count": "踩数",
    "nickname": "作者",
}
print( ",".join([k for k in fields]))