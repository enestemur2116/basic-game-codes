import datetime

records = []


def calculate_kd(kills, deaths):
    if deaths == 0:
        return float("inf")
    return round(kills / deaths, 2)


def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except:
            print("Please enter a valid number.")


def create_record():
    player = input("Player name: ")
    kills = get_int_input("Kills: ")
    deaths = get_int_input("Deaths: ")

    kd = calculate_kd(kills, deaths)

    record = {
        "player": player,
        "kills": kills,
        "deaths": deaths,
        "kd": kd,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    records.append(record)

    print("KD:", kd)


def show_records():
    if not records:
        print("No records found.")
        return

    print("\n--- RECORDS ---")
    for r in records:
        print(
            f"{r['time']} | "
            f"Player:{r['player']} | "
            f"Kills:{r['kills']} | "
            f"Deaths:{r['deaths']} | "
            f"KD:{r['kd']}"
        )


def average_kd():
    valid_kd = [r["kd"] for r in records if r["kd"] != float("inf")]

    if not valid_kd:
        return "Infinite"

    return round(sum(valid_kd) / len(valid_kd), 2)


def best_kd():
    if not records:
        return None
    return max(records, key=lambda r: r["kd"])


def show_statistics():
    if not records:
        print("No data to analyze.")
        return

    avg = average_kd()
    best = best_kd()

    print("\n--- STATISTICS ---")
    print("Average KD:", avg)

    if best:
        print(
            "Best KD -> "
            f"Player:{best['player']} KD:{best['kd']}"
        )


def show_menu():
    print("\n--- PUBG KD TRACKER ---")
    print("1 - Add new record")
    print("2 - Show all records")
    print("3 - Show statistics")
    print("0 - Exit")


while True:
    show_menu()
    choice = input("Choice: ")

    if choice == "1":
        create_record()

    elif choice == "2":
        show_records()

    elif choice == "3":
        show_statistics()

    elif choice == "0":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")

