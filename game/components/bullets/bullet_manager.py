import pygame

from game.utils.constants import SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
              if bullet.rect.colliderect(enemy.rect) and bullet.owner =='player':
                game.enemy_manager.enemies.remove(enemy)
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
                game.update_score()

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner =='enemy':
                self.enemy_bullets.remove(bullet)
                
                if game.player.power_up_type != SHIELD_TYPE and game.player.get_lives() == 0: #verificadorno deescudo y si ha perdido todas sus vidas.
                       game.death_count += 1
                       game.playing = False
                       pygame.time.delay(100)#verefica si tiene vidas
                if game.player.get_lives() >0 :#si se cumple llamar a reduce
                    game.player.reduce_lives()

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "player" and len (self.bullets) < 1:
            self.bullets.append(bullet)

        elif bullet.owner == "enemy" and len(self.enemy_bullets) < 1:
             self.enemy_bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []