"""
    File: pipe_picture_practice.py
    Author: Xin Li
    Purpose: In this project i will draw a single picture of a
            set of pipes.

"""

from graphics import graphics
class Pipes:
    def __init__(self, grid, square_size):
        self._grid = grid
        self._size = square_size
        #self.n = None
        #self.e = None
        #self.s = None
        #self.w = None
        self._hei = len(grid)
        self._wid = len(grid[0])
    def draw(self):
        grid = self._grid
        size = self._size
        hei = self._hei
        wid = self._wid
        gui = graphics(size*int(wid), size*int(hei), 'Pipe Grid')
        water_state = False

        gui.rectangle(0, 0, size*len(grid), size*len(grid), 'gray')
        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[i-2:]=='(f)':
                    water_state = True
                for k in grid[j][i]:
                    if k =='n':
                        gui.line((i*size+size/2), (j*size), (i*size+size/2), (j*size+size/2),'black',(size/10))
                        if water_state == True:
                            gui.line(i*size+size/2, (j*size), (i*size+size/2), (j*size+size/2),'blue',(size/20))
                    if k =='s':
                        gui.line((i*size+size/2), (j*size+size/2), (i*size+size/2), (j*size+size),'black',(size/10))
                        if water_state == True:
                            gui.line(i*size+size/2, (j*size+size/2), (i*size+size/2), (j*size+size),'blue',(size/20))
                    if k =='w':
                        gui.line((i*size), (j*size+size/2), (i*size+size/2), (j*size+size/2),'black',(size/10))
                        if water_state == True:
                            gui.line((i*size), (j*size+size/2), (i*size+size/2), (j*size+size/2),'blue',(size/20))
                    if k =='e':
                        gui.line((i*size+size/2), (j*size+size/2), (i*size+size), (j*size+size/2),'black',(size/10))
                        if water_state == True:
                            gui.line(i*size+size/2, (j*size+size/2), (i*size+size), (j*size+size/2),'blue',(size/20))
                    if k =='+':
                        gui.rectangle((i*size+size/2-(size*3.5/20)), (size*6.5/20), (size*7/20), (size*7/20),'black')
                        if water_state == True:
                            gui.rectangle((i*size+size/2-(size*2.5/20)), (size*7.5/20), (size*5/20), (size*5/20),'blue')
                    water_state = False
                gui.line(size*i, 0, size*i, 600, 'silver', 10)
            gui.line(0, size*j, 600, size*j, 'silver', 10)
    def get_wid(self):
        return self._wid
    def get_hei(self):
        return self._hei
    def set_square_size(self,size):
        self._size = size
    def get_square_size(self):
        return self._size
    def set_fill_state(self, x, y, state):
        grid = self._grid
        if state ==True:
            if '(f)' not in grid[y][x]:
                grid[y][x]+='(f)'
        if state ==False:
            if '(f)' in grid[y][x]:
                grid[y][x] = grid[y][x].strip('(f)')
        self._grid[y][x] = grid[y][x]
        return self._grid[y][x]
    def rotate_cw(self, x, y):
        grid = self._grid
        new_pipe = ''
        for i in grid[y][x]:
            if i =='n':
                new_pipe +='e'
            if i =='e':
                new_pipe +='s'
            if i =='s':
                new_pipe +='w'
            if i =='w':
                new_pipe +='n'
            if i =='+':
                new_pipe +='+'
        sort_pipe = ''
        for a in new_pipe:
            if a == 'n':
                sort_pipe+='n'
        for b in new_pipe:
            if b == 'e':
                sort_pipe+='e'
        for c in new_pipe:
            if c == 's':
                sort_pipe+='s'
        for d in new_pipe:
            if d == 'w':
                sort_pipe+='w'
        if new_pipe[len(new_pipe)-1]=='+':
            sort_pipe+='+'
        grid[y][x] = sort_pipe
        self._grid[y][x] = grid[y][x]
        return self._grid[y][x]
    def rotate_ccw(self, x, y):
        grid = self._grid
        new_pipe = ''
        for i in grid[y][x]:
            if i =='n':
                new_pipe +='w'
            if i =='e':
                new_pipe +='n'
            if i =='s':
                new_pipe +='e'
            if i =='w':
                new_pipe +='s'
            if i =='+':
                new_pipe +='+'
        sort_pipe = ''
        for a in new_pipe:
            if a == 'n':
                sort_pipe+='n'
        for b in new_pipe:
            if b == 'e':
                sort_pipe+='e'
        for c in new_pipe:
            if c == 's':
                sort_pipe+='s'
        for d in new_pipe:
            if d == 'w':
                sort_pipe+='w'
        if new_pipe[len(new_pipe)-1]=='+':
            sort_pipe+='+'
        grid[y][x] = sort_pipe
        self._grid[y][x] = grid[y][x]
        return self._grid[y][x]
    def get_cell(self, x, y):
        grid = self._grid
        cell = (grid[y][x])
        return cell
