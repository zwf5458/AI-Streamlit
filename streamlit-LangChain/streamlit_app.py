from collections import namedtuple  # 导入 namedtuple 模块用于创建命名元组
import altair as alt  # 导入 Altair 库用于创建可视化图表
import math  # 导入 math 模块用于数学计算
import pandas as pd  # 导入 pandas 库用于数据处理和分析
import streamlit as st  # 导入 Streamlit 库用于构建交互式网络应用

"""
# Welcome to Streamlit!  欢迎来到Streamlit！

编辑/streamlit_app.py以按照您的意愿自定义此应用程序 :heart:
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

如果您有任何问题，请查看我们的文档和社区论坛。
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

同时，以下是使用几行代码可以实现的示例:
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')  # 创建一个名为 Point 的命名元组，用于表示螺旋图案中的每个点的坐标
    data = []  # 创建一个空列表，用于存储生成的点的坐标数据

    points_per_turn = total_points / num_turns  # 计算每个转弯中生成的点的数量

    # 循环生成螺旋图案中的每个点的坐标
    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)  # 计算当前点所在的转弯和在转弯中的索引
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn  # 计算当前点的角度
        radius = curr_point_num / total_points  # 计算当前点的半径
        x = radius * math.cos(angle)  # 计算当前点的 x 坐标
        y = radius * math.sin(angle)  # 计算当前点的 y 坐标
        data.append(Point(x, y))  # 将当前点的坐标添加到 data 列表中

    # 使用 Altair 创建一个图表，并将生成的点的坐标数据传递给图表
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

'''
这段代码使用 Streamlit 和 Altair 库生成一个螺旋图案。下面是代码的功能注释：

total_points 和 num_turns 是通过滑块选择的用户输入，分别表示螺旋图案中的点的总数和转弯的次数。
Point 是一个命名元组，用于表示螺旋图案中的每个点的坐标。
data 是一个空列表，用于存储生成的点的坐标数据。
points_per_turn 是每个转弯中生成的点的数量，通过将总点数除以转弯次数得到。
使用循环生成螺旋图案中的每个点的坐标。通过计算当前点所在的转弯和在转弯中的索引，以及角度和半径，计算出每个点的具体坐标，并将其添加到 data 列表中。
使用 Altair 创建一个图表，并将生成的点的坐标数据传递给图表。图表使用圆形标记，具有指定的颜色和透明度，并将 x 和 y 坐标进行编码。
最终，使用 st.altair_chart 将图表显示在 Streamlit 应用程序中。
'''
