word = input()
check = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
for w in word:
    if w in check:
        word = word.replace(w, "")
print(word)