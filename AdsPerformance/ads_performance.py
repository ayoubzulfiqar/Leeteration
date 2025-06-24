class AdPerformanceTracker:
    def __init__(self):
        self._total_impressions = 0
        self._total_clicks = 0
        self._total_conversions = 0
        self._total_cost = 0.0

    def add_data(self, impressions: int, clicks: int, conversions: int, cost: float):
        if impressions < 0 or clicks < 0 or conversions < 0 or cost < 0:
            raise ValueError("Input values cannot be negative.")
        self._total_impressions += impressions
        self._total_clicks += clicks
        self._total_conversions += conversions
        self._total_cost += cost

    def get_metrics(self) -> dict:
        metrics = {
            'total_impressions': self._total_impressions,
            'total_clicks': self._total_clicks,
            'total_conversions': self._total_conversions,
            'total_cost': self._total_cost,
            'ctr': 0.0,
            'conversion_rate': 0.0,
            'cpa': None
        }
        if self._total_impressions > 0:
            metrics['ctr'] = (self._total_clicks / self._total_impressions) * 100.0
        if self._total_clicks > 0:
            metrics['conversion_rate'] = (self._total_conversions / self._total_clicks) * 100.0
        if self._total_conversions > 0:
            metrics['cpa'] = self._total_cost / self._total_conversions
        elif self._total_cost > 0:
            metrics['cpa'] = float('inf')
        else:
            metrics['cpa'] = 0.0
        return metrics

if __name__ == "__main__":
    tracker = AdPerformanceTracker()
    print("--- Initial Metrics ---")
    print(tracker.get_metrics())
    tracker.add_data(impressions=1000, clicks=50, conversions=5, cost=25.0)
    print("\n--- Metrics after Campaign A (Day 1) ---")
    metrics_day1 = tracker.get_metrics()
    for key, value in metrics_day1.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker.add_data(impressions=2000, clicks=80, conversions=10, cost=40.0)
    print("\n--- Metrics after Campaign B (Day 1) ---")
    metrics_day2 = tracker.get_metrics()
    for key, value in metrics_day2.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker.add_data(impressions=500, clicks=0, conversions=0, cost=5.0)
    print("\n--- Metrics after zero clicks data ---")
    metrics_zero_clicks = tracker.get_metrics()
    for key, value in metrics_zero_clicks.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker.add_data(impressions=300, clicks=10, conversions=0, cost=15.0)
    print("\n--- Metrics after zero conversions data ---")
    metrics_zero_conversions = tracker.get_metrics()
    for key, value in metrics_zero_conversions.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker_no_cost_no_conv = AdPerformanceTracker()
    tracker_no_cost_no_conv.add_data(impressions=100, clicks=5, conversions=0, cost=0.0)
    print("\n--- Metrics for no cost, no conversions ---")
    metrics_nc_nc = tracker_no_cost_no_conv.get_metrics()
    for key, value in metrics_nc_nc.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker_cost_no_conv = AdPerformanceTracker()
    tracker_cost_no_conv.add_data(impressions=100, clicks=5, conversions=0, cost=10.0)
    print("\n--- Metrics for cost, no conversions ---")
    metrics_c_nc = tracker_cost_no_conv.get_metrics()
    for key, value in metrics_c_nc.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    tracker_empty = AdPerformanceTracker()
    print("\n--- Metrics for empty tracker ---")
    metrics_empty = tracker_empty.get_metrics()
    for key, value in metrics_empty.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (float)) and value is not float('inf') else f"{key}: {value}")
    try:
        tracker.add_data(impressions=-10, clicks=1, conversions=1, cost=1.0)
    except ValueError as e:
        print(f"\n--- Caught expected error: {e} ---")