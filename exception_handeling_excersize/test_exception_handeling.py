def test_div(x,y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError:
        y = 1
        result = x /y
    except TypeError:
        print("values must be intergers")

    return result


print(test_div(1,"ang"))
print(test_div(1,0))
