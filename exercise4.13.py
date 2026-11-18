foods = ('nasi goreng', 'soto ayam', 'gado-gado', 'sate', 'rendang')

for food in foods:
    print(food)

# Tuple tidak bisa diubah. Tapi kita bisa menimpa tuple dengan tuple baru.
foods = ('nasi goreng', 'bakso', 'lotek', 'sate', 'mie ayam')

print("\nMenu baru:")
for food in foods:
    print(food)