def check_vowels():
    # Código a implementar utilizando input.
    
    nombre1 = input ("Ingrese nombre:")
    
    contiene_a = "a" in nombre1.lower()
    print (f"Contiene a: {contiene_a}")

    contiene_e = "e" in nombre1.lower()
    print (f"Contiene e: {contiene_e}")

    contiene_i = "i" in nombre1.lower()
    print (f"Contiene i: {contiene_i}")

    contiene_o = "o" in nombre1.lower()
    print (f"Contiene o: {contiene_o}")

    contiene_u = "u" in nombre1.lower()
    print (f"Contiene u: {contiene_u}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
