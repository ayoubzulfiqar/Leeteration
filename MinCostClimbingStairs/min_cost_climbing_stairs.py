class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        # prev2 represents the minimum cost to reach step (i-2) and pay its cost.
        # prev1 represents the minimum cost to reach step (i-1) and pay its cost.
        # These are our base cases for the first two steps.
        prev2 = cost[0]
        prev1 = cost[1]

        # Iterate from the third step (index 2) up to the last step (index n-1).
        # For each step i, we calculate the minimum cost to reach it and pay cost[i].
        for i in range(2, n):
            # The minimum cost to reach the current step 'i' (and pay cost[i])
            # is cost[i] plus the minimum of the costs to reach the previous two steps.
            # You can either come from step (i-1) or step (i-2).
            current_cost = cost[i] + min(prev1, prev2)
            
            # Update prev2 and prev1 for the next iteration:
            # The 'old' prev1 becomes the new prev2 (representing dp[i-1] for the next step).
            # The 'current_cost' becomes the new prev1 (representing dp[i] for the next step).
            prev2 = prev1
            prev1 = current_cost
        
        # After iterating through all steps up to n-1,
        # prev1 holds the minimum cost to reach step n-1 (dp[n-1]),
        # and prev2 holds the minimum cost to reach step n-2 (dp[n-2]).
        # The "top of the floor" is effectively one step beyond the last element.
        # You can reach the top either by taking one step from n-1, or two steps from n-2.
        # Therefore, the minimum cost to reach the top is the minimum of dp[n-1] and dp[n-2].
        return min(prev1, prev2)