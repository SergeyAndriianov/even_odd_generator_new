def even_odd_generator(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i

n = 15
for item in even_odd_generator(n):
    print(item)