import csv

def export_to_csv(data):
    with open("export.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerows(data)

print("Eksports darbojas")
