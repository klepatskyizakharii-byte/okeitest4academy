import random
from colorama import init, Fore, Style


init()

dev_rigs = {
    "Laptop": {"power": 100, "durability": 100, "wear": 6},
    "Old PC": {"power": 50, "durability": 40, "wear": 10},
    "Workstation": {"power": 70, "durability": 150, "wear": 8},
    "Supercomputer": {"power": 80, "durability": 120, "wear": 14}
}

gig_list = {
    "Indie Game Project": {"budget": 50, "stress_gain": 10},
    "Mobile Game App": {"budget": 40, "stress_gain": 3},
    "AAA Game Engine": {"budget": 45, "stress_gain": 25},
    "VR Simulation": {"budget": 70, "stress_gain": 1}
}


class Developer:
    def __init__(self, name="Coder", gig=None, studio=None, rig=None):
        self.name = name
        self.budget = 100
        self.energy = 50
        self.snacks = 50
        self.sanity = 100
        self.gig = gig
        self.studio = studio
        self.rig = rig

    def setup_studio(self):
        self.studio = Studio()

    def get_rig(self):
        self.rig = Hardware(dev_rigs)

    def take_gig(self):
        if self.rig.run_code():
            pass
        else:
            self.fix_hardware()
            return
        self.gig = Gig(gig_list)

    def eat_snack(self):
        if self.studio.snacks <= 0:
            self.market("snack_run")
        else:
            if self.energy >= 100:
                self.energy = 100
                return
            self.energy += 5
            self.studio.snacks -= 5

    def code(self):
        if self.rig.run_code():
            pass
        else:
            if self.rig.power < 20:
                self.rig.power += 100
                print(Fore.YELLOW + "Emergency power boost!" + Style.RESET_ALL)
                return
            else:
                self.fix_hardware()
                return
        self.budget += self.gig.budget
        self.energy -= self.gig.stress_gain
        self.snacks -= 4
        self.sanity -= 5

    def market(self, action_type):
        if self.rig.run_code():
            pass
        else:
            if self.rig.power < 20:
                self.rig.power += 100
                print(Fore.YELLOW + "Emergency power boost!" + Style.RESET_ALL)
                return
            else:
                self.fix_hardware()
                return

        if action_type == "snack_run":
            print(Fore.GREEN + "Restocked snacks!" + Style.RESET_ALL)
            self.budget -= 50
            self.studio.snacks += 50
        elif action_type == "power":
            print(Fore.GREEN + "Upgraded power supply!" + Style.RESET_ALL)
            self.budget -= 100
            self.rig.power += 100
        elif action_type == "energy_drink":
            print(Fore.GREEN + "Awesome! Energy drink boost!" + Style.RESET_ALL)
            self.energy += 10
            self.snacks += 2
            self.budget -= 15

    def relax(self):
        self.energy += 10
        self.sanity += 15
        self.studio.bugs += 5

    def clean_studio(self):
        self.energy -= 5
        self.studio.bugs = 0

    def fix_hardware(self):
        self.rig.durability += 100
        self.budget -= 50

    def show_stats(self, day):
        day_msg = f"Day {day} in {self.name}'s studio"
        print(Fore.CYAN + f"{day_msg:=^50}" + Style.RESET_ALL, "\n")
        dev_stats = f"{self.name}'s stats"
        print(Fore.YELLOW + f"{dev_stats:-^50}" + Style.RESET_ALL, "\n")
        print(f"Budget - ${self.budget}")
        print(f"Energy - {self.energy}")
        print(f"Snacks - {self.snacks}")
        print(f"Sanity - {self.sanity}")
        studio_msg = "Studio status"
        print(Fore.YELLOW + f"{studio_msg:-^50}" + Style.RESET_ALL, "\n")
        print(f"Studio Snacks - {self.studio.snacks}")
        print(f"Studio Bugs - {self.studio.bugs}")
        rig_msg = f"{self.rig.brand} rig specs"
        print(Fore.YELLOW + f"{rig_msg:-^50}" + Style.RESET_ALL, "\n")
        print(f"Power - {self.rig.power}")
        print(f"Durability - {self.rig.durability}")

    def is_alive(self):
        if self.energy < 0:
            print(Fore.RED + "Burnout reached..." + Style.RESET_ALL)
            return False
        if self.snacks < 0:
            print(Fore.RED + "Starved of snacks..." + Style.RESET_ALL)
            return False
        if self.budget < -500:
            print(Fore.RED + "Bankrupt..." + Style.RESET_ALL)
            return False

        if self.sanity <= 0:
            recovery_days = random.randint(3, 10)
            print(
                Fore.RED + f"Mental breakdown! Sent to the clinic for {recovery_days} days of recovery..." + Style.RESET_ALL)
            self.sanity = 100
            self.energy = 50
            self.budget -= 150

        return True

    def simulate(self, day):
        if self.is_alive() == False:
            return False
        if self.studio is None:
            print(Fore.GREEN + "Rented a new studio!" + Style.RESET_ALL)
            self.setup_studio()
        if self.rig is None:
            self.get_rig()
            print(Fore.GREEN + f"Purchased hardware: {self.rig.brand}" + Style.RESET_ALL)
        if self.gig is None:
            self.take_gig()
            print(Fore.GREEN + f"Accepted gig: {self.gig.title} with budget ${self.gig.budget}" + Style.RESET_ALL)

        self.show_stats(day)
        dice = random.randint(1, 4)
        if self.snacks < 20:
            print("Running low on snacks, time to eat!")
            self.eat_snack()
        elif self.energy < 20:
            if self.studio.bugs > 15:
                print("Too many bugs to relax, cleaning the code first…")
                self.clean_studio()
            else:
                print("Time to relax and play games!")
                self.relax()
        elif self.budget < 0:
            print("Out of money, need to code!")
            self.code()
        elif self.rig.durability < 15:
            print("Hardware failing, need repairs!")
            self.fix_hardware()
        elif dice == 1:
            print("Time to relax and play games!")
            self.relax()
        elif dice == 2:
            print("Coding session!")
            self.code()
        elif dice == 3:
            print("Refactoring and debugging!")
            self.clean_studio()
        elif dice == 4:
            print("Buying energy drinks!")
            self.market(action_type="energy_drink")


class Hardware:
    def __init__(self, rig_list):
        self.brand = random.choice(list(rig_list))
        self.power = rig_list[self.brand]["power"]
        self.durability = rig_list[self.brand]["durability"]
        self.wear = rig_list[self.brand]["wear"]

    def run_code(self):
        if self.durability > 0 and self.power >= self.wear:
            self.power -= self.wear
            self.durability -= 1
            return True
        else:
            print(Fore.RED + "Hardware failure! Cannot compile." + Style.RESET_ALL)
            return False


class Studio:
    def __init__(self):
        self.bugs = 0
        self.snacks = 0


class Gig:
    def __init__(self, gig_list):
        self.title = random.choice(list(gig_list))
        self.budget = gig_list[self.title]["budget"]
        self.stress_gain = gig_list[self.title]["stress_gain"]


# Цветное меню выбора сложности
print("Select difficulty level:")
print(Fore.GREEN + "1. easy" + Style.RESET_ALL)
print(Fore.YELLOW + "2. medium" + Style.RESET_ALL)
print(Fore.RED + "3. hard" + Style.RESET_ALL)
print(Fore.MAGENTA + "4. impossible" + Style.RESET_ALL)

choice = input("Enter difficulty (easy/medium/hard/impossible): ")

if choice == "easy":
    total_days = 5
elif choice == "medium":
    total_days = 10
elif choice == "hard":
    total_days = 20
elif choice == "impossible":
    total_days = 50
else:
    print("Invalid choice, defaulting to medium (10 days).")
    total_days = 10

coder = Developer(name="Alex")
for day in range(1, total_days + 1):
    if coder.simulate(day) == False:
        print(Fore.RED + "Simulation over." + Style.RESET_ALL)
        break

        #20.11.2026 21:15 Vasya 2.0 vasya krytoi simulator meow meow
        #20.11.2026 21:25 Added sanity if sanity = 0 tam koroche v psixushky
        #20.11.2026 21:37 Game got crashed because of mode Impossible, changed the code
        #20.11.2026 21:50 Coloramchik(pls work)
        #20.11.2026 21:50 upd after test (coloramchik working good)