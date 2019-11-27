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
igracBrzina = 0.1
smerX = 0
smerY = 0
visina_skoka = 200
pocetna_visina = igracY

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
        if dogadjaj.type == pg.KEYDOWN:
            if dogadjaj.key == pg.K_LEFT:
                smerX = -1
            if dogadjaj.key == pg.K_RIGHT:
                smerX = 1
            if dogadjaj.key == pg.K_SPACE:
                smerY = -1
                pocetna_visina = igracY
        if dogadjaj.type == pg.KEYUP:
            if dogadjaj.key == pg.K_LEFT or dogadjaj.key == pg.K_RIGHT:
                smerX = 0
    
    
    # Brisanje igrača
    obrisi_igraca(int(igracX), int(igracY))       

    # Izračunavanje nove pozicije igrača
    igracX = igracX + smerX*igracBrzina
    igracY = igracY + smerY*igracBrzina
    if pocetna_visina - igracY > visina_skoka:
        smerY = 1
    elif pocetna_visina <= igracY:
        smerY = 0
        igracY = visina_prozora - 2*visina_igraca


    # Crtanje igrača
    nacrtaj_igraca(int(igracX), int(igracY))
    
    # Osvežavanje ekrana
    pg.display.update()

# Gašenje biblioteke
pg.quit()

