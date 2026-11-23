"""Generates the profile README artwork (header, terminal, cards) in dark and light themes.
Run: python assets/generate.py  (writes SVGs next to this file)."""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'Cascadia Code', 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace"

THEMES = {
    "dark": dict(
        bg1="#0b1220", bg2="#112645", grid="#1f3a63", text="#e6edf3", muted="#8b9bb4",
        accent="#4493f8", accent2="#3ddbd9", card="#0d1117", border="#30363d",
        pill="#16233a", pilltext="#9cc3ff", term="#0d1117", termbar="#161b22", ok="#3fb950",
    ),
    "light": dict(
        bg1="#eef4ff", bg2="#d6e6ff", grid="#b7cdf0", text="#1b2a4a", muted="#56657d",
        accent="#1f6feb", accent2="#0e9f9b", card="#ffffff", border="#d0d7de",
        pill="#e7f0ff", pilltext="#1f5fbf", term="#f6f8fa", termbar="#eaeef2", ok="#1a7f37",
    ),
}


def header(t):
    nodes = [(850, 70), (980, 52), (1110, 96), (900, 170), (1040, 160), (1155, 214), (950, 262), (1090, 270), (820, 250)]
    links = [(0, 1), (1, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 5), (3, 6), (4, 7), (6, 7), (5, 7), (3, 8), (8, 6)]
    lines, packets = [], []
    for i, (a, b) in enumerate(links):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["accent"]}" stroke-opacity=".35" stroke-width="1.5"/>')
        if i % 2 == 0:
            dur = 2.6 + (i % 5) * 0.55
            packets.append(
                f'<circle r="3.2" fill="{t["accent2"]}"><animateMotion dur="{dur:.2f}s" repeatCount="indefinite" '
                f'begin="{i * 0.37:.2f}s" path="M{x1},{y1} L{x2},{y2}"/></circle>')
    dots = []
    for i, (x, y) in enumerate(nodes):
        r = 9 if i in (1, 4) else 6.5
        dots.append(
            f'<circle cx="{x}" cy="{y}" r="{r + 7}" fill="{t["accent"]}" opacity=".12">'
            f'<animate attributeName="r" values="{r + 4};{r + 11};{r + 4}" dur="3.2s" begin="{i * 0.4:.1f}s" repeatCount="indefinite"/></circle>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{t["card"]}" stroke="{t["accent"]}" stroke-width="2.2"/>')
    chips, x = [], 60
    for label in ["Linux", "Docker", "Kubernetes", "Proxmox", "BGP", "AWS"]:
        w = 26 + len(label) * 10.6
        chips.append(f'<rect x="{x}" y="226" width="{w:.0f}" height="36" rx="18" fill="{t["pill"]}" stroke="{t["accent"]}" stroke-opacity=".35"/>'
                     f'<text x="{x + w / 2:.0f}" y="250" text-anchor="middle" font-size="17" font-weight="600" fill="{t["pilltext"]}">{label}</text>')
        x += w + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["bg1"]}"/><stop offset="1" stop-color="{t["bg2"]}"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["text"]}"/><stop offset="1" stop-color="{t["accent"]}"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t["grid"]}" stroke-opacity=".35" stroke-width="1"/>
    </pattern>
    <clipPath id="clip"><rect width="1200" height="320" rx="18"/></clipPath>
  </defs>
  <style>
    .in {{ animation: up .9s ease-out both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .35s; }} .d3 {{ animation-delay: .55s; }}
    @keyframes up {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}
  </style>
  <g clip-path="url(#clip)">
    <rect width="1200" height="320" fill="url(#bg)"/>
    <rect width="1200" height="320" fill="url(#grid)"/>
    {"".join(lines)}
    {"".join(packets)}
    {"".join(dots)}
  </g>
  <g class="in"><text x="60" y="78" font-size="18" font-weight="600" letter-spacing="3" fill="{t["accent2"]}">HI, I'M</text></g>
  <g class="in d1"><text x="58" y="140" font-size="64" font-weight="800" fill="url(#name)">Ahmed Morsy</text></g>
  <g class="in d2"><text x="60" y="184" font-size="26" font-weight="600" fill="{t["text"]}">DevOps &amp; Cloud Engineer
    <tspan fill="{t["muted"]}" font-weight="400"> · Co-Founder &amp; CTO @ MAHosting</tspan></text></g>
  <g class="in d3">{"".join(chips)}</g>
</svg>'''


TERM = [
    ("cmd", "whoami"),
    ("out", "Ahmed Morsy · DevOps & Cloud Engineer · Alexandria, Egypt"),
    ("cmd", "cat about.txt"),
    ("bul", "Co-founder & CTO of MAHosting: VPS, dedicated and game server hosting"),
    ("bul", "Own network on BGP with in-house XDP/eBPF DDoS filtering"),
    ("bul", "Proxmox + cloud-init provisioning, Docker game hosting at scale"),
    ("bul", "7+ years of code: PHP/Laravel, React/TS, C++, C#/.NET, Java, Unity"),
    ("bul", "Daily AI tooling: Claude Code, Codex, Cursor, MCP servers & agents"),
    ("cmd", "cat status.txt"),
    ("ok", "Open to DevOps, Cloud and Full-Stack roles · remote or on-site"),
]


def terminal(t):
    lh, top, rows = 30, 74, []
    for i, (kind, txt) in enumerate(TERM):
        y = top + i * lh
        delay = 0.3 + i * 0.35
        if kind == "cmd":
            body = (f'<tspan fill="{t["ok"]}" font-weight="700">ahmed@mahosting</tspan><tspan fill="{t["muted"]}">:</tspan>'
                    f'<tspan fill="{t["accent"]}" font-weight="700">~</tspan><tspan fill="{t["muted"]}">$ </tspan>'
                    f'<tspan fill="{t["text"]}">{escape(txt)}</tspan>')
        elif kind == "bul":
            body = f'<tspan fill="{t["accent2"]}">▸ </tspan><tspan fill="{t["text"]}">{escape(txt)}</tspan>'
        elif kind == "ok":
            body = f'<tspan fill="{t["ok"]}">● </tspan><tspan fill="{t["text"]}" font-weight="600">{escape(txt)}</tspan>'
        else:
            body = f'<tspan fill="{t["muted"]}">{escape(txt)}</tspan>'
        rows.append(f'<text class="ln" style="animation-delay:{delay:.2f}s" x="28" y="{y}">{body}</text>')
    h = top + len(TERM) * lh + 26
    cy = top + len(TERM) * lh - 22
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{h}" viewBox="0 0 1000 {h}" font-family="{MONO}" font-size="17">
  <style>
    .ln {{ animation: show .35s ease-out both; }}
    @keyframes show {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    .cur {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
  </style>
  <rect x="1" y="1" width="998" height="{h - 2}" rx="14" fill="{t["term"]}" stroke="{t["border"]}" stroke-width="1.5"/>
  <path d="M1 15a14 14 0 0 1 14-14h970a14 14 0 0 1 14 14v25H1z" fill="{t["termbar"]}"/>
  <circle cx="26" cy="21" r="6.5" fill="#ff5f57"/><circle cx="48" cy="21" r="6.5" fill="#febc2e"/><circle cx="70" cy="21" r="6.5" fill="#28c840"/>
  <text x="500" y="26" text-anchor="middle" font-size="14" fill="{t["muted"]}">ahmed@mahosting: ~</text>
  {"".join(rows)}
  <text x="28" y="{cy + 30}" fill="{t["ok"]}" font-weight="700">ahmed@mahosting<tspan fill="{t["muted"]}">:</tspan><tspan fill="{t["accent"]}">~</tspan><tspan fill="{t["muted"]}">$ </tspan></text>
  <rect class="cur" x="222" y="{cy + 14}" width="10" height="20" fill="{t["text"]}"/>
</svg>'''


CARDS = {
    "hardening": ("linux-server-hardening", "shield",
                  ["Lockout-safe, one-command hardening", "for Debian/Ubuntu servers."],
                  ["SSH", "nftables", "fail2ban", "Bash"]),
    "proxmox": ("proxmox-cloudinit-templates", "server",
                ["Checksum-verified Proxmox cloud-init", "templates for fast VPS provisioning."],
                ["Proxmox", "KVM", "cloud-init", "Bash"]),
    "docker": ("game-server-docker", "box",
               ["Non-root, resource-limited, health-", "checked game server containers."],
               ["Docker", "Compose", "Minecraft", "JVM"]),
    "certs": ("Certifications", "badge",
              ["Cisco CCNA & CCNP (2024) · Harvard CS50", "LabEx Learn DevOps · Adobe Certified"],
              ["Networking", "DevOps", "CS", "Design"]),
}


def icon(kind, t):
    a = t["accent"]
    if kind == "shield":
        return f'<path d="M26 6l16 6v10c0 10-7 17-16 20-9-3-16-10-16-20V12z" fill="none" stroke="{a}" stroke-width="3" stroke-linejoin="round"/><path d="M19 24l5 5 9-10" fill="none" stroke="{t["accent2"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == "server":
        return (f'<rect x="8" y="8" width="36" height="14" rx="3" fill="none" stroke="{a}" stroke-width="3"/>'
                f'<rect x="8" y="28" width="36" height="14" rx="3" fill="none" stroke="{a}" stroke-width="3"/>'
                f'<circle cx="16" cy="15" r="2.5" fill="{t["accent2"]}"/><circle cx="16" cy="35" r="2.5" fill="{t["accent2"]}"/>')
    if kind == "box":
        return (f'<path d="M26 6l18 9v20l-18 9-18-9V15z" fill="none" stroke="{a}" stroke-width="3" stroke-linejoin="round"/>'
                f'<path d="M8 15l18 9 18-9M26 24v20" fill="none" stroke="{t["accent2"]}" stroke-width="3" stroke-linejoin="round"/>')
    return (f'<circle cx="26" cy="20" r="12" fill="none" stroke="{a}" stroke-width="3"/>'
            f'<path d="M19 30l-4 14 11-6 11 6-4-14" fill="none" stroke="{t["accent2"]}" stroke-width="3" stroke-linejoin="round"/>')


def card(key, t):
    title, ic, desc, tags = CARDS[key]
    tx, pills = 28, []
    for tag in tags:
        w = 20 + len(tag) * 8.6
        pills.append(f'<rect x="{tx}" y="160" width="{w:.0f}" height="28" rx="14" fill="{t["pill"]}"/>'
                     f'<text x="{tx + w / 2:.0f}" y="179" text-anchor="middle" font-size="14" font-weight="600" fill="{t["pilltext"]}">{tag}</text>')
        tx += w + 8
    lines = "".join(f'<text x="28" y="{108 + i * 26}" font-size="17" fill="{t["muted"]}">{escape(l)}</text>' for i, l in enumerate(desc))
    arrow = "" if key == "certs" else f'<text x="452" y="52" text-anchor="end" font-size="22" fill="{t["muted"]}">↗</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="226" viewBox="0 0 480 226" font-family="{FONT}">
  <defs><linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["accent"]}"/><stop offset="1" stop-color="{t["accent2"]}"/></linearGradient>
    <clipPath id="c"><rect x="1" y="1" width="478" height="210" rx="16"/></clipPath></defs>
  <rect x="1" y="1" width="478" height="210" rx="16" fill="{t["card"]}"/>
  <rect x="0" y="0" width="480" height="5" fill="url(#edge)" clip-path="url(#c)"/>
  <rect x="1" y="1" width="478" height="210" rx="16" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>
  <g transform="translate(20,22) scale(.82)">{icon(ic, t)}</g>
  <text x="70" y="52" font-size="22" font-weight="700" fill="{t["text"]}">{escape(title)}</text>
  {arrow}
  {lines}
  {"".join(pills)}
</svg>'''


for name, t in THEMES.items():
    (OUT / f"header-{name}.svg").write_text(header(t), encoding="utf-8")
    (OUT / f"terminal-{name}.svg").write_text(terminal(t), encoding="utf-8")
    for key in CARDS:
        (OUT / f"card-{key}-{name}.svg").write_text(card(key, t), encoding="utf-8")
print("ok")
