# Let the user enter a password. If it's wrong, ask again (max 3 attempts).
# Print "Access Denied" if all attempts fail, else "Access Granted".

password = "shry"
attempts =0

for i in range(0, 3):
    user = str(input("enter your password"))

    if(password == user):
        print("pass is coreect")
        break
    else:
        print("try again ")
        attempts +=1

        if attempts == 3:
            print("access denoied")

