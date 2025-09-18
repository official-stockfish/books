import base64, chess, chess.pgn, hashlib, io, json, os, subprocess, zipfile

json_file = "books.json"

""" Run 'python update_json.py' to update the meta data stored in books.json.
    Remove books.json if all the information should be recomputed from scratch.
"""


def get_stats_and_sri(compressedbook, old_stats):
    content_bytes = None
    book = compressedbook
    if compressedbook.endswith(".zip"):
        book, _, _ = compressedbook.rpartition(".zip")
        with zipfile.ZipFile(compressedbook) as zip_file:
            content_bytes = zip_file.read(book)
    if content_bytes is None:
        return book, {}

    content_bytes = content_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")

    sri = base64.b64encode(hashlib.sha384(content_bytes).digest()).decode("utf8")

    if book in old_stats and "sri" in old_stats[book] and old_stats[book]["sri"] == sri:
        return book, None  # book is unchanged, no need to compute stats

    content = content_bytes.decode("utf-8", errors="ignore")
    white = black = 0
    min_depth = 2**16
    max_depth = -1
    if book.endswith(".epd"):
        lines = content.splitlines()
        total = len(lines)

        for line in lines:
            fields = line.split()
            if len(fields) > 1:
                if fields[1] == "w":
                    white += 1
                elif fields[1] == "b":
                    black += 1
                else:
                    print("Error: Invalid FEN {line}")
                    return book, {}
            if len(fields) > 5 and fields[5].isdigit():
                move = int(fields[5])
                ply = (move - 1) * 2 if fields[1] == "w" else (move - 1) * 2 + 1
                min_depth = min(min_depth, ply)
                max_depth = max(max_depth, ply)
    elif book.endswith(".pgn"):
        pgn_stream = io.StringIO(content)
        while True:
            game = chess.pgn.read_game(pgn_stream)
            if game is None:
                break
            ply = game.ply() + len(list(game.mainline_moves()))
            min_depth = min(min_depth, ply)
            max_depth = max(max_depth, ply)
            if ply % 2:
                black += 1
            else:
                white += 1

    if min_depth > max_depth:
        min_depth = max_depth = None

    return book, {
        "total": white + black,
        "white": white,
        "black": black,
        "min_depth": min_depth,
        "max_depth": max_depth,
        "sri": sri,
    }


def get_file_list():
    if os.path.exists(".git"):
        p = subprocess.run(["git", "ls-files"], stdout=subprocess.PIPE)
        files = p.stdout.decode().split("\n")
    else:
        files = os.listdir()
    return sorted(files, key=str.lower)


old_stats = {}
if os.path.isfile(json_file):
    with open(json_file) as f:
        old_stats = json.load(f)
    print(f"Read in stats for {len(old_stats)} books from {json_file}.")

new_stats = {}
for filename in get_file_list():
    if (
        filename.endswith(".epd.zip") or filename.endswith(".pgn.zip")
    ) and os.path.isfile(filename):
        print(f"Processing {filename}", end="", flush=True)
        book, stats = get_stats_and_sri(filename, old_stats)
        if stats is not None:
            new_stats[book] = stats
            if "total" in stats:
                print(
                    f", found {stats['total']} lines (w/b = {stats['white']}/{stats['black']})."
                )
            else:
                print("")
        else:
            new_stats[book] = old_stats[book]
            print(", book unchanged. Use old stats.")


with open(json_file, "w") as f:
    json.dump(new_stats, f, indent=4)
    f.write("\n")  # add missing newline character

print(f"\nSaved results to {json_file}.")
