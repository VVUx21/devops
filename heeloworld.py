print("Hello World from alpine and v3 tag")

with open('names.txt') as f:
    names = f.read().splitlines()
    print(names)
    for name in names:
        print(f"Hello, {name}!")
        print(f"Length of {name}: {len(name)}")
    print(f"Total number of names: {len(names)}")
