# YURI Collagen Night Wrapping Mask — Poolside (Santorini)

Vertical ad built from the 4:13 Santorini poolside reference, on the supplied script.

| | |
|---|---|
| Runtime | 4:45 |
| Format | 1080 × 1920, 30 fps, H.264 |
| Loudness | −15.0 LUFS, −2 dBTP |
| Scenes | 8 (16 generated clips + a peel insert + a closing product section) |

## Files

| File | What it is |
|---|---|
| `Yuri_Poolside_Ad_CAPTIONS.mp4` | Burnt-in captions — the version to run |
| `Yuri_Poolside_Ad_CLEAN.mp4` | Same cut, no captions |

Both are single files, downloadable directly.

## How it was made

- **Dialogue** — Seedance 2.5, 480p, omni_reference, with Seedance's own voices
  throughout. Cast, set and wardrobe are locked to fixed reference images so the
  two women and the Santorini pool stay identical across every clip.
- **Peel insert** — a morning-bathroom cutaway, cut over the line "gently peel
  away the clear film in the morning" while the poolside audio continues.
- **Closing product section (last 38 s)** — composited in code from the real
  product photograph rather than generated, so the tube's flat crimped seal is
  correct. Every text reveal is pinned to a word time measured off the finished
  voiceover. That section's voiceover is TTS; every other voice in the ad is
  Seedance's own.

## Edit notes

- Eight unscripted vocalisations the model added between lines are silenced; the
  picture runs on, so no cut was introduced.
- Dead air is shortened only where a shot change already falls inside it, except
  the walk-away pause before "Damn." and the closing section, which are left
  whole on purpose.
- Captions are read back off the final audio segment by segment, so they cannot
  drift from the picture.

## Known limitation

The cast wear poolside cover-ups rather than swimwear: swimwear cast reference
images are refused by the generator's moderation, which blocks the clip before
any prompt wording matters.
