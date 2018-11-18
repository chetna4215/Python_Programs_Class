"""
1) Looping Statement
2) Conditional and looping statement

Assignment
1. Create a Matrix
2. Matrix multiplication
3. spiral matrix rotation
4. shift elements in matrix

1)                  2)              3)              4)
* * * * *           1 1 1 1 1       0 0 0 0 0       0
* * * * *           1 1 1 1 1       1 1 1 1 1       1 0
* * * * *           1 1 1 1 1       0 0 0 0 0       0 1 0
* * * * *           1 1 1 1 1       1 1 1 1 1       1 0 1 0
* * * * *           1 1 1 1 1       0 0 0 0 0       0 1 0 1 0
5)                  6)              7)                  8)
1                   1 2 3 4 5       01 02 03 04 05      1 0 1 0 1
1 0                 1 2 3 4 5       06 07 08 09 10      0 1 0 1
1 0 1               1 2 3 4 5       11 12 13 14 15      1 0 1
1 0 1 0             1 2 3 4 5       16 17 18 19 20      0 1
1 0 1 0 1           1 2 3 4 5       21 22 23 24 25      1
9)                  10)             11)                 12)
      1             * *   * *       01 02 03 04 05      2
   1    1           *  * *  *       05 04 03 02 01      2 4
  1   1   1         *   *   *       02 04 06 08 10      2 4 8
1   1   1   1       *       *       10 08 06 04 02      2 4 8 16
                    *       *       03 06 09 12 15      2 4 8 16 32
                                    15 12 09 06 03      2 4 8 16 32 64
13) *       *
    * *   * *
    *   *   *
    *       *
    *       *

"""


# n = 1
# while true:
  #  if n==10:
   #     break
   # print(n)

# for i in range(0,5):
 #   for j in range(0,5):
  #      print("*", end=" ")
   # print("\n")

# for printing in one line
# l =[]
# for i in range(0,5):
  #  for j in l:
   #     print("*")

for i in range(0,5):
    print(" * " *5)

for i in range(0,5):
    print(" 1 " *5)

for i in range(0,5):
    n=1
    for j in range(0,i+1):
        print(n, end=" ")
        n=n+1
    print("\n")

for i in range(0,5):
    n=1
    for j in range(0,5):
        print(n,end=" ")
        n=n+1
    print("\n")


for i in range(0,5):
    num=i%2
    for j in range(0,5):
        print(num, end=" ")
    print("\n")

for i in range(0,5):
    num=i%2
    for j in range(0,i+1):
        num=j%2
        print(num, end=" ")
    print("\n")

for i in range(0,5):
    for j in range(0,i+1):
        if(j%2==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("\r")

for i in range(0,5):
    for j in range(0,i+1):
        if(i%2==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("\r")


for i in range(0,5):
    num = i % 2
    for j in range(0,i+1):
        print(num, end=" ")
        num=j%2
        # for k in range(0,j):
        #     n=0
        #     print(n, end=" ")
        #     n=n+1
    print("\r")


num=0
for i in range(0,5):
    for j in range(0,i+1):
        print(num%2, end=" ")
        num+=1
    if i%2==1:
        num+=1
    print("")

num=1
for i in range(0,5):
    for j in range(0,5):
        print("{:02d}".format(num), end=" ")
        num+=1
    print(" ")

for i in range(0,5):
    for j in range(5,i,-1):
        print("*", end=" ")
    print("")

for i in range(5,0,-1):
    for j in range(i, 0, -1):
        print(j%2, end=" ")
    print(" ")
