def celsius_a_fahrenheit(gradi: float) -> float:
    """Converte gradi Celsius in Fahrenheit."""
    return (gradi * 9.0 / 5.0) + 32.0


def km_a_miglia(km: float) -> float:
    """Converte chilometri in miglia terrestri."""
    return km * 0.621371


if __name__ == "__main__":
    print(f"0°C = {celsius_a_fahrenheit(0):.1f}°F")
    print(f"10 km = {km_a_miglia(10):.2f} miglia")
