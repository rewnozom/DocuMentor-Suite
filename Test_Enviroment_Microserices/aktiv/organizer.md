
### Sammanfattande beskrivning av "organisera"-modulen

- **EnhancedCompatibilityOrganizer**  
  - **Syfte:** Att skanna igenom en angiven källkatalog med markdown‑filer, extrahera kompatibilitetsrelationer och organisera dokumenten i grupper baserade på gemensam produktinformation.
  - **Huvudfunktioner:**  
    - **_process_documents:** Läser in varje fil och extraherar kompatibilitetsrelationer via extractor‑modulen.
    - **_organize_files:** Bygger en mapping mellan produktreferenser (artikelnummer och namn) och filer, samt grupperar filerna baserat på dessa relationer.
    - **_create_group_directory & _create_group_readme:** Skapar en ny mapp för varje grupp och kopierar filerna dit, samt genererar en README‑fil med en översikt över relationerna.
    - **_log_results:** Loggar en sammanfattning över organiseringsprocessen (antal filer, saknade filer etc.).
    
- **main-funktionen**  
  - Startar organisatören med angivna käll- och målmappar.
