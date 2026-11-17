"""Builds the SVGs used by the profile README (header, numbers, project cards).

Run from the repository root:  python3 scripts/make_assets.py
Palette and type follow the portfolio at https://taharauf.vercel.app.
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
        ("2", "", "apps live on the", "App Store & Google Play"),
        ("945", "", "commits on a", "HIPAA-compliant EHR"),
        ("2,400", "+", "contributions in", "the last 12 months"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="3+ years, 2 apps live, 945 commits on a HIPAA-compliant EHR, 2,400+ contributions in the last 12 months">',
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


def main():
    (OUT / "work").mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        (OUT / f"header-{theme}.svg").write_text(header(theme))
        (OUT / f"numbers-{theme}.svg").write_text(numbers(theme))
    for p in PROJECTS:
        (OUT / "work" / f'{p["slug"]}.svg').write_text(card(p))
    print("wrote", sorted(str(f.relative_to(OUT)) for f in OUT.rglob("*.svg")))


if __name__ == "__main__":
    main()
