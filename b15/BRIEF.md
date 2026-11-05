# Brief: Amazon.sa listing content for brand HABBAA (batch 15)

You write English + Arabic listing content for the products of your group. Input: /home/claude/b15/in{N}.json (asin, productType, currentTitle, inventoryTitle, bullets, description scraped from the live amazon.sa page).
Output: a Python module /home/claude/b15/c15_{N}.py in EXACTLY the format of /home/claude/b9/c1.py (read it first: it defines C = {} and put(asin, en_title, ar_title, en_bullets, ar_bullets, en_desc, ar_desc, en_keywords, ar_keywords)). Look at /home/claude/b9/C9.json for 2-3 examples of quality and tone.

Validate: `cd /home/claude/b15 && python3 val.py c15_{N}` must print `issues 0`. Fix and rerun until it does.

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

## Batch 15 specifics
14. Your ASINs: key "N" in /home/claude/b15/groups.json. productType per ASIN in /home/claude/b15/inv.txt (asin|productType|sku).
15. Input: open your own NEW amazon.sa tab (tabs_create_mcp; never touch other tabs). Navigate to https://www.amazon.sa/dp/<first asin>?language=en_AE. Do NOT load any remote script. Write your own short inline JS that fetches each '/dp/ASIN?language=en_AE' (same origin), parses with DOMParser, reads #productTitle, '#feature-bullets li span.a-list-item', #productDescription, and the tech/detail tables (#productDetails_techSpec_section_1 tr, #productDetails_detailBullets_sections1 tr, #productOverview_feature_div tr, #detailBullets_feature_div li); also fetch the ar_AE version of the title when the en title is weak. Store results in window, render into a <pre> and read with get_page_text. ALSO look at each listing's main photo (screenshot an <img> of it) to settle colour/count/shape conflicts: the photo wins over weak text. Write /home/claude/b15/in{N}.json as a list of {asin, productType, scrapedTitle, arTitle, bullets, description, techTable, photoNote}. Close your tab at the end.
16. Many listings have weak, auto-generated or copy-pasted data (wrong product types like AREA_DEODORIZER or LIP_BALM, "Number of Items 20", text from another product). Trust (a) the listing's own title, (b) the photo, (c) bullets that clearly describe this product. Never mention a third-party brand or trademark (e.g. Rubik, Crazy String, Bunch O Balloons).
17. Write BOTH languages fully and correctly.
18. Too little reliable info: write honest general-use bullets, no invented specs.
19. Safety: party snow spray cans are aerosols — no hazard words like explosive/fire; only keep safety advice the listing states (e.g. keep away from eyes/flames, adult supervision) and add "use outdoors or in a ventilated area" only if the listing says so; keep each listing's own pack count from its title (the number in brackets). Swim rings: never say life-saving, life hoop, swimming aid or safe; say water toy for use under constant adult supervision in shallow water. Glass marbles: keep the listing's small-parts warning if present (not for children under 3).
20. Tally/finger counters: tasbeeh/dhikr counting is fine, plus laps, stock, attendance; no religious exaggeration.
21. Incense burner: no fire-safety claims beyond what the listing says; say it is for bakhoor/incense.
22. Keep Arabic in Modern Standard Arabic (avoid colloquial words like اللي، عشان، تبي، وحدة); check gender agreement (e.g. مقصات/قصاصة وردية) and dual forms.
