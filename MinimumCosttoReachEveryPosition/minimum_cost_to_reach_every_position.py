class Solution:
    def minCostToReachEveryPosition(self, cost: list[int]) -> list[int]:
        n = len(cost)
        answer = []
        
        # Initialize current_min_cost with a very large value
        # This will hold the minimum cost encountered so far
        # as we iterate through the 'cost' array.
        current_min_cost = float('inf') 
        
        # Iterate through each position i from 0 to n-1
        for i in range(n):
            # To reach position i, we can choose to swap with any person j such that j <= i.
            # If we swap with person j, we pay cost[j]. Once we are at position j,
            # any person k > j is now "behind" us, meaning we can swap with them for free.
            # Therefore, to reach position i, we can pay cost[j] for some j <= i,
            # and then move to position i for free if i > j.
            # The minimum cost to reach position i is thus the minimum of all cost[j]
            # for j from 0 up to i.
            
            # Update current_min_cost to be the minimum of its current value
            # and the cost to swap with the current person i.
            current_min_cost = min(current_min_cost, cost[i])
            
            # Append this minimum cost to the answer array, as it represents
            # the minimum cost to reach position i.
            answer.append(current_min_cost)
            
        return answer