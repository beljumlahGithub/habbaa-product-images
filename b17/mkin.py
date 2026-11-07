import json
d=json.load(open('scr.json'))
inv=[l.split('|',3) for l in open('inv.txt').read().splitlines()]
BAG="Photos (shared by all colour listings): a fan of medium kraft-paper gift bags in many colours with twisted paper handles, and one brown bag shown next to a pen for scale. No print or logo on the bags."
BAGN="12 medium paper bags with twisted paper handles. Size from the listing: about 33 cm length (height) x 26 cm width x 12 cm base width. Colour = the colour in inventoryTitle ({c}) - all 12 bags in that colour. Do NOT write eco-friendly/recyclable. Uses: gifts, shopping, party favours, store packaging, Eid and wedding giveaways. Ignore product type (LIP_BALM is wrong)."
CAN="Photo: one blister card printed 'Happy Birthday' with cartoon decorations, holding one {c} glitter-dotted number candle '{n}' and one thin striped spiral candle of the same colour."
CANN="1 number candle, number {n}, colour {c}, plus one thin spiral candle (visible in photo). Paraffin wax (from listing). Do NOT write a size or weight (listing weight 4 kg is wrong). Arabic: avoid عيد الميلاد/ميلاد; use شمعة رقم {n} للكيك/للتورتة، حفلات، مناسبات. Add usage tip: never leave a lit candle unattended (neutral)."
SC="Sugarcane pulp (bagasse) food packaging, beige. Do NOT write eco-friendly, biodegradable, compostable, 100% safe, healthy-claims. Neutral: 'made of sugarcane pulp', 'for serving and takeaway'. Listing weight/package size data (5 kg, 10x10x8) is wrong - ignore. Do not claim microwave/oven/leak-proof."
PL="Disposable/reusable plastic food packaging. Ignore wrong table data (4 kg weights, 3x1x0.5 cm package, colour White on black items). Do not claim BPA-free, leak-proof, airtight-guaranteed, microwave-safe or food-grade certification unless noted. Uses: takeaway, restaurants, home kitchens, parties, storage in the fridge."
P={
'B0F7XRG42Z':("Round sugarcane bowl with a clear domed plastic lid.","32 oz round bowl with clear lid, 50 pieces ('50 Grains' in title means 50 pieces)."),
'B0F7XQY9CV':("Square sugarcane bowl with a clear lid.","Square container 16 oz with clear lid, 50 pieces."),
'B0F7XRDJWM':("Square sugarcane bowl, clear plastic lid on top.","Square container 24 oz with clear lid, 50 pieces."),
'B0F7XSMVWT':("Small round sugarcane sauce cups with separate clear lids.","Sauce cup 2 oz with clear lid, 100 pieces."),
'B0F7XRJKJX':("Small round sugarcane sauce cups, one photo with a dipping sauce, clear lid.","Sauce cup 4 oz with clear lid, 100 pieces."),
'B0F7XRX3XM':("Large round sugarcane bowl with clear domed lid; a phone shown for scale.","Round bowl 40 oz with clear lid, 10 pieces (title says 10 Count; ignore table 100)."),
'B0F7XMRGQY':("Rectangular sugarcane tray with 5 compartments (one round centre). Lid not shown in photo.","Meal container with 5 compartments, 50 pieces. Title says it comes with a plastic lid - mention lid once, neutrally."),
'B0F7XMRT1L':("Rectangular sugarcane clamshell box with attached (hinged) lid.","Rectangular box with attached lid, 600 ml, 50 pieces."),
'B0F7XMP7L7':("Square sugarcane clamshell burger box; one photo with a burger inside.","Burger box, 50 pieces (title; ignore table 25)."),
'B0F7XJLNG1':("Oval sugarcane trays/plates, stacked; phone shown for scale.","Oval tray, LARGE size, beige, 10 pieces. Ignore table colour Pink."),
'B0F7XGGW86':("Oval sugarcane trays/plates, stacked; phone shown for scale.","Oval tray, MEDIUM size, beige, 10 pieces. Ignore table colour Pink."),
'B0F7XGZ1MH':("Oval sugarcane trays/plates, stacked; phone shown for scale.","Oval tray, SMALL size, beige, 10 pieces. Ignore table colour Pink."),
'B0F7RH51KF':("Brown kraft single-wall paper cups, a tall stack and three sizes shown.","Kraft paper cups, brown, 8 oz, 50 cups. For hot drinks (coffee, tea). No lid mentioned - do not claim a lid. Do not write eco claims."),
'B0F7RGJTCD':("Brown kraft single-wall paper cups, a tall stack and three sizes shown.","Kraft paper cups, brown, 12 oz, 50 cups. For hot drinks. No lid. No eco claims."),
'B0F7R9YM6F':("Black double-wall paper cup with black plastic lid; photo of 5 black sip lids.","Black double-wall paper cups WITH lids, 50 cups. Size not stated - do not invent oz. Hot and cold drinks. No eco claims."),
'B0F7R6ZLL8':("Brown kraft double-wall paper cups in three sizes, no lid shown.","Double-wall brown paper cups, 25 cups. Size not stated - do not invent. Lid unclear - do NOT mention a lid."),
'B0F7R672W9':("White double-wall paper cups; one photo with a stack.","Double-wall white paper cups, 25 cups. Size not stated. No lid."),
'B0F7RS79SZ':("Moulded brown cardboard/pulp cup carrier with 4 cup slots; a hand holding it.","Cup carrier for 4 cups, 50 pieces, for hot and cold drinks, takeaway and delivery. No eco/biodegradable claims."),
'B0F7RV7N2Q':("Moulded brown pulp cup carrier with 2 cup slots.","Cup carrier for 2 cups, 50 pieces."),
'B0F7RQ4DXP':("Brown kraft deli/sandwich wrap sheets: lifestyle photos with fries, fried chicken, sandwiches and hot dogs on the paper; a stack of sheets; text 'pack of 500 classic brown deli paper' on one photo.","Kraft waxed sandwich/deli wrap paper sheets, brown. Pack count conflicts (table 100, photo text 500) - do NOT state a count. Listing bullets wrongly describe air-fryer paper - IGNORE air fryer and heat claims. Uses: wrapping sandwiches, burgers, shawarma, fries, lining baskets/trays, grease-resistant for oily food (photos say grease proof)."),
'B0F7RQ5W3B':("Black waxed wrap sheets: one side black, the other gold/kraft tone.","Black waxed sandwich wrap paper sheets. Count not reliable - do NOT state a count. Uses: wrapping sandwiches, burgers, serving baskets, presentation."),
'B0F7M23229':("Small round clear plastic container with attached hinged lid.","Clear round plastic container with attached lid, 50 pieces (table). Uses: salads, sides, desserts, sauces, takeaway."),
'B0F7M15CRP':("Round clear plastic bowl with domed clear hard lid.","Clear dessert container with hard lid, 50 pieces. Uses: desserts, salads, appetizers, sweets."),
'B0F7M1Y6BJ':("Small round clear sauce cup with attached flip lid.","Round clear sauce container with attached lid, 50 pieces."),
'B0F7M199LJ':("Round clear plastic container with lid, ribbed rim; also a small cup with flip lid.","Round clear plastic sauce containers with lid, 50 pieces (table). Do not claim leak-proof."),
'B0F7M17DP8':("Rectangular clear plastic box with attached hinged lid, ribbed.","Clear rectangular plastic cake box with attached lid, 50 pieces (table). Uses: cake slices, pastries, sweets, sandwiches."),
'B0F7M195LC':("Round black plastic base with clear ribbed lid.","Round plastic food container, black base with clear lid, ribbed, 50 pieces (table). The description wrongly says rectangular - it is ROUND."),
'B0F7M3R65V':("Rectangular black plastic base with clear lid.","Rectangular plastic food container, black base with clear lid, 50 pieces (table)."),
'B0F7LZBP8T':("Black plastic meal container with 2 compartments and clear lid.","Black plastic meal container with compartments (photo: 2) and clear lid, 50 pieces. Title says microwave - you may write 'for heating in the microwave as per the title' only as 'microwave meal container' wording, no temperature claims. Colour black (table White is wrong)."),
'B0F7M2HZ4Z':("Round black plastic container with clear lid, also a stack of three.","Round plastic food container, black base with transparent lid, medium size, 50 pieces. Uses: takeaway, hot and cold meals."),
'B0F7M2MNGP':("Rectangular clear plastic container with clear lid.","Rectangular clear plastic container with lid, medium size, for food and household items. Count unknown - do not state."),
}
CN={'Blue':'blue','Pink':'pink'}
rows=[]
for a,sku,pt,t in inv:
    v=d[a]
    r=dict(asin=a,productType=pt,inventoryTitle=t,bullets=v['bl'],description=v['de'],techTable=v['tb'])
    if 'Paper Bags' in t:
        c='Multicolor (assorted colours)' if 'Multicolor' in t else t.split('|')[-1].strip()
        if c=='OUDI': c='Oudi (keep the colour name Oudi / عودي as is; do not describe the shade)'
        r['photoNote']=BAG; r['note']=BAGN.format(c=c)
    elif t.startswith('Candle'):
        c='blue' if 'Blue' in t else 'pink'
        n=t.strip()[-1] if t.strip()[-1].isdigit() else '0'
        r['photoNote']=CAN.format(c=c,n=n); r['note']=CANN.format(c=c,n=n)
    else:
        pn,no=P[a]; r['photoNote']=pn
        r['note']=no+' '+(SC if 'B0F7X' in a else PL if a.startswith('B0F7M') or a=='B0F7LZBP8T' else 'Food/drink service packaging. Ignore wrong table data (weights like 0.09 g, capacity in grams). No eco/biodegradable claims.')
    rows.append(r)
G={1:rows[0:11]+rows[11:13],2:rows[13:19]+rows[19:25],3:rows[25:31]+rows[31:38],4:rows[38:50]}
for k,v in G.items(): json.dump(v,open(f'in{k}.json','w'),ensure_ascii=False,indent=1); print(k,len(v))
