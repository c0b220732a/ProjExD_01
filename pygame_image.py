import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bd_img = pg.image.load("ex01/fig/3.png")
    bd_img_r = pg.transform.flip(bd_img, True, False)
    bd_img_10 = pg.transform.rotozoom(bd_img_r, 10, 1.0)
    tmr = 0
    
    bd_move = [bd_img_r, bd_img_10]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr % 2 == 0:
            screen.blit(bd_move[0],[300, 200])
        else:
            screen.blit(bd_move[1],[300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(1)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()