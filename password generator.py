import random
import string

def generate_password(length):
    if length < 8:
        length = 8

    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    num = int(input("How many passwords do you want to generate? "))
    with open("passwords.txt", "w") as file:
        for i in range(num):
            length = int(input(f"Enter length for Password #{i+1} (min 8): "))
            password = generate_password(length)
            print(f"Password #{i+1} = {password}")
            file.write(f"Password #{i+1}: {password}\n")
    print("✅ All passwords saved to 'passwords.txt'")

main()
