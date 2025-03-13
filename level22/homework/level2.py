#კომენტარის სახით ახსენით თუ რომელ keyword-ებს ვიყენებთ conditional statement-ებში. ამასთანავე, დეტალურად ჩამოაყალიბეთ conditional statements-ის სინტაქსი


#if პირობა1:
    # კოდი, რომელიც შესრულდება, თუ პირობა1 მართალია
#elif პირობა2:
    # კოდი, რომელიც შესრულდება, თუ პირობა2 მართალია
#else:
    # კოდი, რომელიც შესრულდება, თუ არცერთი პირობა არ არის მართალი

temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("The weather is pleasant.")
else:
    print("It's cold outside.")