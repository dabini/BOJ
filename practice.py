# def solution(answers):
#     num_1 = [1, 2, 3, 4, 5]
#     num_2 = [2, 1, 2, 3, 2,  4, 2, 5]
#     num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     tmp = [0] * 4
#     answer = []
#     for i in range(len(answers)):
#         if answers[i] == num_1[i%5]:
#             tmp[1] += 1
#         if answers[i] == num_2[i%10]:
#             tmp[2] += 1
#         if answers[i] == num_3[i%10]:
#             tmp[3] += 1
#     for i in range(1, 4):
#         if tmp[i] == max(tmp):
#             answer.append(i)
#     return answer
#
# solution(input())


from itertools import permutations


def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    test = []

    for i in range(len(numbers)):
        case = list(set(map(''.join, permutations(numbers, i + 1))))
        for j, number in enumerate(case):
            test.append(int(number))
    test = list(set(test))
    for i, number in enumerate(test):
        if isPrime(number):
            answer += 1
    return answer
numbers = input()
print(solution(numbers))