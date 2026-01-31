
# truncate 메서드는 행이나 열에 대해 특정 범위로 잘라내는 기능을 제공합니다.
import pandas as pd
import numpy as np
# 예제 데이터 생성 5x5 DataFrame
data = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
col = ['col1','col2','col3','col4','col5']
row = ['row1','row2','row3','row4','row5']

df = pd.DataFrame(data=data, index=row, columns=col)
print("Original DataFrame:")
print(df)
# 행 자르기(row2 이전, row3 이후 잘라내기)
trauncated_rows = df.truncate(before='row2', after='row4')
print("After Truncate DataFrame:")
print(trauncated_rows)

