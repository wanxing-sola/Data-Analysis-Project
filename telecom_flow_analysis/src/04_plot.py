import pandas as pd
import matplotlib.pyplot as plt
import os

# 解决中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取清洗后原始数据
df = pd.read_csv("D:/telecom_flow_analysis/data/processed/clean_telecom.csv")
# 读取正确统计文件
fee_stat = pd.read_csv("D:/telecom_flow_analysis/result/fee_stat.csv")
area_stat = pd.read_csv("D:/telecom_flow_analysis/result/area_stat.csv")

# 图1：各消费分层平均使用时长柱状图
plt.figure(figsize=(10, 4))
plt.bar(fee_stat["消费分层"], fee_stat["平均使用时长"])
plt.title("各消费分层用户月均使用时长对比")
plt.xlabel("消费分层")
plt.ylabel("平均使用分钟")
plt.savefig("D:/telecom_flow_analysis/result/时长对比图.png")
plt.show()

# 图2：不同地域客户流失率折线图
plt.figure(figsize=(10, 4))
plt.plot(area_stat["地理区域"], area_stat["流失率"], marker="o")
plt.title("不同地域客户流失率")
plt.savefig("D:/telecom_flow_analysis/result/地域流失折线图.png")
plt.show()