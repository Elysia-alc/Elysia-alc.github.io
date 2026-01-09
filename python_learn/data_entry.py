# 数据输入
# input() 函数用于从控制台获取用户输入的数据，默认以字符串形式返回
# print("who are you ?")
name = input("who are you ?")
print("i know, you are %s." % name)
age = input("how old are you ?")
age = int(age)  # 将输入的字符串转换为整数类型
print("you are %d years old." % age, type(age))

# 定义两个变量，用以获取从键盘输入的内容，并给出提示信息：
# 变量1，变量名：user_name，记录用户名称
# 变量2，变量名：user_type，记录用户类型
user_name = input("请输入您的用户名")
user_type = input("请输入您的用户类型")
print(f"您好：{user_name},您是尊贵的：{user_type}用户，欢迎您的光临。")
