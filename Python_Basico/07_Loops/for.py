for numero in range(1, 6):
    print(numero) # 1, 2, 3, 4, 5

frutas = ["maça", "melancia", "uva"]
for f in frutas:
    print(f"fruta atual: {f}")

print("-------------")

for multiplicador in range(1, 11):
    for multiplicado in range(1, 11):
        print(f"{multiplicado} * {multiplicador} = {multiplicado * multiplicador}")
    print("-------------")