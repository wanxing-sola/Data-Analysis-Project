import pandas as pd
import os

# 读取清洗后数据
df = pd.read_csv("D:/telecom_flow_analysis/data/processed/clean_telecom.csv")

# 1. 按消费分层统计（唯一自建分层字段）
fee_stat = df.groupby("消费分层").agg(
    平均使用时长=("过去三个月的平均每月使用分钟数", "mean"),
    平均月话费=("平均月费用", "mean"),
    用户数量=("客户ID", "count"),
    流失人数=("是否流失", "sum")
).reset_index()
print("消费分层维度统计：")
print(fee_stat)

# 2. 按地理区域统计
area_stat = df.groupby("地理区域").agg(
    平均使用时长=("过去三个月的平均每月使用分钟数", "mean"),
    流失率=("是否流失", "mean")
).reset_index()
print("地域维度统计：")
print(area_stat)

# 自动创建result文件夹
result_dir = "D:/telecom_flow_analysis/result"
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

# 保存统计结果
fee_stat.to_csv("D:/telecom_flow_analysis/result/fee_stat.csv", index=False, encoding="utf-8")
area_stat.to_csv("D:/telecom_flow_analysis/result/area_stat.csv", index=False, encoding="utf-8")
print("统计表格已保存至result文件夹")