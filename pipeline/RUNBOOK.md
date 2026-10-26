# HABBAA daily A+ runbook (Amazon.sa)

Goal: every day, add Premium A+ content to ~50 **active HABBAA-brand ASINs that have no A+ yet**.
Owner: BJ (hello@beljumlah.sa). Standing instruction: do not ask him anything — decide, execute, report briefly in Arabic at the end.

## Hard rules
- Only ASINs that appear in NO A+ content (any status, incl. drafts). Another account user (A2CUUBNFI4LBA4, "… Premium AR" names) runs A+ in parallel — never touch their content; re-check coverage right before attaching ASINs.
- Only HABBAA-brand titles (A+ requires brand ownership).
- Saudi Arabic, natural and error-free. No claims that are not in the listing (bullets/title). Skip sizes when the listing contradicts itself.
- Amazon keyword filter blocks these substrings, also ACROSS word boundaries (check with spaces removed): `مص`, `كس`, `لعن`, `بز`, `ثدي`, `علق`, `هور`, `جن`, `نيك`, `لسبو`, `فوهة` (strip tashkeel too). Amazon ALSO reads the text inside the images, so image copy must pass the same filter. Examples that fail: لاتكس (use مطاط)، مانيكير (use أدوات أظافر)، السبورة (use اللوح الأبيض)، فوهة (use فتحة)، حجم صغير، للعناية/العناية، مصمم، مصاصة، مصنوع، الكسر، العنابي، بزوايا، "توصلك سليمة". `day1.py` aborts if any line contains them.
- AI scenes must keep the product identical to the source photo. Reject any scene with misspelled/gibberish Latin text on products (letter balloons!), wrong material/colour, or extra products. Never use competitor images that carry another brand's text as a design base.
- Content names end with `AR v2` (marks this pipeline's work).

## Template (Premium, 3 × "صورة كاملة لنظام Premium")
1. hero — lifestyle photo, product LEFT, text RIGHT (brand, 2-line headline, 2-line benefit, gold rule)
2. uses — 4 rounded tiles + labels (first tile = rightmost)
3. features — product cut-out (or framed photo for white products: `photo=True`) + 4 feature bullets
Desktop 1464×600, mobile 600×450, Arabic alt text on each.

## Daily steps
1. **Coverage**: in Seller Central tab: `fetch('/aplus/api/ListContentMetadata?filteredContentTypes=')` → items[].asins → covered set.
2. **Active list**: `/myinventory/inventory?…&pageSize=100&status=active&page=1..10`; scrape rows with regex `\n(title)\nASIN\n(B0…)\nرقم تخزين السلعة\n(sku)` while scrolling (45×650px); accumulate in localStorage.
3. Uncovered ∩ HABBAA → group by first 3 title words → take the biggest families until ≥50 ASINs. Skip families listed in `state/done.json`.
4. Per family, open one representative `https://www.amazon.sa/dp/ASIN?language=ar_AE`: title, bullets, image ids (`#altImages img` → `images/I/<id>`).
5. Import images to Magnific with `creations_upload_image` (`https://m.media-amazon.com/images/I/<id>._SL1500_.jpg`), download via the returned pikaso URL (shell can't reach m.media-amazon.com, but pikaso works).
6. Generate with `images_generate` mode `imagen-nano-banana-2`, product photo as `references` image: 1 hero 21:9 (product in left 40%, empty right half, "no text") ×2 + 4 square use scenes. Review every image (contact sheet) and regenerate rejects.
7. Write a `dayN.py` like `day1.py` (FAM config: hero/uses/feat/alt) → `python3 dayN.py` → review sheets → push finals to `aplus/dN-<fam>-<n>-<mod>-{desktop,mobile}.jpg`.
8. Editor (Claude in Chrome): `…/workflow/ebc-premium/content/new/edit` → load `aplus/helpers.js` (see below) → `hbType(hbF().name, '<Name> AR v2')` → for each module: `await hbAddModule('صورة كاملة','صورة كاملة لنظام Premium')` returns [x,y] → REAL left_click at [x,y] → `hbImg(placeholder,'dN-fam-1-hero',alt)` (placeholder = leaf element with text `الضغط لإضافة صورة`).
9. Re-check coverage, `hbClickText('التالي: تطبيق أرقام ASIN')` → `hbAsins(list)` (bulk CSV — it REPLACES the list) → expect `عدد ASIN المطبق عليها (n)` and 0 `خطأ (`.
10. `hbClickText('التالي: مراجعة وإرسال')` → find "إرسال للموافقة" (top) → real click → confirm dialog button at ~(540,424).
11. Verify with ListContentMetadata (status approved/submitted), append families + ASINs to `state/done.json`, push.
12. Report to BJ in Arabic: families, ASIN count, anything blocked.

Load helpers in page:
```js
const code=await (await fetch('https://raw.githubusercontent.com/beljumlahGithub/habbaa-product-images/main/aplus/helpers.js?'+Date.now())).text(); (0,eval)(code);
```

## Editor shortcuts (day 2+)
- Load `aplus/helpers.js` then `aplus/hb2.js`; per content: `hb2Start(name)` → real-click coords → `hb2Step('dN',fam,1..3)` (each returns next coords) → `hb2Asins(list)` → `hb2Review()` → use `find` for the top "إرسال للموافقة" ref and then the modal's confirm ref (coordinates shift with viewport).
- Alt texts come from `aplus/dN-alts.json`.
- If validation fails ("فشل التحقق"), click "إصلاح المحتوى", read `hbErrors()`; fix copy, rebuild, push images as `-v2`, then in the module click "تعديل", click both small `x` in the dialog, drop new files (see hbReplace pattern in git history), click "إضافة".
- Skip Saudi National Day / emblem / flag families (garbled emblem/shahada risk).

## Batch-3 lessons
- Category-level contents work: group small families by category (e.g. kitchen gadgets, storage) — one content per category, tiles show different products.
- Before using a product, look at its listing photo: skip items whose product/packaging shows another brand (Staedtler, IKEA names, Safari, Xiaomili, Star Decor...). HABBAA A+ must not sit on another brand's product.
- AI scenes: check for car badges / laptop logos; pick the hero variant without them.
- After every submit, verify the green banner "تم إرسال المحتوى ... بنجاح" (or English "successfully submitted"); a missed confirm click leaves a silent draft. Re-check ListContentMetadata ~1 min later: status goes draft → approved.
- If Seller Central switches to English (new tab group), add `?mons_sel_locale=ar_AE` to the editor URL so the Arabic helpers work.
- Replace images in a draft: module "تعديل/Edit" → both small x → `hbRep(name)` drag-drop (see aplus/hb2 usage in session) → retype alt with real triple-click + ctrl+a + type (alt fields are shadow inputs) → "إضافة/Add".
- `photo='pad'` in features() pads white-background product photos instead of cropping.

## Gotchas
- Amazon.com shows a bot-check interstitial — do not bypass it; derive style from known US premium-brand patterns.
- JS calls time out at 45 s; keep each call short. Don't trigger native dialogs (leaving the editor mid-edit can).
- Fonts: `pipeline/fonts/Tajawal-*.ttf` (set `HB_FONTS`). PIL must have raqm (`features.check('raqm')`).
