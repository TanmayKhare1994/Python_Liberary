num = input("Enter the number")
lst = []
def Cpn(k):
    i = 1
    sum = 0
    while (i < k):
        if (i % k == 0):
            sum += i;

        i = i + 1;



for r in range(1, num):
    Cpn(r)

for item in lst:
    print(item)
