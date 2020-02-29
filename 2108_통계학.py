from collections import Counter
def find_num(lst):
    mode_dict = Counter(lst)
    modes = mode_dict.most_common()
    if len(lst) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod
N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

print(round(sum(lst)/len(lst))) #산술평균
print(lst[len(lst)//2]) #중앙값
print(find_num(lst)) #최빈값
print(lst[-1] - lst[0])