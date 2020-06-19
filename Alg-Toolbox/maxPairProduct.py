import sys

num = input()
num = int(num)

List = input()

numList = List.split()

if len(numList) != num:
    print('Number list is incomplete. expecting {} provided {}'.format(num, len(numList)))

numList = list(map(int, numList))
maxA = int(max(numList))
numList.remove(maxA)
maxB = int(max(numList))

print(maxA * maxB)

