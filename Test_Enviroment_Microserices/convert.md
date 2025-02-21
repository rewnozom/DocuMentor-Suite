### Sammanfattning:

1. **convert_json_to_parquet.py**  
   - **Syfte:** Letar upp alla JSON‑filer i en angiven indata‑katalog (styrd av YAML‑filen), konverterar varje fil till en Parquet‑fil i en separat utdata‑katalog, och validerar konverteringen genom att jämföra dataframe‑dimensioner.  
   - **Terminalutskrifter:** Använder symboler (t.ex. 🚨, 📄, ✅, ✔️, ❌) för tydlig statusrapportering.

2. **convert_parquet_to_json.py**  
   - **Syfte:** Letar upp alla Parquet‑filer i en angiven indata‑katalog, konverterar varje fil till JSON i en separat utdata‑katalog, och validerar konverteringen på samma sätt som JSON‑till‑Parquet-scriptet.  
   - **Terminalutskrifter:** Visar information om läsning, konvertering och validering med symboler.

3. **file_checker.py**  
   - **Syfte:** Kontrollerar giltigheten av filer (både JSON och Parquet) i angivna kataloger. För JSON räknas antalet tokens i fältet "ai_output" med hjälp av en transformer‑tokenizer, och för Parquet läses dataframe‑dimensioner. Resultatet skrivs ut strukturerat med tydliga symboler.  
   - **Utdata:** Skriver en sammanfattande rapport (en loggfil sparad i den inmatade katalogen) samt terminalutskrifter.

Alla tre script använder YAML‑konfiguration för att enkelt kunna justera indata-/utdatakataloger, token‑gränser, modellnamn med mera.

