class Solution:
    def canAliceWin(self, n: int) -> bool:
        current_stones = n
        stones_to_remove = 10
        is_alice_turn = True

        while True:
            # Check if the current player can make a move
            # A player cannot make a move if:
            # 1. The remaining stones are less than the required stones to remove.
            # 2. The required stones to remove is 0 or less (as removing 0 or negative stones is not a valid move).
            if current_stones < stones_to_remove or stones_to_remove <= 0:
                # The current player cannot make a move, so they lose.
                # The other player (who just made a move) wins.
                if is_alice_turn:
                    # It's Alice's turn, but she cannot move. Alice loses.
                    return False
                else:
                    # It's Bob's turn, but he cannot move. Bob loses, which means Alice wins.
                    return True

            # If the current player can make a move, perform it
            current_stones -= stones_to_remove

            # Prepare for the next turn
            stones_to_remove -= 1
            is_alice_turn = not is_alice_turn