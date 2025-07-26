import matplotlib.pyplot as plt

# Step 1: Input values manually
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5','Days 6']
moisture_levels = []

print("Enter soil moisture level (0 to 100) for each day:")
for day in days:
    level = float(input(f"{day}: "))
    moisture_levels.append(level)

# Step 2: Show decision
for i, level in enumerate(moisture_levels):
    if level < 30:
        print(f"{days[i]}: Soil is dry. Start irrigation.")
    elif level > 70:
        print(f"{days[i]}: Soil is too wet. Do not irrigate.")
    else:
        print(f"{days[i]}: Moisture is optimal.")

# Step 3: Plot the graph
plt.plot(days, moisture_levels, marker='o', linestyle='-', color='green')
plt.axhline(y=30, color='red', linestyle='--', label='Too Dry')
plt.axhline(y=70, color='blue', linestyle='--', label='Too Wet')
plt.title('Soil Moisture Trend')
plt.xlabel('Days')
plt.ylabel('Moisture Level (%)')
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()
