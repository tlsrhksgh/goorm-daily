# 함수를 이용한 열 단위 결합 (combine)

# DataFrame.combine(other, func, fill_value=None, overwrite=True, **kwargs)
## 개요
## DataFrame.combine() 메서드는 두 개의 DataFrame을 결합할 때 사용자 정의 함수를 적용하여 열 단위로 결합할 수 있도록 합니다. 이 메서드는 각 열에 대해 지정된 함수를 적용하여 새로운 값을 생성합니다.

import pandas as pd
import numpy as np

# 예제 데이터 생성
n=np.nan
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[1,3,4],
         [n,8,2],
         [2,6,7]]
data2 = [[7,2,3],
         [2,4,2],
         [3,1,5]]
# df1은 결측치(np.nan)가 포함된 DataFrame이기 때문에 전체 컬럼(dtype)이 float로 강제 변환됨.
df1 = pd.DataFrame(data1,row,col) 
df2 = pd.DataFrame(data2,row,col)

# func인수에 np.maximum을 입력하여 df1과 df2의 요소를 비교, 큰 값으로 결합
# print(df1.combine(df2,np.maximum))

#fill_value 인수를 사용하여 결측치를 특정 값으로 대체한 후 결합. 
# col1, row2의 결측치가 9로 대체되어 df2의 값 2와 비교됨.
# print(df1.combine(df2,np.maximum,fill_value=9))

#overwrite 인수는 기본값이 True로 설정되어 있어, df1의 값이 존재하는 경우 df2의 값을 덮어씀.
# overwrite=False로 설정하면 df1의 값이 존재하는 경우 df2의 값을 사용
col3 = ['col1','col2']
row3 = ['row1','row2']
data3 = [[1,2],
         [3,4]]
df3 = pd.DataFrame(data3, row3, col3)
print(df1.combine(df3, np.maximum, overwrite=False))

### combine_first ###
# DataFrame.combine_first(other) 메서드는 두 개의 DataFrame을 
# 결합할 때 첫 번째(self) DataFrame의 결측치를 두 번째 DataFrame의 값으로 채우는 데 사용됩니다.
# 즉, 첫 번째 DataFrame의 값이 존재하면 그 값을 유지하고, 
# 결측치인 경우에만 두 번째 DataFrame의 값을 사용합니다.
col4 = ['col1','col2','col3']
row4 = ['row1','row2','row3']
data4 = [[n,n,1],
         [n,n,1],
         [1,1,1]]
data5 = [[2,2,2],
         [2,n,2],
         [2,1,2]]
df4 = pd.DataFrame(data4, row4, col4)
df5 = pd.DataFrame(data5, row4, col4)
print(df4.combine_first(df5))
