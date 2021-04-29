# Task 1
# Formula for sequence

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Try and While statements to avoid breaking
while True:
    try:
        no_of_terms = int(input("Number of Fibonacci terms: "))
        if no_of_terms < 0:
            print("Must be a positive number: ")
            continue
    except ValueError:
        print("Not a number, try again ")
        continue
    break

# Number of terms are printed according to no_of_terms in
for i in range(no_of_terms):
    print(fib(i))
