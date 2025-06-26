class Solution:
    def findLosers(self, n: int, k: int) -> list[int]:
        received_ball = set()
        all_friends = set(range(1, n + 1))

        current_friend = 1
        received_ball.add(current_friend)

        turn = 1
        while True:
            steps = turn * k
            
            # Calculate the next friend using 0-indexed arithmetic for modulo, then convert back to 1-indexed
            next_friend_0_indexed = (current_friend - 1 + steps) % n
            next_friend = next_friend_0_indexed + 1

            if next_friend in received_ball:
                break
            else:
                received_ball.add(next_friend)
                current_friend = next_friend
                turn += 1
        
        losers = sorted(list(all_friends - received_ball))
        return losers