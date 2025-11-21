import random
target=random.randint(1,100)
attempt=1

while(True):
    print("---------------")
    print(f"Attempt number: {attempt}")
    user=int(input("Enter the number betweeen 1-100:"))
    if user>target:
        print("Target is lower")
    elif user<target:
        print("Target is higher")
    elif user== target:
        print(f"Congrats, the number was: {target}")
        print(f"you found it in {attempt} attempts ")
        break
    attempt+=1
