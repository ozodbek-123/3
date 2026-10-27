jami = 0
soni = 0
while True:
    x = float(input())
    if x == 0:
        break
    jami += x
    soni += 1
print(f"Jami: {jami:.0f}")
print(f"Kiritilgan xarajatlar soni: {soni}")
print(f"O‘rtacha: {jami/soni:.2f}")