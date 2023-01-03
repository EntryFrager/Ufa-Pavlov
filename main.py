import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.board = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        t = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                x0 = self.left + j * self.cell_size
                y0 = self.top + i * self.cell_size
                pygame.draw.rect(screen, (255, 255, 255), (x0, y0, self.cell_size, self.cell_size), 1)
                t.append(0)
            self.board.append(t)

    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, screen)

    def get_cell(self, mouse_pos):
        x1, y1 = mouse_pos
        for i in range(1, self.height + 1):
            for j in range(1,  self.width + 1):
                x0 = self.left + j * self.cell_size
                y0 = self.top + i * self.cell_size
                if x1 < x0 and y1 < y0:
                    return (j - 1, i - 1)
        return 'None'

    def on_click(self, cell_coords, screen):
        x1 = self.left + cell_coords[0] * self.cell_size
        y1 = self.top + cell_coords[1] * self.cell_size
        color = screen.get_at((x1 + 1, y1 + 1))[:3]
        if color == (0, 0, 0):
            screen.fill((0, 255, 0), (x1, y1, self.cell_size, self.cell_size))
            self.board[cell_coords[1]][cell_coords[0]] = 1
        else:
            screen.fill((0, 0, 0), (x1, y1, self.cell_size, self.cell_size))
            self.board[cell_coords[1]][cell_coords[0]] = 1


class Life(Board):
    def start(self):



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Недореверси')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    board = Board(8, 8)
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                mouse = pygame.mouse.get_pressed(num_buttons=5)
                key = pygame.key.get_pressed()[pygame.K_SPACE]
                if mouse[0]:
                    board.get_click(event.pos, screen)
                elif mouse[2]:
                    board.get_click(event.pos, screen)
                print(key)
        board.render()
        pygame.display.flip()
    pygame.quit()
