harorat = (18, 20, 17, 23, 25, 21, 19)
yuqori = [t for t in harorat if t > 20]
print("Haroratlar:", ", ".join(map(str, yuqori)))
print(f"Kunlar soni: {len(yuqori)}")