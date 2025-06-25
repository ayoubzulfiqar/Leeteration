```python
def solve():
    n = int(input())
    scores = {}
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    
    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]
    
    if len(winners) == 1:
        print(winners[0])
        return
    
    scores_history = {}
    for name in scores:
        scores_history[name] = []
        
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        
        for player in scores_history:
            if player == name:
                if len(scores_history[player]) > 0:
                    scores_history[player].append(scores_history[player][-1] + score)
                else:
                    scores_history[player].append(score)
            else:
                if len(scores_history[player]) > 0:
                    scores_history[player].append(scores_history[player][-1])
                else:
                    scores_history[player].append(0)
    
    potential_winners = [name for name in scores if scores[name] == max_score]
    
    for name in potential_winners:
        for i in range(n):
            if scores_history[name][i] >= max_score:
                
                is_winner = True
                for other_name in potential_winners:
                    if other_name != name and scores_history[other_name][i] >= max_score:
                        is_winner = False
                        break
                if is_winner:
                    print(name)
                    return

solve()
```