import time,requests,sys
username='0490201xx' #身份
qq=''
def msg():
        global qq
        if username == "0490201xx":
                qq="18xxxxxx428"
                notify()
        elif username == "04xxxxxx4":
                qq="25xxxxxx389"
                notify()
def notify():
        data={
    "msg":"学号:"+username+"健康打卡完成", #需要发送的消息
    "qq":qq #需要接收消息的QQ号码
        }
        response = requests.post("https://qmsg.zendee.cn/send/bxxxxxxxxxxxxxxxxxxxxeed",data=data)
        print(response)
        print(qq)
        print(data)
        sys.exit()

msg()