# Učitavanje biblioteke
import pygame as pg
pg.init()

# Pravimo prozor i postavljamo pozadinsku sliku
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
igracBrzina = 0.1
smerX = 0

def obrisi_igraca(x, y):
    prz.blit(pozadina, (x, y, sirina_igraca, visina_igraca), (x, y, sirina_igraca, visina_igraca))

def nacrtaj_igraca(x, y):
    prz.blit(igracSlika, (x, y))

# Glavna petlja
igra = True
while igra:
    for dogadjaj in pg.event.get():
        
        # Ispitujemo da li je kliknuto na dugme za zatvaranje prozora
        if dogadjaj.type == pg.QUIT:
            igra = False

        # Provera tastera
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] == 0 and keys[pg.K_LEFT] == 0:
            smerX = 0
        elif dogadjaj.type == pg.KEYDOWN:
            if dogadjaj.key == pg.K_LEFT:
                smerX = -1
            if dogadjaj.key == pg.K_RIGHT:
                smerX = 1       
            
    # Brisanje igrača
    obrisi_igraca(int(igracX), int(igracY))
    
    # Izračunavanje nove pozicije igrača
    igracX = igracX + smerX*igracBrzina

    # Crtanje igrača
    nacrtaj_igraca(int(igracX), int(igracY))
    
    # Osvežavanje ekrana
    pg.display.update()

# Gašenje biblioteke
pg.quit()

