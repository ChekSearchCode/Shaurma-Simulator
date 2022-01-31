import pygame
import ctypes

class Main:

    pygame.display.set_mode((
        ctypes.windll.user32.GetSystemMetrics(0),
        ctypes.windll.user32.GetSystemMetrics(1)
    ))
    pygame.display.set_caption("Shaurma Simulator")

    pygame.time.Clock().tick(60)

    run = True

    def __init__(self):

        pygame.init()

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_ESCAPE]:
                self.run = False
                pygame.quit()

if __name__ == "__main__":
    program = Main()