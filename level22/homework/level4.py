# მოცემული Flowchart-ის მიხედვით დაწერეთ if else statement-ებისგან შემდგარი კოდი, და კომენტარის სახით დაწერეთ თუ რა იქნება კოდის შედეგი მაშინ, როდესაც მომხმარებელი არის სტუდენტი და მის მიერ შემოტანილი ასაკი იქნება 17
 
status = input("Are you a student? (yes/no): ").strip().lower()  # მომხმარებელი შემოიტანს სტუდენტობაზე პასუხს
age = int(input("Enter your age: "))  # მომხმარებელი შემოიტანს თავის ასაკს

if status == "yes":
    if age < 18:
        print("You are a minor student.")
    else:
        print("You are an adult student.")
else:
    if age < 18:
        print("You are a minor non-student.")
    else:
        print("You are an adult non-student.")
