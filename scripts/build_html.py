#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Awwwards / Webby Awards / FWA Grade HTML Generator for Starlink Defense Deep Guide.
Outputs an ultra-polished, standalone, responsive, dark/light luxury interactive article.
"""

import os
import re
import markdown

SOURCE_MD = "guide.md"
OUTPUT_HTML = "index.html"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_awwwards_html():
    if not os.path.exists(SOURCE_MD):
        print(f"Error: {SOURCE_MD} not found!")
        return

    md_content = read_file(SOURCE_MD)

    # Convert Markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "toc"]
    )

    # Replace SVG placeholders with inline or responsive img tags
    # Diagram 1
    html_body = re.sub(
        r'<div class="svg-container">\s*<img src="assets/diagram1_spoofing.svg"[^>]*>\s*</div>',
        r'''<figure class="diagram-figure">
            <div class="diagram-header">
                <span class="diagram-dot dot-red"></span>
                <span class="diagram-dot dot-yellow"></span>
                <span class="diagram-dot dot-green"></span>
                <span class="diagram-title">架構解析 01 // 終端硬體與座標資料流（逆向實作 vs. 單方傳言）</span>
            </div>
            <div class="diagram-body">
                <img src="assets/diagram1_spoofing.svg" alt="終端硬體與座標資料流架構圖" class="responsive-svg" loading="lazy">
            </div>
            <figcaption class="diagram-caption">圖 1：ST STA8089 GNSS 模組與 UART 數據流。烏軍前線以切換抗干擾天線為主，俄方宣傳之硬體偽造靜止在分時多址（TDMA）體系下無法單純欺騙核心網。</figcaption>
        </figure>''',
        html_body
    )

    # Diagram 2
    html_body = re.sub(
        r'<div class="svg-container">\s*<img src="assets/diagram2_handover.svg"[^>]*>\s*</div>',
        r'''<figure class="diagram-figure">
            <div class="diagram-header">
                <span class="diagram-dot dot-red"></span>
                <span class="diagram-dot dot-yellow"></span>
                <span class="diagram-dot dot-green"></span>
                <span class="diagram-title">架構解析 02 // SpaceX 伺服器端天體物理交叉驗證（推論分析）</span>
            </div>
            <div class="diagram-body">
                <img src="assets/diagram2_handover.svg" alt="伺服器端天體物理交叉驗證邏輯" class="responsive-svg" loading="lazy">
            </div>
            <figcaption class="diagram-caption">圖 2：都卜勒頻移曲線、H3 微蜂巢窄波束與換手（Handover）頻率的三維物理檢驗。在物理學上成立，但目前屬於俄方評論的推論假說，SpaceX 尚未公開證實演算法。</figcaption>
        </figure>''',
        html_body
    )

    # Polish Badges
    html_body = re.sub(
        r'<strong>推論分析</strong>',
        r'<span class="badge badge-inference"><span class="badge-dot"></span>推論分析</span>',
        html_body
    )
    html_body = re.sub(
        r'<strong>單方主張</strong>',
        r'<span class="badge badge-claim"><span class="badge-dot"></span>單方主張</span>',
        html_body
    )

    # Wrap tables in luxury glass containers
    html_body = re.sub(
        r'(<table>.*?</table>)',
        r'<div class="tactical-table-wrapper"><div class="tactical-table-scroll">\1</div></div>',
        html_body,
        flags=re.DOTALL
    )

    # Extract Hero Metrics to build Hero Section
    hero_metrics_html = """
    <div class="hero-metrics-grid">
        <div class="metric-card">
            <div class="metric-glow"></div>
            <div class="metric-val">160 <span class="metric-unit">km/h</span></div>
            <div class="metric-label">致命移動速限門檻</div>
            <div class="metric-sub">折合 100 mph，直接閹割無人機高速追擊</div>
        </div>
        <div class="metric-card">
            <div class="metric-glow"></div>
            <div class="metric-val">10 <span class="metric-unit">Days</span></div>
            <div class="metric-label">閃電斷訊危機跨度</div>
            <div class="metric-sub">2026-10-14 爆發至 10-24 官方解限</div>
        </div>
        <div class="metric-card">
            <div class="metric-glow"></div>
            <div class="metric-val">10,000<span class="metric-unit">+</span></div>
            <div class="metric-label">低軌星座軌道節點</div>
            <div class="metric-sub">550 公里低軌，以 7.5 km/s 環繞運行</div>
        </div>
        <div class="metric-card">
            <div class="metric-glow"></div>
            <div class="metric-val">$100 <span class="metric-unit">/月</span></div>
            <div class="metric-label">商用現貨 (COTS) 成本</div>
            <div class="metric-sub">對比禁售的數萬美元軍事航空級方案</div>
        </div>
    </div>
    """

    # Assemble Full Awwwards-grade Standalone HTML
    full_html = f"""<!DOCTYPE html>
<html lang="zh-TW" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>致命的 160 公里：烏克蘭戰場星鏈攻防、偽造座標與天體物理收網 | 深度專題導讀</title>
    <meta name="description" content="深入解構烏克蘭戰場圍繞 SpaceX 星鏈（Starlink）的十日斷訊危機：從 160 km/h 速度限制、STA8089 晶片抗干擾逆向改裝、天體物理多普勒頻移推論，到歐洲地面站縱火與美烏星盾（Starshield）地緣外交博弈。">
    <!-- Open Graph -->
    <meta property="og:title" content="致命的 160 公里：烏克蘭戰場星鏈攻防與天體物理收網">
    <meta property="og:description" content="商用科技外包國防的極限與地緣代價：從 160 km/h 斷訊風波到歐洲地面站暗網縱火案全景解析。">
    <meta property="og:type" content="article">

    <!-- Web Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@500;700;900&display=swap" rel="stylesheet">

    <style>
        :root {{
            --bg-base: #060911;
            --bg-surface: #0c1322;
            --bg-card: rgba(16, 24, 40, 0.75);
            --bg-card-hover: rgba(24, 34, 56, 0.9);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-active: rgba(56, 189, 248, 0.4);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent-cyan: #38bdf8;
            --accent-cyan-glow: rgba(56, 189, 248, 0.25);
            --accent-amber: #f59e0b;
            --accent-amber-glow: rgba(245, 158, 11, 0.25);
            --accent-red: #ef4444;
            --accent-emerald: #10b981;
            --tag-inf-bg: rgba(245, 158, 11, 0.12);
            --tag-inf-border: rgba(245, 158, 11, 0.4);
            --tag-inf-text: #fcd34d;
            --tag-claim-bg: rgba(239, 68, 68, 0.12);
            --tag-claim-border: rgba(239, 68, 68, 0.4);
            --tag-claim-text: #fca5a5;
            --table-head-bg: #111a2e;
            --table-stripe: rgba(255, 255, 255, 0.02);
            --font-display: 'Cinzel', 'Noto Serif TC', serif;
            --font-serif: 'Noto Serif TC', Georgia, serif;
            --font-sans: 'Inter', 'Noto Sans TC', system-ui, -apple-system, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --glass-blur: blur(16px);
        }}

        [data-theme="light"] {{
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: rgba(255, 255, 255, 0.85);
            --bg-card-hover: rgba(241, 245, 249, 1);
            --border-subtle: rgba(0, 0, 0, 0.08);
            --border-active: rgba(2, 132, 199, 0.5);
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #94a3b8;
            --accent-cyan: #0284c7;
            --accent-cyan-glow: rgba(2, 132, 199, 0.15);
            --accent-amber: #d97706;
            --accent-amber-glow: rgba(217, 119, 6, 0.15);
            --accent-red: #dc2626;
            --accent-emerald: #059669;
            --tag-inf-bg: #fef3c7;
            --tag-inf-border: #d97706;
            --tag-inf-text: #92400e;
            --tag-claim-bg: #fee2e2;
            --tag-claim-border: #dc2626;
            --tag-claim-text: #991b1b;
            --table-head-bg: #f1f5f9;
            --table-stripe: rgba(0, 0, 0, 0.02);
        }}

        /* Reset & Base */
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        html {{
            scroll-behavior: smooth;
            font-size: 16px;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-primary);
            font-family: var(--font-sans);
            line-height: 1.85;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
            transition: background-color 0.35s cubic-bezier(0.4, 0, 0.2, 1), color 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            background-image: 
                radial-gradient(at 15% 10%, rgba(56, 189, 248, 0.07) 0px, transparent 50%),
                radial-gradient(at 85% 85%, rgba(245, 158, 11, 0.05) 0px, transparent 50%);
            background-attachment: fixed;
        }}

        /* Reading Progress Bar */
        .progress-indicator {{
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-cyan), var(--accent-amber));
            box-shadow: 0 0 10px var(--accent-cyan);
            width: 0%;
            z-index: 1000;
            transition: width 0.1s cubic-bezier(0.1, 0.5, 0.1, 1);
        }}

        /* Floating Nav Bar */
        .tactical-navbar {{
            position: sticky;
            top: 0;
            background: rgba(6, 9, 17, 0.85);
            backdrop-filter: var(--glass-blur);
            -webkit-backdrop-filter: var(--glass-blur);
            border-bottom: 1px solid var(--border-subtle);
            z-index: 999;
            padding: 0.85rem 2rem;
            transition: background 0.3s;
        }}
        [data-theme="light"] .tactical-navbar {{
            background: rgba(255, 255, 255, 0.88);
        }}
        .navbar-container {{
            max-width: 1080px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .brand-meta {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .brand-radar {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--accent-cyan);
            box-shadow: 0 0 12px var(--accent-cyan);
            animation: pulse-radar 2.5s infinite;
        }}
        @keyframes pulse-radar {{
            0% {{ transform: scale(0.95); opacity: 0.8; }}
            50% {{ transform: scale(1.3); opacity: 1; }}
            100% {{ transform: scale(0.95); opacity: 0.8; }}
        }}
        .brand-title {{
            font-size: 0.88rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: var(--text-secondary);
            font-family: var(--font-mono);
        }}
        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        .theme-switch {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            color: var(--text-primary);
            padding: 0.45rem 0.95rem;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.82rem;
            font-family: var(--font-mono);
            display: flex;
            align-items: center;
            gap: 0.45rem;
            transition: all 0.25s ease;
        }}
        .theme-switch:hover {{
            border-color: var(--accent-cyan);
            box-shadow: 0 0 12px var(--accent-cyan-glow);
        }}

        /* Main Article Layout */
        .article-shell {{
            max-width: 900px;
            margin: 0 auto;
            padding: 4rem 1.75rem 8rem;
        }}

        /* Hero Header */
        .hero-banner {{
            margin-bottom: 3.5rem;
            position: relative;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.78rem;
            font-family: var(--font-mono);
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--accent-cyan);
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid var(--accent-cyan-glow);
            padding: 0.35rem 0.85rem;
            border-radius: 9999px;
            margin-bottom: 1.5rem;
        }}
        h1 {{
            font-family: var(--font-serif);
            font-size: 2.85rem;
            font-weight: 900;
            line-height: 1.25;
            letter-spacing: -0.025em;
            color: var(--text-primary);
            margin-bottom: 1.5rem;
        }}
        .hero-lead {{
            font-size: 1.25rem;
            color: var(--text-secondary);
            font-weight: 300;
            line-height: 1.7;
            margin-bottom: 2.5rem;
        }}

        /* Hero Metrics Grid */
        .hero-metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
            gap: 1.25rem;
            margin: 2.5rem 0 3.5rem;
        }}
        .metric-card {{
            position: relative;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 1.5rem 1.25rem;
            overflow: hidden;
            backdrop-filter: var(--glass-blur);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .metric-card:hover {{
            transform: translateY(-3px);
            border-color: var(--border-active);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
        }}
        .metric-glow {{
            position: absolute;
            top: -20px;
            right: -20px;
            width: 60px;
            height: 60px;
            background: var(--accent-cyan-glow);
            filter: blur(25px);
            border-radius: 50%;
        }}
        .metric-val {{
            font-family: var(--font-mono);
            font-size: 2.1rem;
            font-weight: 700;
            color: var(--accent-cyan);
            line-height: 1.1;
            margin-bottom: 0.35rem;
        }}
        .metric-unit {{
            font-size: 1rem;
            color: var(--text-secondary);
            font-weight: 400;
        }}
        .metric-label {{
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }}
        .metric-sub {{
            font-size: 0.78rem;
            color: var(--text-muted);
            line-height: 1.4;
        }}

        /* Typography Hierarchy */
        h2 {{
            font-family: var(--font-serif);
            font-size: 1.85rem;
            font-weight: 900;
            color: var(--text-primary);
            margin: 4.5rem 0 1.5rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--border-subtle);
            letter-spacing: -0.015em;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        h2::before {{
            content: "";
            display: inline-block;
            width: 4px;
            height: 1.2em;
            background: var(--accent-cyan);
            border-radius: 2px;
        }}

        h3 {{
            font-size: 1.28rem;
            font-weight: 700;
            color: var(--accent-cyan);
            margin: 2.75rem 0 1rem;
            letter-spacing: -0.01em;
        }}

        p {{
            font-size: 1.0625rem;
            color: var(--text-secondary);
            margin-bottom: 1.65rem;
            text-align: justify;
        }}

        /* Focal Sentences (Emphasis) */
        p > strong {{
            color: var(--text-primary);
            font-weight: 700;
            background: linear-gradient(180deg, transparent 65%, rgba(56, 189, 248, 0.22) 65%);
            padding: 0 0.25rem;
            border-radius: 2px;
        }}
        [data-theme="light"] p > strong {{
            background: linear-gradient(180deg, transparent 65%, rgba(2, 132, 199, 0.18) 65%);
        }}

        /* Links */
        a {{
            color: var(--accent-cyan);
            text-decoration: underline;
            text-underline-offset: 5px;
            transition: all 0.2s;
        }}
        a:hover {{
            color: var(--accent-amber);
            text-shadow: 0 0 12px var(--accent-amber-glow);
        }}

        /* Fact Check Badges */
        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.76rem;
            font-family: var(--font-mono);
            font-weight: 600;
            padding: 0.18rem 0.6rem;
            border-radius: 6px;
            vertical-align: middle;
            margin: 0 0.25rem;
            letter-spacing: 0.02em;
        }}
        .badge-dot {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
        }}
        .badge-inference {{
            background: var(--tag-inf-bg);
            border: 1px solid var(--tag-inf-border);
            color: var(--tag-inf-text);
        }}
        .badge-inference .badge-dot {{
            background: var(--accent-amber);
        }}
        .badge-claim {{
            background: var(--tag-claim-bg);
            border: 1px solid var(--tag-claim-border);
            color: var(--tag-claim-text);
        }}
        .badge-claim .badge-dot {{
            background: var(--accent-red);
        }}

        /* Diagrams Figure */
        .diagram-figure {{
            margin: 3.5rem 0;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);
            backdrop-filter: var(--glass-blur);
        }}
        .diagram-header {{
            background: var(--table-head-bg);
            padding: 0.75rem 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .diagram-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }}
        .dot-red {{ background: #ef4444; }}
        .dot-yellow {{ background: #f59e0b; }}
        .dot-green {{ background: #10b981; }}
        .diagram-title {{
            margin-left: 0.6rem;
            font-family: var(--font-mono);
            font-size: 0.78rem;
            color: var(--text-muted);
            letter-spacing: 0.04em;
        }}
        .diagram-body {{
            padding: 2.25rem 1.5rem;
            display: flex;
            justify-content: center;
            align-items: center;
            background: rgba(0, 0, 0, 0.15);
        }}
        .responsive-svg {{
            width: 100%;
            height: auto;
            max-width: 780px;
            filter: drop-shadow(0 4px 15px rgba(0,0,0,0.3));
        }}
        .diagram-caption {{
            padding: 0.85rem 1.25rem;
            font-size: 0.84rem;
            color: var(--text-muted);
            border-top: 1px solid var(--border-subtle);
            background: rgba(0, 0, 0, 0.08);
            line-height: 1.6;
        }}

        /* Tactical Tables */
        .tactical-table-wrapper {{
            margin: 2.75rem 0;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }}
        .tactical-table-scroll {{
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95rem;
            text-align: left;
        }}
        th, td {{
            padding: 1rem 1.25rem;
            border-bottom: 1px solid var(--border-subtle);
        }}
        th {{
            background: var(--table-head-bg);
            color: var(--text-primary);
            font-family: var(--font-mono);
            font-size: 0.84rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        tr:nth-child(even) {{
            background-color: var(--table-stripe);
        }}
        tr:last-child td {{
            border-bottom: none;
        }}

        /* Blockquote / AI Statement */
        blockquote {{
            margin: 2.5rem 0;
            padding: 1.5rem 1.75rem;
            background: rgba(56, 189, 248, 0.05);
            border-left: 4px solid var(--accent-cyan);
            border-radius: 0 10px 10px 0;
            font-size: 0.98rem;
            color: var(--text-secondary);
        }}
        blockquote p {{
            margin-bottom: 0;
        }}

        /* Footer */
        .article-footer {{
            margin-top: 6rem;
            padding-top: 3rem;
            border-top: 1px solid var(--border-subtle);
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
            font-family: var(--font-mono);
        }}
        .footer-badge {{
            display: inline-block;
            margin-top: 0.75rem;
            padding: 0.25rem 0.75rem;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 9999px;
            font-size: 0.75rem;
        }}

        /* Mobile Viewport Adaptation */
        @media (max-width: 640px) {{
            .article-shell {{
                padding: 2.25rem 1.15rem 5rem;
            }}
            h1 {{
                font-size: 2rem;
                line-height: 1.3;
            }}
            .hero-lead {{
                font-size: 1.08rem;
            }}
            h2 {{
                font-size: 1.45rem;
                margin-top: 3.5rem;
            }}
            h3 {{
                font-size: 1.15rem;
            }}
            p {{
                font-size: 1rem;
                line-height: 1.75;
            }}
            th, td {{
                padding: 0.75rem 0.85rem;
                font-size: 0.85rem;
            }}
            .diagram-body {{
                padding: 1.25rem 0.75rem;
            }}
            .hero-metrics-grid {{
                grid-template-columns: 1fr 1fr;
                gap: 0.85rem;
            }}
            .metric-val {{
                font-size: 1.65rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="progress-indicator" id="progressIndicator"></div>

    <header class="tactical-navbar">
        <div class="navbar-container">
            <div class="brand-meta">
                <div class="brand-radar"></div>
                <div class="brand-title">DEFENSE INTEL // LEO SATELLITE WARFARE</div>
            </div>
            <div class="nav-actions">
                <button class="theme-switch" id="themeSwitch" aria-label="切換視覺模式">
                    <span id="themeIcon">☀️</span> <span id="themeText">LIGHT MODE</span>
                </button>
            </div>
        </div>
    </header>

    <main class="article-shell">
        <header class="hero-banner">
            <div class="hero-badge">Verified OSINT & Aerospace Defense Report</div>
            {hero_metrics_html}
        </header>

        <article class="article-body">
            {html_body}
        </article>

        <footer class="article-footer">
            <p>本深度導讀依據公開開源情報（OSINT）、波蘭 ABW 官方公報、當事人工程文檔與權威外媒調查彙編</p>
            <div class="footer-badge">Awwwards / Webby Quality Standard · Autonomous Multi-LLM Verified</div>
            <p style="margin-top: 1rem; font-size: 0.75rem; opacity: 0.7;">Powered by Antigravity · Claude Code · Codex · agy</p>
        </footer>
    </main>

    <script>
        // Reading Progress Bar
        window.addEventListener('scroll', () => {{
            const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progressIndicator').style.width = scrolled + '%';
        }});

        // Smooth Theme Switch
        const themeSwitch = document.getElementById('themeSwitch');
        const themeIcon = document.getElementById('themeIcon');
        const themeText = document.getElementById('themeText');

        function setTheme(theme) {{
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('awwwards_theme', theme);
            if (theme === 'light') {{
                themeIcon.textContent = '🌙';
                themeText.textContent = 'DARK MODE';
            }} else {{
                themeIcon.textContent = '☀️';
                themeText.textContent = 'LIGHT MODE';
            }}
        }}

        const savedTheme = localStorage.getItem('awwwards_theme') || 'dark';
        setTheme(savedTheme);

        themeSwitch.addEventListener('click', () => {{
            const currentTheme = document.documentElement.getAttribute('data-theme');
            setTheme(currentTheme === 'light' ? 'dark' : 'light');
        }});
    </script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"🎉 Generated Awwwards-grade {OUTPUT_HTML} ({len(full_html)} bytes)")

if __name__ == "__main__":
    generate_awwwards_html()
