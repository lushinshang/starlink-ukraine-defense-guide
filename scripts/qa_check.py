#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA validation script for index.html
"""

import re
import sys
from bs4 import BeautifulSoup

def qa():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    warnings = []

    soup = BeautifulSoup(html, "html.parser")

    # 1. Check title & meta
    if not soup.title or len(soup.title.text.strip()) == 0:
        errors.append("Missing <title>")
    else:
        print(f"✓ Title: {soup.title.text[:40]}...")

    viewport = soup.find("meta", attrs={"name": "viewport"})
    if not viewport:
        errors.append("Missing viewport meta tag")
    else:
        print("✓ Viewport configured correctly for mobile devices")

    # 2. Check headings hierarchy
    h1 = soup.find_all("h1")
    if len(h1) != 1:
        warnings.append(f"Expected 1 h1 tag, found {len(h1)}")
    else:
        print(f"✓ Single H1: {h1[0].text[:40]}...")

    h2 = soup.find_all("h2")
    print(f"✓ H2 count: {len(h2)}")

    # 3. Check Mermaid diagrams
    mermaid_blocks = soup.find_all("pre", class_="mermaid")
    if len(mermaid_blocks) < 2:
        warnings.append(f"Expected at least 2 Mermaid diagrams, found {len(mermaid_blocks)}")
    else:
        print(f"✓ Mermaid diagrams: {len(mermaid_blocks)} blocks present")
        for idx, mb in enumerate(mermaid_blocks):
            txt = mb.text.strip()
            if not txt.startswith("flowchart") and not txt.startswith("graph"):
                errors.append(f"Mermaid #{idx} does not start with flowchart/graph")
            else:
                print(f"  - Diagram #{idx+1} valid flowchart header: {txt.splitlines()[0]}")

    # 4. Check Tables and Containers
    tables = soup.find_all("table")
    print(f"✓ Tables count: {len(tables)}")
    table_containers = soup.find_all("div", class_="table-container")
    if len(tables) != len(table_containers):
        warnings.append(f"Mismatch: {len(tables)} tables but {len(table_containers)} .table-container")
    else:
        print("✓ All tables properly wrapped in responsive .table-container")

    # 5. Check Links
    links = soup.find_all("a")
    print(f"✓ Total links: {len(links)}")
    for a in links:
        href = a.get("href", "")
        if not href or href == "#":
            warnings.append(f"Empty or placeholder href in link: {a.text}")

    # 6. Check Badges
    badges = soup.find_all("span", class_=re.compile(r"badge"))
    print(f"✓ Fact-check badges count: {len(badges)}")

    # 7. Check AI Disclosure
    disclosure = soup.find("aside", class_="ai-disclosure")
    if not disclosure:
        errors.append("Missing .ai-disclosure element")
    else:
        print("✓ AI disclosure banner present")

    print("\n--- QA Results ---")
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  ❌ {err}")
        sys.exit(1)
    else:
        print("🎉 ALL CRITICAL CHECKS PASSED!")

    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠️ {w}")
    else:
        print("No warnings.")

if __name__ == "__main__":
    qa()
