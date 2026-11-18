# Shrinking guest list
guests = ['Charles Leclerc', 'George Russell', 'Kimi Antonelli', 'Max Verstappen', 'Lewis Hamilton']

print("Maaf, meja baru tidak sampai tepat waktu. Saya hanya bisa mengundang dua orang.\n")

# pop() satu per satu sampai tersisa dua nama
removed = guests.pop()
print(f"Maaf {removed}, saya tidak bisa mengundang Anda makan malam.")
removed = guests.pop()
print(f"Maaf {removed}, saya tidak bisa mengundang Anda makan malam.")
removed = guests.pop()
print(f"Maaf {removed}, saya tidak bisa mengundang Anda makan malam.")

print()
print(f"{guests[0]}, Anda masih diundang makan malam.")
print(f"{guests[1]}, Anda masih diundang makan malam.")

# del untuk mengosongkan list
del guests[0]
del guests[0]

print()
print(guests)