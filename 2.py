def fibbo(max):
    s = [1,2]
    while sum(s[-2:])<max:
        s.append(sum(s[-2:]))
    return sum([n for n in s if n%2 is 0  ])


print(fibbo(4000000))