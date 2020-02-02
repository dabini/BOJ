N = int(input())

for n in range(N):
    lst = [0, 0, 0, 0]
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = A[1:]
    B = B[1:]
    if A.count(4) >  B.count(4):
        print("A")
    elif A.count(4) ==  B.count(4):
        if A.count(3) > B.count(3):
            print("A")
        elif A.count(3) == B.count(3):
            if A.count(2) > B.count(2):
                print("A")
            elif A.count(2) == B.count(2):
                if A.count(1) > B.count(1):
                    print("A")
                elif A.count(1) == B.count(1):
                    print("D")
                else:
                    print("B")
            else:
                print("B")
        else:
            print("B")
    else:
        print("B")