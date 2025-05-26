# Dummy script for logging impedance measurements
freq = input("Enter frequency (Hz): ")
mag = input("Enter magnitude (Ohms): ")
phase = input("Enter phase (degrees): ")

with open("impedance_log.csv", "a") as f:
    f.write(f"{freq},{mag},{phase}\n")

print("Logged impedance data.")
