cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inp = input()

for i in cro_alpha:
    inp = inp.replace(i, '0')

print(len(inp))