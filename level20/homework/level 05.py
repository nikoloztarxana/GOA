#while ციკლის მეშვეობით, შექმენით რიცხვების დიაპაზონი 1-დან 100 ჩათვლით, შეამოწმეთ თუ რიცხვი არის ლუწი, დაბეჭდეთ ეს რიცხვი while ციკლში და მიუწერეთ რომ ლუწია, თუ კენტია, დაბეჭდეთ ეს რიცხვი და გვერძე მიუწერეთ რომ კენტია / მაგ: (1 კენტიტა, 2 ლუწია, 3 კენტია, 4 ლუწია...)



num = 1  

while num <= 100:  
    if num % 2 == 0:
        print(f"{num} ლუწია")
    else:
        print(f"{num} კენტია")
    num += 1  