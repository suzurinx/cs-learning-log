fizzbuzz = lambda n: "-".join([
    "FizzBuzz" if i % 15 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    str(i)
    for i in range(1, n + 1)
])

print(fizzbuzz(9))
print(fizzbuzz(20))