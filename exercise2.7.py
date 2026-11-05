# Stripping names
name = "\t\nChris Hemsworth\n\t"

print("Dengan whitespace:")
print(repr(name))
print(name)

print("\nlstrip():")
print(repr(name.lstrip()))

print("\nrstrip():")
print(repr(name.rstrip()))

print("\nstrip():")
print(repr(name.strip()))