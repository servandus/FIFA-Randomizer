import random
import tkinter as tk

def randomizer(result_label):
    positions = ["Goalkeeper", "Defender", "Midfielder", "Striker"]
    players = ["Benja", "Pollo", "Jesus", "Ser"]
    assigned_positions = {}
    
    for i in players:
        if "Goalkeeper" not in assigned_positions.values():
            position = random.choice(positions)
            if position == "Goalkeeper":
                positions.remove("Goalkeeper")
        else:
            position = random.choice(positions)
        
        assigned_positions[i] = position
    
    result = "\n".join([f"{player} will be a {position}" for player, position in assigned_positions.items()])
    result_label.config(text=result)

def main():
    root = tk.Tk()
    root.title("Randomizer")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    start_button = tk.Button(frame, text="Start Randomizer", command=lambda: randomizer(result_label))
    start_button.pack(pady=5)

    result_label = tk.Label(frame, text="", justify="left", padx=10, pady=10)
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()