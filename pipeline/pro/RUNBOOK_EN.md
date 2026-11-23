# English A+ from approved Arabic Pro A+ (BJ 2026-11-23: same design, English text only; skip other-brand products)
1. Find gaps: in Seller Central `ListContentMetadata` → ASINs active in `localStorage.hbR` with no en_AE content.
   Pro AR contents (`... Pro AR`) map to `aplus/pro/<fam>-*` images.
2. `python3 pipeline/pro/ocr.py <fam>` → read the Arabic copy → write `pipeline/pro/en_copy/<fam>.json`
   (hero{head[2],sub,chips[3]}, feat{title,sub,feats[4]}, steps{title,steps[3]}, uses{title,sub,tiles[4] in AR order rightmost-first,note}, specs{rows}).
   Facts only from the listing/Arabic copy. English, no Arabic letters.
3. `python3 pipeline/pro/en_overlay.py <fam>` → aplus/pro/<fam>EN-*.jpg ; check /tmp/<fam>EN.jpg ; add 5 alts to aplus/pro/alts.json ; git push.
4. Editor (see pipeline/pro/README.md): new Premium content, language English, `hb3Mods('<fam>EN', 'HABBAA <Name> EN Pro')`,
   `hb3Brand()` + real click (1420,433), `hb3Finish(asins)`; wait for END before navigating away.
5. Content edit pages of submitted drafts freeze the tab — do not open them; close frozen tabs and open a new tab.
