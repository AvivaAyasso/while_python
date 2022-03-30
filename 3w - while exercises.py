#3
guess=int(input("guess number"))
while guess<9 and  guess>1:
    num=int(input("enter number"))
    if guess==num:
        print("well guessed")
        guess=+1

#11
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

#12
#Find the negative number and change the numbers next to it to negative
l = [1, 8, 12, 48, -3, 14, 22, 15]
i = 0
while i < len(l):
    if l [i] < 0:
        if i > 0:
            l[i-1] *=-1
        if i < len(l)-1:
            l[i+1]*=-1
        i += 1
    i +=1
print(l)
