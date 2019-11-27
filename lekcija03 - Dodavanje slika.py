# Učitavanje biblioteke
import pygame as pg
pg.init()

# Pravimo prozor
sirina_prozora = 400
visina_prozora = 400
prz = pg.display.set_mode((sirina_prozora, visina_prozora))
prz.fill(pg.Color("white"))

# Naslov i ikona
pg.display.set_caption("Moja igrica")
icon = pg.image.load("Icon.png")
pg.display.set_icon(icon)

# Igrač
igracSlika = pg.image.load("Player.png")
sirina_igraca = 40
visina_igraca = 40
igracSlika = pg.transform.scale(igracSlika, (sirina_igraca, visina_igraca))
igracX = 200
igracY = 200

def igrac():
    prz.blit(igracSlika, (igracX-sirina_igraca//2, igracY-visina_igraca//2))

# Glavna petlja
igra = True
while igra:
    for dogadjaj in pg.event.get():
        
        # Ispitujemo da li je kliknuto na dugme za zatvaranje prozora
        if dogadjaj.type == pg.QUIT:
            igra = False

    # Crtanje igrača
    igrac()
    
    # Osvežavanje ekrana
    pg.display.update()

# Gašenje biblioteke
pg.quit()

