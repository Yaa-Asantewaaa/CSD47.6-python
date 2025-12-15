# Makola Market Inventory and Sales System
inventory = {
    "Tomatoes":{"stock":150, "price_per_unit":5.0},
    "Onions":{"stock":80, "price_per_unit":3.5},
    "Garden Eggs":{"stock":200, "price_per_unit":1.0}
}
item = {}
while True:
    item = input("Enter the item name (or 'exit' to quit): ")
    if item.lower() == 'exit':
        print("Closing sales.Total transactions completed.")
        break
    if item in inventory:
        quantity = int(input(f"Enter the quantity of {item} you want to buy: "))
        if quantity <= inventory[item]["stock"]:
            total_price = quantity * inventory[item]["price_per_unit"]
            inventory[item]["stock"] -= quantity
            print(f"Sales successful! {quantity} {item}(s): ${total_price:.2f}")
            print(f"{inventory[item]['stock']} units of {item} remaining in stock.")
        else:
            print(f"Sorry, only {inventory[item]['stock']} units of  {item}(s) in stock.")
    else:
        print("Item is not found in inventory.Check spelling.")

# Ghana Water Company (GWCL) Billing Calculator
consumption = float(input("Total water consumption for the month (in cubic meters): "))
SERVICE_CHARGE = 15.00
TOTAL_BILL = SERVICE_CHARGE
CONSUMPTION_COSTS = 0
if consumption <= 15:
    CONSUMPTION_COSTS = consumption * 0.90
elif consumption <= 30:
    CONSUMPTION_COSTS = (15 * 0.90) + ((consumption - 15) * 1.20)
else:
    CONSUMPTION_COSTS = (15 * 0.90) + (15 * 1.20) + ((consumption - 30) * 1.80)
TOTAL_BILL += CONSUMPTION_COSTS
print("#nMonthly Water Bill Summary")
print(f"Consumption: {consumption} cubic meters")
print(f"Service Charge: ${SERVICE_CHARGE:.2f}")
print(f"Consumption Costs: ${CONSUMPTION_COSTS:.2f}")
print(f"Total Bill: ${TOTAL_BILL:.2f}")

# Traffic Speed Analyzer for Road Safety
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100
speeding_violations=[]
for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)
TOTAL_VEHICLES = len(recorded_speeds)
TOTAL_VIOLATIONS = len(speeding_violations)
PERCENTAGE_SPEEDING = (TOTAL_VIOLATIONS / TOTAL_VEHICLES) * 100
TOTAL_SPEED = 0
for speed in recorded_speeds:
    TOTAL_SPEED += speed
AVERAGE_SPEED = TOTAL_SPEED / TOTAL_VEHICLES
print(f"Total vehicles recorded: {TOTAL_VEHICLES}")
print(f"Total speeding violations: {TOTAL_VIOLATIONS}")
print(f"Percentage of vehicles speeding: {round(PERCENTAGE_SPEEDING, 2)}%")
print(f"Average speed of all vehicles: {round(AVERAGE_SPEED, 2)} km/h")
focused_segment =  recorded_speeds [2:8]
print(f"\nSpeeds for focused inspection segment (3rd to 8th vehicles): {focused_segment}")
