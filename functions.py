def boardOutput():
    ui.textBrowser.setText(stockfish.get_board_visual())
    print(stockfish.get_board_visual())