# använd print för att skriva ut en hälsning

print("tjena och välkommen till mitt program")

# använd den inbyggda funktionen input för att fråga efter

# användarens namn
user_name = input("vad heter du, skriv ditt namn: ")


# använd f för att formatera print och skriv ut

# en hälsning med användares namn
print(f"hej {user_name}. vad kul att du är här")

print(f"så {user_name}, jag undrar hur gammal du är...")
user_age = input("kan du säga det här: ")
print(f"jaså?, tänka sig att du är {user_age} år ")

# konvertera user_age till int innan matte
user_age_converted = int(user_age)
if user_age_converted > 16:
    print("det menas att du får dricka i andra länder")
else:
    print("lite synd, men ok 💀. du missade den bästa tiden")