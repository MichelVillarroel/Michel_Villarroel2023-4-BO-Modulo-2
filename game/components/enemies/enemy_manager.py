from game.components.enemies.enemy import Enemy, ENEMY_1, ENEMY_2


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)  

    def add_enemy(self):
        if len(self.enemies) < 2:##
            enemy = Enemy()
            self.enemies.append(enemy)

    def reset(self):
        self.bullets =[]
        self.enemy_bullets = []
            