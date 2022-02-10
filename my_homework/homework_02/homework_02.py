for i in range(0, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print(str(i) + ' FizzBuzz')
        else:
            print(str(i) + ' Fizz')
    elif i % 5 == 0:
        print(str(i) + ' Buzz')
