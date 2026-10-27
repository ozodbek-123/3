zaxira = 12
while zaxira > 0:
    sotildi = int(input("Sotildi: "))
    if sotildi > zaxira:
        sotildi = zaxira
    zaxira -= sotildi
    print(f"Qoldi: {zaxira}")
print("Ombor bosh")