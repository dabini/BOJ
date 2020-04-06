wordx, wordy = map(str, input().split())
arr = [["."]*len(wordx) for _ in range(len(wordy))]
check = False
for x in range(len(wordx)):
    for y in range(len(wordy)):
        if wordy[y] == wordx[x]:
            i, j = x, y
            check = True
            break
    if check:
        break

for b in range(len(wordy)):
    arr[b][i] = wordy[b]
for a in range(len(wordx)):
    arr[j][a] = wordx[a]

for k in range(len(wordy)):
    print("".join(arr[k]))