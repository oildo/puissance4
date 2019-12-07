import pygame

class Field(pygame.Surface):
    """docstring for Field."""

    def __init__(self, fenetre, x, y, width, height):
        super().__init__((width, height))
        self.fenetre = fenetre
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.WIDTH = 7
        self.HEIGHT = 6
        self.MARGE = 20

        self.colors = [  # (0) blue (background) / (1) grey / (2) yellow, (3) red
            (30, 98, 224), (220, 220, 220), (230, 255, 18), (183, 0, 0)
        ]

        self.field= []
        max = self.HEIGHT - 1
        self.last = []

        i = 0
        j = 0
        while i < self.HEIGHT:
            self.field.append([])
            while j < self.WIDTH:
                self.field[i].append(0)  # 0 = null 1 = red 2 = yellow
                j +=1
            i +=1
            j = 0

        i = 0
        while i < self.WIDTH:
            self.last.append(max)
            i +=1


    def draw(self):
        self.fill(self.colors[0])


        div_x = int(self.width/self.WIDTH)
        div_y = int(self.height/self.HEIGHT)

        rad = int((div_x - self.MARGE)/2)

        loc_x = int(div_x/2)
        loc_y = int(div_y/2)

        i = 0
        j = 0
        while i < self.HEIGHT:
            while j < self.WIDTH:
                if self.field[i][j] == 0:
                    pygame.draw.circle(self, self.colors[1], \
                     (int(j * div_x + loc_x), int(i * div_y + loc_y) ), \
                        rad)
                elif self.field[i][j] == 1:
                    pygame.draw.circle(self, self.colors[3], \
                     (int(j * div_x + loc_x), int(i * div_y + loc_y) ), \
                        rad)
                elif self.field[i][j] == 2:
                    pygame.draw.circle(self, self.colors[2], \
                     (int(j * div_x + loc_x), int(i * div_y + loc_y) ), \
                        rad)

                j +=1
            i +=1
            j = 0

        self.fenetre.blit(self, (self.x, self.y))

    def which_column(self, position):
        return int(position[0]/(self.width/self.WIDTH))

    def print_field(self):
        i = 0
        print()
        while i < self.HEIGHT:
            print(i)
            print(self.field[self.HEIGHT - 1 - i])
            i +=1

    def add_token(self, column, value):
        if self.last[column] >= 0:
            self.field[self.last[column]][column] = value
            self.last[column] -= 1
            return True
        else:
            return False

    def init(self):
        self.field= []
        max = self.HEIGHT - 1
        self.last = []

        i = 0
        j = 0
        while i < self.HEIGHT:
            self.field.append([])
            while j < self.WIDTH:
                self.field[i].append(0)  # 0 = null 1 = red 2 = yellow
                j +=1
            i +=1
            j = 0

        i = 0
        while i < self.WIDTH:
            self.last.append(max)
            i +=1
    
    def is_win_def(self):
        
        # horizontal
        for i in self.field:
            j = 0
            while j < self.WIDTH - 3:
                if not i[j] == 0 and i[j] == i[j + 1] == i[j + 2] == i[j +3]:
                    return i[j]
                j +=1

        
        # --------------------------------------------------------------------
        # vertical
        j = 0
        while j < self.WIDTH:
            i = 0
            while i < self.HEIGHT - 3:
                if not self.field[i][j] == 0 and self.field[i][j] == self.field[i + 1][j] == self.field[i +2][j] == self.field[i +3][j]:
                    return self.field[i][j]
                i+=1
            j += 1
        # --------------------------------------------------------------------
        # horizontal \

        i = 0
        while i < self.HEIGHT - 3 :
            j = 0
            while j < self.WIDTH - 3 : 
                if not self.field[i][j] == 0 and self.field[i][j] == self.field[i + 1][j +1] == self.field[i + 2][j + 2] == self.field[i + 3][j + 3]:
                    return self.field[i][j]
                j += 1
            i += 1
        # --------------------------------------------------------------------
        # horizontal /
        i = 0
        while i < self.HEIGHT - 3 :
            j = 0
            while j < self.WIDTH - 3 : 
                if not self.field[i][j + 3] == 0 and self.field[i][j + 3] == self.field[i + 1][j + 2] == self.field[i + 2][j + 1] == self.field[i + 3][j]:
                    return self.field[i][j + 3]
                j += 1
            i += 1


        return 0

    def get_color(self, code):
        return self.colors[code]

