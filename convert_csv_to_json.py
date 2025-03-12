import pandas as pd
import json

# Define input and output file paths
csv_file = "final_cocktails.csv"   # Input CSV file
json_file = "cocktail_dataset.json"  # Output JSON file

# Load the CSV file
df = pd.read_csv(csv_file)

# Convert dataset to JSON format
cocktails = []
for _, row in df.iterrows():
    cocktail = {
        "id": row["id"],
        "name": row["name"],
        "alcoholic": row["alcoholic"],
        "category": row["category"],
        "glassType": row["glassType"],
        "instructions": row["instructions"],
        "drinkThumbnail": row["drinkThumbnail"],
        "ingredients": row["ingredients"].strip("[]").replace("'", "").split(", "),
        "ingredientMeasures": row["ingredientMeasures"].strip("[]").replace("'", "").split(", ")
    }
    cocktails.append(cocktail)

# Save as JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(cocktails, f, indent=4, ensure_ascii=False)

print(f"Successfully converted '{csv_file}' to '{json_file}'")
