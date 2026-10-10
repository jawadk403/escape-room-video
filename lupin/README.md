# Lupin – "The Gentleman Thief" × Yuri (FINAL master, full size)

Final edit: **4:46.9 (286.9 s), 720×1280 (9:16), 24 fps, H.264 High (CRF 18, bt709) + AAC 320 kbps, −16 LUFS integrated, true peak −1.7 dBFS.**
Two versions, both original full-size files (7z "store" mode = no compression, no quality loss):

| Version | File inside the archive | Size | Parts |
|---|---|---|---|
| **Captioned** (burned-in captions, hook title, chapter labels, end card) | `Lupin_FINAL_captioned.mp4` | 395,532,637 bytes (396 MB) | `Lupin_FINAL_captioned.7z.001` … `.004` |
| **Clean** (no dialogue captions; keeps hook title, chapter labels, "7 NIGHTS LATER", end card) | `Lupin_FINAL_clean.mp4` | 401,095,763 bytes (401 MB) | `Lupin_FINAL_clean.7z.001` … `.005` |

Also in this folder:

- `Lupin_FINAL.srt` – subtitles timed to the final cut
- `Lupin_all_clips.zip` – the 23 raw Seedance 2.5 clips (480×854, original audio), numbered in film order

GitHub rejects any single file over 100 MB, so each MP4 is split into volumes of 95 MiB.

## How to get the MP4

1. Download **all parts of one version** into the same folder (e.g. `Lupin_FINAL_captioned.7z.001`, `.002`, `.003`, `.004`).
2. Extract **only the `.001` file** – the other parts are read automatically and you get one merged, full-size MP4.
   - Android: ZArchiver
   - Windows: 7-Zip or WinRAR
   - Mac: Keka or The Unarchiver

Checked: extracting `.001` gives a file byte-identical to the original render.

SHA-256 of the extracted MP4s:

```
8f6a6c3b1f85f947a0f5d255847bc01688e7186f296b8615be3884d3c116322b  Lupin_FINAL_captioned.mp4
91051462cba2b9418534ddb2989e9d4ae2af383b6aa78718c161a209eb41804c  Lupin_FINAL_clean.mp4
```

## Direct download links

Base: `https://github.com/jawadk403/escape-room-video/raw/main/lupin/`

- `Lupin_FINAL_captioned.7z.001` … `.004`
- `Lupin_FINAL_clean.7z.001` … `.005`
- `Lupin_FINAL.srt`
- `Lupin_all_clips.zip`

## Edit notes

- Footage: Seedance 2.5 (480p, 9:16) with audio and lip-sync generated inside the model; upscaled once to 720×1280 and graded to a soft, grainy 35 mm look. Same grade logic for every clip; luminance matched per clip.
- Cuts only – no dissolves except the fade through black into "7 NIGHTS LATER". No slow motion, no whooshes.
- Music and sound effects are original (synthesised for this edit); music is levelled per section and ducked under dialogue.
- Captions: white bold 1–4 word phrases, keywords highlighted in gold, timed to the audio and spelled exactly as in the script.
