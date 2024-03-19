time = int(input("Enter your time :"))

sat = time // 3600
dagighe = time // 3600 // 60
saniye = time % 3600

print(f"{sat} : {dagighe} : {saniye}")
