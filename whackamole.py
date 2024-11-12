import pygame
import random


def main():
    x = 0
    y = 0
    randx = 0
    randy = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(pygame.mouse.get_pos())
                    #print(x)
                    #print(y)
                    if x <= event.pos[0] <= (x + 32) and y <= event.pos[1] <= (y + 32):
                        randx = random.randrange(0, 20)
                        randy = random.randrange(0, 16)
            screen.fill("pink")
            line_color = "blue"
            for i in range(0,640,32):
                pygame.draw.line(screen, line_color, (i+32, 0), (i+32, 512))
                for j in range(0,512,32):
                    pygame.draw.line(screen, line_color, (0, j+32), (640, j+32))


            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            x = 32*randx
            y = 32*randy



            #updates the display to show changes
            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
