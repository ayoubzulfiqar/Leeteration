import collections

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        scores_by_id = collections.defaultdict(list)

        for student_id, score in items:
            scores_by_id[student_id].append(score)

        result = []
        for student_id in sorted(scores_by_id.keys()):
            scores = scores_by_id[student_id]
            scores.sort(reverse=True)
            
            top_5_scores = scores[:5]
            
            average = sum(top_5_scores) // 5 

            result.append([student_id, average])
        
        return result