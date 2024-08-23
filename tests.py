temperature = 2
if temperature > 25:
    print("It's hot outside. Wear shorts!")
elif temperature > 15:
    print("It's warm. Maybe a light jacket")
else:
    print("Brrr! It's cold. Bundle up!")

for i in range(5):
    print(f"This is loop iteration{i}")

countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
    print ("Blast off!")