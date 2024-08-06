def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name = "Rashid",power = "Lasers")
print_kwargs(name = "Rashid",power = "Lasers")
print_kwargs(name = "Rashid",power = "Lasers",enemy="none")