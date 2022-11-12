from flask import Flask, render_template, request, redirect
import utils

app = Flask(__name__)


@app.route('/order', methods=["GET", "POST"])
def order():
    # 1.如果是GET请求，就看到新建订单的页面
    if request.method == "GET":
        return render_template('order.html')

    # 2.如果是POST请求，提交携带 数量+视频的URL
    count = request.form.get('count')
    video_url = request.form.get('url')

    # 订单号
    oid = utils.gen_oid()

    # 3.写入数据库（库 & 表结构）【MySQL数据库】
    utils.db_create_task(count, video_url, oid)

    # 4.写入队列【Redis】
    utils.redis_push_task(oid)

    return redirect("/order/list")


@app.route('/order/list')
def order_list():
    """ 获取所有订单列表 """

    # 去数据库获取所有的订单信息
    res = utils.db_fetch_all_task()

    # 展示在页面上
    return render_template("order_list.html", res=res)


if __name__ == '__main__':
    app.run()
