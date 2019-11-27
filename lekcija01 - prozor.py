# Učitavanje biblioteke
import pygame as pg
pg.init()

# Pravimo prozor
prz = pg.display.set_mode((400,400))
prz.fill(pg.Color("white"))

# Ovde je prostor za crtanje

# Osvežavanje ekrana
pg.display.update()

# Čekanje na kraju
pg.time.wait(3000)

# Gašenje biblioteke
pg.quit()

