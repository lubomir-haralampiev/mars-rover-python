def ensure_has_odd_lentgh(list):
    if len(list) % 2 == 0:
        raise ValueError("The array has even length")
