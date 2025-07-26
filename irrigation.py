import matplotlib.pyplot as plt

def get_decision(moisture):
    if moisture < 500:
        return "💧 Pump ON"
    else:
        return "✅ Moisture OK - Pump OFF"

# Empty lists to hold data
moisture_values = []
decisions = []

# Get manual input
n = int(input("How many readings do you want to enter? "))
for i in range(n):
    val = int(input(f"Enter moisture value {i+1} (0–1023): "))
    moisture_values.append(val)
    decisions.append(get_decision(val))

# Display the decision for each reading
print("\nSummary:")
for i in range(n):
    print(f"Reading {i+1}: {moisture_values[i]} → {decisions[i]}")

# Plot the moisture values
plt.plot(range(1, n+1), moisture_values, marker='o', color='green', label='Soil Moisture')
plt.axhline(y=500, color='red', linestyle='--', label='Threshold (500)')
plt.title("Simulated Soil Moisture Readings")
plt.xlabel("Reading Number")
plt.ylabel("Moisture Level (0–1023)")
plt.legend()
plt.grid(True)
plt.show()
