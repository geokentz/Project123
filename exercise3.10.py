# Every Function
# List gunung, memakai semua fungsi/metode dari Bab 3.
mountains = ['Everest', 'Fuji', 'Rinjani']
print(mountains)

print(mountains[0])
print(mountains[-1])
mountains[1] = 'Semeru'   
mountains.append('K2')   
mountains.insert(0, 'Kilimanjaro') 
print(mountains)

del mountains[1]
print(mountains)

popped = mountains.pop()
print(f"pop(): {popped}")

mountains.remove('Rinjani')
print(mountains)


print(sorted(mountains))
print(mountains)

mountains.sort()
print(mountains)

mountains.reverse()
print(mountains)

print(len(mountains))