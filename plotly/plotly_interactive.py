# import plotly.express as px

# df = px.data.iris()

# fig = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     hover_name="species",
#     hover_data={
#         "sepal_width": True,
#         "sepal_length": True,
#         "petal_length": False
#     }
# )

# fig.show()

## 버튼 (update menus)을 이용한 trace 보이기/숨기기
# import plotly.graph_objects as go

# fig = go.Figure()

# fig.add_trace(go.Scatter(
#     x=[1, 2, 3],
#     y=[10, 20, 30],
#     name="A"    
# ))

# fig.add_trace(go.Scatter(
#     x=[1, 2, 3],
#     y=[30, 20, 10],
#     name="B"
# ))

# fig.update_layout(
#     updatemenus=[
#         dict(
#             buttons=[
#                 dict(label="A만 보기",
#                      method="update",
#                      args=[{"visible": [True, False]}]),
#                 dict(label="B만 보기",
#                      method="update",
#                      args=[{"visible": [False, True]}]),
#                 dict(label="모두",
#                      method="update",
#                      args=[{"visible": [True, True]}])                
#             ]
#         )
#     ]
# )

# fig.show()

## slider를 이용한 시간/단계 인터랙션
import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    animation_frame="species",
)

fig.show()