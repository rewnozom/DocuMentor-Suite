import os
import json

MAX_FILE_SIZE_MB = 100  # Maxstorlek per fil i MB
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024  # Konvertera till bytes
OUTPUT_DIR = "./completed_data"  # Sökväg där JSON-filerna ska sparas

def ensure_output_directory():
    """ Skapar output-mappen om den inte finns """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def load_json_file(file_path):
    """
    Försöker läsa in en JSON-fil och returnerar dess innehåll.
    Om filen är ogiltig, returnera None.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Fel vid JSON parsing av {file_path}: {e} (Fil hoppas över)")
        return None
    except Exception as e:
        print(f"Övrigt fel vid läsning av {file_path}: {e} (Fil hoppas över)")
        return None

def split_and_save_json(data, output_prefix="combined"):
    """
    Delar upp en stor lista av JSON-data i flera filer om den överskrider MAX_FILE_SIZE_BYTES.
    """
    ensure_output_directory()  # Säkerställ att output-mappen finns
    file_index = 0
    current_chunk = []
    current_size = 0

    for entry in data:
        json_entry = json.dumps(entry, ensure_ascii=False, indent=2)
        entry_size = len(json_entry.encode("utf-8"))

        # Om den aktuella filen skulle bli för stor, spara den och börja en ny
        if current_size + entry_size > MAX_FILE_SIZE_BYTES:
            output_file = os.path.join(OUTPUT_DIR, f"{output_prefix}_{file_index}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(current_chunk, f, indent=2, ensure_ascii=False)
            print(f"Skapade {output_file} med {len(current_chunk)} poster")
            
            # Nollställ för nästa fil
            file_index += 1
            current_chunk = []
            current_size = 0

        # Lägg till posten i den aktuella filen
        current_chunk.append(entry)
        current_size += entry_size

    # Spara den sista filen om det finns data kvar
    if current_chunk:
        output_file = os.path.join(OUTPUT_DIR, f"{output_prefix}_{file_index}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(current_chunk, f, indent=2, ensure_ascii=False)
        print(f"Skapade {output_file} med {len(current_chunk)} poster")

def combine_json_files(data_directory="./DATA"):
    combined_entries = []

    # Gå igenom alla undermappar och filer
    for root, dirs, files in os.walk(data_directory):
        for file in files:
            if file.lower().endswith(".json"):
                file_path = os.path.join(root, file)
                data = load_json_file(file_path)
                if data is None:
                    continue  # Hoppa över filer som inte kunde läsas

                # Om filen innehåller en lista med poster, lägg till dem i listan
                if isinstance(data, list):
                    combined_entries.extend(data)
                # Om filen innehåller ett enskilt objekt, lägg till det i listan
                elif isinstance(data, dict):
                    combined_entries.append(data)

    print(f"Totalt antal poster: {len(combined_entries)}")
    split_and_save_json(combined_entries)

if __name__ == "__main__":
    combine_json_files()
