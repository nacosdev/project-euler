
def find_triplet(s):
        found = False
        a = 0
        b = 0
        c = 0
        for a in range(1, int(s / 3)):
                for b in range(a, int(s/2)):
                        c = s - a - b
                        if ((a * a + b * b) == c * c):
                                found = True
                                break
                if (found):
                        break
        return a,b,c

a,b,c = find_triplet(1000)

print(a,b,c)
print('Prod: {}'.format(a*b*c))