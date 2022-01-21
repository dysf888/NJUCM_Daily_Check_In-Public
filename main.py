import ddddocr,sys,time,requests
from playwright.sync_api import Playwright, sync_playwright
username =sys.argv[1]
password =sys.argv[2]
qq="your qq number"
name=""
def msg():
        global qq
        global name
        if username == "xxxxx":                 #此处为多用户,只有三个人目前采用简单方式,如需自己修改
                qq="xxxx"
                name="xxx"
                notify()
        elif username == "xx":
                qq="xx"
                name="xx"
                notify()
        elif username == "xx":
                qq="xx"
                name="xxx"
                notify()
def notify():
        data={
    "msg":"Dear :"+name+ ", At "+str(time.asctime( time.localtime(time.time())))+" , "+"健康打卡完成!", #需要发送的消息
    "qq":qq #需要接收消息的QQ号码
        }
        response = requests.post("https://qmsg.zendee.cn/send/xxxxxxxxxxxx",data=data)
        print(response)
        print(qq)
        print(data)
        sys.exit()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://122.194.115.171:866/login.aspx")
    time.sleep(6)
    page.click("input[name=\"userbh\"]")
    page.fill("input[name=\"userbh\"]", username)
    page.click("input[type=\"password\"]")
    page.fill("input[type=\"password\"]", password)
    #验证码处理部分
    page.locator("#Image1").screenshot(path="screenshot.jpg")
    ocr = ddddocr.DdddOcr()
    with open("screenshot.jpg", 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    print(res)
    time.sleep(3)
    page.click("textarea[name=\"vcode\"]")
    page.fill("textarea[name=\"vcode\"]", res)
    page.click("input[name=\"save2\"]")
    page.click("text=疫情防控")
    time.sleep(1)
    page.click("text=每日打卡(上午)")
    time.sleep(1)
    page.frame(name="r_3_3").click("input[name=\"szdbhqk\"]")
    page.frame(name="r_3_3").fill("input[name=\"szdbhqk\"]", "无")
    with page.expect_popup() as popup_info:
        page.frame(name="r_3_3").click("input[name=\"jrszdsfwzgfxdq\"]")
    page2 = popup_info.value
    time.sleep(1)
    page2.click("#MyDataGrid td:has-text(\"否\")")
    with page.expect_popup() as popup_info:
        page.frame(name="r_3_3").click("input[name=\"skmys\"]")
    page3 = popup_info.value
    time.sleep(1)
    page3.click("#MyDataGrid td:has-text(\"绿码\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"brjkqk\"]")
    page4 = popup_info.value
    time.sleep(1)
    page4.click("#MyDataGrid td:has-text(\"健康\")")
    time.sleep(1)
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"dtzctw\"]")
    page5 = popup_info.value
    time.sleep(1)
    page5.click("#MyDataGrid td:has-text(\"36.8℃\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"qzhysqk\"]")
    page6 = popup_info.value
    time.sleep(1)
    page6.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"jrywksfrqk\"]")
    page7 = popup_info.value
    time.sleep(1)
    page7.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"sfyxlfz\"]")
    page8 = popup_info.value
    time.sleep(1)
    page8.click("#MyDataGrid td:has-text(\"否\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"ywdfhljfxdq\"]")
    page9 = popup_info.value
    time.sleep(1)
    page9.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"sfjxhsjc\"]")
    page10 = popup_info.value
    time.sleep(1)
    page10.click("#MyDataGrid td:has-text(\"否\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"ywgwljs\"]")
    page11 = popup_info.value
    time.sleep(1)
    page11.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"ywyjwryjcs\"]")
    page12 = popup_info.value
    time.sleep(1)
    page12.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"ywyqzysglryjc\"]")
    page13 = popup_info.value
    time.sleep(1)
    page13.click("#MyDataGrid td:has-text(\"无\")")
    with page.expect_popup() as popup_info:
            page.frame(name="r_3_3").click("input[name=\"glgczt\"]")
    page14 = popup_info.value
    time.sleep(1)
    page14.click("text=非隔离观察状态")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.frame(name="r_3_3").click("text=增加记录")
    context.close()
    browser.close()
    msg()
    


with sync_playwright() as playwright:
    run(playwright)
