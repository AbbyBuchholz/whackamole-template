import pygame
import random

#trying
def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")

        height=512
        width=640
        block_size = 32
        mole_X =0
        mole_Y =0
        pygame.display.set_caption("Whack-a-mole Program")

        screen = pygame.display.set_mode((width, height))


        def draw_grid():
            for x in range(0, width, block_size):
                for y in range(0, height, block_size):
                    pygame.draw.line(screen, "black", [x,y], [x + block_size,y])
                    pygame.draw.line(screen, "black", [x,y], [x, y + block_size])


        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    event.pos = pygame.mouse.get_pos()
                    if mole_X*32 <= event.pos[0] <= mole_X*32 + 32 and mole_Y*32 <= event.pos[1] <= mole_Y*32 + 32:
                        mole_X = random.randrange(20)
                        mole_Y = random.randrange(16)
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_X * block_size, mole_Y * block_size)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
