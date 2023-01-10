def pattern(n):
    for i in n:
        print("|", end = " " )
        print("*" * int(i))
n = "01325"
pattern(n)