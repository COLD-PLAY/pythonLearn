from wxpy import *
import requests

# 创建一个机器人对象，也就是你的微信
robot = Bot()
# API
# 得到好友对象，有name，city，sex等属性
# my_chats = robot.chats() # 得到所有聊天对象（好友、群聊和公众号列表）的合集
# my_friends = robot.friends() # 得到好友对象的合集
# my_groups = robot.groupd() # 得到群聊对象的合集
# my_mps = robot.mps() # 得到公众号的合集
# # 这些合集都有search() 方法，可以传入名字、
# # 性别等参数找到符合条件的对象并返回一个 “list”

# friend = my_friends.search(name = '米西狮子', sex = MALE)[0] # 等等参数
# friend.send('hhhhhhh') # 还有一些方法可以发送图片等文件

# for friend in my_friends:
# 	print(friend.name)

# 注册器
@robot.register()
def reply_message(msg):
	# 打印收到的所有消息
	print(msg)
	if msg.chat in robot.friends() and msg.chat.name != '东惠':
		url = 'http://www.tuling123.com/openapi/api?key=4d8310b6007c454c9fab02bd2923e8fb&info=' + msg.text
		# 拿到json 的text 做回复内容
		response = '自动回复： ' + requests.get(url).json()['text']
		print(response)
		msg.chat.send(response)
		# 如果有人在群里面@ 我
	elif (isinstance(msg.chat, Group) and msg.is_at):
		# 从我的图灵机器人拿到回复内容，需要注册并拿到key
		url = 'http://www.tuling123.com/openapi/api?key=4d8310b6007c454c9fab02bd2923e8fb&info=' + msg.text[msg.text.find('狮子') + 2:]
		response = '自动回复： ' + requests.get(url).json()['text']
		# 打印自动回复的消息
		print(response)
		# 发送消息
		msg.chat.send(response)

# 开始监听
robot.start()

# http://www.tuling123.com/openapi/api?key=4d8310b6007c454c9fab02bd2923e8fb&info
