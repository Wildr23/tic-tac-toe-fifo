#!/usr/bin/env python3
"""
Tic Tac Toe - Console Version (Independent FIFO Mode)
X and O each have their own 3-mark limit. When a player places their 4th mark,
their OLDEST mark of THE SAME TYPE is removed.

Example: X can have up to 3 X's on board. When X places 4th X, oldest X vanishes.
         Same applies to O - independent FIFO queue per player!
"""

def print_board(board):
    """Print the current game board."""
    print("\n")
    print(f"  {board[0]} | {board[1]} | {board[2]} ")
    print("  ---------")
    print(f"  {board[3]} | {board[4]} | {board[5]} ")
    print("  ---------")
    print(f"  {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def print_instructions():
    """Print game instructions."""
    print("=" * 50)
    print("TIC TAC TOE - INDEPENDENT FIFO MODE")
    print("=" * 50)
    print("Positions: 1 | 2 | 3")
    print("           4 | 5 | 6")
    print("           7 | 8 | 9")
    print("-" * 50)
    print("RULES:")
    print("- X can have up to 3 X marks on the board!")
    print("- O can have up to 3 O marks on the board!")
    print("- When a player places their 4th mark,")
    print("  THE OLDEST MARK OF THE SAME TYPE vanishes (FIFO)")
    print("- First player to get all 3 in a row/column/diagonal WINS!")
    print("=" * 50)
    print("\n")

def is_valid_position(board, position):
    """Check if the position is valid (within bounds and not taken)."""
    return 0 <= position < 9 and board[position] == ''

def count_marks_for_player(board, player):
    """Count how many marks a player has on the board."""
    return sum(1 for mark in board if mark == player)

def check_winner(board):
    """Check for a winner - all 3 marks in same player."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    return None

def get_player_move(board, player):
    """Get a valid move from the player."""
    while True:
        try:
            position = int(input(f"\nPlayer {player}, enter your position (1-9): ")) - 1
            if is_valid_position(board, position):
                return position
            else:
                print("Invalid position! Please choose an empty spot (1-9).")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def remove_oldest_mark_of_player(board, mark_order_queue, player):
    """Remove the oldest mark of a specific player from the board."""
    if len(mark_order_queue) == 0:
        return
    
    oldest_index = mark_order_queue.pop(0)  # Remove first element from queue (FIFO)
    
    if oldest_index >= 0 and oldest_index < len(board):
        old_mark = board[oldest_index]
        print(f"→ FIFO! Removing oldest {player} at position {oldest_index + 1} ({old_mark})...")
        board[oldest_index] = ''

def play_game():
    """Main game function."""
    board = [''] * 9
    mark_order_X = []  # Track order for X marks (FIFO queue)
    mark_order_O = []  # Track order for O marks (FIFO queue)
    current_player = 'X'
    max_marks_per_player = 3
    
    print_instructions()
    
    while True:
        print_board(board)
        
        move = get_player_move(board, current_player)
        
        # If this player already has 3 marks on board, remove their oldest mark first
        if len(mark_order_X) >= max_marks_per_player and current_player == 'X':
            print("\n⚠️ X has max marks (3)! Placing new mark will remove oldest X...")
            remove_oldest_mark_of_player(board, mark_order_X, 'X')
        
        if len(mark_order_O) >= max_marks_per_player and current_player == 'O':
            print("\n⚠️ O has max marks (3)! Placing new mark will remove oldest O...")
            remove_oldest_mark_of_player(board, mark_order_O, 'O')
        
        # Place the mark
        board[move] = current_player
        
        if current_player == 'X':
            mark_order_X.append(move)
        else:
            mark_order_O.append(move)
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            
            # Count marks for display
            x_count = count_marks_for_player(board, 'X')
            o_count = count_marks_for_player(board, 'O')
            
            print(f"\n🎉 PLAYER {winner} WINS! 🎉")
            print("All 3 marks were in a line!")
            print(f"(Board has {x_count} X's and {o_count} O's)")
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break
            
            # Reset game
            board = [''] * 9
            mark_order_X = []
            mark_order_O = []
            current_player = 'X'
            print("\n" + "=" * 50 + "\n")
        else:
            x_count = count_marks_for_player(board, 'X')
            o_count = count_marks_for_player(board, 'O')
            
            status_msg = f"\nBoard state: {x_count} X(s) | {o_count} O(s)"
            if len(mark_order_X) >= max_marks_per_player:
                status_msg += " ← Next X will remove oldest!"
            elif len(mark_order_O) >= max_marks_per_player:
                status_msg += " ← Next O will remove oldest!"
            
            print(status_msg)
            
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

def main():
    """Entry point."""
    while True:
        play_game()
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()