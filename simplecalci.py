# 🎉 Welcome to the Fun Calculator! 🎉
# Made just for smart kids who love numbers 😄

print("✨✨ WELCOME TO THE MAGIC CALCULATOR ✨✨")
print("Let's do some math together! 🧮")
print("--------------------------------------")

# Ask the user for two numbers
num1 = float(input("👉 Enter your first number: "))
num2 = float(input("👉 Enter your second number: "))

# Show the menu
print("\nWhat do you want to do today?")
print("1️⃣ Add (+)")
print("2️⃣ Subtract (-)")
print("3️⃣ Multiply (×)")
print("4️⃣ Divide (÷)")

# Take the user's choice
choice = input("🌟 Choose 1, 2, 3, or 4: ")

# Perform the calculation
if choice == '1':
    print(f"🎈 Yay! {num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"🎈 Cool! {num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"🎈 Wow! {num1} × {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"🎈 Awesome! {num1} ÷ {num2} = {num1 / num2}")
    else:
        print("😅 Oops! You can’t divide by zero!")
else:
    print("😕 That’s not a valid choice. Try again next time!")

print("--------------------------------------")
print("🎉 Thanks for playing with the calculator! 🎉")
