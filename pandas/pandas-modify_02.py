# 복사 (copy) 메서드를 사용하여 DataFrame 복사하기

# 얕은복사 깊은복사 개념
# shallow copy(얕은 복사): 원본 객체와 복사된 객체가 동일한 데이터에 대한 참조를 공유합니다.
# pandas 3.0부터는Series와 DataFrame 모두 copy(deep=False)에서는
# Copy-on-Write(COW)가 적용되어 수정 시 자동 분리되며, 원본과 사본이 동시에 변경되지는 않습니다.
# 단, numpy에서는 여전히 참조를 공유하므로 주의가 필요합니다.

# deep copy(깊은 복사): 원본 객체와 복사된 객체가 별도의 데이터를 가지게 됩니다.
# 따라서 한쪽에서 데이터를 변경해도 다른 쪽에는 영향을 미치지 않습니다. 

# deep copy와 shallow copy의 차이점
import pandas as pd
import numpy as np
# 예제 데이터 생성
data = [[1,2,3],[4,5,6],[7,8,9]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df1 = pd.DataFrame(data=data, index=row, columns=col)
df2 = df1.copy(deep=True) # deep copy
df3 = df1.copy(deep=False) # shallow copy
# df1의 값을 변경
df1.iloc[0,0] = 100
print("Original DataFrame (df1):")
print(df1)
print("\nDeep Copied DataFrame (df2):")
print(df2)
print("\nShallow Copied DataFrame (df3):")
print(df3)
# df3의 값을 변경
df3.iloc[1,1] = 200
print("\nAfter modifying df3:")
print("Original DataFrame (df1):")
print(df1)