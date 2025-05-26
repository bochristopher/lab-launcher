import os

def run_script(name):
    print(f"Running: {name}")
    os.system(f"python3 {name}")

scripts = {
    "1": "calibration.py",
    "2": "log_impedance.py",
    "3": "exit"
}

while True:
    print("\nAvailable Scripts:")
    for key, val in scripts.items():
        print(f"{key}: {val}")

    choice = input("Choose a script: ")
    if choice == "3":
        break
    elif choice in scripts:
        run_script(scripts[choice])
    else:
        print("Invalid choice.")
