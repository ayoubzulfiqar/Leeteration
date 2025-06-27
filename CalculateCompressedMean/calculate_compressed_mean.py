def calculate_compressed_mean(compressed_data):
    total_sum = 0
    total_count = 0
    for value, frequency in compressed_data:
        total_sum += value * frequency
        total_count += frequency
    if total_count == 0:
        return 0.0
    return float(total_sum) / total_count