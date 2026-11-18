# Versi foods.py dari buku (bagian copy list), dengan dua for loop.
my_foods = ['pizza', 'shawarma', 'burger']
friend_foods = my_foods[:]

my_foods.append('sushi')
friend_foods.append('es krim')

print("Favorit makanan saya adalah:")
for food in my_foods:
    print(food)

print("\nFavorit makanan temanku adalah:")
for food in friend_foods:
    print(food)