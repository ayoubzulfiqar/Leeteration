import collections

class Solution:
    def find_largest_order_customer(self, orders_table: list[dict]) -> int | None:
        if not orders_table:
            return None

        customer_order_counts = collections.defaultdict(int)
        for order in orders_table:
            customer_number = order['customer_number']
            customer_order_counts[customer_number] += 1

        max_orders = max(customer_order_counts.values())

        result_customer = None
        for customer, count in customer_order_counts.items():
            if count == max_orders:
                result_customer = customer
                break

        return result_customer