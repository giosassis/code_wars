# def validate_pin(pin) -> bool:
#     return bool(len(pin) == 4 or len(pin) == 6) and pin.isdigit()

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

test_pins = ["1234", "a234", "12345", "123456", "1234a6", "0000"]
for pin in test_pins:
    result = validate_pin(pin)
    print(f"PIN: {pin}, Valid: {result}")


