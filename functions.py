from speech import *

def boardOutput(stockfish, ui):
    ui.textBrowser.setText(stockfish.get_board_visual())
    print(stockfish.get_board_visual())

def playerMove(ui):
    ui.statusLabel.setText("Currently listening for player move...")
    print("PlayerMove Function")
    listenAudio()
    
    