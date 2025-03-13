#მოცემული კოდი გადაიტანეთ Vscode-ში და გაასწორეთ შეცდომები, რათა სწორად იმუშაოს:

#Status == "Student"
#if status == "student":
   #print(True)
#else:
#print(False) 




status = "Student"  # 'Status' -> 'status' (ცვლადის სახელი უნდა იყოს პატარა ასოებით)

if status.lower() == "student":  # 'Status' -> 'status', ასევე '.lower()' რომ რეგისტრი არ ჰქონდეს მნიშვნელობა
    print(True)
else:
    print(False)  # შეწეული ჩანაწერი ('indentation' პრობლემა)