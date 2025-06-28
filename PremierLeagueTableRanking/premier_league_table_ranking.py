import collections

def calculate_premier_league_table(matches):
    team_stats = collections.defaultdict(lambda: {
        'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0
    })

    for team1_name, score1, team2_name, score2 in matches:
        team_stats[team1_name]['MP'] += 1
        team_stats[team2_name]['MP'] += 1

        team_stats[team1_name]['GF'] += score1
        team_stats[team1_name]['GA'] += score2
        team_stats[team2_name]['GF'] += score2
        team_stats[team2_name]['GA'] += score1

        if score1 > score2:
            team_stats[team1_name]['W'] += 1
            team_stats[team1_name]['Pts'] += 3
            team_stats[team2_name]['L'] += 1
        elif score1 < score2:
            team_stats[team2_name]['W'] += 1
            team_stats[team2_name]['Pts'] += 3
            team_stats[team1_name]['L'] += 1
        else:
            team_stats[team1_name]['D'] += 1
            team_stats[team1_name]['Pts'] += 1
            team_stats[team2_name]['D'] += 1
            team_stats[team2_name]['Pts'] += 1

    for team_name in team_stats:
        stats = team_stats[team_name]
        stats['GD'] = stats['GF'] - stats['GA']

    table_data = []
    for team_name, stats in team_stats.items():
        table_data.append((
            team_name,
            stats['MP'],
            stats['W'],
            stats['D'],
            stats['L'],
            stats['GF'],
            stats['GA'],
            stats['GD'],
            stats['Pts']
        ))

    table_data.sort(key=lambda x: (-x[8], -x[7], -x[5], x[0]))

    return table_data

if __name__ == "__main__":
    sample_matches = [
        ("Manchester United", 3, "Liverpool", 1),
        ("Arsenal", 2, "Chelsea", 2),
        ("Liverpool", 0, "Arsenal", 1),
        ("Chelsea", 4, "Manchester United", 0),
        ("Manchester United", 1, "Arsenal", 1),
        ("Liverpool", 2, "Chelsea", 3),
        ("Tottenham", 2, "Everton", 1),
        ("Everton", 0, "Arsenal", 3),
        ("Chelsea", 1, "Tottenham", 1)
    ]

    premier_league_table = calculate_premier_league_table(sample_matches)

    print(f"{'Team':<20} {'MP':>3} {'W':>3} {'D':>3} {'L':>3} {'GF':>3} {'GA':>3} {'GD':>4} {'Pts':>3}")
    print("-" * 65)

    for team_row in premier_league_table:
        team_name, mp, w, d, l, gf, ga, gd, pts = team_row
        print(f"{team_name:<20} {mp:>3} {w:>3} {d:>3} {l:>3} {gf:>3} {ga:>3} {gd:>4} {pts:>3}")