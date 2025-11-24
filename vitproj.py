def sales_calculator(cost=None, revenue=None, profit=None, markup=None, grossMargin=None):
  
    if markup is not None:
        markup = markup / 100
    if grossMargin is not None:
        grossMargin = grossMargin / 100

    # 1) cost + revenue
    if cost is not None and revenue is not None:
        profit = revenue - cost

    # 2) cost + profit
    elif cost is not None and profit is not None:
        revenue = cost + profit

    # 3) revenue + profit
    elif revenue is not None and profit is not None:
        cost = revenue - profit

    # 4) cost + markup
    elif cost is not None and markup is not None:
        profit = cost * markup
        revenue = cost + profit

    # 5) revenue + markup
    elif revenue is not None and markup is not None:
        cost = revenue / (1 + markup)
        profit = revenue - cost

    # 6) revenue + grossMargin
    elif revenue is not None and grossMargin is not None:
        profit = revenue * grossMargin
        cost = revenue - profit

    # 7) cost + margin
    elif cost is not None and grossMargin is not None:
        profit = cost * grossMargin / (1 - grossMargin)
        revenue = cost + profit

    else:
        raise ValueError("You must provide a valid combination of TWO values.")

    markup = (profit / cost) if cost else 0
    grossMargin = (profit / revenue) if revenue else 0

    return {
        "cost": cost,
        "revenue": revenue,
        "profit": profit,
        "markup_percent": markup * 100,
        "grossMargin_percent": grossMargin * 100
    }

if __name__ == "__main__":
    print("Enter two fields from:")
    print("1. cost")
    print("2. revenue")
    print("3. profit")
    print("4. markup (%)")
    print("5. grossMargin (%)")

    a = input("Enter first field you want to provide: ").strip().lower()
    b = input("Enter second field you want to provide: ").strip().lower()
   
    values = {"cost": None, "revenue": None, "profit": None, "markup": None, "grossMargin": None}

    values[a] = float(input(f"Enter value for {a}: "))
    values[b] = float(input(f"Enter value for {b}: "))

    result = sales_calculator(**values)

    print("\n--- Sales Summary ---")
    print(f"Cost: {result['cost']:.2f}")
    print(f"Revenue: {result['revenue']:.2f}")
    print(f"Profit: {result['profit']:.2f}")
    print(f"Markup: {result['markup_percent']:.2f}%")
    print(f"Gross Margin: {result['grossMargin_percent']:.2f}%")