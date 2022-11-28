from stockfish import Stockfish
from pyqt5_tools import *
import sys
from uiContents import *
from functions import *
import time

#Creates a new chess game
stockfish = Stockfish(path="C:/Users\eligr\Downloads\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

#play sequence
#ask user for voice of what they played for computer to recognize it
#input to stockfish

#TODO: MAKE GUI



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_ChessAI()
ui.setupUi(MainWindow)
ui.recogspeechsetlabel.clear()
ui.statusLabel.clear()
MainWindow.show()


#ui.newGame.clicked.connect()



sys.exit(app.exec_())



