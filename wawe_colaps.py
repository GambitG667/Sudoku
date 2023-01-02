import random

#обрывки старого проекта, поэтому такие дибильные названия, по сути обрезанная реализация алгоритма колапса волновой функции

class Field():
    
    def __init__(self):
        self.superposition = []
        self.neighbors = []
        self.value = 0
        for i in range(9):
            self.superposition.append(True)

    def set_neighbor(self, neighbors):
        self.neighbors = neighbors
    
    def UpdateSuperposition(self, pos_val):
        if self.value == 0 and self.superposition[pos_val-1]:
            self.value = pos_val
            for i in self.neighbors:
                i.close_value(pos_val)
    
    def close_value(self, value):
        if (not self.value):
            self.superposition[value-1] = False


def create_sudoku():
    sudoku = []
    for i in range(9):
        sudoku.append([])
        for j in range(9):
            sudoku[i].append(Field())
    for i in range(9):
        for j in range(9):
            naibors = []
            for k in range(9):
                naibors.append(sudoku[k][j])
                naibors.append(sudoku[i][k])
            for k in range(3):
                for m in range(3):
                    naibors.append(sudoku[i//3*3+k][j//3*3+m])
            sudoku[i][j].set_neighbor(naibors)
    return sudoku
