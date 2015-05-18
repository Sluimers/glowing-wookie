'''
Created on May 17, 2015

@author: rogier
'''
import unittest
import Main

class Test(unittest.TestCase):

    def testPossibilities(self):
        mapW, mapH = 3, 3
        boardSize = mapW * mapH
        chessboard = Main.ChessBoard(mapW, mapH)
         
        pieces = ['R','R']
        
        puzzle = Main.OverlapPuzzle(chessboard, pieces)
        
        nPositions1 = puzzle.nUniquePositions()
        
        piece_position_combinations = Main.itertools.combinations(range(boardSize), len(pieces))
        piece_type_combinations = list(Main.my_itertools.permutations_unique(pieces))
        
        len_piece_position_combinations = sum(1 for x in piece_position_combinations)
        len_piece_type_combinations = sum(1 for x in piece_type_combinations)
        
        self.assertEqual(len_piece_position_combinations, 36, "Position combinations failed")
        self.assertEqual(len_piece_type_combinations, 1, "Piece combinations failed")
        
        nPositions2 = len_piece_position_combinations * len_piece_type_combinations
        
        self.assertEqual(nPositions1, nPositions2, "Combination calculations failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()