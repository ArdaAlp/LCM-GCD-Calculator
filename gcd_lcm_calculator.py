# Greatest Common Divisor Algorithm

def gcd(num1, num2):
    if (num1 >= num2):
        for i in range(1, num2 + 1):
            if (num1 % i == 0 and num2 % i == 0):
                gcd = i
        return gcd
    
    else:
        for i in range(1, num1 + 1):
            if (num1 % i == 0 and num2 % i == 0):
                gcd = i
        return gcd

# Least Common Multiple Algorithm
# ATTENTION: The formula of dividing the product of two numbers by their GCD (Greatest Common Divisor) is not used for LCM (Least Common Multiple) calculation!

def lcm(num1, num2):
    temp = num1
    if (num1 >= num2):
        for i in range(1, num1 + 1):
            if (num1 % num2 == 0):
                lcm = num1
            else:
                num1 = num1 + temp

        return lcm
    
    else:
        for i in range(1, num2 + 1):
            if (num2 % num1 == 0):
                lcm = num2
            else:
                num2 = num2 + temp

    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"for {num1} and {num2} \nGCD: {gcd(num1, num2)} LCM: {lcm(num1, num2)}")
