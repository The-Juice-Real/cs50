import validators

user_email = input("What's your email address? ").strip().lower()

if validators.email(user_email):
    print("Valid")
else:
    print("Invalid")