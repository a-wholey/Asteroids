import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Monospace", 32)
    score = 0
    lives = 3
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #Adding Score
        score_text = font.render("Score: " + str(score), True, "White")
        screen.blit(score_text, (10,10))

        #Adding Lives
        lives_text = font.render("Lives:" + str(lives), True, "White")
        screen.blit(lives_text, (1000, 10))
    
        #Updating Positions of Objects
        updatable.update(dt)

        #Shooting Asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 1
                        
        #Checking Collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                if lives == 0:
                    print(f"Game over! Score: {score}")
                    sys.exit()
                lives -= 1
                asteroid.kill()
        
        #Drawing Objects
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        #Limiting frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()