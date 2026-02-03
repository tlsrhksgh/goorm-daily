# 파이썬을 이용한 선형 및 비선형 추세선
# 선형 최소제곱법(OLS) 회귀 추세선 또는 비선형 국소 가중 산점도 평활화(LOWESS) 추세선을 산점도에 추가합니다.

# OLS(Ordinary Least Squares)
# OLS란, Ordinary Least Squares의 약자로, 오차의 제곱을 최소화 하는 β와 α를 추정하는 방식이다. 
# 이해가 안되서 좀 더 쉬운 예제를 보아하니, 점들이 잔뜩 찍혀 있을 때, 그 점들 사이를 가장 잘 통과하는 직선 하나를 고르는 방법이라고 한다! 일단 이정도로만..
# α (알파) : 기울기 (x가 1 증가할 때 y가 얼마나 변하는지?)
# β (베타) : 시작점 (x가 0일 때 y가 어디서 시작하는지?)

import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", 
                 y="tip", 
                 facet_col="smoker", # 흡연자 / 비흡연자 그래프를 나눔
                 color="sex", 
                 trendline="ols")
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.query("sex == 'Male' and smoker == 'Yes'").px_fit_results.iloc[0].summary()


