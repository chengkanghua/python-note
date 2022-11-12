from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/order', methods=["GET", "POST"])
def order():
    # 1.如果是GET请求，就看到新建订单的页面
    if request.method == "GET":
        return render_template('order.html')

    # 2.如果是POST请求，提交携带 数量+视频的URL
    count = request.form.get('count')
    video_count = request.form.get('url')
    print(count, video_count)

    # 3.写入数据库（库 & 表结构）【MySQL数据库】

    # 4.写入队列【Redis】
    return "下单成功"


if __name__ == '__main__':
    app.run()
