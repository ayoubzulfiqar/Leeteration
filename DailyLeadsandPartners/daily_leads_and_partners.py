from collections import defaultdict

def daily_leads_and_partners(daily_sales: list[dict]) -> list[dict]:
    grouped_data = defaultdict(lambda: {'leads': set(), 'partners': set()})

    for row in daily_sales:
        date_id = row['date_id']
        make_name = row['make_name']
        lead_id = row['lead_id']
        partner_id = row['partner_id']

        group_key = (date_id, make_name)
        
        grouped_data[group_key]['leads'].add(lead_id)
        grouped_data[group_key]['partners'].add(partner_id)
    
    result = []
    for (date_id, make_name), counts in grouped_data.items():
        unique_leads = len(counts['leads'])
        unique_partners = len(counts['partners'])
        
        result.append({
            'date_id': date_id,
            'make_name': make_name,
            'unique_leads': unique_leads,
            'unique_partners': unique_partners
        })
            
    return result