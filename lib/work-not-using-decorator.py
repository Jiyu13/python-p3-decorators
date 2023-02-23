# to much repetition in wrapper functions

def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

def sweep_floors(times):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else:
        print("I'm off duty!")


def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing the dishes...")
    else:
        print("I'm off duty!")


def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else:
        print("I'm off duty!")


sweep_floors = check_working_hours(sweep_floors)
sweep_floors(2500)
# I'm off duty!

wash_dishes = check_working_hours(wash_dishes)
wash_dishes(2000)
# Washing the dishes...

chop_vegetables = check_working_hours(chop_vegetables)
chop_vegetables(2900)
# I'm off duty!
