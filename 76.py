'''

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''
import datetime

# Va de abajo hacia arriba
# ejemplo hasta el 4:
# 1 + 1 + 1 + 1
# 2 + 1 + 1
# 2 + 2
# 3 + 1
def p76(maxi, maxi_total, init = [0]):
    for n in range(1, maxi + 1):
        init[-1] = n
        diff = maxi_total - sum(init)
        if diff < 0:
            break
        if diff == 0:
            #print(init)
            global Counter
            Counter += 1
        else:
            new_arr = init.copy()
            new_arr.append(0)
            p76(n, maxi_total,init= new_arr)
tt1 = datetime.datetime.now()
number = int(input('Ingrese numero: '))
#number = 8
Counter = -1
p76(number, number)#, init=[3, 3, 3])
print(Counter)
tt2 = datetime.datetime.now()
print('Execute time:', tt2-tt1)





#def optimized67(max):

'''
7
6 + 1
5 + 2
5 + 1 + 1
4 + 3
4 + 2 + 1
4 + 1 + 1 + 1
3 + 3 + 1
3 + 2 + 2
3 + 2 + 1 + 1
3 + 1 + 1 + 1 + 1
2 + 2 + 2 + 1
2 + 2 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1

6
5 + 1
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1

5
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1



3 + 3 + 3 + 1
3 + 3 + 2 + 2
3 + 3 + 2 + 1 + 1
3 + 3 + 1 + 1 + 1 + 1
3 + 2 + 2 + 2 + 1
3 + 2 + 2 + 1 + 1 + 1
3 + 2 + 1 + 1 + 1 + 1 + 1
3 + 1 + 1 + 1 + 1 + 1 + 1 + 1
2 + 2 + 1 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1


[11, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[11, 2, 1, 1, 1, 1, 1, 1, 1]
[11, 2, 2, 1, 1, 1, 1, 1]
[11, 2, 2, 2, 1, 1, 1]
[11, 2, 2, 2, 2, 1]
[11, 3, 1, 1, 1, 1, 1, 1]
[11, 3, 2, 1, 1, 1, 1]
[11, 3, 2, 2, 1, 1]
[11, 3, 2, 2, 2]
[11, 3, 3, 1, 1, 1]
[11, 3, 3, 2, 1]
[11, 3, 3, 3]
[11, 4, 1, 1, 1, 1, 1]
[11, 4, 2, 1, 1, 1]
[11, 4, 2, 2, 1]
[11, 4, 3, 1, 1]
[11, 4, 3, 2]
[11, 4, 4, 1]
[11, 5, 1, 1, 1, 1]
[11, 5, 2, 1, 1]
[11, 5, 2, 2]
[11, 5, 3, 1]
[11, 5, 4]
[11, 6, 1, 1, 1]
[11, 6, 2, 1]
[11, 6, 3]
[11, 7, 1, 1]
[11, 7, 2]
[11, 8, 1]
[11, 9]





[50]
204225
Execute time: 0:00:13.167738
'''
