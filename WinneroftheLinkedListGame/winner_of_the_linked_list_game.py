# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def gameWinner(self, head: Optional[ListNode]) -> str:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        n = len(values)

        if n == 0:
            return "Tie"

        # dp[i][j] stores the maximum net score (current player's score - opponent's score)
        # achievable from the sublist values[i...j]
        dp = [[0] * n for _ in range(n)]

        # Base cases: sublists of length 1
        # When only one element is left, the current player takes it,
        # so their net score is just the value of that element.
        for i in range(n):
            dp[i][i] = values[i]

        # Fill DP table for increasing sublist lengths (l)
        # length ranges from 2 to n (inclusive)
        for length in range(2, n + 1):
            # i is the starting index of the sublist
            # j is the ending index of the sublist
            # i ranges from 0 to n - length
            for i in range(n - length + 1):
                j = i + length - 1

                # Option 1: Current player picks values[i] (left end)
                # Current player gains values[i].
                # The game then continues with the sublist values[i+1...j].
                # It's now the opponent's turn. The opponent will play optimally
                # to maximize their net score from values[i+1...j], which is dp[i+1][j].
                # From the current player's perspective, this means the opponent's
                # net score dp[i+1][j] is subtracted from the current player's net gain.
                choice1 = values[i] - dp[i+1][j]

                # Option 2: Current player picks values[j] (right end)
                # Similar logic as above, but for picking from the right end.
                choice2 = values[j] - dp[i][j-1]

                # The current player chooses the option that maximizes their net score.
                dp[i][j] = max(choice1, choice2)

        # The final result is dp[0][n-1], representing the maximum net score Alice can achieve
        # when playing on the entire list values[0...n-1].
        final_net_score = dp[0][n-1]

        if final_net_score > 0:
            return "Alice"
        elif final_net_score < 0:
            return "Bob"
        else:
            return "Tie"