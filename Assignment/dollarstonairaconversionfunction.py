def dollars_to_naira(amount_in_dollars):
    rate = 1550
    naira_amount = amount_in_dollars * rate
    
    return round(naira_amount, 2)
