ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}
umumiy = ali & vali
faqat = ali ^ vali
print("Umumiy janrlar:", ", ".join(sorted(umumiy)))
print("Faqat bittasiga yoqadi:", ", ".join(sorted(faqat)))