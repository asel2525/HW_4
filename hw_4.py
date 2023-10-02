# 1

try:
    score = int(input("Enter score: "))
except:
    print("Error, please enter numeric input between 0 and 100")
    exit()

def func(score):
        if score > 100 or score < 0:
            print("Error, please enter numeric input between 0 and 100")
        elif score >= 90:
            print("Grade is A")
        elif score >= 80:
            print("Grade is B")
        elif score >= 70:
            print("Grade is C")
        elif score >= 60:
            print("Grade is D")
        else:
            print("Grade is F")

func(score)
    
# 2

try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter a numeric number!")
    exit()

def computepay(hours, rate):
        if hours > 40:
            extra_hours = hours - 40
            extra_rate = rate * 1.5
            salary = (40 * rate) + (extra_hours * extra_rate)
            print("Pay: "+str(float(salary)))
        else:
            salary = hours * rate
            print("Pay: " + str(salary))
            
computepay(hours, rate)

# 3

def num_divide3(num):
    count = 0
    for i in range(1, num+1):
        if i % 3 == 0:
            count += 1
    return count


while True:
    user_input = input("Enter a positive integer: ")

    if user_input.lower() == 'done':
        print("Bye")
        break

    try:
        num = int(user_input)
        if num < 0:
            print("Please enter a positive integer.")
        else:
            result = num_divide3(num)
            print(f"Numbers divisible by 3 among numbers from 1 to {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        
    