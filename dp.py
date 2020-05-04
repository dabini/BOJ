import sys

def find(words):
    tmp = 0
    while words:
        cnt = 0
        check = []
        for word in words:
            if word not in check:
                check.append(word)
                cnt += len(word)
            if cnt + len(check)-1 > W:
                k = check.pop()
                cnt -= len(k)
                check.pop()
                break

        tmp += (W-cnt-(len(check)-1)) ** 3
        for c in check:
            words.remove(c)
    return tmp

input = sys.stdin.readline

W = int(input())
words = list(map(str, input().split()))
print(find(words))