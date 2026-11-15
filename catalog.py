print("Catalog de note digital")
print("-" * 50)
note_elevi = []
print("\n1. Profesor")
print("2. Elev")
print("3. Iesire")
print("-" * 50)

nume_user = input("Introdu numele - ")
alegere_user = int(input("Ce optiune alegi (1, 2 sau 3)? - "))

while True:
    if alegere_user == 1:
        while True:
            print("\n--- MENIU PROFESOR ---")
            print("1. Adauga nota elev")
            print("2. Vezi situatie elevi")
            print("3. Iesire")
            alegere_profesor = int(input("Ce optiune alegeti? - "))
            
            if alegere_profesor == 1:
                nume_elev = input("Introdu numele elevului - ")
                materie = input("Introdu materia - ")
                nota = float(input("Introdu nota elevului - "))
                note_elevi.append((nume_elev, materie, nota))
                print("Nota a fost adaugata cu succes!")
                
            elif alegere_profesor == 2:
                print("\n--- SITUATIA ELEVILOR ---")
                if not note_elevi:
                    print("Nu exista note adaugate inca")
                else:
                    for elev, materie, nota in note_elevi:
                        print(f"Elev: {elev} | Materie: {materie} | Nota: {nota}")
            elif alegere_profesor == 3:
                print("La revedere!")
                break
            else:
                print("Optiune invalida!")
        break
        
    elif alegere_user == 2:
        while True:
            print("\n--- MENIU ELEV ---")
            print("1. Adauga notele si vezi media")
            print("2. Iesire")
            alegere_elev = int(input("Ce optiune alegi? - "))
            
            if alegere_elev == 1:
                suma_note = 0.0
                numar_note = 0
                while True:
                    nota_text = input("Introdu nota (sau apasa Enter pentru a opri): ")
                    if not nota_text:
                        break
                    
                    nota = float(nota_text)
                    suma_note = suma_note + nota
                    numar_note = numar_note + 1
                
                if numar_note == 0:
                    print("Nu ai introdus nicio nota")
                else:
                    media = suma_note / numar_note
                    print(f"Media ta este: {media:.2f}")
            elif alegere_elev == 2:
                print("La revedere!")
                break
            else:
                print("Optiune invalida!")
        break
        
    elif alegere_user == 3:
        print("La revedere!")
        break
    else:
        print("Optiune invalida!")
        alegere_user = int(input("Ce optiune alegi (1, 2 sau 3)? - "))
