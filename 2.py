n = 20
guess = None

while guess != n:
    guess = input("Uhádni číslo od 10 do 20")
    guess = int(guess)

    if guess == n:
        print("Správně, uhodl jsi číslo")
        break
    else:
        print("Zkus to znovu")