import Problema_gzhg
import math
import pygame

def mtt(position, target, velocity, dt):
    dx = target[0] - position[0]
    dy = target[1] - position[1]

    distance = math.sqrt(dx**2 + dy**2)

    if distance < 5:
        return 1

    if distance > 0:
        dx /= distance
        dy /= distance

    position[0] += dx * velocity * dt
    position[1] += dy * velocity * dt

    return 0

def reset_positions():
    global PZ, PM, PG, PGR, PB, Bdir, i, j
    PZ = [200, 300]
    PM = [300, 400]
    PG = [150, 430]
    PGR = [350, 450]
    PB = [250, 500]
    Bdir = True
    i = 0
    j = 0

V = Problema_gzhg.solucion_optima()
print(V)

clock = pygame.time.Clock()
vel = 0.15

pygame.init()
screen = pygame.display.set_mode((1103, 733))
img = pygame.image.load('lagoo.png')
img1 = pygame.image.load('Fox.png')
img2 = pygame.image.load('Harina.png')
img3 = pygame.image.load('Granjero.png')
img4 = pygame.image.load('Ganso.png')
img5 = pygame.image.load('bote.png')

# Cargar las imágenes de los botones
start_button_img = pygame.image.load('START.png')
start_button_img = pygame.transform.scale(start_button_img, (200, 200))
start_button_rect = start_button_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

exit_button_img = pygame.image.load('EXIT.png')
exit_button_img = pygame.transform.scale(exit_button_img, (100, 50))
exit_button_rect = exit_button_img.get_rect(bottomleft=(10, screen.get_height() - 10))

end_button_img = pygame.image.load('EXIT.png')
end_button_img = pygame.transform.scale(end_button_img, (150, 75))

restart_button_img = pygame.image.load('RESTART.png')
restart_button_img = pygame.transform.scale(restart_button_img, (150, 75))

end_button_rect = end_button_img.get_rect(center=(screen.get_width() // 2 - 100, screen.get_height() // 2))
restart_button_rect = restart_button_img.get_rect(center=(screen.get_width() // 2 + 100, screen.get_height() // 2))

img1 = pygame.transform.scale_by(img1, 0.3)
img2 = pygame.transform.scale_by(img2, 0.25)
img3 = pygame.transform.scale_by(img3, 0.3)
img4 = pygame.transform.scale_by(pygame.transform.flip(img4, True, False), 0.3)
img5 = pygame.transform.scale_by(img5, 1.2)

done = False
bg = (127, 127, 127)

# Posiciones iniciales
POZ = [200, 300]
POM = [300, 400]
POG = [150, 430]
POGR = [350, 450]
POB = [250, 500]

# Posiciones al otro lado del río
POLZ = [650, 300]
POLM = [770, 350]
POLG = [850, 350]
POLGR = [700, 450]
POLB = [600, 500]

# Posiciones del bote
POBZ = [400, 480]
POBM = [400, 480]
POBG = [400, 480]

PZ = [200, 300]
PM = [300, 400]
PG = [150, 430]
PGR = [350, 450]
PB = [250, 500]

Bdir = True

i = 0
j = 0

# Estados del juego
start_menu = True
animation_finished = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_menu and start_button_rect.collidepoint(event.pos):
                start_menu = False 

            if animation_finished:
                if end_button_rect.collidepoint(event.pos):
                    done = True
                elif restart_button_rect.collidepoint(event.pos):
                    animation_finished = False
                    reset_positions()

            if not start_menu and not animation_finished and exit_button_rect.collidepoint(event.pos):
                done = True

    screen.fill(bg)

    if start_menu:
        # Mostrar todo en su posición inicial y el botón de inicio
        screen.fill(bg)
        rect = img.get_rect()
        rect.center = 550, 362
        screen.blit(img, rect)
        screen.blit(img1, PZ)
        screen.blit(img2, PM)
        screen.blit(img4, PG)
        screen.blit(img3, PGR)
        screen.blit(pygame.transform.flip(img5, Bdir, False), PB)
        screen.blit(start_button_img, start_button_rect.topleft)
    elif animation_finished:
        screen.fill(bg)
        rect = img.get_rect()
        rect.center = 550, 362
        screen.blit(img, rect)
        screen.blit(end_button_img, end_button_rect.topleft)
        screen.blit(restart_button_img, restart_button_rect.topleft)
    else:
        # Continuar con la animación después de presionar el botón START
        screen.fill(bg)
        rect = img.get_rect()
        rect.center = 550, 362

        screen.blit(img, rect)
        screen.blit(img1, PZ)
        screen.blit(img2, PM)
        screen.blit(img4, PG)
        screen.blit(img3, PGR)
        screen.blit(pygame.transform.flip(img5, Bdir, False), PB)

        dt = clock.tick(60)

        # Mostrar el botón de salida en todo momento durante la animación
        screen.blit(exit_button_img, exit_button_rect.topleft)

        if i < len(V):
            objs = list(V[i])
            for obj in objs:
                if obj == 'Granjero':
                    objs.remove(obj)

            if len(objs) > 0:
                if Bdir:
                    if objs[0] == 'Ganso':
                        if j == 0:
                            j += mtt(PG, POBG, vel, dt)
                        elif j == 1:
                            j += mtt(PB, POLB, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                            mtt(PG, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PG, POLG, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = False
                            i += 1
                    if objs[0] == 'Zorro':
                        if j == 0:
                            j += mtt(PZ, POBZ, vel, dt)
                        elif j == 1:
                            j += mtt(PB, POLB, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                            mtt(PZ, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PZ, POLZ, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = False
                            i += 1
                    if objs[0] == 'Maiz':
                        if j == 0:
                            j += mtt(PM, POBM, vel, dt)
                        elif j == 1:
                            j += mtt(PB, POLB, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                            mtt(PM, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PM, POLM, vel, dt)
                            mtt(PGR, POLGR, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = False
                            i += 1
                    if objs[0] == 'Granjero':
                        if j == 0:
                            j += mtt(PB, POLB, vel, dt)
                        if j == 1:
                            j = 0
                            Bdir = False
                            i += 1
                else:
                    if objs[0] == 'Ganso':
                        if j == 0:
                            j += mtt(PG, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 1:
                            j += mtt(PB, POB, vel, dt)
                            mtt(PGR, POGR, vel, dt)
                            mtt(PG, [POB[0] + 150, POB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PG, POG, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = True
                            i += 1
                    if objs[0] == 'Zorro':
                        if j == 0:
                            j += mtt(PZ, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 1:
                            j += mtt(PB, POB, vel, dt)
                            mtt(PGR, POGR, vel, dt)
                            mtt(PZ, [POB[0] + 150, POB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PZ, POZ, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = True
                            i += 1
                    if objs[0] == 'Maiz':
                        if j == 0:
                            j += mtt(PM, [POLB[0] + 150, POLB[1] - 50], vel, dt)
                        elif j == 1:
                            j += mtt(PB, POB, vel, dt)
                            mtt(PGR, POGR, vel, dt)
                            mtt(PM, [POB[0] + 150, POB[1] - 50], vel, dt)
                        elif j == 2:
                            j += mtt(PM, POM, vel, dt)
                        elif j == 3:
                            j = 0
                            Bdir = True
                            i += 1
                    if objs[0] == 'Granjero':
                        if j == 0:
                            j += mtt(PB, POB, vel, dt)
                            mtt(PGR, POGR, vel, dt)
                        if j == 1:
                            j = 0
                            Bdir = True
                            i += 1
        else:
            animation_finished = True

    pygame.display.update()