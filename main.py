import json
import os


class KDTracker:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.players = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.players = json.load(file)
        else:
            self.players = []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.players, file, indent=4)

    def add_player(self, name, kills, deaths):
        kd = kills / deaths if deaths != 0 else kills
        player = {
            "player_name": name,
            "kills": kills,
            "deaths": deaths,
            "kd": round(kd, 2)
        }
        self.players.append(player)
        self.save_data()
        print("Player added successfully.")

    def show_players(self):
        if not self.players:
            print("No data found.")
            return

        for index, player in enumerate(self.players, start=1):
            print(
                f"{index}. {player['player_name']} | "
                f"Kills: {player['kills']} | "
                f"Deaths: {player['deaths']} | "
                f"KD: {player['kd']}"
            )

    def show_average_kd(self):
        if not self.players:
            print("No data available.")
            return

        total_kd = sum(player["kd"] for player in self.players)
        average_kd = total_kd / len(self.players)
        print(f"Average KD: {round(average_kd, 2)}")

    def show_best_player(self):
        if not self.players:
            print("No data available.")
            return

        best_player = max(self.players, key=lambda p: p["kd"])
        print(
            f"Best Player: {best_player['player_name']} "
            f"with KD {best_player['kd']}"
        )


def show_menu():
    print("\n--- PUBG KD Tracker ---")
    print("1. Add player")
    print("2. Show all players")
    print("3. Show average KD")
    print("4. Show best player")
    print("5. Exit")


def main():
    tracker = KDTracker()

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Player name: ")
            kills = int(input("Kills: "))
            deaths = int(input("Deaths: "))
            tracker.add_player(name, kills, deaths)

        elif choice == "2":
            tracker.show_players()

        elif choice == "3":
            tracker.show_average_kd()

        elif choice == "4":
            tracker.show_best_player()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
