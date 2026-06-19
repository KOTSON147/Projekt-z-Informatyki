import pandas as pd


df = pd.read_excel("tankopedia.csv")

while True:
    komenda = input("\n> ").strip()

    if komenda.lower() == "koniec":
        break

    elif komenda.lower() == "nacja":
        print("\nDostępne nacje:")
        for x in sorted(df["Nacja"].unique()):
            print("-", x)

    elif komenda.lower() == "typ":
        print("\nDostępne typy:")
        for x in sorted(df["Typ"].unique()):
            print("-", x)

    elif komenda.lower() == "tier":
        print("\nDostępne tiery:")
        for x in sorted(df["Tier"].unique()):
            print("-", x)

    else:
        wynik = df[
            (df["Nacja"] == komenda) |
            (df["Typ"] == komenda) |
            (df["Tier"].astype(str) == komenda)
        ]

        if len(wynik):
            print(wynik.to_string(index=False))
        else:
            print("Brak wyników.")