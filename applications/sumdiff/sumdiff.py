"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


sums = {}
diffs = {}

for x in q:
    for y in q:
        s = f(x) + f(y)
        if s not in sums:
            sums[s] = [(x, y)]
        else:
            sums[s].append((x, y))

        d = f(x) - f(y)
        if d not in diffs:
            diffs[d] = [(x, y)]
        else:
            diffs[d].append((x, y))

for skey in sums:
    for dkey in diffs:
        for svalue in sums[skey]:
            for dvalue in diffs[dkey]:
                a, b, c, d = svalue[0], svalue[1], dvalue[0], dvalue[1]
                if f(a) + f(b) == f(c) - f(d):
                    print(
                        f"f({a}) + f({b}) = f({c}) - f({d})"
                        f"    {f(a)} + {f(b)} = {f(c)} - {f(d)}"
                    )
