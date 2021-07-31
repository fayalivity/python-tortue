import turtle

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


# 5 marches de 30*30px
nb_marche = input("combien de marche ? ")
taille_marche = input("quelle taille de marche ?")
t = turtle.Turtle()
escalier(int(taille_marche), int(nb_marche))

turtle.done()