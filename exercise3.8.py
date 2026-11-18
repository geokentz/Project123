# Seeing the World
Lokasi = ['Jepang', 'China', 'Indonesia', 'Mesir', 'Norwegia']

print("Urutan asli:")
print(Lokasi)

print("\nsorted() alfabet:")
print(sorted(Lokasi))
print("Masih urutan asli:")
print(Lokasi)

print("\nsorted() terbalik:")
print(sorted(Lokasi, reverse=True))
print("Masih urutan asli:")
print(Lokasi)

Lokasi.reverse()
print("\nSetelah reverse():")
print(Lokasi)

Lokasi.reverse()
print("\nSetelah reverse() lagi (kembali asli):")
print(Lokasi)

Lokasi.sort()
print("\nSetelah sort() (alfabet):")
print(Lokasi)

Lokasi.sort(reverse=True)
print("\nSetelah sort(reverse=True):")
print(Lokasi)