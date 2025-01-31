import random
import pygame
import sys
from pygame.locals import *

# Initialize global constants
Frame_Speed = 30
Window_Width = 640
Window_Height = 480
Speed_Reveal = 8
Box_Size = 40
Gap_Size = 10
Border_Width = 10
Border_Height = 7

assert (Border_Width * Border_Height) % 2 == 0, 'The board must have an even number of boxes for pairs of matches.'
X_margin = (Window_Width - (Border_Width * (Box_Size + Gap_Size))) // 2
Y_margin = (Window_Height - (Border_Height * (Box_Size + Gap_Size))) // 2

# Colors
Gray = (100, 100, 100)
Navyblue = (60, 60, 100)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Orange = (255, 128, 0)
Purple = (255, 0, 255)
Cyan = (0, 255, 255)

# Game colors
BackGround_color = Gray
Light_BackGround_color = Navyblue
Box_Color = Cyan
HighLight_Color = Yellow

# Shapes
CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

All_colors = [Red, Green, Blue, Yellow, Orange, Purple, Cyan]
All_Shapes = [CIRCLE, SQUARE, DIAMOND, LINES, OVAL]

assert len(All_colors) * len(All_Shapes) * 2 >= Border_Width * Border_Height, \
    "Board is too big for the number of shapes/colors defined."


def main():
    global Frame_Speed_Clock, DIS_PlaySurf

    pygame.init()
    Frame_Speed_Clock = pygame.time.Clock()
    DIS_PlaySurf = pygame.display.set_mode((Window_Width, Window_Height))

    pygame.display.set_caption('Memory Game')

    mouse_x, mouse_y = 0, 0
    Board = Randomized_Board()
    Boxes_revealed = GenerateData_RevealedBoxes(False)

    first_selection = None
    DIS_PlaySurf.fill(BackGround_color)
    Start_Game(Board)

    while True:
        mouse_clicked = False
        DIS_PlaySurf.fill(BackGround_color)
        Draw_Board(Board, Boxes_revealed)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouse_clicked = True

        box_x, box_y = Box_Pixel(mouse_x, mouse_y)
        if box_x is not None and box_y is not None:
            if not Boxes_revealed[box_x][box_y]:
                Draw_HighlightBox(box_x, box_y)
            if not Boxes_revealed[box_x][box_y] and mouse_clicked:
                Reveal_Boxes_Animation(Board, [(box_x, box_y)])
                Boxes_revealed[box_x][box_y] = True
                if first_selection is None:
                    first_selection = (box_x, box_y)
                else:
                    shape1, color1 = get_Shape_Color(Board, first_selection[0], first_selection[1])
                    shape2, color2 = get_Shape_Color(Board, box_x, box_y)

                    if shape1 != shape2 or color1 != color2:
                        pygame.time.wait(1000)
                        Cover_Boxes_Animation(Board, [first_selection, (box_x, box_y)])
                        Boxes_revealed[first_selection[0]][first_selection[1]] = False
                        Boxes_revealed[box_x][box_y] = False
                    elif Won(Boxes_revealed):
                        Game_Won(Board)
                        pygame.time.wait(2000)

                        Board = Randomized_Board()
                        Boxes_revealed = GenerateData_RevealedBoxes(False)
                        Start_Game(Board)
                    first_selection = None

        pygame.display.update()
        Frame_Speed_Clock.tick(Frame_Speed)


def GenerateData_RevealedBoxes(value):
    return [[value] * Border_Height for _ in range(Border_Width)]


def Randomized_Board():
    icons = [(shape, color) for color in All_colors for shape in All_Shapes]
    random.shuffle(icons)
    num_icons_used = Border_Width * Border_Height // 2
    icons = icons[:num_icons_used] * 2
    random.shuffle(icons)

    board = []
    for x in range(Border_Width):
        column = []
        for y in range(Border_Height):
            column.append(icons.pop(0))
        board.append(column)
    return board


def leftTop_Coord(box_x, box_y):
    left = box_x * (Box_Size + Gap_Size) + X_margin
    top = box_y * (Box_Size + Gap_Size) + Y_margin
    return left, top


def Box_Pixel(x, y):
    for box_x in range(Border_Width):
        for box_y in range(Border_Height):
            left, top = leftTop_Coord(box_x, box_y)
            box_rect = pygame.Rect(left, top, Box_Size, Box_Size)
            if box_rect.collidepoint(x, y):
                return box_x, box_y
    return None, None


def Draw_Board(board, revealed):
    for box_x in range(Border_Width):
        for box_y in range(Border_Height):
            left, top = leftTop_Coord(box_x, box_y)
            if not revealed[box_x][box_y]:
                pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, Box_Size, Box_Size))
            else:
                shape, color = get_Shape_Color(board, box_x, box_y)
                Draw_Icon(shape, color, box_x, box_y)


def Draw_HighlightBox(box_x, box_y):
    left, top = leftTop_Coord(box_x, box_y)
    pygame.draw.rect(DIS_PlaySurf, HighLight_Color, (left - 5, top - 5, Box_Size + 10, Box_Size + 10), 4)


def Draw_Icon(shape, color, box_x, box_y):
    quarter = Box_Size // 4
    half = Box_Size // 2
    left, top = leftTop_Coord(box_x, box_y)

    if shape == CIRCLE:
        pygame.draw.circle(DIS_PlaySurf, color, (left + half, top + half), half - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DIS_PlaySurf, color, (left + quarter, top + quarter, Box_Size - half, Box_Size - half))
    # Add other shapes as needed


def get_Shape_Color(board, box_x, box_y):
    return board[box_x][box_y]


def Reveal_Boxes_Animation(board, boxes):
    for coverage in range(Box_Size, -Speed_Reveal - 1, -Speed_Reveal):
        Box_Cover(board, boxes, coverage)


def Cover_Boxes_Animation(board, boxes):
    for coverage in range(0, Box_Size + Speed_Reveal, Speed_Reveal):
        Box_Cover(board, boxes, coverage)


def Box_Cover(board, boxes, coverage):
    for box in boxes:
        left, top = leftTop_Coord(box[0], box[1])
        pygame.draw.rect(DIS_PlaySurf, BackGround_color, (left, top, Box_Size, Box_Size))
        shape, color = get_Shape_Color(board, box[0], box[1])
        Draw_Icon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, coverage, Box_Size))
    pygame.display.update()
    Frame_Speed_Clock.tick(Frame_Speed)


def Start_Game(board):
    covered_boxes = GenerateData_RevealedBoxes(False)
    boxes = [(x, y) for x in range(Border_Width) for y in range(Border_Height)]
    random.shuffle(boxes)

    Draw_Board(board, covered_boxes)
    for i in range(0, len(boxes), 8):
        Reveal_Boxes_Animation(board, boxes[i:i + 8])
        Cover_Boxes_Animation(board, boxes[i:i + 8])


def Game_Won(board):
    for _ in range(13):
        DIS_PlaySurf.fill(BackGround_color)
        pygame.display.update()
        pygame.time.wait(300)


def Won(revealed_boxes):
    return all(all(row) for row in revealed_boxes)


if __name__ == "__main__":
    main()