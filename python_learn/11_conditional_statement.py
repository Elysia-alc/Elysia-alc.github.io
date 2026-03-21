"""
判断语句

布尔（bool）类型：
True、False
true本质上是一个数字记作1
false本质上是一个数字记作0

比较运算符：
==  判断内容是否相等，满足为True，否则为False  如a = 3，b = 5，则a == b 结果为False
!=  判断内容是否不等，满足为True，否则为False  如a = 3，b = 5，则a != b 结果为True
>   判断左边是否大于右边，满足为True，否则为False  如a = 3，b = 5，则a > b 结果为False
<   判断左边是否小于右边，满足为True，否则为False  如a = 3，b = 5，则a < b 结果为True
>=  判断左边是否大于等于右边，满足为True，否则为False  如a = 3，b = 5，则a >= b 结果为False
<=  判断左边是否小于等于右边，满足为True，否则为False  如a = 3，b = 5，则a <= b 结果为True
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1的值是{bool_1}，类型是{type(bool_1)}")
print(f"bool_2的值是{bool_2}，类型是{type(bool_2)}")
# 比较运算符的使用
num1 = 10
num2 = 10
print(f"num1与num2比较的结果是：{num1 == num2}")

num_a = 5
num_b = 10
print(f"num_a与num_b比较的结果为：{num_a == num_b}")

# if语句的使用
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已经成年了")  # if语句的缩进为4个空格
else:
    print("您还未成年")
print("程序结束")

# 通过input语句获取键盘输入的身高
# 判断身高是否超过120cm,并通过print给出提示信息。
height = int(input("请输入您的身高（cm）："))
print("欢迎来到动物园。")
if height > 120:
    print("您的身高超过120cm，游玩需购票10元。")
else:
    print("您的身高未超过120cm，游玩免费。")
print("祝您玩的开心！")

# if...elif...else语句的使用
height_1 = int(input("请输入您的身高（cm）："))
vip_level = int(input("请输入您的VIP等级（1-3级）："))
print("欢迎来到动物园。")
if height_1 < 120:
    print("您的身高未超过120cm，游玩免费。")
elif vip_level >= 2:  # 第二个条件判断，如果第一个条件满足，则不会执行该条件判断
    print("您的VIP等级为2级或以上，游玩免费。")
else:
    print("您的身高超过120cm，游玩需购票10元。")
print("祝您玩的开心！")
