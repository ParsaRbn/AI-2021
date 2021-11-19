from random import *
N = 8

def checkAttack(i,j):
        for k in arr:
                if k ==i:
                        return False
        for k in range(0,j):
                row = arr[k]
                col = k

                ans1 = row - col
                # ans1 = abs(ans1)
                ans2 = i-j
                # ans2 = abs(ans2)


                if ans1 == ans2:
                        return False
                ans1 = row + col
                ans2 = i + j
                if ans1 == ans2:
                        return False
        return True


queen =[
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        ]
arr = [ -1, -1, -1, -1, -1, -1, -1, -1 ]
flag = 0
flag2 = 0
j = 0
i = 0
while(j<N):
        flag = 0
        i = 0
        while(i<N):
                if flag2 == 1:
                        ans = arr[j]
                        queen[ans][j] = 0
                        i = ans + 1
                        arr[j] = -1
                        if i>=N:
                                continue
                        flag2 = 0
                if i==0 and j==0:
                        i = randint(0,7)
                        # i=2
                        queen[i][j]= 1
                        arr[0]=i
                        flag = 1
                        i = i+1
                        break
                else:
                        check = checkAttack(i,j) #2,1
                        if check == True:
                                queen[i][j]=1
                                arr[j] = i
                                flag = 1
                                i = i+1
                                break
                        else:
                                i = i+1
        if flag ==0:
                j = j - 1
                flag2 = 1
        else:
                j = j + 1
print(queen[0])
print(queen[1])
print(queen[2])
print(queen[3])
print(queen[4])
print(queen[5])
print(queen[6])
print(queen[7])



print("Row indexes:")
print(arr)