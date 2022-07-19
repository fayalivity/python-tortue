import turtle

#je modifie
def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    # taille du carré = i+1 * taille_depart
    for i in range(0, nb):
        carre((i+1)*taille_depart)


cote = input("taille du cote : ")
nb_carres = input("nombre de carré : ")

t = turtle.Turtle()
carres(int(cote), int(nb_carres))

turtle.done()
