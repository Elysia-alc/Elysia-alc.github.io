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
