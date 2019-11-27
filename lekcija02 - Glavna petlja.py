# Učitavanje biblioteke
import pygame as pg
pg.init()

# Pravimo prozor
sirina_prozora = 400
visina_prozora = 400
prz = pg.display.set_mode((sirina_prozora, visina_prozora))
prz.fill(pg.Color("white"))

# Glavna petlja
igra = True
while igra:
    for dogadjaj in pg.event.get():
        
        # Ispitujemo da li je kliknuto na dugme za zatvaranje ptozora
        if dogadjaj.type == pg.QUIT:
            igra = False

    # Ovde je prostor za crtanje
    
    # Osvežavanje ekrana
    pg.display.update()

# Gašenje biblioteke
pg.quit()

