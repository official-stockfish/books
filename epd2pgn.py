import chess, sys


def epd_to_pgn(bookname):
    epds = set()
    duplicates = []
    pgnname = bookname.replace(".epd", ".pgn")
    with open(bookname) as epd, open(pgnname, "w") as pgn:
        for count, line in enumerate(epd):
            assert ";" not in line, "Expect FENs w/ or w/o move counters"
            fields = line.split()
            epd = " ".join(fields[:4])
            epd = chess.Board(epd).epd()  # remove superfluous ep square
            if epd in epds:
                duplicates.append(count + 1)
            else:
                epds.add(epd)
            pgn.write('[FEN "' + line.strip() + '"]\n')
            pgn.write('[Result "*"]\n')
            pgn.write("\n")
            pgn.write("*\n\n")

    if duplicates:
        dstr = ",".join([str(g) for g in duplicates])
        print(f"Warning: The following FENs are a duplicate: {dstr}.")

    print(f"Wrote the converted book to {pgnname}.")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].endswith(".epd"):
        epd_to_pgn(sys.argv[1])
    else:
        print(f"Usage: python {sys.argv[0]} <book.epd>")
        print("\nConverts an .epd into a .pgn book, keeping the order intact.")
