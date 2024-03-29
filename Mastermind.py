import random

place1 = random.randint(0, 8)
place2 = random.randint(0, 8)
place3 = random.randint(0, 8)
place4 = random.randint(0, 8)

# Boucle pour éviter les doublons
while place2 == place1:
    place2 = random.randint(0, 8)

while place3 == place2 or place3 == place1:
    place3 = random.randint(0, 8)
    
while place4 == place3 or place4 == place2 or place4 == place1 :
    place4 = random.randint(0, 8)

print(place1, place2, place3, place4)

