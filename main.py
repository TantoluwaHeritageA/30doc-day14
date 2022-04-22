
def guess_number():
    attempt = 5
    actual_num = 34
    count = 0
    while attempt > 0:
        guess = int(input("Guess a number from 1 to 50: "))
        if guess == actual_num:
            print(f"correct! you got the answer right in {count} tries")

            break

        else:
            attempt = attempt - 1
            count += 1
            if guess > actual_num:
                print("wrong! The number is lesser than,", guess)
            elif guess < actual_num:
                print("wrong! The number is greater than,", guess)
            if attempt == 0:
                print("Game over !!!!")


guess_number()
