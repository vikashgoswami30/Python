def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Vikash", Position="SDE")
print_kwargs(name="Vikash", Position="SDE",Real="Owner")
print_kwargs(name="Vikash")