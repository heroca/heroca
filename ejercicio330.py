for nro in range(1,101):
    if nro%3==0 and nro%5==0:
        print("FizzBuzz")
    elif nro%3==0:
        print("Fizz")
    elif nro%5==0:
        print("Buzz")
    else:
        print(nro)