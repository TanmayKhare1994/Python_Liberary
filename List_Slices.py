# Slices gives the Range of result
Sqaures= [0,11,12,3,4,5,6,7,8,9]

print Sqaures[2:6]
print Sqaures[1:]
print Sqaures[:5]

print Sqaures[::2] #3rd parameter for steps (how many steps for counting)
print Sqaures[0:7:2]

# -itve values
print Sqaures[-6:-1:]
"""
lenn= len(Sqaures)-1
while(lenn>=0):
    print Sqaures[lenn];
    lenn-=1;
 """
print Sqaures.reverse()


