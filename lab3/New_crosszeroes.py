import pygame

cell_size = 100
step = 10

#Colors in the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

class GameField():
    def __init__(self, sign):
        self._cross = pygame.image.load('images/cross.png')
        self._zero = pygame.image.load('images/zero.png')
        self.void = pygame.image.load('images/void.png')
        self.width = self.heigth = cell_size * 3 + step * 4
        self.size_window = (self.width, self.heigth)
        self.screen = pygame.display.set_mode(self.size_window)
        pygame.display.set_caption('CROSS & ZEROES')
        self.signat = sign
        for string in range(3):
            for column in range(3):
                x = column * cell_size + (column + 1) * step
                y = string * cell_size + (string + 1) * step
                print(sign, type(sign))
                if sign == 0:
                    self.screen.blit(self.void, (x, y))
                    #pygame.draw.rect(self.screen, white, (x, y, cell_size, cell_size))
                elif sign == 1:
                    #pygame.draw.rect(self.screen, red, (x, y, cell_size, cell_size))
                    self.screen.blit(self._cross, (x, y))
                elif sign == 2:
                    #pygame.draw.rect(self.screen, blue, (x, y, cell_size, cell_size))
                    self.screen.blit(self._zero, (x, y))


    def coord_check(self, x, y):
        for column in range(3):
            for string in range(3):
                grid_left = step * (column + 1) + cell_size * column
                grid_right = step * (column + 1) + cell_size * (column + 1)
                grid_up = step * (string + 1) + cell_size * string
                grid_down = step * (string + 1) + cell_size * (string + 1)
                if grid_left <= x <= grid_right and grid_up <= y <= grid_down:
                    return True

    def get_coords(self, x, y):
        self.i, self.j = x, y
        self.column = x // (cell_size + step)
        self.string = y // (cell_size + step)
        return self.column, self.string


class GameRound():
    def __init__(self):
        self.sign_cell = [[0] * 3 for i in range(3)]

    def massive_field(self, i, j, queue):
        self.queue = queue
        if self.sign_cell[i][j] == 0:
            if self.queue%2 == 0:
                self.sign_cell[i][j] = 1
            else:
                self.sign_cell[i][j] = 2
            print(self.sign_cell[i][j], self.queue, i, j)
        return self.sign_cell[i][j]


class GameWindow():

    def game_loop(self):
        finished = False
        q = 0
        self.sign = 0
        while not finished:
            self.game_field = GameField(self.sign)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self.game_field.coord_check(x, y):
                        string, column = self.game_field.get_coords(x, y)
                        self.sign = self.game_round.massive_field(column, string, q)
                        q += 1
                        print(self.sign)

        #return self.sign

    def __init__(self):
        pygame.init()

        self.game_round = GameRound()


                #if self.sign == 0:
                    #self.screen.blit(self.cross, (x, y))
                    #print(self.sign)
                   # pygame.display.update()
        #self.sign = game_loop()





def main():
    window = GameWindow()
    window.game_loop()
    print('Game over!')

if __name__ == "__main__":
    main()

