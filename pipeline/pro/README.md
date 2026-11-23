# Pro A+ pipeline (restored 2026-11-23)
- premlib.py: Arabic template. premlib_en.py: English variant (import it instead of premlib).
- English: pass chips reversed, feats as [B,A,D,C], tiles reversed (layout is right-to-left).
- Editor: content language dropdown click (942,397) then (1037,430) = English; load aplus/helpers.js, hb2.js, hb3.js;
  hb3Mods(fam,name) → hb3Brand() + real click on HABBAA option (1420,433) → hb3Finish(asins). Wait for END before navigating.
- Images go to aplus/pro/<fam>-<n>-<mod>-{desktop,mobile}.jpg, alts in aplus/pro/alts.json.
- Scene sources live in Magnific (creations); family configs were lost in the 2026-11-23 workspace reset.
