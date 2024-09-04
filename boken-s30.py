svar = input ("Skriv ett tal: ")
convert_svar_to_float = float(svar)
produkt = convert_svar_to_float * convert_svar_to_float 
print(f"Talet i kvadrat är {produkt:12.4f}")
# :12.4f = Det innan punkten är hur många tal det ska vara. Om summan blir mindre än tolv så skulle talen gå steg till höger tills det blir 12 tolv. Det efter punkten är hur många decimaler talet ska ha.
print(f"Talet i kvadrat är {produkt + 12:12.4f}")
print(f"Talet i kvadrat är {produkt + 50000:12.4f}")
print(f"Talet i kvadrat är {produkt:12.4f}")
print(f"Talet i kvadrat är {produkt - 234:12.4f}")
print(f"Talet i kvadrat är {produkt + 45674635435:12.4f}")

