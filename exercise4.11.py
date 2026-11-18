pizzas = ['pepperoni', 'margherita', 'hawaiian']

# [:] membuat salinan terpisah. pizza_teman = pizzas BUKAN salinan.
pizza_teman = pizzas[:]

pizzas.append('four cheese')
pizza_teman.append('bbq chicken')

print("Favorit pizzaku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nFavorit pizza temanku adalah:")
for pizza in pizza_teman:
    print(pizza)