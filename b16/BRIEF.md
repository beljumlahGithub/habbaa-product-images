# Brief: Amazon.sa listing content for brand HABBAA (batch 16)

You write English + Arabic listing content for the products of your group. Input: /home/claude/b16/in{N}.json (asin, productType, inventoryTitle, bullets, description, techTable, photoNote, note).
Output: a Python module /home/claude/b16/c16_{N}.py in EXACTLY the format of /home/claude/b9/c1.py (read it first: it defines C = {} and put(asin, en_title, ar_title, en_bullets, ar_bullets, en_desc, ar_desc, en_keywords, ar_keywords)). Look at /home/claude/b9/C9.json for 2-3 examples of quality and tone.

Validate: `cd /home/claude/b16 && python3 val.py c16_{N}` must print `issues 0`. Fix and rerun until it does.

Hard rules (the owner reviews strictly, no errors allowed):
1. FACTS ONLY from the input (titles, bullets, description). Never invent dimensions, weights, capacities, counts, materials, colours, certifications, warranty, safety claims, age grades. If a size/count appears in the inventory title or bullets, keep it exactly. If facts conflict, use the inventoryTitle. If something is unknown, leave it out.
2. Title 60-200 chars, starts with "HABBAA", no word more than 2 times, includes main keyword + key spec (size/count/colour) + main uses. Arabic title also starts with "HABBAA".
3. Exactly 5 bullets per language, each 40-480 chars, style "Short Benefit Label: sentence". Last bullet often = what is in the pack / how to use (only if known).
4. Description: EN 700-2000 chars, AR 500-2000 chars, plain text, no HTML, no "<" ">".
5. Keywords (search terms) each language <= 249 BYTES (Arabic letters are 2 bytes each). No brand names, no ASINs, no repeating title words where possible; include synonyms and Saudi/Gulf colloquial Arabic search words (e.g. بالون، بلالين، شموع عيد، كاسات ورق، مظلة/شمسية).
6. No emoji, no promo words (best, free, sale, discount, eco-friendly, biodegradable, guarantee, warranty, premium quality, certified, approved, 100%, #1, cure, treat; Arabic: ضمان، الأفضل، مجاني، خصم، معتمد، شهادة، 100%، رقم 1). No competitor or third-party brand names.
7. Arabic must be natural Modern Standard Arabic that reads well for Saudi customers (not machine translation). Use Arabic comma "،". Numbers can stay as digits with units (سم، مل، جرام).
8. Do not change prices or mention prices. Avoid medical claims.
9. Avoid in Arabic text the words: عيد الميلاد، ميلاد، شفرات (use "حفلة"، "مناسبة"، "شمعة رقم للكيك" etc. instead; for razors use "موس"/"حافة").
10. Each product must be distinct; variants of the same family (e.g. balloons of different colours/counts, number candles 0-9) must each carry their own colour/number/count correctly.

When done, report: number of products, `val.py` result, and any product where input data looked contradictory or wrong (asin + reason). Do not touch any other files.
11. If an input row has a "note" field, follow it.
12. Products in the input that belong to the same family (e.g. Waraq playing cards 1/2/3 packs, Allah-name calligraphy stands, zip lock bag sizes, finger tally counter pack sizes, putty knives, spray bottles) must stay accurate to each listing's own pack count / size / colour from its inventoryTitle.
13. Religious items (Allah names calligraphy): respectful wording, no jokes, no "decoration only" that sounds dismissive; Arabic name spelled correctly (الرزاق، الفتاح، الرحمن، الغفار).

## Batch 16 specifics
14. Your input is ready in /home/claude/b16/in{N}.json. Do NOT browse; do not open any browser tab. Write /home/claude/b16/c16_{N}.py and run `cd /home/claude/b16 && python3 val.py c16_{N}` until `issues 0` (val prints nothing when clean - then report issues 0).
15. photoNote describes what the product photos really show (checked by the owner's team). The photo wins over weak or copy-pasted text. The "note" field is mandatory guidance per product.
16. Many listings have weak, auto-generated or copy-pasted data (wrong product types, "Number of Items 20", odd machine-translated bullets like "Grits", "Beads"). Trust (a) the inventoryTitle, (b) photoNote/note, (c) bullets that clearly describe this product. Never mention a third-party brand or trademark.
17. Write BOTH languages fully and correctly.
18. Too little reliable info: write honest general-use bullets, no invented specs.
19. Safety and health: no medical claims for braces, massagers, moth balls; no safety guarantees. Sky lanterns: do not add hazard or eco claims; neutral wording about occasions; you may say "follow local regulations and use in open outdoor spaces" ONLY as a usage tip in the last bullet (no fear words).
20. Tally counters: tasbeeh/dhikr counting is fine, plus laps, stock, attendance.
21. Religious calligraphy (Allah names): respectful, correct spelling الودود، الرحمن، السلام، الوكيل.
22. Keep Arabic in Modern Standard Arabic (avoid colloquial words like اللي، عشان، تبي، وحدة); check gender agreement and dual forms.
23. Amazon's Arabic keyword filter blocks these substrings anywhere in Arabic text, even inside longer words and across word boundaries (check with spaces removed): مص، كس، لعن، بز، ثدي، علق، هور، جن، نيك، لسبو، فوهة. Examples to avoid: مصنوع (use من خامة / من مادة)، مصمم (use بتصميم)، العناية/للعناية (use لنظافة/للاهتمام)، إكسسوارات، مانيكير، للتعليق (use للتثبيت)، جنب. val.py checks this.