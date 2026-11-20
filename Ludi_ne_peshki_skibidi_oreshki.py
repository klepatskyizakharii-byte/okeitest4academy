import time


def get_time(func, *args):
    start = time.time()
    res = func(*args)
    end = time.time()
    return res, end - start


def my_func(n):
    s = 0
    for i in range(n):
        s += i
    return s



def test_func():

    res, t = get_time(time.sleep, 1)
    assert res is None
    assert t >= 1

    # Тест 2: проверка с нашей функцией
    res, t = get_time(my_func, 100000)
    assert res == 4999950000
    assert t >= 0

    print("Test done good")


test_func()

result, work_time = get_time(my_func, 1000000)
print("Result:", result)
print("Time of work:", work_time, "seconds.")