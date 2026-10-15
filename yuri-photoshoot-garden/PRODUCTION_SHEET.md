# YURI — "The Photoshoot" (rose garden → studio)

Realistic / Netflix-style dialogue ad, copied from a 6:44 reference (720x1280, 121 shots, avg 3.3s per shot).
Final cut: **6:02**, 1080x1920, burned-in captions, single MP4.

## Cast — pulled from the reference video itself

The cast was not generated from scratch. Clean frames were cut straight out of the reference and used as
locked character references on every clip, so the people are photoreal and match the reference exactly.

| Character | Reference frames used |
|---|---|
| Maria, 65, gardener | face (1.55s), garden wardrobe (19.0s), studio champagne dress (366.0s), ID-card portrait (76.3s) |
| James, 57, photographer | garden navy shirt (3.05s), studio grey polo (310.0s) |
| Victoria, mid-50s | before — tired, ivory blouse (48.4s / 50.2s); after — radiant, pink floral (325.0s) |
| Studio assistant | 293.6s |

Product reference: **the client's own tube and brush**, photographed by her and cropped from that photo —
a clean light pink (#E3A8AC) matte body, flat crimped ribbed seal in the same pink, white widely-spaced
YURI / KOREAN BEAUTY / COLLAGEN NIGHT WRAPPING MASK / 75ML · 2.53 FL.OZ., a **narrow** polished gold ring
sitting directly above a clear ribbed flip-top cap, and the flat white silicone brush in its wrapper.

The first pass of this ad used a tube built from a written spec instead, which came out greyish and
dusty-rose. Every clip where the product is handled was regenerated against her photograph: V06 (reveal),
V07 (demo), V08 (ingredients), V09 ("keep it"), V11 (studio) and V14 (closing). The demo is done with the
brush, and the tube is in hand on every beat where the dialogue refers to it.

## Clip plan — Seedance 2.5, 480p, 9:16, native dialogue

Dialogue is spoken by the model inside each clip (no separate TTS track attached), with multi-shot
coverage inside every clip: wide, medium, over-the-shoulder both ways, reaction close-up, detail insert.

| Clip | Scenes | Secs | Lines | Content |
|---|---|---|---|---|
| V01 | 1 | 30 | 13 | hook — James photographs Maria through the roses |
| V02 | 2–4 | 30 | 17 | the card, Victoria approaches, the ID |
| V03 | 4–5 | 30 | 8 | "what did you do?" |
| V04 | 5 | 30 | 7 | "like me?" |
| V05 | 5 | 30 | 4 | tried everything / "then tell me what it is" |
| V06 | 6 | 30 | 17 | tube reveal (PILOT — checked and approved first) |
| V07 | 7 | 30 | 5 | hand demo with the brush: clear gel, sets, peels off as one film |
| V08 | 7 | 30 | 7 | ingredients, sixty days |
| V09 | 8 | 30 | 8 | the phone call, "keep it" |
| V10 | 9 | 22 | 5 | TWO MONTHS LATER, studio |
| V10b | 10–11 | 30 | 10 | Victoria's reveal, the shoot |
| V11 | 11–12 | 24 | 7 | "how much I love photographing you" |
| V14 | 13 | 16 | 2 | closing product + offer (Wan 3.0) |

Inserts overlaid in the edit: a collagen visualisation over the ingredients line (no faces, no tube),
and a clean driver's-licence macro over the ID beat in V02.

## Post

- Hard cuts only, no transitions; a 45 ms audio fade across every join so no cut clicks.
- Grade: gentle contrast and warm lift, soft vignette, fine grain. Not sharpened.
- Music bed under the whole cut, ducked under dialogue by an envelope follower.
- Captions: white bold, black outline, no box, max **three words** per card, timed from ASR
  word alignment so each card sits exactly on its words.
- "TWO MONTHS LATER" title over the studio wide; offer card burned over the closing product scene.
- Two-pass VBR so the whole ad ships as one file under 100 MB.

## Notes worth keeping for the next ad

- Seedance 2.5 **blocked the product-only packshot four times** as NSFW, whatever the wording.
  It passed on Wan 3.0 when framed as a tabletop scene (marble, roses, petals) rather than a packshot.
  Avoid "stands upright", "floating" and product-only framing on Seedance.
- The ID-card photo took three attempts. Passing both the ID crop **and** the present-day face as
  references, and asking for a natural-colour photo, was what finally matched the character.
- Higgsfield's upload host is unreachable from this environment; media is imported by URL from this
  repo instead.
- **Never build the product from a written description.** Ask for the client's own product photo before
  the first clip and carry it as an image reference on every shot that touches the product — a spec in
  words got the colour, the gold ring's width and the cap all slightly wrong, and that cost a full
  round of regenerations late in the job.
- Seedance will quietly re-cast a character mid-clip in a wide shot. Naming the exact wardrobe and
  adding "she is NEVER in a patterned dress / there is no third woman" fixed it on the re-roll.
- Burned-in card text must be measured, not eyeballed: at 1080 wide, DejaVu Sans Bold runs off the
  frame above roughly 48 px for a 32-character line.
