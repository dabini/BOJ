N = int(input())
seat = list(input())

if N+1 - seat.count('L')//2 < N:
    print(N+1 - seat.count('L')//2)
else:
    print(N)