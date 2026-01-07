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