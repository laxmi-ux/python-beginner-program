'''
s=set()
print(s,type(s))
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
'''

s1={3,4,5,6,7,10,9,8,1,2,1,2}
#print(s1)

s2={1,2,3,4,12,13,11}
s3={14,15}
#print(s1.clear())

print(s1.union(s2).union(s3))

print(s1.intersection(s2))
s1.pop()
print(s1)
s1.remove(8)
print(s1)