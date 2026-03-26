import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
import circleshape
from player import Player
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


        milliseconds = clock.tick(60)
        dt = milliseconds / 1000




if __name__ == "__main__":
    main()
