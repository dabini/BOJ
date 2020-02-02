dial = [[], [], ['A','B' ,'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
        ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

inp = list(input())
out = 0

for i in inp:
    for j in range(1, 10):
        if i in dial[j]:
            out += j + 1
print(out)