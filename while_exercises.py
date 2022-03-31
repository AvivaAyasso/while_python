#1
num = 1
while num <= 20:
    if num % 2 != 0:
     print(num)
    num = num + 1

#3
number = int(input("enter a number"))
while number <= 20:
    if number % 2 != 0:
        print(number)
    number = number + 1

#5
guessnum = int(input("please enter a number between 1-1000"))
start = 1
end = 1000
ran = (start+end)//2
while guessnum != ran:
    if guessnum > ran:
        start = end//2
        ran = (start+end)//2
    else:
        end = end // 2
        ran = (start + end)//2
print("found", guessnum)

num1 = 100
while num1 < 250:
    if num1 % 2 != 0:
        print(num1)
    num1 = num1+1

num = 52
while num >= 23:
    print(num)
    num = num - 1

TestScor = int(input("plese enter a score"))
while TestScor != 100:
    print("Must be re-examined")
    TestScor = int(input("plese enter a score"))
    if TestScor == 100:
      print("you rule,enter a scend scor")
      TestScor = int(input("plese enter a score"))

import math
aviva = int(input("plese enter a number"))
while aviva != 10:
    print("Try again")
    aviva = int(input("plese enter a number"))
if aviva == 10:
    print(math.pow(aviva,2))

n = 0
p = false
sum = 0
while n < 32:
    sum += n
    if(sum >= 20) and (p==fase):
        print(n)
        p=true
    n += 1
    print(sum)

num = 1
while num < 21:
    if num %2 != 0:
        print(num)
    num = num+1

l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
    print(l [i] ** 2)
    i += 1