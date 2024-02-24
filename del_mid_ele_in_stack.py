st=[]
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)
vt=[]
while st:
  vt.append(st.pop())
n=len(vt)
target=n//2
for i in range(0,n):
  if i==target:
    continue
  st.append(vt[i])
  
print(st)