from collections import Counter
import math
import numpy as np
import itertools
import my_itertools

'''
Created on May 11, 2015

@author: rogier
'''

class ChessBoard(object):
    def __init__(self, width, height):
        #[y][x] - board only, for sequential drawing purposes
        self.squares = np.array([['.' for w in range(width) ] for h in range(height)], np.character)
        
    def clearBoard(self):
        dimensions = self.squares.shape
        w, h = 1, 0
        self.squares = np.array([['.' for i in range(dimensions[w]) ] for j in range(dimensions[h])], np.character)
        
    def toString(self):
        squares = self.squares
        dimensions = squares.shape
        h = 0
        for y in range(dimensions[h]):
            print((b''.join(self.squares[y])).decode("utf-8") )
        print()

class ChessPieceFactory:
    factories = {}
    def addFactory(self, _id, chessGameFactory):
        ChessPieceFactory.factories.put[_id] = chessGameFactory
    addFactory = staticmethod(addFactory)
    
    def createChessPiece(self, _id):
        if not ChessPieceFactory.factories.has_key(_id):
            ChessPieceFactory.factories[id] = \
              eval(id + '.Factory()')
        return ChessPieceFactory.factories[id].create()
    createChessPiece = staticmethod(createChessPiece)

class ChessPiece(object): 
    def __init__(self, position = None):
        self.setPosition(position)
    
    def setPosition(self, position):
        if position:
            self.x = position[0]
            self.y = position[1]
        else:
            self.x = None
            self.y = None

class ChessKing(ChessPiece):
    def validatePosition(self, positions, occupationMap):
        #TODO: should be an assertion
        if self.x == None or self.y == None:
            return False
        mx, my = 0, 1
        sx = self.x
        csx = sx - 1
        cex = sx + 2
        sy = self.y
        csy = sy - 1
        cey = sy + 2
        
        boardDimensions = occupationMap.shape
        
        range_x = range(max(0, csx), min(cex, boardDimensions[mx]))
        range_y = range(max(0, csy), min(cey, boardDimensions[my]))
        
        for x in range_x:
            for y in range_y:
                if occupationMap[x][y]:
                    if x != sx or y != sy:
                        return False
        return True
    class Factory:
        def create(self): return ChessKing()
        
class ChessQueen(ChessPiece):
    def validatePosition(self, positions, occupationMap): 
        #TODO: should be an assertion
        if self.x == None or self.y == None:
            return False
        mx, my = 0, 1
        sx = self.x
        sy = self.y
        
        boardDimensions = occupationMap.shape
        mapW, mapH = boardDimensions[mx], boardDimensions[my]
        
        range_x = range(0, mapW)
        range_y = range(0, mapH)
        
        for x in range_x:
            if occupationMap[x][sy]:
                if x != sx:
                    return False
        for y in range_y:
            if occupationMap[sx][y]:
                if y != sy:
                    return False
                
        i, j = sx, sy
        while True:
            i += 1
            j += 1
            if i < mapW and j < mapH:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i += 1
            j -= 1
            if i < mapW and j > -1:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i -= 1
            j += 1
            if i > -1 and j < mapH:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i -= 1
            j -= 1
            if i > -1 and j > -1:
                if occupationMap[i][j]:
                    return False
            else: 
                break
                
        return True
    class Factory:
        def create(self): return ChessKing()
        
class ChessRook(ChessPiece):
    def validatePosition(self, positions, occupationMap):
        #TODO: should be an assertion
        if self.x == None or self.y == None:
            return False
        mx, my = 0, 1
        sx = self.x
        sy = self.y
        
        boardDimensions = occupationMap.shape
        
        range_x = range(0, boardDimensions[mx])
        range_y = range(0, boardDimensions[my])
        
        for x in range_x:
            if occupationMap[x][sy]:
                if x != sx:
                    return False
        for y in range_y:
            if occupationMap[sx][y]:
                if y != sy:
                    return False
        return True
    class Factory:
        def create(self): return ChessRook()
        
class ChessBishop(ChessPiece):
    def validatePosition(self, positions, occupationMap):
        #TODO: should be an assertion
        if self.x == None or self.y == None:
            return False
        mx, my = 0, 1
        sx = self.x
        sy = self.y
        
        boardDimensions = occupationMap.shape
        mapW, mapH = boardDimensions[mx], boardDimensions[my]
        
        i, j = sx, sy
        while True:
            i += 1
            j += 1
            if i < mapW and j < mapH:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i += 1
            j -= 1
            if i < mapW and j > -1:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i -= 1
            j += 1
            if i > -1 and j < mapH:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        i, j = sx, sy
        while True:
            i -= 1
            j -= 1
            if i > -1 and j > -1:
                if occupationMap[i][j]:
                    return False
            else: 
                break
        return True
    class Factory:
        def create(self): return ChessKing()
        
class ChessKnight(ChessPiece):
    def validatePosition(self, positions, occupationMap):
        #TODO: should be an assertion
        if self.x == None or self.y == None:
            return False
        mx, my = 0, 1
        sx = self.x
        sy = self.y
        
        boardDimensions = occupationMap.shape
        
        xp1 = sx + 1
        xp2 = xp1 + 1 
        bxp1 =  xp1 < boardDimensions[mx]
        bxp2 = False
        if bxp1:
            bxp2 = xp2 < boardDimensions[mx]
        xm1 = sx - 1
        xm2 = xm1 - 1 
        bxm1 = xm1 > -1
        bxm2 = False
        if bxm1:
            bxm2 = xm2 > -1
        yp1 = sy + 1
        yp2 = yp1 + 1 
        byp1 = yp1 < boardDimensions[my]
        byp2 = False
        if byp1:
            byp2 = yp2 < boardDimensions[my]
        ym1 = sy - 1
        ym2 = ym1 - 1 
        bym1 = ym1 > -1
        bym2 = False
        if bym1:
            bym2 = ym2 > -1
        
        if bxp1 and byp2:
            if occupationMap[xp1][yp2]:
                return False
        if bxp1 and bym2:
            if occupationMap[xp1][ym2]:
                return False
        if bxm1 and byp2:
            if occupationMap[xm1][yp2]:
                return False
        if bxm1 and bym2:
            if occupationMap[xm1][ym2]:
                return False
        if bxp2 and byp1:
            if occupationMap[xp2][yp1]:
                return False
        if bxp2 and bym1:
            if occupationMap[xp2][ym1]:
                return False
        if bxm2 and byp1:
            if occupationMap[xm2][yp1]:
                return False
        if bxm2 and bym1:
            if occupationMap[xm2][ym1]:
                return False
            
        return True
    class Factory:
        def create(self): return ChessKing()        
        
class ChessGame: 
    def __init__(self, chessboard, pieceNames):
        self.board = chessboard
        self.npieces = len(pieceNames)
        self.pieces = pieceNames
        self.king = ChessKing()
        self.queen = ChessQueen()
        self.rook = ChessRook()
        self.bishop = ChessBishop()
        self.knight = ChessKnight()
        
    def addPiece(self, piece):
        self.pieces.append(piece)
        
    def printPosition(self, positions, piecetypes):
        squares = self.board.squares
        squaresDimension = squares.shape
        my, mx = 0, 1  # map inverse
        mapW, mapH = squaresDimension[mx], squaresDimension[my]
        self.board.clearBoard()
        for i in range(len(positions)):
            x = positions[i] % mapW
            y = int(positions[i] / mapW)
            squares[y][x] = piecetypes[i]
        for y in range(mapH):
            print((b''.join(squares[y])).decode("utf-8") )
        print()
        
class OverlapPuzzle(ChessGame):
    def __init__(self, chessboard, pieces):
        super().__init__(chessboard, pieces)
        self.OccupationMap = None
        self.preValidationOrthoList = None
        
    def __preValidatePosition(self, pieces):
        for i in range(len(pieces)):
            if self.preValidationOrthoList[i] == True:
                if pieces[i] == 'Q' or pieces[i] == 'R':
                    return False
        return True
        
    def __setOccupationMap(self, positions):
        squaresDimension = self.board.squares.shape
        my, mx = 0, 1  # map inverse
        mapW, mapH = squaresDimension[mx], squaresDimension[my]
        self.OccupationMap = np.zeros((mapW, mapH))
        
        occupationXLines = np.full(mapH, -1)
        occupationYLines = np.full(mapW, -1)
        
        self.preValidationOrthoList = [False for i in range(len(positions))]
        
        for i in range(len(positions)):
            x = positions[i] % mapW
            y = int(positions[i] / mapW)
            self.OccupationMap[x][y] = 1
            self.__fillOrthoOccupationLine(occupationXLines, x, i)
            self.__fillOrthoOccupationLine(occupationYLines, y, i)
            
               
    def __fillOrthoOccupationLine(self, occupationLines, l, i):
        occupationLine = occupationLines[l]
        if occupationLine == -1:
            occupationLine = i
        elif occupationLine == -2:
            self.PreValidationOrthoList[i] = True
        else:
            self.PreValidationOrthoList[occupationLine] = True
            self.PreValidationOrthoList[i] = True
            occupationLines[l] = -2
        
    def __validatePosition_full_board(self, piececombinations):
        boardSquares = self.board.squares
        boardSize = boardSquares.size
        boardDimensions = boardSquares.shape
        occupationMap = self.OccupationMap
        mx = 1
        mapW = boardDimensions[mx]
        positions = list(range(boardSize))
        king = self.king
        queen = self.queen
        rook = self.rook
        bishop = self.bishop 
        knight = self.kinght 
        for i in range(boardSize):
            x = i % mapW
            y = int(i / mapW)
            if piececombinations[i] == 'K':
                king.setPosition([x,y])
                if(king.validatePosition(positions, occupationMap) == False):
                    return False
            elif piececombinations[i] == 'Q':
                queen.setPosition([x,y])
                if(queen.validatePosition(positions, occupationMap) == False):
                    return False
            elif piececombinations[i] == 'R':
                rook.setPosition([x,y])
                if(rook.validatePosition(positions, occupationMap) == False):
                    return False
            elif piececombinations[i] == 'B':
                bishop.setPosition([x,y])
                if(bishop.validatePosition(positions, occupationMap) == False):
                    return False
            elif piececombinations[i] == 'N':
                knight.setPosition([x,y])
                if(knight.validatePosition(positions, occupationMap) == False):
                    return False
        return True

    #TODO: use this function with existing pieces made by a factory 
    def __validatePosition(self, positions, piecetypes):
        boardDimensions = self.board.squares.shape
        mx = 1
        mapW = boardDimensions[mx]
        occupationMap = self.OccupationMap
        king = self.king
        queen = self.queen
        rook = self.rook
        bishop = self.bishop 
        knight = self.knight 
        for i in range(len(positions)):
            x = positions[i] % mapW
            y = int(positions[i] / mapW)
            if piecetypes[i] == 'K':
                king.setPosition([x,y])
                if(king.validatePosition(positions, occupationMap) == False):
                    return False
            elif piecetypes[i] == 'Q':
                queen.setPosition([x,y])
                if(queen.validatePosition(positions, occupationMap) == False):
                    return False
            elif piecetypes[i] == 'R':
                rook.setPosition([x,y])
                if(rook.validatePosition(positions, occupationMap) == False):
                    return False
            elif piecetypes[i] == 'B':
                bishop.setPosition([x,y])
                if(bishop.validatePosition(positions, occupationMap) == False):
                    return False
            elif piecetypes[i] == 'N':
                knight.setPosition([x,y])
                if(knight.validatePosition(positions, occupationMap) == False):
                    return False
        return True
    
    def nUniquePositions(self):
        boardsize = self.board.squares.size
        pieces = self.pieces
        npieces = self.npieces
        nMultiplicities = math.factorial(boardsize - npieces)
        d = Counter(pieces)
        for x in d.values():
            nMultiplicities *= math.factorial(x)
        return int(math.factorial(boardsize) / nMultiplicities)
    
    def solve(self):
        pieces = self.pieces
        npieces = self.npieces
        boardsize = self.board.squares.size
        
        if npieces < boardsize:
            #works only if there's enough squares for the pieces to fill
            piece_position_combinations = itertools.combinations(range(self.board.squares.size), len(pieces))
            piece_type_combinations = list(my_itertools.permutations_unique(pieces))
            
            for i in piece_position_combinations:
                self.__setOccupationMap(i)
                for j in piece_type_combinations:
                    if self.__preValidatePosition(j):
                        if self.__validatePosition(i,j):
                            self.printPosition(i, j)
        else:
            #TODO: test this part
            piece_combinations_full_board = set([])
            permutations = itertools.permutations([d['Type'] for d in pieces], boardsize)
            for i in permutations:
                piece_combinations_full_board.add(i)
            print(piece_combinations_full_board)
            for j in piece_combinations_full_board:
                self.__validatePosition_full_board(j)
            

if __name__ == '__main__':
    chessboard = ChessBoard(7, 7)
    pieceNames = ['K','K','Q','Q','B','B','N']
    puzzle = OverlapPuzzle(chessboard, pieceNames)
    print('Unique positions:', puzzle.nUniquePositions())
    puzzle.solve()
        
    print("exit..")