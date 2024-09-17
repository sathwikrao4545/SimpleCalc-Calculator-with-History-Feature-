
def add(*nums):
    return sum(nums)

def sub(*nums):
    result = nums[0]
    for num in nums[1:]:
        result -= num
    return result

def mul(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

def div(*nums):
    result = nums[0]
    for num in nums[1:]:
        if num == 0:
            print("Division by zero is not possible")
            return None
        result /= num
    return result

def mod(*nums):
    result = nums[0]
    for num in nums[1:]:
        result %= num
    return result

def power(*nums):
    result = nums[0]
    for num in nums[1:]:
        result **= num
    return result

# Menu options
def menu():
    print("\n--- Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. View Calculation History")
    print("8. Exit")


def Calci():
    history = []  # List to store calculation history

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 8:  # Exit the calculator
            break

        if choice == 7:  # View calculation history
            if history:
                print("\n--- Calculation History ---")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")                 
            else:
                print("\nNo calculations yet.")
            continue

        if choice in [1, 2, 3, 4, 5, 6]:
            try:
                nums = list(map(float, input("Enter numbers separated by space: ").split()))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                continue

            if len(nums) < 2:
                print("Please enter at least two numbers.")
                continue

           
            if choice == 1:
                result = add(*nums)
                operation = "Addition"
            elif choice == 2:
                result = sub(*nums)
                operation = "Subtraction"
            elif choice == 3:
                result = mul(*nums)
                operation = "Multiplication"
            elif choice == 4:
                result = div(*nums)
                if result is None:
                    continue  
                operation = "Division"
            elif choice == 5:
                result = mod(*nums)
                operation = "Modulus"
            elif choice == 6:
                result = power(*nums)
                operation = "Power"

            # Record the calculation in history
            history.append(f"{operation} of {nums} = {result}")

            # Print the result
            print(f"{operation} of {nums} is {result}")

        else:
            print("Invalid choice! Please select a valid option.")
            continue


Calci()
