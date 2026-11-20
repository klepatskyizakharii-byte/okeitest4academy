class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1



nums = MyNumbers(1, 5)

print("type of call iter():", iter(nums))

for i in nums:
    print(i)

    #test 1 type of call iter(): <generator object MyNumbers.__iter__ at 0x000001F41AC68FB0>
    #test 2 type of call iter(): <generator object MyNumbers.__iter__ at 0x000001E696A58FB0>
    #test 3 type of call iter(): <generator object MyNumbers.__iter__ at 0x00000291F1B08FB0>
    #незнаю генератор или нет