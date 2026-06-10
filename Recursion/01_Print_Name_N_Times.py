Enter number of times: 5
Enter a name: John




n = int(input("Enter number of times: "))
name = input("Enter a name: ")

def print_name(n, name):
    if n == 0:  # Base Case
        return "Done"

    print(name)
    print_name(n - 1, name)

print_name(n, name)


John
John
John
John
John
Done
