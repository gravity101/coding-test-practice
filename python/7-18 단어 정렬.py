import sys

sys.stdin = open("C:/input/카드정렬.txt", 'r')
n = int(input())

word = {str(input()) for _ in range(n)}

word = sorted(word, key=lambda x : x[0])

print(sorted(word, key=lambda x : len(x)))