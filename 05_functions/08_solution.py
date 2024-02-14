def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Harshvardhan",childhood_crush="D",gym_crush="P")