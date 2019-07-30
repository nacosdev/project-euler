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
lista = []
maxi_total = 7
def p76(init):
    maxi_rel = maxi_total - sum(init)
    for n in range(maxi_rel - 1, 0, -1):

        rest = maxi_rel - n
        if rest <= n:
            new_arr = [n, rest]
            if sum(init + new_arr) == maxi_total:
                lista.append(init + [n, rest])
            if rest > 1:
                new_arr = init + [n] + [rest - 1] + [1]
                if rest - 1 != 1:
                    p76(new_arr)
                lista.append(new_arr)

        else:
            new_arr = [n, n]
            if sum(init + new_arr) == maxi_total:
                lista.append(init + [n, rest])
                if n > 1:
                    p76(init + [n - 1] + [1])
            else:
                if sum(init + new_arr + [n]) > maxi_total:
                    diff = maxi_total - sum (init + new_arr)
                    lista.append(init + new_arr + [diff])
                    p76(init + new_arr + [diff])
                if sum(init + new_arr + [n]) == maxi_total:
                    lista.append(init + new_arr + [n])
                    if n > 1:
                        p76(init + new_arr + [diff-1] + [1])
                if sum(init + new_arr + [n]) < maxi_total:
                    p76(init + new_arr + [n])



'''
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

'''
print(p76([]))
for item in lista:
    print(item)


#for x in range(1, 0, -1):
    #print(x)