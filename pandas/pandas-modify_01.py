# 열 삽입(insert column) - DataFrame에 새로운 열을 추가하는 방법
import pandas as pd 
import numpy as np
# 예제 데이터 생성
data = [[1,2,3],[4,5,6],[7,8,9]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']

df = pd.DataFrame(data=data, index=row, columns=col)
df.insert(3, 'col4', [10,11,12]) # loc=3에 'col4' 열 삽입
df.insert(3, 'col3', [10,11,12], allow_duplicates=True) # loc=3에 'col3' 열 삽입(중복 허용)False면 오류 발생
print(df)

# 열 삭제(delete column) - DataFrame에서 열을 삭제하는 방법
item = df.pop('col3') # 'col3' 열을 DataFrame에서 제거하고 해당 열을 반환
print(item)




