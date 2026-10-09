email = input("Enter your email address: ")

is_valid = (
    "@" in email
    and "." in email
    and " " not in email
    and not email.startswith("@")
)

if is_valid:
    print("Valid email")
else:
    print("Invalid email")
