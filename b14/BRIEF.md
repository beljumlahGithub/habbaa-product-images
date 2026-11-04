# Brief: Amazon.sa listing content for brand HABBAA (batch 14)

You write English + Arabic listing content for the products of your group. Input: /home/claude/b14/in{N}.json (asin, productType, currentTitle, inventoryTitle, bullets, description scraped from the live amazon.sa page).
Output: a Python module /home/claude/b14/c14_{N}.py in EXACTLY the format of /home/claude/b9/c1.py (read it first: it defines C = {} and put(asin, en_title, ar_title, en_bullets, ar_bullets, en_desc, ar_desc, en_keywords, ar_keywords)). Look at /home/claude/b9/C9.json for 2-3 examples of quality and tone.

Validate: `cd /home/claude/b14 && python3 val.py c14_{N}` must print `issues 0`. Fix and rerun until it does.

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

## Batch 14 specifics
14. Your ASINs are listed in /home/claude/b14/groups.json under your group number. productType per ASIN is in /home/claude/b14/inv.txt (asin|productType|sku).
15. Input building: open your own NEW amazon.sa tab (tabs_create_mcp, never reuse other tabs), navigate to https://www.amazon.sa/dp/<first asin>?language=en_AE, then javascript_tool: `(0,eval)(await (await fetch('https://raw.githubusercontent.com/beljumlahGithub/habbaa-product-images/main/b12/extract.js')).text()); await X12([...your asins])` (wait ~20 s, it is async; if the call times out, store the promise result in window and poll). Then read the JSON with get_page_text (it renders into <pre id=dd>). Write /home/claude/b14/in{N}.json as a list of {asin, productType, scrapedTitle, bullets, description, techTable}. Close your tab at the end.
16. Many listings have weak, auto-generated or copy-pasted data (e.g. "Number of Items 20" on single items, LED light text on a foil banner, "Area Deodorizer", essential-oil text on unrelated items, competitor or third-party names like "Hiba", "Little Bud", "3M", "FDA", "Halloween", "Hanukkah"). Trust (a) the listing's own key fact in its title, (b) bullets that clearly describe this product. Drop copy-paste and anything from another product. Never mention a third-party brand.
17. Write BOTH languages fully and correctly; whichever matches the listing goes live.
18. If a product truly has too little reliable information for 5 honest bullets, write useful general-use bullets (how to use, where it fits) with no new factual claims, never invent specs.
19. Health/personal-care items (face masks, lice comb, foot files, cuticle nippers, cotton swabs, sleep mask, stress ball): no medical, pain-relief, protection-level, antibacterial or "prevents disease" claims. A cloth face mask is a "fabric face cover"; do not claim it filters viruses or dust unless the title says dust and even then say "everyday use". Cotton swabs: do not tell to insert into the ear canal. Lice comb: you may say it helps comb out lice and nits from hair (that is its function), no treatment claims.
20. Children items (swim ring): keep the listing's age range and supervision warning; never say it is a life-saving or swimming aid.
21. Paper cups: the 5 cup ASINs share a family; keep each ASIN's own size (oz/ml) and pack count exactly as in its own live title; if the title count conflicts with other fields, use the title.
22. Religious item (Al Ghaffar stand): respectful wording, Arabic name spelled الغفار.
