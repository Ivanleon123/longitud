# longitud.py

def longitud(element):
    """Retorna la longitud d'una llista o d'una cadena."""
    return len(element)

# Proves de la funció
if __name__ == "__main__":
    # Exemples de prova
    cadena = "Hola, món!"
    llista = [1, 2, 3, 4, 5]

    print(f"La longitud de la cadena '{cadena}' és: {longitud(cadena)}")
    print(f"La longitud de la llista {llista} és: {longitud(llista)}")
    
    # Més exemples
    cadena_vacia = ""
    llista_buit = []

    print(f"La longitud de la cadena buida és: {longitud(cadena_vacia)}")
    print(f"La longitud de la llista buida és: {longitud(llista_buit)}")
    print(f"La longitud de 'Python' és: {longitud('Python')}")
    print(f"La longitud de [1, 2, 3, 4, 5, 6, 7] és: {longitud([1, 2, 3, 4, 5, 6, 7])}")
