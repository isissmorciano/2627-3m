from .conversioni import celsius_a_fahrenheit, km_a_miglia


def main() -> None:
    temp_c = float(input("Inserisci temperatura in °C: "))
    dist_km = float(input("Inserisci distanza in km: "))

    temp_f = celsius_a_fahrenheit(temp_c)
    dist_mi = km_a_miglia(dist_km)

    print(f"{temp_c:.1f}°C equivalgono a {temp_f:.1f}°F")
    print(f"{dist_km:.2f} km equivalgono a {dist_mi:.2f} miglia")


if __name__ == "__main__":
    main()
