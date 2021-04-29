def deck_generator ():
    cont_palos = 1 # Contador para los palos (1 de 4)
    cont_cartas = 1 # Contador para las cartas de cada palo (1 de 10)
    deck = []
    while cont_palos < 4 and cont_cartas < 10:
        if cont_palos == 1:
            palo = "Bastos"
        elif cont_palos == 2:
            palo = "Oros"
        elif cont_palos == 3:
            palo = "Espadas"
        elif cont_palos == 4:
            palo = "Copas"
        while cont_cartas <= 10:
            if cont_cartas == 1:
                deck.append("As de " + palo)
            elif cont_cartas == 10:
                deck.append("Rey de " + palo)
            elif cont_cartas == 9:
                deck.append("Caballo de " + palo)
            elif cont_cartas == 8:
                deck.append("Sota de " + palo)
            else:
                deck.append(str(cont_cartas) + " de " + palo)
            cont_cartas += 1
        cont_cartas = 1
        cont_palos += 1
    return deck

deck = deck_generator()
print(deck)
