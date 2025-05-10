import chess, chess.pgn, sys


def pgn_to_epd(bookname):
    epds = set()
    fens = []
    duplicates = []
    count = 0
    pgn = open(bookname)
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        count += 1
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
        epd = board.epd()  # ignore move counters when checking for duplicates
        if epd in epds:
            duplicates.append(count)
        else:
            epds.add(epd)
        fens.append(board.fen())

    if duplicates:
        dstr = ",".join([str(g) for g in duplicates])
        print(f"Warning: The following games lead to a duplicated exit: {dstr}.")

    epdname = bookname.replace(".pgn", ".epd")
    with open(epdname, "w") as f:
        for fen in fens:
            f.write(fen + "\n")
    print(f"Wrote the converted book to {epdname}.")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].endswith(".pgn"):
        pgn_to_epd(sys.argv[1])
    else:
        print(f"Usage: python {sys.argv[0]} <book.pgn>")
        print("\nConverts a .pgn into an .epd book, keeping the order intact.")
