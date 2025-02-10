# Stockfish Chess Books Repository

📌 **This directory contains a collection of books that may be used for chess engine development in Stockfish.**

## 📂 Contents

### 1. **Types of Books**
   - **Unbalanced Human Openings (UHO)**: A curated collection by Stefan Pohl focusing on unbalanced and creative play.
   - **FRC/Chess960 Books**: Books designed for Fischer Random Chess.
   - **DFRC Openings**: Datasets for **Double Fischer Random Chess**.
   - **Popular Position Books**: Collections based on position frequency, including Lichess-based data.
   - **Endgame Books**: Specialized datasets for evaluating endgame play.
   - **Drawkiller Books**: Designed to reduce early draws and encourage fighting chess.
   - **Hybrid Book**: Hybrid book beta.

### 2. **File Formats**
   - **EPD (.epd)**: Chess position databases storing multiple positions.
   - **PGN (.pgn)**: Standard format for storing chess games and move sequences.
   - **Python Scripts (.py)**: Utilities for processing and converting datasets, including:
     - `epd2pgn.py` - Converts EPD books to PGN format.
     - `epd_inverter.py` - Inverts an EPD book for analysis.
