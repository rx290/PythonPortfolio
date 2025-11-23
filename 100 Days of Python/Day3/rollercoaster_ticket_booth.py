height = float(input("Please Enter Your Height in CM: "))

if height>120:
    age= int(input("Please Enter Your Age: "))
    if age <12:
        photos = input("Do you want photos?: ")
        print("8$ Please!") if photos.lower() == 'yes' else print("5$ Please!")
    elif age >12 and age <18:
        photos = input("Do you want photos?: ")
        print("10$ Please!") if photos.lower() == 'yes' else print("7$ Please!")
    elif age >45 and age <55:
        photos = input("Do you want photos?: ")
        print("3$ Please!") if photos.lower() == 'yes' else print("It is free for you, Enjoy!")
    else:
        photos = input("Do you want photos?: ")
        print("15$ Please!") if photos.lower() == 'yes' else print("12$ Please!")

else:
    print("You can't ride")