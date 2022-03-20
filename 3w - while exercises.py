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
