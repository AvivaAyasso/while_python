1
num = 1
while num <= 20:
    if num % 2 != 0:
     print(num)
    num = num + 1

3
number = int(input("enter a number"))
while number <= 20:
    if number % 2 != 0:
        print(number)
    number = number + 1

5
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


