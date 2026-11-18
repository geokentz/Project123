# Memakai list kubik dari Exercise 4-8/4-9.
cubes = [number ** 3 for number in range(1, 11)]

print("Tiga item pertama dalam daftar adalah:")
print(cubes[:3])

print("Tiga item dari tengah daftar adalah:")
print(cubes[3:6])

print("Tiga item terakhir dalam daftar adalah:")
print(cubes[-3:])