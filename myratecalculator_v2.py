INTEREST_RATE = 0.035

year = 0
count = 0
withdraw = 0
deposit = 0

while True:
    print("==============menu=================")
    print("a) how much is your deposit?")
    print("b) how long do you want to deposit?")
    print("c) display your future balance")
    print("d) analyze your balance")
    print("e) how much is your withdraw per year?")
    print("q) quit")

    
    command = input("please select the menu:")
    if command == "q":
        print("Goodbye")
        break
            
    if command == "a":
        while True:
            deposit = input("how much is your deposit?")
            if deposit.isdigit():
                deposit = int(deposit)
                break
            else:
                print("your deposit must be a positive integer.")
                        
    if command == "b":
        while True:
            year = input("how long do you deposit?")
            if year.isdigit():
                year = int(year)
                break
            else:
                print("year must be a positive integer.")
    
    if command == "c":
            balance = deposit
            count = 0
            for i in range(year):
                if balance - withdraw > 0:
                    balance = balance * (1 + INTEREST_RATE) - withdraw
                    count = count + 1
                    print(f"year {count:>2d}: ${balance:.2f}")
                else:
                    print("balance is not enough for withdraw:", balance)
                    break
        
    if command == "d":
        balance = deposit
        count = 0
        while True:
            if balance <= deposit * 2: # ??? why withdraw not added
                balance = balance * (1 + INTEREST_RATE)
                count = count + 1
            else:
                break
        print(f"It will take {count} years for your deposit to be doubled. After that, your balance will be ${balance:.2f}.")
    
    if command == "e":
        while True:
            withdraw = input("how much do you withdraw per year?")
            if withdraw.isdigit():
                withdraw = int(withdraw)
                break
            else:
                print("your withdraw must be a positive integer.")