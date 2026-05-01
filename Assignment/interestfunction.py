def compound_interest(balance, rate, years):
    # validation rulesdef compound_interest(balance, rate, years):
    # validation rules
    if rate < 0:
        raise ValueError("Rate cannot be negative")

    if years < 1:
        raise ValueError("Years must be at least 1")

    # formula: balance × (1 + rate) ^ years
    result = balance * (1 + rate) ** years

    return round(result, 2)
    if rate < 0:
        raise ValueError("Rate cannot be negative")

    if years < 1:
        raise ValueError("Years must be at least 1")

    # formula: balance × (1 + rate) ^ years
    result = balance * (1 + rate) ** years

    return round(result, 2)
