![](_page_0_Picture_0.jpeg)

# **IO-5022 Gen2 anslutningar**

## **Enhetsadress: Datum:**

| P2 OPTION (extern strömförsörjning)    |   |       |                                     |                             |                               |                     |                        |
|----------------------------------------|---|-------|-------------------------------------|-----------------------------|-------------------------------|---------------------|------------------------|
| DC+ a                                  |   | 5     |                                     |                             |                               |                     |                        |
| DC- b                                  |   | 6     |                                     |                             |                               |                     |                        |
| P3 OUTPUT (sabotageavkänning / tamper) |   |       |                                     |                             |                               |                     |                        |
| SAB (NC)                               |   | 7     |                                     |                             |                               |                     |                        |
|                                        |   | 8     |                                     |                             |                               |                     |                        |
| P18 Ingångar                           |   |       | Givartyp                            | Obalanserad /<br>dubbelbal. | Aktivt hög (NO)<br>/ låg (NC) | Larm<br>adress      | Benämning,<br>notering |
| I/O PORT1                              | b | 9     |                                     | /                           | /                             |                     |                        |
|                                        | a | 10    |                                     |                             |                               |                     |                        |
| I/O PORT2                              | b | 11    |                                     |                             |                               |                     |                        |
|                                        | a | 12    |                                     | /                           | /                             |                     |                        |
| P19 Utgångar                           |   |       | Givartyp                            | Aktivt hög (NO) / låg (NC)  |                               | Benämning, notering |                        |
| I/O PORT3                              | b | 13    |                                     |                             |                               |                     |                        |
|                                        | a | 14    |                                     | /                           |                               |                     |                        |
| I/O PORT4                              | b | 15    |                                     |                             |                               |                     |                        |
|                                        | a | 16    |                                     | /                           |                               |                     |                        |
| P5 LOCAL BUS                           |   | Stift | UC, spänningskälla, ev. larmcentral |                             |                               |                     |                        |
| DC+                                    | a | 25    |                                     |                             |                               |                     |                        |
| DC-                                    | b | 26    |                                     |                             |                               |                     |                        |
| RS485                                  | A | 27    |                                     |                             |                               |                     |                        |
| RS485                                  | B | 28    |                                     |                             |                               |                     |                        |
| Enhetens placering / anteckningar      |   |       |                                     |                             |                               |                     |                        |
|                                        |   |       |                                     |                             |                               |                     |                        |

# **Ingångar kan ställas till olika funktioner**

Egenskaper som programmeras i R-CARD M5 – anges med fördel i tabellen:

- Aktivt hög (NO, standardinställning) eller aktivt låg (NC).
- Obalanserad ingång (standardinställning) eller dubbelbalanserad.

# **Utgångar kan ställas till olika funktioner**

Utgångarna kan vara potentialfria eller matande. Detta ställs med hjälp av byglingsgrupperna P12 – P13. I R-CARD M5 väljer du aktivt hög (NO) eller aktivt låg (NC) – anges med fördel i tabellen.

Rekommendation vid val av lokal eller extern matning (P6): När matande utgång önskas, välj extern matning och bygla matning på P5/25 till P2/5 och P5/26 till P2/6 för att få separata säkringar för utgångarna i förhållande till elektroniken.