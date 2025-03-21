for q in range(0, 5):
    for w in range(0, 5):
        print(' * ', end = '')
    print()

for e in range(0, 5):
    for r in range(e, 5):
        print(" * ", end = '')
    print()

for t in range(1, 6):
    for y in range(0, t):
        print(' * ', end = '')
    print()

for i in range(0, 5):
    for x in range(0, 5):
        if i <= x:
            print(' * ', end = '')
        else:
            print('   ', end = '')
    print()

for t in range(1, 6):
    for z in range(5, 0, -1):
        if t < z:
            print('   ', end = '')
        else:
            print(' * ', end = '')
    print()