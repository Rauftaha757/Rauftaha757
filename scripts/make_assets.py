"""Builds the SVGs used by the profile README (header, numbers, project cards).

Run from the repository root:  python3 scripts/make_assets.py
Palette and type follow the portfolio at https://taharauf-portfolio.vercel.app.
"""

import random
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', SFMono-Regular, Menlo, Consolas, monospace"
SERIF = "'Instrument Serif', Georgia, 'Times New Roman', serif"

THEMES = {
    "dark": dict(bg="#0a0a0b", panel="#111113", fg="#f2f1ec", muted="#8b8b90", line="#26262b", accent="#c4ee18", accent_text="#c4ee18", glow=0.20, cell="#c4ee18", empty="#1a1a1e"),
    "light": dict(bg="#fafaf7", panel="#ffffff", fg="#0a0a0b", muted="#6b6b70", line="#e4e4de", accent="#c4ee18", accent_text="#5f7f00", glow=0.45, cell="#8fb800", empty="#ecece6"),
}


def t(x, y, text, size, fill, family=SANS, weight=400, spacing=0, anchor="start", style="normal", opacity=1):
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'letter-spacing="{spacing}" text-anchor="{anchor}" font-style="{style}" fill="{fill}" opacity="{opacity}">{escape(text)}</text>'
    )


def chip(x, y, label, c, mono_w=8.6):
    w = round(len(label) * mono_w + 30)
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="none" stroke="{c["line"]}"/>'
        + t(x + 15, y + 22, label, 14, c["fg"], MONO, 500, 0.5, opacity=0.85)
    ), w


def header(theme):
    c = THEMES[theme]
    W, H = 1280, 400
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Taha Rauf, Software Engineer">',
        "<defs>",
        f'<radialGradient id="g" cx="78%" cy="45%" r="45%"><stop offset="0" stop-color="{c["accent"]}" stop-opacity="{c["glow"]}"/><stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/></radialGradient>',
        f'<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{c["fg"]}" stroke-opacity="0.045"/></pattern>',
        f'<clipPath id="r"><rect width="{W}" height="{H}" rx="28"/></clipPath>',
        "<style>@keyframes p{0%,100%{opacity:.25}50%{opacity:1}} .a{animation:p 3.2s ease-in-out infinite} @media (prefers-reduced-motion: reduce){.a{animation:none}}</style>",
        "</defs>",
        '<g clip-path="url(#r)">',
        f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>',
        f'<rect width="{W}" height="{H}" fill="url(#grid)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#g)"/>',
    ]

    # A contribution-style grid on the right, a quiet nod to shipping every day.
    rnd = random.Random(757)
    cols, rows, size, gap = 15, 7, 18, 6
    x0, y0 = W - 64 - cols * (size + gap) + gap, 104
    for col in range(cols):
        for row in range(rows):
            lvl = rnd.choices([0, 1, 2, 3, 4], weights=[3, 3, 3, 2, 2])[0]
            x, y = x0 + col * (size + gap), y0 + row * (size + gap)
            if lvl == 0:
                parts.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="4" fill="{c["empty"]}"/>')
            else:
                op = [0, 0.28, 0.5, 0.75, 1][lvl]
                anim = ' class="a" style="animation-delay:%.2fs"' % (rnd.random() * 3) if lvl == 4 and rnd.random() < 0.6 else ""
                parts.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="4" fill="{c["cell"]}" opacity="{op}"{anim}/>')

    # Eyebrow, name, tagline.
    parts.append(f'<circle cx="70" cy="82" r="5" fill="{c["accent"]}"/>')
    parts.append(t(86, 87, "SOFTWARE ENGINEER  ·  ISLAMABAD, PAKISTAN", 15, c["muted"], MONO, 500, 3))
    parts.append(t(58, 210, "Taha Rauf", 124, c["fg"], SANS, 700, -5))
    parts.append(
        f'<text x="64" y="272" font-family="{SANS}" font-size="28" fill="{c["fg"]}" opacity="0.85">'
        f'Production apps, from the database to the '
        f'<tspan font-family="{SERIF}" font-style="italic" font-size="32" fill="{c["accent_text"]}" opacity="1">App Store.</tspan></text>'
    )

    # Stack chips.
    x = 64
    for label in ["Flutter", "Swift & Kotlin", "Supabase", "PostgreSQL", "AWS Amplify Gen 2", "AI"]:
        svg, w = chip(x, 316, label, c)
        parts.append(svg)
        x += w + 10

    parts.append(t(W - 64, 87, "OPEN TO FULL-TIME ROLES", 13, c["accent_text"], MONO, 600, 2.5, anchor="end"))
    parts.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" stroke="{c["line"]}"/>')
    parts.append("</g></svg>")
    return "\n".join(parts)


def numbers(theme):
    c = THEMES[theme]
    W, H = 1280, 190
    items = [
        ("3", "+", "years shipping", "production software"),
        ("3", "", "apps in production:", "BrainCode, GymGPT, AlphaPilot"),
        ("945", "", "commits on a", "HIPAA-compliant EHR"),
        ("2,400", "+", "contributions in", "the last 12 months"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="3+ years, 3 apps in production (BrainCode, GymGPT, AlphaPilot), 945 commits on a HIPAA-compliant EHR, 2,400+ contributions in the last 12 months">',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="24" fill="{c["panel"]}" stroke="{c["line"]}"/>',
    ]
    col = W / 4
    for i, (num, suffix, l1, l2) in enumerate(items):
        x = i * col + 44
        if i:
            parts.append(f'<line x1="{i * col}" y1="36" x2="{i * col}" y2="{H - 36}" stroke="{c["line"]}"/>')
        parts.append(
            f'<text x="{x}" y="100" font-family="{SANS}" font-size="64" font-weight="700" letter-spacing="-3" fill="{c["fg"]}">'
            f'{escape(num)}<tspan fill="{c["accent_text"]}">{escape(suffix)}</tspan></text>'
        )
        parts.append(t(x + 2, 136, l1, 17, c["muted"]))
        parts.append(t(x + 2, 160, l2, 17, c["muted"]))
    parts.append("</svg>")
    return "\n".join(parts)


PROJECTS = [
    dict(slug="ehr", name="Hospice EHR", accent="#c4ee18", eyebrow="LEADING ENGINEER · US HEALTHCARE",
         tagline="HIPAA-compliant EHR on AWS Amplify Gen 2",
         points=["RBAC across 25+ roles, enforced in API and UI", "~30% lower API latency on patient records", "Clinical forms of 1,700+ fields, never half-saved"],
         tags=["Flutter Web", "AppSync", "Cognito", "Lambda"]),
    dict(slug="braincode", name="BrainCode", accent="#c9a14a", eyebrow="LIVE IN PRODUCTION · NETHERLANDS",
         tagline="Mental wellness for people and their employers",
         points=["Payment webhooks grant plans on the server", "Resumable offline downloads, background audio", "Two-phase boot for a faster first frame"],
         tags=["Flutter", "Supabase", "FCM", "Shorebird"]),
    dict(slug="gymgpt", name="GymGPT", accent="#e5322d", eyebrow="LIVE IN PRODUCTION · FITNESS",
         tagline="An AI personal trainer you can talk to",
         points=["GPT-4o replies streamed token by token (SSE)", "Deterministic plan engine with 138 tests", "Custom-painted muscle maps and charts"],
         tags=["Flutter", "Supabase", "OpenAI", "RevenueCat"]),
    dict(slug="boleia", name="Boleia", accent="#f1e11e", eyebrow="SOLE DEVELOPER · ANGOLA",
         tagline="Carpooling matched on the driver's real route",
         points=["PostGIS matching along the route line", "A booking engine that cannot double-book", "Live GPS tracking that glides, not jumps"],
         tags=["Flutter", "PostgreSQL", "PostGIS", "Realtime"]),
    dict(slug="dim-studio", name="Dim Studio", accent="#3b82f6", eyebrow="MAIN DEVELOPER · CAR DEALERSHIPS",
         tagline="A showroom photo studio powered by AI",
         points=["100-photo batches on Dart isolates", "Sliding-window rate limiter, priority queue", "Crash-safe: resumes after the app is killed"],
         tags=["Flutter", "Isolates", "Gemini", "SQLite"]),
    dict(slug="earned-athletix", name="Earned Athletix", accent="#e9edf2", eyebrow="MAIN DEVELOPER · FAMILIES",
         tagline="Kids earn screen time by working out",
         points=["iOS: Swift DeviceActivity extension", "Android: Kotlin foreground service + watchdog", "One MethodChannel API for both platforms"],
         tags=["Flutter", "Swift", "Kotlin", "Supabase"]),
]


def card(p):
    c = THEMES["dark"]
    W, H = 600, 340
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p["name"])}: {escape(p["tagline"])}">',
        "<defs>",
        f'<radialGradient id="g" cx="100%" cy="0%" r="70%"><stop offset="0" stop-color="{p["accent"]}" stop-opacity="0.22"/><stop offset="1" stop-color="{p["accent"]}" stop-opacity="0"/></radialGradient>',
        f'<clipPath id="r"><rect width="{W}" height="{H}" rx="22"/></clipPath>',
        "</defs>",
        '<g clip-path="url(#r)">',
        f'<rect width="{W}" height="{H}" fill="{c["panel"]}"/>',
        f'<rect width="{W}" height="{H}" fill="url(#g)"/>',
        f'<circle cx="38" cy="45" r="5" fill="{p["accent"]}"/>',
        t(54, 50, p["eyebrow"], 12, c["muted"], MONO, 500, 2),
        t(32, 108, p["name"], 44, c["fg"], SANS, 700, -1.5),
        t(34, 142, p["tagline"], 20, c["fg"], SERIF, 400, 0, style="italic", opacity=0.8),
    ]
    y = 186
    for pt in p["points"]:
        parts.append(t(34, y, "↳", 15, p["accent"], MONO, 600))
        parts.append(t(58, y, pt, 15.5, c["fg"], SANS, 400, opacity=0.88))
        y += 28
    x = 32
    for tag in p["tags"]:
        w = round(len(tag) * 7.6 + 24)
        parts.append(f'<rect x="{x}" y="{H - 58}" width="{w}" height="28" rx="14" fill="#ffffff" fill-opacity="0.06"/>')
        parts.append(t(x + 12, H - 39, tag, 12.5, c["fg"], MONO, 500, 0.3, opacity=0.75))
        x += w + 8
    parts.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="22" fill="none" stroke="{c["line"]}"/>')
    parts.append("</g></svg>")
    return "\n".join(parts)


# Apple release tools, drawn as tiles that match skillicons.dev (256 px tiles,
# rx 60, 44 px apart), since skillicons has none of them. Xcode and the App
# Store glyph are from Simple Icons (CC0, 24x24 paths); TestFlight is drawn here.
XCODE_PATH = "M19.06 5.3327c.4517-.1936.7744-.2581 1.097-.1936.5163.1291.7744.5163.968.7098.1936.3872.9034.7744 1.2261.8389.2581.0645.7098-.6453 1.0325-1.2906.3227-.5808.5163-1.3552.4517-1.5488-.0645-.1936-.968-.5808-1.1616-.5808-.1291 0-.3872.1291-.8389.0645-.4517-.0645-.9034-.5808-1.1616-.968-.4517-.6453-1.097-1.0325-1.6778-1.3552-.6453-.3227-1.3552-.5163-2.065-.6453-1.0325-.2581-2.065-.4517-3.0975-.3227-.5808.0645-1.2906.1291-1.8069.3227-.0645 0-.1936.1936-.0645.1936s.5808.0645.5808.0645-.5807.1292-.5807.2583c0 .1291.0645.1291.1291.1291.0645 0 1.4842-.0645 2.065 0 .6453.1291 1.3552.4517 1.8069 1.2261.7744 1.4197.4517 2.7749.2581 3.2266-.968 2.1295-8.6472 15.2294-9.0344 16.1328-.3873.9034-.5163 1.4842.5807 2.065s1.6778.3227 2.0005-.0645c.3872-.5163 7.0339-17.1654 9.2925-18.2624zm-3.6138 8.7117h1.5488c1.0325 0 1.2261.5163 1.2261.7098.0645.5163-.1936 1.1616-1.2261 1.1616h-.968l.7744 1.2906c.4517.7744.2581 1.1616 0 1.4197-.3872.3872-1.2261.3872-1.6778-.4517l-.9034-1.5488c-.6453 1.4197-1.2906 2.9684-2.065 4.7753h4.0009c1.9359 0 3.5492-1.6133 3.5492-3.5492V6.5588c-.0645-.1291-.1936-.0645-.2581 0-.3872.4517-1.4842 2.0004-4.001 7.4856zm-9.8087 8.0019h-.3227c-2.3231 0-4.1945-1.8714-4.1945-4.1945V7.0105c0-2.3231 1.8714-4.1945 4.1945-4.1945h9.3571c-.1936-.1936-.968-.5163-1.7423-.4517-.3227 0-.968.1291-1.3552-.1291-.3872-.3227-.3227-.5163-.9034-.5163H4.9277c-2.6458 0-4.7753 2.1295-4.7753 4.7753v11.7447c0 2.6458 2.1295 4.7753 4.4527 4.7108.6452 0 .8388-.5162 1.0324-.9034zM20.4152 6.9459v10.9058c0 2.3231-1.8714 4.1945-4.1945 4.1945H11.897s-.3872 1.0325.8389 1.0325h3.8719c2.6458 0 4.7753-2.1295 4.7753-4.7753V8.8173c.0646-.9034-.7098-1.4842-.9679-1.8714zm-18.5851.0646v10.8413c0 1.9359 1.6133 3.5492 3.5492 3.5492h.5808c0-.0645.7744-1.4197 2.4522-4.2591.1936-.3872.4517-.7744.7098-1.2261H4.4114c-.5808 0-.9034-.3872-.968-.7098-.1291-.5163.1936-1.1616.9034-1.1616h2.3877l3.033-5.2916s-.7098-1.2906-.9034-1.6133c-.2582-.4517-.1291-.9034.129-1.1615.3872-.3872 1.0325-.5808 1.6778.4517l.2581.3872.2581-.3872c.5808-.8389.968-.7744 1.2906-.7098.5163.1291.8389.7098.3872 1.6133L8.864 14.0444h1.3552c.4517-.7744.9034-1.5488 1.3552-2.3877-.0645-.3227-.1291-.7098-.0645-1.0325.0645-.5163.3227-.968.6453-1.3552l.3872.6453c1.2261-2.1295 2.1295-3.9364 2.3877-4.6463.1291-.3872.3227-1.1616.1291-1.8069H5.3794c-2.0005.0001-3.5493 1.6134-3.5493 3.5494zM4.605 17.7872c0-.0645.7744-1.4197.7744-1.4197 1.2261-.3227 1.8069.4517 1.8714.5163 0 0-.8389 1.4842-1.097 1.7423s-.5808.3227-.9034.2581c-.5164-.129-.839-.6453-.6454-1.097z"
APPSTORE_PATH = "M8.8086 14.9194l6.1107-11.0368c.0837-.1513.1682-.302.2437-.4584.0685-.142.1267-.2854.1646-.4403.0803-.3259.0588-.6656-.066-.9767-.1238-.3095-.3417-.5678-.6201-.7355a1.4175 1.4175 0 0 0-.921-.1924c-.3207.043-.6135.1935-.8443.4288-.1094.1118-.1996.2361-.2832.369-.092.1463-.175.2979-.259.4492l-.3864.6979-.3865-.6979c-.0837-.1515-.1667-.303-.2587-.4492-.0837-.1329-.1739-.2572-.2835-.369-.2305-.2353-.5233-.3857-.844-.429a1.4181 1.4181 0 0 0-.921.1926c-.2784.1677-.4964.426-.6203.7355-.1246.311-.1461.6508-.066.9767.038.155.0962.2984.1648.4403.0753.1564.1598.307.2437.4584l1.248 2.2543-4.8625 8.7825H2.0295c-.1676 0-.3351-.0007-.5026.0092-.1522.009-.3004.0284-.448.0714-.3108.0906-.5822.2798-.7783.548-.195.2665-.3006.5929-.3006.9279 0 .3352.1057.6612.3006.9277.196.2683.4675.4575.7782.548.1477.043.296.0623.4481.0715.1675.01.335.009.5026.009h13.0974c.0171-.0357.059-.1294.1-.2697.415-1.4151-.6156-2.843-2.0347-2.843zM3.113 18.5418l-.7922 1.5008c-.0818.1553-.1644.31-.2384.4705-.067.1458-.124.293-.1611.452-.0785.3346-.0576.6834.0645 1.0029.1212.3175.3346.583.607.7549.2727.172.5891.2416.9013.1975.3139-.044.6005-.1986.8263-.4402.1072-.1148.1954-.2424.2772-.3787.0902-.1503.1714-.3059.2535-.4612L6 19.4636c-.0896-.149-.9473-1.4704-2.887-.9218m20.5861-3.0056a1.4707 1.4707 0 0 0-.779-.5407c-.1476-.0425-.2961-.0616-.4483-.0705-.1678-.0099-.3352-.0091-.503-.0091H18.648l-4.3891-7.817c-.6655.7005-.9632 1.485-1.0773 2.1976-.1655 1.0333.0367 2.0934.546 3.0004l5.2741 9.3933c.084.1494.167.299.2591.4435.0837.131.1739.2537.2836.364.231.2323.5238.3809.8449.4232.3192.0424.643-.0244.9217-.1899.2784-.1653.4968-.4204.621-.7257.1246-.3072.146-.6425.0658-.9641-.0381-.1529-.0962-.2945-.165-.4346-.0753-.1543-.1598-.303-.2438-.4524l-1.216-2.1662h1.596c.1677 0 .3351.0009.5029-.009.1522-.009.3007-.028.4483-.0705a1.4707 1.4707 0 0 0 .779-.5407A1.5386 1.5386 0 0 0 24 16.452a1.539 1.539 0 0 0-.3009-.9158Z"
TILE = {"dark": "#242938", "light": "#F4F2ED"}


def _glyph(path, fill, size=168):
    k = size / 24
    off = (256 - size) / 2
    return f'<g transform="translate({off} {off}) scale({k:.4f})"><path fill="{fill}" d="{path}"/></g>'


def _testflight(theme):
    # A propeller in a ring, after the TestFlight icon.
    blue = "#1E90FF"
    blades = "".join(
        f'<ellipse cx="128" cy="86" rx="21" ry="44" fill="{blue}" transform="rotate({a} 128 128)"/>' for a in (0, 120, 240)
    )
    return (
        f'<circle cx="128" cy="128" r="86" fill="none" stroke="{blue}" stroke-width="13"/>'
        + blades
        + f'<circle cx="128" cy="128" r="19" fill="{TILE[theme]}"/><circle cx="128" cy="128" r="10" fill="{blue}"/>'
    )


def apple_tools(theme):
    tiles = [
        ("Xcode", f'<rect width="256" height="256" rx="60" fill="{TILE[theme]}"/>' + _glyph(XCODE_PATH, "#147EFB")),
        ("TestFlight", f'<rect width="256" height="256" rx="60" fill="{TILE[theme]}"/>' + _testflight(theme)),
        (
            "App Store Connect",
            '<defs><linearGradient id="asc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1AC8FC"/><stop offset="1" stop-color="#1A74E8"/></linearGradient></defs>'
            '<rect width="256" height="256" rx="60" fill="url(#asc)"/>' + _glyph(APPSTORE_PATH, "#ffffff", 150),
        ),
    ]
    w = len(tiles) * 256 + (len(tiles) - 1) * 44
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * 48 / 256:.2f}" height="48" viewBox="0 0 {w} 256" role="img" aria-label="Xcode, TestFlight, App Store Connect">'
    ]
    for i, (name, body) in enumerate(tiles):
        parts.append(f'<g transform="translate({i * 300} 0)"><title>{name}</title>{body}</g>')
    parts.append("</svg>")
    return "".join(parts)


def main():
    (OUT / "work").mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        (OUT / f"header-{theme}.svg").write_text(header(theme))
        (OUT / f"numbers-{theme}.svg").write_text(numbers(theme))
        (OUT / f"apple-tools-{theme}.svg").write_text(apple_tools(theme))
    for p in PROJECTS:
        (OUT / "work" / f'{p["slug"]}.svg').write_text(card(p))
    print("wrote", sorted(str(f.relative_to(OUT)) for f in OUT.rglob("*.svg")))


if __name__ == "__main__":
    main()
