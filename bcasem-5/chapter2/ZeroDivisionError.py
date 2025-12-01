try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a / b
    f.write("Writing %d into myfile" % c)

except ZeroDivisionError:
    print("Division by zero happened")
    print("Please do not enter 0 as the second number")

except ValueError:
    print("Invalid input. Please enter exactly two integers separated by space")

finally:
    f.close()
    print("File closed")
