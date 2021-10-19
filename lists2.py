
"""
Listing Mexican Presidents
"""

presidents = ["AMLO", "Peña Nieto", "Felipe Calderon", "Vicente Fox"]
for item in presidents:
    print(f"{item} regresa los billetes!")

for index in range(0, len(presidents)):
    print(presidents[index])


cars = ["audi", "bmw", "volvo"]

[print(car.upper()) if car == "bmw" else print(car.title()) for car in cars]
