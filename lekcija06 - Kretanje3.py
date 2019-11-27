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
igracX = sirina_prozora//2 - sirina_igraca//2
igracY = visina_prozora - 2*visina_igraca
igracBrzina = 0.1
smerX = 0

def igrac(x, y):
    prz.blit(igracSlika, (x, y))

# Glavna petlja
igra = True
while igra:
    for dogadjaj in pg.event.get():
        
        # Ispitujemo da li je kliknuto na dugme za zatvaranje prozora
        if dogadjaj.type == pg.QUIT:
            igra = False

        # Provera tastera
        if dogadjaj.type == pg.KEYDOWN:
            if dogadjaj.key == pg.K_LEFT:
                smerX = -1
            if dogadjaj.key == pg.K_RIGHT:
                smerX = 1
        if dogadjaj.type == pg.KEYUP:
            if dogadjaj.key == pg.K_LEFT or dogadjaj.key == pg.K_RIGHT:
                smerX = 0
            

    # Izračunavanje nove pozicije igrača
    igracX = igracX + smerX*igracBrzina

    # RGB boja prozora kojom se briše
    prz.fill((255, 255, 255))

    # Crtanje igrača
    igrac(int(igracX), int(igracY))
    
    # Osvežavanje ekrana
    pg.display.update()

# Gašenje biblioteke
pg.quit()

