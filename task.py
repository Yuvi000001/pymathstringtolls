def sum_of_two():
    print("\n--- Sum of Two Numbers ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)


def odd_even():
    print("\n--- Odd or Even Checker ---")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


def factorial():
    print("\n--- Factorial Calculation ---")
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)


def fibonacci():
    print("\n--- Fibonacci Series ---")
    n = int(input("How many Fibonacci numbers? "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def string_reverse():
    print("\n--- String Reverse ---")
    s = input("Enter a string: ")
    print("Reversed string:", s[::-1])


def palindrome():
    print("\n--- Palindrome Check ---")
    s = input("Enter a word: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


def leap_year():
    print("\n--- Leap Year Check ---")
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is NOT a Leap Year")


def armstrong():
    print("\n--- Armstrong Number ---")
    num = int(input("Enter a number: "))
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    if num == total:
        print(num, "is an Armstrong number")
    else:
        print(num, "is NOT an Armstrong number")


while True:
    print("""
===============================
       All Programs
===============================
1. Sum of Two Numbers
2. Odd or Even
3. Factorial
4. Fibonacci
5. String Reverse
6. Palindrome
7. Leap Year
8. Armstrong Number
9. Exit
""")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        sum_of_two()
    elif choice == 2:
        odd_even()
    elif choice == 3:
        factorial()
    elif choice == 4:
        fibonacci()
    elif choice == 5:
        string_reverse()
    elif choice == 6:
        palindrome()
    elif choice == 7:
        leap_year()
    elif choice == 8:
        armstrong()
    elif choice == 9:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid Choice! Try Again.")
