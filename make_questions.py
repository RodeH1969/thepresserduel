import requests
import os
import time

API_KEY = "sk_fb908392edbca54a9b58d2ca74794e5b451d8508d856d454"
VOICE_ID = "Aa6nEBJJMKJwJkCx8VU2"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio")

# Every block of 5:
# 1. Bracket equation
# 2. Subtraction
# 3. Multiplication
# 4. Square
# 5. Addition
#
# (num, spoken_text, answer)

QUESTIONS = [

    # ── BLOCK 1 ─────────────────────────────────────────────────────────────────
    (1,  "3 times, open bracket, 4 plus 2, close bracket, plus 2, minus, open bracket, 5 times 2, close bracket",            0),
    (2,  "47 minus 19",                                                                                                        28),
    (3,  "12 times 14",                                                                                                        168),
    (4,  "13 squared",                                                                                                         169),
    (5,  "273 plus 345",                                                                                                       618),

    # ── BLOCK 2 ─────────────────────────────────────────────────────────────────
    (6,  "4 times, open bracket, 7 minus 3, close bracket, plus 6 divided by 2",                                              19),
    (7,  "83 minus 37",                                                                                                        46),
    (8,  "9 times 13",                                                                                                         117),
    (9,  "11 squared",                                                                                                         121),
    (10, "456 plus 278",                                                                                                       734),

    # ── BLOCK 3 ─────────────────────────────────────────────────────────────────
    (11, "open bracket, 8 plus 4, close bracket, times 3, minus 5 times, open bracket, 2 plus 1, close bracket",              21),
    (12, "91 minus 54",                                                                                                        37),
    (13, "14 times 11",                                                                                                        154),
    (14, "7 squared",                                                                                                          49),
    (15, "382 plus 419",                                                                                                       801),

    # ── BLOCK 4 ─────────────────────────────────────────────────────────────────
    (16, "open bracket, 6 plus 3, close bracket, times, open bracket, 7 minus 4, close bracket",                              27),
    (17, "74 minus 28",                                                                                                        46),
    (18, "8 times 17",                                                                                                         136),
    (19, "15 squared",                                                                                                         225),
    (20, "547 plus 364",                                                                                                       911),

    # ── BLOCK 5 ─────────────────────────────────────────────────────────────────
    (21, "5 times, open bracket, 8 minus 3, close bracket, minus, open bracket, 4 plus 2, close bracket, times 3",            7),
    (22, "132 minus 67",                                                                                                       65),
    (23, "13 times 13",                                                                                                        169),
    (24, "9 squared",                                                                                                          81),
    (25, "628 plus 247",                                                                                                       875),

    # ── BLOCK 6 ─────────────────────────────────────────────────────────────────
    (26, "open bracket, 12 minus 4, close bracket, times, open bracket, 3 plus 2, close bracket, divided by 4",               10),
    (27, "165 minus 88",                                                                                                       77),
    (28, "16 times 12",                                                                                                        192),
    (29, "14 squared",                                                                                                         196),
    (30, "736 plus 185",                                                                                                       921),

    # ── BLOCK 7 ─────────────────────────────────────────────────────────────────
    (31, "7 times, open bracket, 5 plus 3, close bracket, minus, open bracket, 6 times 4, close bracket",                     32),
    (32, "204 minus 137",                                                                                                      67),
    (33, "7 times 18",                                                                                                         126),
    (34, "12 squared",                                                                                                         144),
    (35, "819 plus 364",                                                                                                       1183),

    # ── BLOCK 8 ─────────────────────────────────────────────────────────────────
    (36, "open bracket, 9 plus 3, close bracket, divided by 4, plus, open bracket, 7 times 2, close bracket",                 17),
    (37, "312 minus 178",                                                                                                      134),
    (38, "15 times 14",                                                                                                        210),
    (39, "16 squared",                                                                                                         256),
    (40, "467 plus 538",                                                                                                       1005),

    # ── BLOCK 9 ─────────────────────────────────────────────────────────────────
    (41, "open bracket, 7 minus 2, close bracket, squared, plus 3 times 4",                                                   37),
    (42, "425 minus 268",                                                                                                      157),
    (43, "19 times 11",                                                                                                        209),
    (44, "17 squared",                                                                                                         289),
    (45, "583 plus 749",                                                                                                       1332),

    # ── BLOCK 10 ────────────────────────────────────────────────────────────────
    (46, "open bracket, 5 plus 3, close bracket, squared, divided by 8, plus 6 times 3",                                      26),
    (47, "703 minus 456",                                                                                                      247),
    (48, "23 times 14",                                                                                                        322),
    (49, "18 squared",                                                                                                         324),
    (50, "847 plus 596",                                                                                                       1443),
]

def generate_audio(text, filepath):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY,
    }
    body = {
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.78,
            "style": 0.15,
            "use_speaker_boost": True,
            "speed": 0.7
        }
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code != 200:
        raise Exception(f"API error {response.status_code}: {response.text}")
    with open(filepath, "wb") as f:
        f.write(response.content)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"\nThe Presser — Question Audio Maker")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Voice:  Adam  |  50 questions  |  10 blocks of 5")
    print(f"Pattern per block: bracket equation · subtraction · multiplication · square · addition")
    print(f"{'─' * 60}")

    done = 0
    failed = []

    for num, spoken, answer in QUESTIONS:
        filename = f"q{str(num).zfill(3)}.mp3"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Delete old file if exists to force regeneration at new speed
        if os.path.exists(filepath):
            os.remove(filepath)
        if False and os.path.exists(filepath):
            print(f"  [{num:02d}/50] {filename} exists — skipping")
            done += 1
            continue

        qtype = {1:"bracket",2:"subtract",3:"multiply",4:"square",5:"addition"}[(num-1)%5+1]
        print(f"  [{num:02d}/50] ({qtype:8s})  {filename}...", end="", flush=True)

        try:
            generate_audio(spoken, filepath)
            print(f" ✓  = {answer}")
            done += 1
        except Exception as e:
            print(f" ✗  {e}")
            failed.append((num, str(e)))

        time.sleep(0.4)

    print(f"{'─' * 60}")
    print(f"Complete: {done}/50 saved to assets/audio/")
    if failed:
        print(f"Failed ({len(failed)}) — re-run to retry:")
        for num, err in failed:
            print(f"  Q{num:02d}: {err}")

if __name__ == "__main__":
    main()