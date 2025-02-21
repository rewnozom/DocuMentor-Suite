
### Sammanfattning av "analysera"-modulen

- **MarkdownAnalyzer**  
  - **Syfte:** Analysera markdown‑filer för att extrahera och gruppera innehållet i logiskt avgränsade sektioner.
  - **Funktioner:**  
    - Läser in en markdown‑fil och använder en ContentAnalyzer för att dela upp texten.
    - Identifierar sektionstyper (t.ex. produktinformation, kompatibilitet, tekniska data) och beräknar en konfidens för varje sektion.
    - Skriver ut en detaljerad översikt över identifierade sektioner (typ, radintervall, konfidens, innehåll).
  
- **Main‑funktionen**  
  - Startar analysen på en given fil (här "example.md") och skriver ut resultaten, vilket gör att du enkelt kan testa och verifiera analysen.



----------------------

### Sammanfattande beskrivning

- **DirectoryMarkdownAnalyzer**  
  - **Syfte:** Att skanna igenom en vald katalog (och dess undermappar) med markdown‑filer och analysera varje fil med hjälp av din ContentAnalyzer.
  - **Funktioner:**  
    - **analyze_directory:** Hämtar alla markdown‑filer i den angivna katalogen och analyserar dem.
    - **print_analysis:** Skriver ut en detaljerad översikt av varje fil med information om sektionernas typ, radnummer, konfidensnivå samt det faktiska innehållet.
  
