import pandas as pd

# 读取数据
df = pd.read_csv("D:/telecom_flow_analysis/data/raw/train.csv")

# 基础查看
print("数据集行数、列数：", df.shape)
print("前5行数据：")
print(df.head())
print("所有字段名：")
print(df.columns.tolist())
print("数据类型：")
print(df.dtypes)
# 查看缺失值
print("每列缺失值数量：")
print(df.isnull().sum())
# 数值字段统计（流量、话费、消费）
print(df.describe())