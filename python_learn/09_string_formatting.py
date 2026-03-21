"""
字符串格式化
使用百分号 (%) 进行格式化
%s - 字符串 (str)
%d - 整数 (int)
%f - 浮点数 (float)
"""

name = "张三"
age = 18
height = 1.75
print("我的名字是%s,年龄是%d,身高是%f。" % (name, age, height))

# 字符串格式化精度控制
# m，控制宽度，要求是数字，设置的宽度小于字符串实际宽度时无效
# .n，小数点后精度，要求是数字，会进行四舍五入
print("我的名字是%s，年龄是%2d，身高是%.2f。" % (name, age, height))

# 字符串格式化 - 快速写法
print(f"我的名字是{name}，年龄是{age}，身高是{height:.2f}。")

# 字符串格式化 - 表达式的格式化
print("我的名字是%s，年龄是%d，身高是%.2f" % (name, age + 1, height + 0.05))
print(f"我的名字是{name}，年龄是{age + 1}，身高是{height + 0.05:.2f}。")

# 定义如下变量：
# name_company，公司名
# stock_price，当前股价
# stock_code，股票代码
# stock_price_daily_growth_factor，股票每日增长系数，浮点数类型，比如1.2
# growth_days，增长天数
# 计算，经过growth_days天的增长后，股价达到了多少钱
# 使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数。
name_company = "xx公司"  # 公司名
stock_price = 100.00  # 当前股价
stock_code = "000001"  # 股票代码
stock_price_daily_growth_factor = 1.2  # 股票每日增长系数
growth_days = 10  # 增长天数
final_stock_price = stock_price * (stock_price_daily_growth_factor**growth_days)
print(
    f"公司名：{name_company}，股票代码：{stock_code}，当前股价：{stock_price}，每日增长系数：{stock_price_daily_growth_factor}，经过{growth_days}天的增长后，股价达到了{final_stock_price:.2f}"
)
