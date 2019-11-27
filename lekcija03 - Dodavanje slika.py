# Učitavanje biblioteke
import pygame as pg
pg.init()

# Pravimo prozor i postavljamo pozdinsku sliku
sirina_prozora = 800
visina_prozora = 600
prz = pg.display.set_mode((sirina_prozora, visina_prozora))
pozadina = pg.image.load("pozadina.png").convert()
prz.blit(pozadina, (0, 0))

# Naslov i ikona
pg.display.set_caption("Moja igrica")
icon = pg.image.load("ikona.png")
pg.display.set_icon(icon)

# Igrač
igracSlika = pg.image.load("igrac.png").convert()
sirina_igraca = 80
visina_igraca = 80
igracX = sirina_prozora//2 - sirina_igraca//2
igracY = visina_prozora - 2*visina_igraca

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

