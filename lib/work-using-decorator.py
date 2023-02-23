def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper


@check_working_hours
def sweep_floors(times):
    print("Sweeping the floors...")


@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(2500)
wash_dishes(2000)
chop_vegetables(2900)

# I'm off duty!
# Washing the dishes...
# I'm off duty!