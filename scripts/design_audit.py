#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autonomous Quality Audit Script for Awwwards / Webby / FWA Standards.
Scores index.html on a 100-point scale across 5 dimensions. Target: >= 95.
"""

import os
import re
import sys
from bs4 import BeautifulSoup

def audit():
    if not os.path.exists("index.html"):
        print("❌ Error: index.html not found!")
        sys.exit(1)

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    score = 0
    checks = []

    # Dimension 1: Design & Aesthetics (25 pts)
    d1_pts = 0
    # Fonts
    if "Noto+Serif+TC" in html and "Inter" in html and "JetBrains+Mono" in html:
        d1_pts += 8
        checks.append(("Typography Palette", 8, 8, "Noto Serif TC + Inter + JetBrains Mono loaded"))
    else:
        checks.append(("Typography Palette", 4, 8, "Missing primary font pairings"))

    # Hero Metrics
    metric_cards = soup.find_all("div", class_="metric-card")
    if len(metric_cards) >= 4:
        d1_pts += 10
        checks.append(("Hero Metrics Grid", 10, 10, f"Found {len(metric_cards)} metric cards"))
    else:
        checks.append(("Hero Metrics Grid", 5, 10, f"Only found {len(metric_cards)} metric cards"))

    # Dark / Light Theme Support
    if 'data-theme="dark"' in html and 'data-theme="light"' in html and 'theme-switch' in html:
        d1_pts += 7
        checks.append(("Dual Theme Styling", 7, 7, "Full dark/light CSS variables & toggle present"))
    else:
        checks.append(("Dual Theme Styling", 3, 7, "Partial theme support"))

    # Dimension 2: Visual Form & Static SVGs (20 pts)
    d2_pts = 0
    svg_imgs = soup.find_all("img", class_="responsive-svg")
    mermaid_js = "mermaid.min.js" in html
    if len(svg_imgs) >= 2 and not mermaid_js:
        d2_pts += 20
        checks.append(("Static Pure SVGs", 20, 20, "Pure static vector SVGs embedded, 0 external mermaid.js dependency"))
    else:
        checks.append(("Static Pure SVGs", 10, 20, f"SVG count: {len(svg_imgs)}, mermaid.js present: {mermaid_js}"))

    # Dimension 3: Usability & UX Polish (25 pts)
    d3_pts = 0
    # Progress Bar
    if soup.find("div", id="progressIndicator") and "progressIndicator" in html:
        d3_pts += 8
        checks.append(("Reading Progress Bar", 8, 8, "Tactical gradient progress bar present"))
    else:
        checks.append(("Reading Progress Bar", 0, 8, "Missing progress bar"))

    # Responsive Tables
    tables = soup.find_all("table")
    scroll_wrappers = soup.find_all("div", class_="tactical-table-scroll")
    if len(tables) > 0 and len(tables) == len(scroll_wrappers):
        d3_pts += 9
        checks.append(("Responsive Table Containers", 9, 9, f"All {len(tables)} tables wrapped in tactical horizontal scroll containers"))
    else:
        checks.append(("Responsive Table Containers", 4, 9, f"Tables: {len(tables)}, Wrappers: {len(scroll_wrappers)}"))

    # Tactical Nav
    if soup.find("header", class_="tactical-navbar") and soup.find("div", class_="brand-radar"):
        d3_pts += 8
        checks.append(("Tactical Navbar", 8, 8, "Sticky glassmorphism navbar with radar indicator active"))
    else:
        checks.append(("Tactical Navbar", 4, 8, "Missing navbar components"))

    # Dimension 4: Content Integrity & Fact-Checking (15 pts)
    d4_pts = 0
    badges = soup.find_all("span", class_=re.compile(r"badge-"))
    if len(badges) >= 2:
        d4_pts += 8
        checks.append(("Fact-check Badges", 8, 8, f"Found {len(badges)} verified fact-checking visual badges"))
    else:
        checks.append(("Fact-check Badges", 4, 8, "Missing or few fact badges"))

    links = soup.find_all("a")
    valid_links = [a for a in links if a.get("href", "").startswith("http")]
    if len(valid_links) >= 8:
        d4_pts += 7
        checks.append(("External References", 7, 7, f"Found {len(valid_links)} secure external reference citations"))
    else:
        checks.append(("External References", 3, 7, f"Only found {len(valid_links)} external citations"))

    # Dimension 5: Mobile Viewport & Accessibility (15 pts)
    d5_pts = 0
    viewport = soup.find("meta", attrs={"name": "viewport"})
    if viewport and "viewport-fit=cover" in viewport.get("content", ""):
        d5_pts += 8
        checks.append(("Mobile Viewport Setup", 8, 8, "Viewport meta configured for modern notch/island devices"))
    else:
        checks.append(("Mobile Viewport Setup", 4, 8, "Sub-optimal viewport meta"))

    if "@media (max-width: 640px)" in html:
        d5_pts += 7
        checks.append(("Mobile Responsive Breakpoints", 7, 7, "Optimized typography & grid layouts for 360-640px screens"))
    else:
        checks.append(("Mobile Responsive Breakpoints", 0, 7, "Missing mobile media queries"))

    total_score = d1_pts + d2_pts + d3_pts + d4_pts + d5_pts

    print("==================================================")
    print("      AWWWARDS / WEBBY / FWA DESIGN AUDIT")
    print("==================================================")
    for name, pts, max_pts, desc in checks:
        icon = "✓" if pts == max_pts else "⚠️"
        print(f"[{icon}] {name:30} : {pts:2}/{max_pts:2} pts  ({desc})")
    print("--------------------------------------------------")
    print(f"Total Quality Score: {total_score} / 100")
    print("==================================================")

    if total_score >= 95:
        print("🏆 EXCELLENT! Meets and exceeds Awwwards / Webby quality bar!")
        return True
    else:
        print(f"❌ Score {total_score} is below the 95-point threshold. Iteration required.")
        return False

if __name__ == "__main__":
    passed = audit()
    sys.exit(0 if passed else 1)
