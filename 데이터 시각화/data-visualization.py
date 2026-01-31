import plotly.express as px


df = px.data.iris()
print(type(df))
print(df.shape)
print(df.columns)
print(df.head())

# 산점도 기본 (색으로 분류)
fig = px.scatter(
    df, 
    x="sepal_width", 
    y="sepal_length",
    color="species",
    hover_data=["petal_width", "petal_length"],
    title="Iris Sepal width vs Length"
)
# fig.show()

# 히스토그램
fig = px.histogram(
    df, x="petal_length", color="species",
    nbins=20, barmode="overlay",
    title="Iris: Petal Length Distribution"
)
# fig.show()

# 박스플롯
fig = px.box(
    df, x="species", y="petal_width",
    points="all",
    title="Iris: Petal Width by Species"
)
# fig.show()

# facet(소분면)로 비교
fig = px.scatter(
    df, x="petal_width", y="petal_length", color="species",
    facet_col="species",
    title="Facet Scatter by Species"
)
# fig.show()

# 스타일 수정(Layout/traces)
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.update_traces(marker=dict(size=10, opacity=0.8))
fig.update_layout(
    legend_title_text="Species",
    xaxis_title="Sepal Width",
    yaxis_title="Sepal Length"
)
fig.show()
