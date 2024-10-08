from pytrends.request import TrendReq

# 连接到 Google Trends
pytrends = TrendReq(hl='zh-CN', tz=360)  # 设置语言为中文

# 获取每日搜索趋势
trending_searches_df = pytrends.trending_searches(pn='united_states')  # 使用美国作为示例

# 打印结果（标题和链接）
for trend in trending_searches_df[0]:
    print(f"热搜标题: {trend}")
    print(f"链接: https://trends.google.com/trends/explore?q={trend}")
    print("***\n")
