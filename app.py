import utils
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from datetime import timedelta
import string

app = Flask(__name__)

# 配置缓存更新时间
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) #将缓存时间设置为一秒

# 配置默认路由，指向模板页
@app.route('/')
def index():
    return render_template("main.html")

#配置中间C1部分数据格式
@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

#配置中间C2部分数据格式
@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

#配置左边第一部分数据格式
@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,deal = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        #  a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        deal.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "deal": deal})

#配置左边第二部分数据格式
@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

#配置右边第一部分数据格式
@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city,"confirm": confirm})

#配置右边第二部分数据格式
@app.route("/r2")
def get_r2_data():
    res = []
    for tup in utils.get_r2_data():
        # print(tup)
        res.append({"name": tup[0], "value": int(tup[1])})
    print(res)
    return jsonify({"data":[{'name': '上海', 'value': 2},{'name': '上海sss', 'value': 2}]})



#获取服务器时间
@app.route("/time")
def get_time():
    return utils.get_time()

#主函数
if __name__ == '__main__':

    app.run(port=5800)