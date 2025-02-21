import os
import glob
import json
import logging

# Sätt upp loggning
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

DATA_DIR = "completed_data"
FIXED_DIR = "fixed_data"  # Mapp för fixerade JSON-filer

def validate_and_fix_json(directory):
    """
    Validerar JSON-filer och tar bort ogiltiga poster.
    """
    json_files = glob.glob(os.path.join(directory, "*.json"))
    os.makedirs(FIXED_DIR, exist_ok=True)  # Skapa mapp för fixerade filer

    total_files = len(json_files)
    invalid_files = []
    total_entries = 0
    removed_entries = 0

    logging.info(f"🔍 Börjar validera och fixa {total_files} JSON-filer i '{directory}'...")

    for file in json_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Om filen innehåller "qa_pairs" eller "fine_tuning_data", extrahera dem
            if isinstance(data, dict):
                if "qa_pairs" in data:
                    data = data["qa_pairs"]
                elif "fine_tuning_data" in data:
                    data = data["fine_tuning_data"]
                else:
                    logging.warning(f"⚠️ Okänt format i {file}.")
                    invalid_files.append(file)
                    continue

            # Kontrollera att det nu är en lista med rätt struktur
            if not isinstance(data, list):
                logging.error(f"❌ {file} innehåller inte en lista av objekt!")
                invalid_files.append(file)
                continue

            valid_entries = []
            for i, entry in enumerate(data):
                total_entries += 1
                user_input = entry.get("user_input")
                ai_output = entry.get("ai_output")

                if not isinstance(user_input, str) or not isinstance(ai_output, str):
                    logging.warning(f"🚨 Tar bort ogiltig post i {file}, rad {i + 1}: {entry}")
                    removed_entries += 1
                else:
                    valid_entries.append({"user_input": user_input, "ai_output": ai_output})

            # Om inga giltiga poster finns kvar, ta bort filen helt
            if not valid_entries:
                logging.error(f"🗑 Raderar {file} - inga giltiga poster kvar!")
                os.remove(file)
                continue

            # Spara den fixade filen utan ogiltiga poster
            fixed_file_path = os.path.join(FIXED_DIR, os.path.basename(file))
            with open(fixed_file_path, "w", encoding="utf-8") as f:
                json.dump(valid_entries, f, ensure_ascii=False, indent=4)

            logging.info(f"✅ Sparade fixad version av {file} i {FIXED_DIR}/")

        except json.JSONDecodeError as e:
            logging.error(f"❌ Felaktig JSON-syntax i {file}: {e}")
            invalid_files.append(file)
        except Exception as e:
            logging.error(f"❌ Oväntat fel vid inläsning av {file}: {e}")
            invalid_files.append(file)

    logging.info("✅ Validering och fixning klar!")
    logging.info(f"📂 Totalt {total_files} filer, {total_entries} poster kontrollerade.")
    
    if removed_entries == 0:
        logging.info("🎉 Inga ogiltiga poster hittades!")
    else:
        logging.warning(f"⚠️ {removed_entries} poster togs bort på grund av fel.")

    if invalid_files:
        logging.warning(f"🚨 {len(invalid_files)} filer hade problem och kan behöva kontrolleras manuellt:")
        for f in invalid_files:
            logging.warning(f" - {f}")

    return invalid_files


# Kör validering och fixning
if __name__ == "__main__":
    invalid_files = validate_and_fix_json(DATA_DIR)
