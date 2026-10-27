A = (3, 7)
B = (8, 2)
sa = sum(A)
sb = sum(B)
print(f"A yig‘indisi: {sa}")
print(f"B yig‘indisi: {sb}")
if sa > sb:
    print("A kattaroq")
elif sb > sa:
    print("B kattaroq")
else:
    print("Yig‘indilar teng")