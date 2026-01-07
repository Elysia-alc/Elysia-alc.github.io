"""
数据类型
string（字符串）、int（整数）、float（浮点数）
"""

# type()语句
# 用于查看数据类型
print(type(1))
print(type(13.14))
print(type("hello"))

int_type = type(123)
float_type = type(13.14)
string_type = type("hello")
print(int_type)
print(float_type)
print(string_type)

name = "Alice"
name_type = type(name)
print(name_type)

# 数据类型转换
# int()、float()、str()
str_num = int("100")
print(type(str_num), str_num)

float_str = str(13.14)
print(type(float_str), float_str)

# 整数与浮点数之间转换
int_float = float(100)
print(type(int_float), int_float)
# 浮点数转整数会丢失精度
float_int = int(13.14)
print(type(float_int), float_int)
