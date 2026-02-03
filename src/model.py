def calculate_payout(rainfall_mm):
    if rainfall_mm > 80:
        return 12000  # Catastrophic (Adjusted to calibrate premium)
    elif rainfall_mm > 70:
        return 8000   # Severe
    elif rainfall_mm > 60:
        return 5000   # Moderate
    else:
        return 0      # Normal
