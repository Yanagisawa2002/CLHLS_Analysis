import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# 假设 df 是你的 DataFrame
df = pd.read_csv('0007.tsv',sep='\t', low_memory=False)  # 如果你需要从文件中读取 DataFrame

cols = df.columns[:30]  # 选择前30列

missing_data = df[cols].isnull()

# 创建颜色映射
colormap = ListedColormap(['#000099', '#ffff00'])

# 使用 imshow 来绘制热图，'nearest'插值方式保证每个数据点显示为一个块
plt.imshow(missing_data, interpolation='nearest', cmap=colormap)

# 添加颜色条
plt.colorbar()

# 添加标签
plt.xticks(ticks=np.arange(len(cols)), labels=cols, rotation=90)
plt.yticks(ticks=np.arange(len(df.index)), labels=df.index)

plt.show()  # 显示图形
