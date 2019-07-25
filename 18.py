from collections import defaultdict
import json, datetime

Triangle_string = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

Triangle = []

for index, row in enumerate(Triangle_string.split('\n')):
    row_int = [int(n) for n in row.split(' ')]
    Triangle.append(row_int)



def p18(Rows, deph):
    position = 0
    suma = Rows[0][0]
    for index in range(1,len(Rows)):
        row = Rows[index]
        maxs = defaultdict(int)
        k1 = str(row[position])
        k2 = str(row[position + 1])
        maxs = {}
        maxs[k1] = {'suma' : row[position], 'last_pos': position}
        maxs[k2] = {'suma' : row[position + 1], 'last_pos': position + 1}

        for next_index in range(1,deph):
            try:
                next_row = Rows[next_index + index]
                for k in maxs:
                    if next_row[maxs[k]['last_pos']] > next_row[maxs[k]['last_pos'] + 1]:
                        maxs[k]['suma'] += next_row[maxs[k]['last_pos']]
                    else:
                        maxs[k]['suma'] += next_row[maxs[k]['last_pos'] + 1]
                        maxs[k]['last_pos'] += 1
            except:
                pass
        if maxs[k1]['suma'] < maxs[k2]['suma']:
            position += 1
        suma += row[position]
        print(row[position])
    return suma
tt1 = datetime.datetime.now()
suma = p18(Triangle, 5)
print(suma)
tt2 = datetime.datetime.now()
print('Tardo {} segundos.'.format((tt2-tt1).seconds))
