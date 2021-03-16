'''
Draw a rectangle

Implement the draw_rectangle(width, height) function to return matrices like this:
1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
There are further optional parameters, border_color, fill_color, and border_width, all with default values of 1.
Called with default arguments, the returned matrix is a width-by-height rectangle shape marked by 1s.
The rectangle's border has border_color, and it is filled with fill_color.
The third optional parameter, border_width, specifies the width of the border.
There are no completely empty rows or columns in the returned matrix.
The function provides reasonable answers to edge cases (all combinations of integers as parameters).'''

# def draw_rectangle(width, height):
#     matrix = []
#     return matrix


def draw_rectangle(width: int = 20, height: int = 18, border_color: int = 2, fill_color: str = 1, border_width: int = 3) -> list:
    matrix = []
    for row in range(1,height):
        if row  <= border_width:
            line = [border_color]*width
        if (row  > border_width) and (row <  height - border_width):
            line = [border_color]*border_width + [fill_color]*(width-2*border_width) + [border_color]*border_width
        if row >=  height - border_width:
            line = [border_color]*width
        matrix.append(line)
    return matrix


def draw_triangle(height=5, border_color = 1, fill_color = 2, border_width = 1):
    width = height * 2 - 1
    matrix = []
    for row_index in range(height):
        empty_space = [0] * row_index
        available_space = width - len(empty_space) * 2
        border = [border_color] * min(border_width, available_space) 
        left_border = border
        right_border = [border_color] * min(border_width, available_space - len(left_border)) 

        if row_index < border_width or height - row_index <= border_width:
            fill = [border_color] * (available_space - len(left_border) - len(right_border))
        else:
            fill = [fill_color] * (available_space - len(left_border) - len(right_border))

        line = empty_space + left_border + fill + right_border + empty_space
        matrix.append(line)

    return matrix[::-1]

#zadanie
def draw_christmas_tree(blocks):
    matrix = []
    for block in range(0,blocks):
        triangle = draw_triangle(block+3)
        matrix.append(triangle[-3:])
    
    len(matrix[-1][0])
    number_of_zeros = blocks
    new_matrix = []
    new_row = []
    for row in matrix: 
        new_row = []
        for sub_row in row:
           new_sub_row = [] 
           new_sub_row = [0]*number_of_zeros + sub_row + [0]*number_of_zeros
           new_matrix.append(new_sub_row)
        number_of_zeros -= 1
    return new_matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    #embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)
    #embroider(draw_rectangle(),color_scheme)
    #embroider(draw_triangle(),color_scheme)
    embroider(draw_christmas_tree(10),color_scheme)
    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)
