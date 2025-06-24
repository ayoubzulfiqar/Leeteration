def calculate_query_metrics(queries_table):
    grouped_queries = {}
    for query in queries_table:
        query_name = query['query_name']
        if query_name not in grouped_queries:
            grouped_queries[query_name] = []
        grouped_queries[query_name].append(query)

    result = []
    for query_name, query_list in grouped_queries.items():
        total_ratio_sum = 0
        poor_query_count = 0
        total_queries_in_group = len(query_list)

        for query in query_list:
            total_ratio_sum += query['rating'] / query['position']
            if query['rating'] < 3:
                poor_query_count += 1

        quality = round(total_ratio_sum / total_queries_in_group, 2)
        
        poor_query_percentage = round((poor_query_count / total_queries_in_group) * 100, 2)

        result.append({
            'query_name': query_name,
            'quality': quality,
            'poor_query_percentage': poor_query_percentage
        })
    
    return result