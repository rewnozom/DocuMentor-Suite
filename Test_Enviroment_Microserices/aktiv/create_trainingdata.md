
# create_trainingdata.py – Träningsdatagenerator

Denna modul skannar igenom en angiven källkatalog med markdown-filer, 
extraherar kompatibilitetsrelationer med hjälp av CompatibilityExtractor och 
en EnhancedCompatibilityFormatter, och genererar ett träningsdataset för AI-modellering.

Utdata sparas i flera format (JSON, CSV, Parquet) samt en översikt (command overview)
och metadata om processen. Alla inställningar styrs via en YAML-konfigurationsfil.


### YAML Konfigurationsfil (trainingdata_config.yaml)

> spara följande innehåll i en YAML‑fil: `trainingdata_config.yaml` i samma mapp som modulen:

```yaml
source_directory: "./converted_docs"
output_directory: "./Compatibility_Trainingdata"
output_formats:
  - json
  - csv
  - parquet
json_filename: "compatibility_training.json"
csv_filename: "compatibility_training.csv"
parquet_filename: "compatibility_training.parquet"
command_overview_filename: "command_overview.md"
metadata_filename: "generation_metadata.json"
log_level: "INFO"
```

---

### Sammanfattande Beskrivning av "Skapa träningsdata"-modulen

- **Syfte:**  
  Denna modul ansvarar för att skapa ett strukturerat träningsdataset för AI‑modeller genom att:
  - Skanna igenom en angiven katalog med markdown‑filer.
  - Extrahera kompatibilitetsrelationer med hjälp av en extractor.
  - Generera flera träningsdataexempel (TrainingExample‑objekt) via en utökad formatter.
  - Spara utdata i flera format (JSON, CSV, Parquet) och skapa en översikt (command overview) samt metadata.
  
- **Konfiguration:**  
  Alla viktiga inställningar (såsom käll- och målmappar, utdataformat, filnamn och loggnivå) styrs via en YAML‑fil (trainingdata_config.yaml) så att du enkelt kan ändra beteendet utan att röra i koden.

- **Huvudklasser och Metoder:**  
  - **CompatibilityTrainingGenerator:**  
    - `generate_training_data`: Huvudmetoden som processar filer, extraherar relationer, genererar träningsdata och sparar utdata.
    - `_process_file`: Läser varje fil, extraherar kompatibilitetsrelationer, genererar träningsdataexempel och samlar metadata.
    - `_save_training_data`, `_generate_command_overview`, `_save_metadata`, `_log_summary`: Metoder för att spara utdata och logga en sammanfattning.

