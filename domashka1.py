import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_kushat(self):
        print("Time to kushat nom nom")
        self.progress += 0.12
        self.gladness -= 3

    def to_gylat(self):
        print("I will go outside")
        self.gladness += 3

    def to_chill(self):
        print("Rest time sleep on sofa lol")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("I feel bad...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"gladness is = {self.gladness}")
        print(f"progress is = {round(self.progress, 2)}")

    def live(self, day):
        print(f"Day {day} of {self.name} life")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_kushat()
        elif live_cube == 2:
            self.to_gylat()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

stud = Dog(name="sandosik_barbosik")

for day in range(365):
    if stud.alive == False:
        break
    stud.live(day)