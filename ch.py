import random

print("угадай число от 1 до 15!")
x = None
a = random.randint(1, 15)

while x != a:
    x = int(input("число: "))
    
    # Эти проверки теперь внутри цикла и срабатывают на каждом шаге
    if x < a:
        print("боольщеее")
    elif x > a:
        print("меньще")

print("правильно!")

