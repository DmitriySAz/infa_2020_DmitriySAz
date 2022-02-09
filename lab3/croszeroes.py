import pygame
from enum import Enum

FPS = 60
CELL_SIZE = 100
STEP = 10


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий тип значков и имя.
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type

class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        i: int
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а также выясняет место клика.
    """

    def __init__(self, field):
        # загрузить картинки значков клеток...
        #self._cross = pygame.image.load('images/cross.png')
        #self._zero = pygame.image.load('images/zero.png')
        #self.void = pygame.image.load('images/void.png')
        # отобразить первичное состояние поля
        #self.new_field = pygame.image.load('images/field.png')
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        """Проверка правильности позиции клика мышкой"""
        for column in range(3):
            for string in range(3):
                grid_left = STEP * (column + 1) + CELL_SIZE*column
                grid_right = STEP * (column + 1) + CELL_SIZE*(column + 1)
                grid_up = STEP * (string + 1) + CELL_SIZE*string
                grid_down = STEP * (string + 1) + CELL_SIZE * (string + 1)
                if grid_left <= x <= grid_right and grid_up <= y <= grid_down:
                     return True

    def get_coords(self, x, y):
        self.i, self.j = x, y
        self.column = x // (CELL_SIZE + STEP)
        self.string = y // (CELL_SIZE + STEP)
        return self.column, self.string  # TODO: реально вычислить клетку клика


class GameRoundManager:
    """
    Менеджер игры, запускающий все процессы.
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 1
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        print(player)
        # игрок делает клик на поле


class GameWindow:
    """
    Содержит виджет поля,
    а также менеджера игрового раунда.
    """

    def __init__(self):
        # инициализация pygame
        pygame.init()


        self.window_size = (3*CELL_SIZE + 4*STEP, 3*CELL_SIZE + 4*STEP)
        self._title = "Crosses & Zeroes"
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(self._title)
        #self.cross = pygame.image.load('images/cross.png')
        #self.field = pygame.image.load('images/field.png')
        #self.new_field = self.screen.blit(self.field, (200, 100))
        for string in range(3):
            for column in range (3):
                x = column * CELL_SIZE + (column+1)*STEP
                y = string * CELL_SIZE + (string+1)*STEP
                pygame.draw.rect(self.screen, (255,255,255), (x, y, CELL_SIZE, CELL_SIZE))
        player1 = Player("Петя", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
                        #pygame.display.flip()
                        print(i, j)
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == "__main__":
    main()
