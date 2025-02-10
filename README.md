# Stockfish Chess Books Repository

📌 **This directory contains a collection of books that may be used for chess engine development in Stockfish.**

## 📂 Contents

### 1. **Types of Books**
   - **Unbalanced Human Openings (UHO)**: A curated collection by Stefan Pohl focusing on unbalanced and moves 100% played by humans.
   - **FRC/Chess960 Books**: Datasets for **Chess960/Fischer Random Chess**.
   - **DFRC Openings**: Datasets for **Double Fischer Random Chess**.
   - **@bjbraams's Chess Database**: Biased (dbcn) and known from human master play.
   - **Popular Position Books**:
   - **Endgame Books**:
   - **Drawkiller Books**:
   - **Hybrid Book**:

### 2. **File Formats**
   - **EPD (.epd)**: Chess position databases storing multiple positions.
   - **PGN (.pgn)**: Standard format for storing chess games and move sequences.
   - **Python Scripts (.py)**: Utilities for processing and converting datasets, including:
     - `epd2pgn.py` - Converts EPD books to PGN format.
     - `epd_inverter.py` - Inverts an EPD book for analysis.
