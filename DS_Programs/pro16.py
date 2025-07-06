def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("megha")