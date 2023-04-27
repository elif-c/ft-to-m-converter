def parse(user_input_arg):
    parts = user_input_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    user_input = input("Enter feet and inches: ")
    parsed = parse(user_input)
    result = convert(parsed['feet'], parsed['inches'])
    print(f"{parsed['feet']} feet and {parsed['inches']} inches equals {result}")
