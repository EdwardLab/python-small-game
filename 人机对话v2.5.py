#无聊练手程序，对话程序
#By:xingyujie
#代码以GPL-V3协议发布
import os
import time
print("这是一个很无聊程序")
print("收集信息:")
name = input("请输入你的名字:")
age = input("请输入你的年龄:")
addr = input("请输入你的家庭住址:")
phone = input("请输入手机号码:")
print("请核对信息，名字:" + name + "，年龄:" + age + "，地址:" + addr + "，电话:" + phone)
time.sleep(5)
if name == '邢伟寅':
    print("寅猪来了，肥猪八戒，猪崽")
    pig = input("请输入你的体重(公斤)")
    tizhong = pig*1000
    print("你的体重:" + tizhong + "你好重啊！")
elif name == '查乖乖':
    print("查乖乖大王驾到！")
else:
    print("好的，看来你不是寅猪，也不是查乖乖，我们继续")
time.sleep(2)
print("新闻！")
time.sleep(3)
print("名为:" + name + "的家门口，地址:" + addr + "！着火啦！快去灭火，消防员已经赶到！")
time.sleep(4)
print("让我猜猜你的年龄！")
time.sleep(1)
print("你的年龄:" + age)
if age < '12':
    print("小学生！你好！")
elif age < '20':
    print("年轻人！奋斗吧！")
elif age < '30':
    print("努力工作！创造更美好的未来！")
elif age < '40':
    print("中年了，注意多喝水，工作完了要注意休息哦！")
elif age < '60':
    print("快退休了！快解放了！很快了！")
elif age < '70':
    print("恭喜你，退休了，环游世界吧！")
elif age < '90':
    print("人老了，让儿女陪陪你，注意休息保养！")
elif age > '90':
    print("太老了，请在家在医院修养")
time.sleep(6)
#调用OS库，输出信息
print("让我看看你的IP信息(滑稽)")
time.sleep(2)
os.system("ifconfig")
time.sleep(1)
os.system('echo "牛逼不？马牛逼！"')
#调用Time库
print("我先休息3秒")
time.sleep(3)
print("手机爆炸程序，即将启动")
time.sleep(4)
for i in range(101):
  print( "\r{:3%}".format(i))
time.sleep(1)
print("啊哈，好玩的")
#next
ayp = input("你是猪吗？(是or不是)")
if ayp == '是':
    print("你承认了，恭喜你，" + name + "Fatpig")
elif ayp == '不是':
    print("??你敢说你不是猪？肥" + name + "，下次一定说！")
else:
    print("你是智障么？是还是不是？字都不会打？你特么打的什么东西:" + ayp + "！给我认真点:" + name)
time.sleep(5)
print("你刚刚说的你" + ayp + "猪")
time.sleep(2)
print("电话轰炸系统，轰炸电话:" + phone + "已经开始轰炸，请稍后...")
time.sleep(3)
print("给你说个恐怖的故事:我其实就在你身后，转身往后看")
