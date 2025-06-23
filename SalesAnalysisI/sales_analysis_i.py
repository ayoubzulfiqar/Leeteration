def perform_sales_analysis():
    try:
        sales_str = input()
        sales_figures = [float(x) for x in sales_str.split()]

        if not sales_figures:
            print(f"{0.00:.2f}")
            print(f"{0.00:.2f}")
            print(f"{0.00:.2f}")
            print(f"{0.00:.2f}")
            return

        total_sales = sum(sales_figures)
        num_sales = len(sales_figures)
        average_sales = total_sales / num_sales
        max_sale = max(sales_figures)
        min_sale = min(sales_figures)

        print(f"{total_sales:.2f}")
        print(f"{average_sales:.2f}")
        print(f"{max_sale:.2f}")
        print(f"{min_sale:.2f}")

    except ValueError:
        pass
    except EOFError:
        pass

perform_sales_analysis()