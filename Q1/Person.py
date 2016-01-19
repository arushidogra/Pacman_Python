''' Huh'''
class Person():
    ''' This is the Person class '''
    def __init__(self):
        ''' This is init '''
        pass
    def checkWall(self, xcoord, ycoord, Board):
        ''' this is check wall'''
        if Board[xcoord][ycoord] == 'X':
            return 0
        else:
            return 1
