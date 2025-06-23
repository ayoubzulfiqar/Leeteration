class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        
        # Create a list of tuples (score_value, original_index)
        indexed_scores = []
        for i in range(n):
            indexed_scores.append((score[i], i))
            
        # Sort the indexed_scores in descending order based on the score_value
        indexed_scores.sort(key=lambda x: x[0], reverse=True)
        
        # Initialize the result array with empty strings
        answer = [""] * n
        
        # Assign ranks based on sorted order
        for rank_pos, (s, original_idx) in enumerate(indexed_scores):
            if rank_pos == 0:
                answer[original_idx] = "Gold Medal"
            elif rank_pos == 1:
                answer[original_idx] = "Silver Medal"
            elif rank_pos == 2:
                answer[original_idx] = "Bronze Medal"
            else:
                # For 4th place onwards, the rank is the placement number
                answer[original_idx] = str(rank_pos + 1)
                
        return answer