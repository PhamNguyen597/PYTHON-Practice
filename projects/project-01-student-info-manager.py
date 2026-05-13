def isValidChessboard(board):
    pieceofchess=['king','queen','bishop','pawn','knight','rook']
    bpiece=0
    wpiece=0
    bking=0
    wking=0
    bpawn=0
    wpawn=0
    for position,piece in board.items():
        if len(position)!=2:
            return False
        if position[0]not in '12345678':
            return False
        if position[1] not in 'abcdefgh':
            return False
        if piece[0] not in 'wb':
            return False
        if piece[1:]not in pieceofchess:
            return False
        if piece[0]=='w':
            wpiece+=1
            if piece[1:]=='king':
                wking+=1
            elif piece[1:]=='pawn':
                wpawn+=1
        elif piece[0]=='b':
            bpiece+=1
            if piece[1:]=='king':
                bking+=1
            elif piece[1:]=='pawn':
                bpawn+=1
    if wpiece>16 or bpiece>16:
        return False
    if wpawn>8 or bpawn>8:
        return False
    if wking!=1 or bking!=1:
        return False    
    return True
print(isValidChessboard({'1h':'bking', '6c':'wqueen', '2g':'bbishop','5h':'bqueen', '3e':'wking'}))
