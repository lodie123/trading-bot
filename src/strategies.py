def simple_strategy(price_history):
    """
    Simpele strategie:
    - koopt als de prijs een beetje daalt
    - verkoopt als de prijs stijgt
    """
    if len(price_history) < 2:
        return None

    if price_history[-1] < price_history[-2]:
        return "BUY"
    elif price_history[-1] > price_history[-2]:
        return "SELL"
    return None
