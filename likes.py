def likes(names: list[str]) -> str:
    count = len(names)

    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"
    pass

test_names = ['Daley Wong', 'Galatea', 'Largo', 'Leon McNichol', 'Brian J. Mason', 'Linna Yamazaki', 'Nene Romanova', 'Sylia Stingray', 'Quincy Rosenkreutz', 'Sylvie', 'Macky Stingray']
result = likes(test_names)
print(result)  # Output: "Alice, Bob
