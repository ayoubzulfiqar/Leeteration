import collections

class Solution:
    def game_play_analysis_ii(self, activity: list[dict]) -> list[dict]:
        player_first_login = {}

        for record in activity:
            player_id = record['player_id']
            event_date = record['event_date']
            device_id = record['device_id']

            if player_id not in player_first_login:
                player_first_login[player_id] = {
                    'event_date': event_date,
                    'device_id': device_id
                }
            else:
                current_first_login_date = player_first_login[player_id]['event_date']

                if event_date < current_first_login_date:
                    player_first_login[player_id] = {
                        'event_date': event_date,
                        'device_id': device_id
                    }
                elif event_date == current_first_login_date:
                    current_device_id = player_first_login[player_id]['device_id']
                    if device_id < current_device_id:
                        player_first_login[player_id]['device_id'] = device_id
        
        result = []
        for player_id, data in player_first_login.items():
            result.append({
                'player_id': player_id,
                'device_id': data['device_id']
            })
        
        result.sort(key=lambda x: x['player_id'])
        
        return result