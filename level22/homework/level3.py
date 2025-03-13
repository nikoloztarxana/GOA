#ცვლადში შეინახეთ თქვენი საყვარელი სიმღერის სახელი, შემდეგ კი მომხმარებელს შემოატანინეთ მისი საყვარელი სიმღერა. იმ შემთხვევაში თუ თქვენი და მომხმარებლის საყვარელი სიმღერა ემთხვევა - გამოიტანეთ "we have the same favorite song", სხვა შემთხვევაში კი გამოიტანეთ "we have different favorite songs"


my_favorite_song = "Bohemian Rhapsody"  # თქვენი საყვარელი სიმღერა

user_favorite_song = input("Enter your favorite song: ")  # მომხმარებელი შემოიტანს თავის საყვარელ სიმღერას

if my_favorite_song.lower() == user_favorite_song.lower():  #tolower() რეგისტრის უგულებელყოფისთვის
    print("We have the same favorite song")
else:
    print("We have different favorite songs")
