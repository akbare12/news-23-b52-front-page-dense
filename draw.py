#!/usr/bin/env python3
"""news-23 b52 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026.
1024x1024 front page, 31 stories. PIL only; run: python3 draw.py -> entry.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu"

def F(size, bold=False):
    return ImageFont.truetype(os.path.join(FD, "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), size)

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
GOLD = (212, 175, 55)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
NAVY = (16, 32, 64)
TEAL = (0, 128, 128)
CREAM = (250, 244, 224)
GREY = (90, 90, 90)
LGREY = (230, 230, 230)

# ---------- masthead ----------
d.rectangle([0, 0, W, 58], fill=BLACK)
d.text((14, 8), "THE WORLD TODAY", font=F(34, True), fill="white")
d.text((W - 14 - d.textlength("MONDAY 23 NOVEMBER 2026", font=F(17, True)), 20),
       "MONDAY 23 NOVEMBER 2026", font=F(17, True), fill=GOLD)

# ---------- kicker ----------
d.text((14, 62), "AI rout hits Asia  ·  UN chief urges AI rules  ·  US lead over China at record low  ·  Anthropic IPO $107.3B",
       font=F(13, True), fill=RED)

# ---------- number strip: 2 rows x 5 ----------
nums = [
    ("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", NAVY),
    ("11,762", "EBOLA CASES, DRC", (0, 110, 60)), ("10T won", "SEOUL STABILISATION FUND", (150, 100, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (110, 40, 140)),
    ("$450M", "SKUBAL DEAL", (110, 40, 140)), ("165", "RUSSIAN MISSILES IN A WEEK", DARKRED),
    ("12,000", "CLEARED IN MANCHESTER", NAVY), ("264 kg", "EXPLOSIVES SEIZED IN LEBANON", (150, 100, 0)),
    ("$107.3B", "ANTHROPIC IPO — LARGEST", (110, 40, 140)),
]
colw = W // 5
for i, (val, lab, col) in enumerate(nums):
    cx = (i % 5) * colw + 12
    cy = 75 if i < 5 else 99
    d.text((cx, cy), val, font=F(18, True), fill=col)
    d.text((cx, cy + 17), lab, font=F(8), fill=BLACK)
d.line([0, 131, W, 131], fill=BLACK, width=1)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", 7, (0, 128, 128)), ("AMERICAS 8", 8, NAVY),
           ("MIDDLE EAST 6", 6, (180, 120, 0)), ("EUROPE 5", 5, (110, 60, 160)),
           ("AFRICA 3", 3, DARKRED), ("WORLD 2", 2, (90, 90, 90))]
x = 0
for name, n, col in regions:
    wseg = int(round(n / 31 * W))
    if name == "WORLD 2":
        wseg = W - x
    d.rectangle([x, 133, x + wseg, 149], fill=col)
    lab = name
    fnt = F(10, True)
    tw = d.textlength(lab, font=fnt)
    tx = x + max(3, (wseg - tw) // 2)
    d.text((tx, 136), lab, font=fnt, fill="white")
    x += wseg

# ---------- UTC strip ----------
d.text((8, 152), "THE DAY IN UTC   ~00:00 Kospi dives  ~06:30 Guterres opens  ~09:00 Power Index  ~12:00 Paris 2% tax  ~15:00 Kyiv missiles  ~18:00 IPO $97.17",
       font=F(9), fill=BLACK)
d.text((W - 8 - d.textlength("~ APPROX", font=F(9, True)), 152), "~ APPROX", font=F(9, True), fill=GREY)

# ---------- hero scenes ----------
# column geometry: 3 cols, 4px gaps
cols = [(0, 338), (342, 680), (684, 1024)]
SC_Y0, SC_Y1 = 166, 296      # scene area
CAP_Y0, CAP_Y1 = 296, 314    # black caption strip
TXT_Y0 = 320                 # hero text block starts (6px gap below caption)

# --- scene 1: Kospi chart ---
x0, x1 = cols[0]
d.rectangle([x0, SC_Y0, x1, SC_Y1], fill=(8, 20, 48))
d.text((x0 + 8, SC_Y0 + 4), "-3.3%", font=F(26, True), fill=(255, 70, 60))
pts = [(x0 + 12 + i * 30, SC_Y0 + 78 - v) for i, v in enumerate([0, 14, 6, 22, 10, 26, 16, 30, 20, 34, 26])]
d.line(pts, fill=(255, 120, 80), width=2)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 190, 60))
# skyline at bottom of scene (tops well above caption)
import random
random.seed(23)
bx = x0 + 10
while bx < x1 - 18:
    bw = random.randint(14, 26)
    bh = random.randint(18, 42)
    by = SC_Y1 - bh
    d.rectangle([bx, by, bx + bw, SC_Y1], fill=(20, 40, 80))
    for wy in range(by + 4, SC_Y1 - 4, 9):
        for wx in range(bx + 3, bx + bw - 3, 7):
            d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 220, 90))
    bx += bw + 4
d.rectangle([x0, CAP_Y0, x1, CAP_Y1], fill=BLACK)
d.text((x0 + 8, CAP_Y0 + 3), "KOSPI 4,708.54  ·  -161 PTS", font=F(10, True), fill="white")

# --- scene 2: Guterres ---
x0, x1 = cols[1]
d.rectangle([x0, SC_Y0, x1, SC_Y1], fill=TEAL)
d.text((x0 + 10, SC_Y0 + 6), "150 DELEGATES", font=F(25, True), fill=(255, 200, 60))
d.text((x0 + 10, SC_Y0 + 36), "BACK A RISK", font=F(25, True), fill="white")
d.text((x0 + 10, SC_Y0 + 66), "FRAMEWORK", font=F(25, True), fill="white")
# globe bottom-right, clear of text
gx, gy, gr = x1 - 42, SC_Y1 - 34, 26
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline="white", width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline="white", width=1)
d.line([gx - gr, gy, gx + gr, gy], fill="white", width=1)
d.line([gx - gr, gy - 12, gx + gr, gy - 12], fill="white", width=1)
d.line([gx - gr, gy + 12, gx + gr, gy + 12], fill="white", width=1)
d.rectangle([x0, CAP_Y0, x1, CAP_Y1], fill=BLACK)
d.text((x0 + 8, CAP_Y0 + 3), "UN  ·  BRIDGETOWN", font=F(10, True), fill="white")

# --- scene 3: Power Index bars ---
x0, x1 = cols[2]
d.rectangle([x0, SC_Y0, x1, SC_Y1], fill=CREAM)
d.text((x0 + 8, SC_Y0 + 4), "NARROWEST SINCE 2018", font=F(11, True), fill=BLACK)
d.text((x1 - 8 - d.textlength("GAP 5.3", font=F(11, True)), SC_Y0 + 4), "GAP 5.3", font=F(11, True), fill=(150, 110, 0))
bars = [("78.9", "US", NAVY, 78.9), ("73.6", "CHINA", (178, 34, 34), 73.6), ("40.5", "INDIA", (200, 160, 40), 40.5)]
base = SC_Y1 - 2
bw = 78
gap = 14
bx = x0 + 22
for val, lab, col, v in bars:
    bh = int(v * 1.05)
    d.text((bx + bw // 2 - d.textlength(val, font=F(13, True)) // 2, base - bh - 20), val,
           font=F(13, True), fill=BLACK)
    d.rectangle([bx, base - bh, bx + bw, base], fill=col)
    d.text((bx + bw // 2 - d.textlength(lab, font=F(10, True)) // 2, base - 16), lab,
           font=F(10, True), fill="white")
    bx += bw + gap
d.rectangle([x0, CAP_Y0, x1, CAP_Y1], fill=BLACK)
d.text((x0 + 8, CAP_Y0 + 3), "ASIA POWER INDEX 2026", font=F(10, True), fill="white")

# ---------- hero text blocks (below caption strip, 6px gap) ----------
heroes = [
    ("1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS"),
    ("3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 — gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
for (x0, x1), (num, head, body, src) in zip(cols, heroes):
    # numbered circle
    d.ellipse([x0 + 4, TXT_Y0 + 2, x0 + 24, TXT_Y0 + 22], fill=DARKRED)
    tw = d.textlength(num, font=F(11, True))
    d.text((x0 + 14 - tw / 2, TXT_Y0 + 5), num, font=F(11, True), fill="white")
    hl = wrap(d, head, F(16, True), x1 - x0 - 32)
    y = TXT_Y0 + 26
    for ln in hl[:2]:
        d.text((x0 + 30, y), ln, font=F(16, True), fill=BLACK)
        y += 19
    bl = wrap(d, body, F(11), x1 - x0 - 12)
    y = TXT_Y0 + 68
    for ln in bl[:2]:
        d.text((x0 + 8, y), ln, font=F(11), fill=BLACK)
        y += 14
    # source + chip on their own bottom row
    d.text((x0 + 8, TXT_Y0 + 98), src, font=F(9), fill=GREY)
    chip = "REPORTED"
    cw = d.textlength(chip, font=F(8, True)) + 10
    d.rectangle([x1 - 8 - cw, TXT_Y0 + 96, x1 - 8, TXT_Y0 + 110], fill=NAVY)
    d.text((x1 - 8 - cw + 5, TXT_Y0 + 99), chip, font=F(8, True), fill="white")

# ---------- MORE OF THE DAY bar ----------
d.rectangle([0, 430, W, 448], fill=BLACK)
d.text((10, 433), "MORE OF THE DAY  —  10 STORIES", font=F(12, True), fill="white")

# ---------- 10 cards: 2 rows x 5 ----------
cards = [
    ("AMERICAS", "BESSENT: NVIDIA ANSWERS", "Treasury chief wants China answers.", "Reuters", "REPORTED"),
    ("FBI", "FBI PROBES NCIC HACK", "Hackers hit police NCIC database.", "AP", "REPORTED"),
    ("WHITE HOUSE", "TRUMP: IRAN STRIKES MAY RESUME", "Strikes may resume in New Year.", "Reuters", "REPORTED"),
    ("MARKETS", "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED"),
    ("SPORT", "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED"),
    ("SPORT", "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED"),
    ("LEGAL", "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED"),
    ("TECH", "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED"),
    ("EUROPE", "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM"),
    ("SPACE", "RUSSIAN NUCLEAR SATELLITE", "Intel: satellite may carry a nuke.", "Reuters", "CLAIM"),
]
catcol = {"AMERICAS": (0, 128, 128), "FBI": DARKRED, "WHITE HOUSE": (150, 110, 0),
          "MARKETS": (0, 110, 60), "SPORT": DARKRED, "LEGAL": (110, 60, 160),
          "TECH": NAVY, "EUROPE": (110, 60, 160), "SPACE": (90, 90, 90)}
cw = W // 5
for i, (cat, head, body, src, chip) in enumerate(cards):
    cx = (i % 5) * cw
    cy = 450 if i < 5 else 538
    ch = 86
    d.rectangle([cx, cy, cx + cw - 2, cy + 15], fill=catcol[cat])
    d.text((cx + 6, cy + 2), cat, font=F(9, True), fill="white")
    d.text((cx + cw - 14, cy + 2), str(i + 1), font=F(9, True), fill="white")
    hl = wrap(d, head, F(11, True), cw - 14)
    y = cy + 18
    for ln in hl[:2]:
        d.text((cx + 6, y), ln, font=F(11, True), fill=BLACK)
        y += 13
    d.text((cx + 6, cy + 48), body, font=F(9), fill=BLACK)
    # source + chip on own bottom row, chip right-aligned inside card
    d.text((cx + 6, cy + 68), src, font=F(8), fill=GREY)
    chipw = d.textlength(chip, font=F(8, True)) + 10
    chipcol = NAVY if chip == "REPORTED" else DARKRED
    d.rectangle([cx + cw - 10 - chipw, cy + 66, cx + cw - 10, cy + 80], fill=chipcol)
    d.text((cx + cw - 10 - chipw + 5, cy + 69), chip, font=F(8, True), fill="white")
d.line([0, 626, W, 626], fill=BLACK, width=1)

# ---------- map + ALSO ----------
d.rectangle([0, 628, 330, 646], fill=BLACK)
d.text((8, 631), "WHERE IT HAPPENED", font=F(11, True), fill="white")
d.rectangle([340, 628, W, 646], fill=BLACK)
d.text((348, 631), "ALSO ON MONDAY", font=F(11, True), fill="white")
# map: light grid + green blobs
d.rectangle([0, 648, 330, 880], fill=(235, 245, 255))
for gx in range(0, 331, 22):
    d.line([gx, 648, gx, 880], fill=(215, 228, 245), width=1)
for gy in range(648, 881, 22):
    d.line([0, gy, 330, gy], fill=(215, 228, 245), width=1)
# stylised continents (blobs)
d.ellipse([18, 668, 150, 800], fill=(150, 205, 140))
d.ellipse([150, 660, 320, 790], fill=(150, 205, 140))
d.ellipse([120, 800, 230, 872], fill=(150, 205, 140))
d.ellipse([250, 800, 322, 868], fill=(150, 205, 140))
pins = [(60, 690), (95, 812), (215, 690), (80, 760), (110, 745), (245, 700),
        (130, 720), (45, 735), (100, 790), (135, 815), (255, 672), (270, 700), (290, 680)]
for i, (px, py) in enumerate(pins, 1):
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=DARKRED, outline="white", width=1)
    tw = d.textlength(str(i), font=F(8, True))
    d.text((px - tw / 2, py - 6), str(i), font=F(8, True), fill="white")
d.text((8, 836), "Pins 1–13: 1 Seoul · 2 Bridgetown · 3 Beijing", font=F(8), fill=BLACK)
d.text((8, 850), "4 Washington · 5 New York · 6 Tehran · 7 Chicago", font=F(8), fill=BLACK)
d.text((8, 864), "8 SF · 9 Denver · 10 Austin · 11 Warsaw · 12 Kyiv · 13 Moscow", font=F(8), fill=BLACK)

also = [
    "14. Paris: 100+ back 2% billionaire tax", "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week", "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe", "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike", "21. West Bank settler attacks",
    "22. Iran war: no deal in sight", "23. Lebanon seizes 264 kg explosives",
    "24. Bahrain: strike hits plant, 2 hurt", "25. Sudan: defences down drones",
    "26. DRC: fighting traps Ebola teams", "27. Bangladesh: Hasina jailed if she returns",
    "28. Seoul minister quits in exam row", "29. SK Telecom -7.3% as hype cools",
    "30. China eases margin rules", "31. Seoul readies 10T-won fund",
]
for i, t in enumerate(also):
    ax = 348 if i < 9 else 686
    ay = 654 + (i % 9) * 24
    d.text((ax, ay), t, font=F(11), fill=BLACK)

# ---------- DATE CHECK ----------
d.rectangle([0, 884, W, 950], outline=DARKRED, width=2)
d.text((10, 888), "DATE CHECK", font=F(13, True), fill=DARKRED)
d.text((W - 10 - d.textlength("READ 23 NOV 2026, 23:59 UTC — STORIES DATED 23 NOV ONLY", font=F(8, True)), 891),
       "READ 23 NOV 2026, 23:59 UTC — STORIES DATED 23 NOV ONLY", font=F(8, True), fill=DARKRED)
left = "LEFT OUT — NOT 23 NOV: Democrats reach 258 seats (22 Nov) · Sparta II fire (22 Nov) · El Chapo Isidro captured (22 Nov) · EU–Indonesia pact (21 Nov) · Nigeria boat (21 Nov) · ICJ Myanmar ruling (19 Nov)"
ll = wrap(d, left, F(10), W - 24)
y = 906
for ln in ll[:2]:
    d.text((12, y), ln, font=F(10), fill=BLACK)
    y += 13
d.text((12, 934), "NOT YET: Dymer search continues (14 missing) · 4 House races uncalled · COP32 venue not set · WHO evacuating trapped Ebola staff",
       font=F(10), fill=BLACK)

# ---------- footer ----------
d.text((10, 956), "Sources: Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy Institute (Asia Power Index 2026).", font=F(8), fill=GREY)
d.text((10, 968), "CHIPS: REPORTED = confirmed by wires · CLAIM = one side's claim, not independently confirmed · ONGOING = still developing", font=F(8), fill=GREY)
d.text((10, 980), "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.", font=F(8), fill=GREY)

# ---------- bottom bar ----------
d.rectangle([0, 994, W, 1024], fill=BLACK)
bt = "THE WORLD TODAY  —  Monday 23 November 2026  ·  31 stories  ·  6 regions"
d.text(((W - d.textlength(bt, font=F(13, True))) / 2, 1003), bt, font=F(13, True), fill=GOLD)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out)
print("saved", out, os.path.getsize(out), "bytes")
