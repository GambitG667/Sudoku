import pygame as pg
from wawe_colaps import create_sudoku, Field

WIDTH = 540  # ширина игрового окна
HEIGHT = 540 # высота игрового окна
FPS = 30 # частота кадров в секунду

WID = 40 #Ширина сетки
HEI = 40 #Высота сетки

BLACK = (47, 79, 79)
WHITE = (255, 228, 225)
RED = (205, 92, 92)
GREEN = (50, 205, 50)
BLUE = (30, 144, 255)

pg.init()
pg.font.init()
pg.mixer.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sudoku")
clock = pg.time.Clock()

font = pg.font.SysFont('couriernew', 20)
big_font = pg.font.SysFont('couriernew', 60)

sudoku = create_sudoku()


def draw_sels(): #Служебная функция для рисования сетки
    for i in range(1,9):
        if i%3 == 0:
            pg.draw.line(sc, WHITE, (i*60,0),(i*60,540),3)
            pg.draw.line(sc, WHITE, (0,i*60),(540,i*60),3)
        else:
            pg.draw.line(sc, WHITE, (i*60,0),(i*60,540))
            pg.draw.line(sc, WHITE, (0,i*60),(540,i*60))


def render(): #функция рендера рисует сетку и либо значение, либо все возможные значения
    global sc
    sc.fill(BLACK)
    draw_sels()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j].value != 0:
                text = big_font.render(f"{sudoku[i][j].value}", True, WHITE)
                sc.blit(text, (i*60+10, j*60))
            else:
                for k in range(3):
                    for n in range(3):
                        if sudoku[i][j].superposition[n*3+k]:
                            text = font.render(f"{n*3+k+1}", True, WHITE)
                        else:
                            text = font.render(f"{n*3+k+1}", True, BLUE)
                        sc.blit(text,(i*60+k*20+5,j*60+n*20))


running = True
while running: #рабочий цикл
    clock.tick(FPS)
    render()

    for i in pg.event.get():
        # check for closing window
        if i.type == pg.QUIT:
            running = False
        elif i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                x,y = i.pos[0]//60, i.pos[1]//60
                i = i.pos[0]//20%3 + i.pos[1]//20%3*3
                sudoku[x][y].UpdateSuperposition(i+1)
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_r: #рестарт, что бы не перезапускать
                sudoku = create_sudoku()

    
    pg.display.flip()

pg.quit()
