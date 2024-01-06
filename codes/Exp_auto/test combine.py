import pandas as pd

# 创建第一个示例 DataFrame
data_A_n = {
    'A_n_温度1': [20, 22, 24, 23, 5],
    'A_n_温度2': [25, 27, 29, 22, 4]
}
all_A_n_x_ys_df = pd.DataFrame(data_A_n)

# 创建第二个示例 DataFrame
data_R_n = {
    'R_n_温度1': [30, 32, 34],
    'R_n_温度2': [35, 37, 39]
}
all_R_n_x_ys_df = pd.DataFrame(data_R_n)

# 使用 pd.concat 水平合并这两个 DataFrame
df_combined_df_all_A_n_x_ys_df = pd.concat([all_A_n_x_ys_df, all_R_n_x_ys_df], axis=1)

# 打印合并后的 DataFrame
print(df_combined_df_all_A_n_x_ys_df)
print(type(data_A_n))
print(type(all_A_n_x_ys_df))