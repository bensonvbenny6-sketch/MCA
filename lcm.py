


def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


a = int(input("Enter the value of 1st number: "))
b = int(input("Enter the value of 2nd number: "))

print("The LCM is", find_lcm(a, b))
