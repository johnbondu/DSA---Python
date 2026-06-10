def print_n_to_1(n):
    if n == 0:
        return

    print(n)
    print_n_to_1(n - 1)

print_n_to_1(n)

# output --->
# Enter a  number: 5
# 4
# 3
# 2
# 1

# Print 1 to N using Recursion 


# numfun(3)
# │
# ├─ print(3)
# ├─ numfun(2)
# │   ├─ print(2)
# │   ├─ numfun(1)
# │   │   ├─ print(1)
# │   │   ├─ numfun(0)
# │   │   │   └─ return "Done"
