# Yuri – "59 vows" ad (FINAL edit, full quality, not re-compressed)

Two finished versions of the same edit, 480×854 (9:16), 24 fps, 4:51.9 (291.875 s), H.264 CRF 17 (~3.8 Mbps) + AAC 320k, mastered to about -15 LUFS integrated, true peak -1.5 dB.

| Version | What it is |
|---|---|
| `YURI_59vows_FINAL_captioned` | Hook text + burned-in captions + stickers + animated CTA end card |
| `YURI_59vows_FINAL_clean` | Same edit with **no captions and no hook text** (stickers and CTA end card are kept) |

GitHub doesn't allow a single file over 100 MB, so each MP4 is packed (no compression, byte-for-byte identical, checked with `cmp`) into a 2-part 7z archive:

```
YURI_59vows_FINAL_captioned.7z.001   (95 MB)
YURI_59vows_FINAL_captioned.7z.002   (49 MB)
YURI_59vows_FINAL_clean.7z.001       (95 MB)
YURI_59vows_FINAL_clean.7z.002       (52 MB)
```

## How to get the MP4

1. Download both parts of the version you want into the same folder.
2. Open/extract **only `.7z.001`**. The `.002` is read automatically.
   - Android: ZArchiver
   - Windows: 7-Zip or WinRAR
   - Mac: Keka or The Unarchiver
3. The full-size MP4 comes out as one file (captioned 151,038,500 bytes, clean 154,278,773 bytes).

## Other files (normal downloads, no extraction needed)

| File | What it is |
|---|---|
| `YURI_59vows_FINAL.srt` | Captions, timed to the audio, exact script spelling |
| `YURI_59vows_chunks.zip` | All 29 original Seedance 2.5 clips (480×854) plus `CHUNKS.txt` |
| `YURI_59vows_audio_stems.zip` | Separate stems (dialogue, music, SFX, ambience) so levels can be re-balanced |

## Notes

- Dialogue, lip-sync and voices come only from Seedance 2.5. Music, SFX and ambience were synthesized for this edit (no Higgsfield music or SFX model exists).
- Music and SFX levels were set by measurement (music about 20 dB under speech), not by ear. The stems zip is there in case anything needs adjusting.
- Source clips are native 480p, so the finished video is 480×854. Nothing was upscaled or re-compressed after the final render.
