# -*- coding: utf-8 -*-
"""
Generate Lab 3 PDF Report for Food Corner Website
"""
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors

# ── Paths ──
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACT_DIR = r"C:\Users\PMLS\.gemini\antigravity\brain\4607a850-c170-425b-86c6-99022c7159eb"
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "Lab3_CSS_Report_Muhammad_Junaid.pdf")

HERO_IMG = os.path.join(ARTIFACT_DIR, "hero_section_1790832354072.jpg")
MENU_IMG = os.path.join(ARTIFACT_DIR, "menu_section_1790832378999.jpg")
ABOUT_IMG = os.path.join(ARTIFACT_DIR, "about_contact_footer_1790832406181.jpg")

# ── Colors ──
ORANGE = HexColor("#e67e22")
DARK = HexColor("#2c2c2c")
CREAM = HexColor("#faf3e0")
LIGHT_GRAY = HexColor("#f5f5f5")
CODE_BG = HexColor("#f8f8f8")

# ── Build Document ──
doc = SimpleDocTemplate(
    OUTPUT_PDF,
    pagesize=A4,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='CoverTitle',
    fontSize=28,
    leading=34,
    alignment=TA_CENTER,
    textColor=DARK,
    fontName='Helvetica-Bold',
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name='CoverSubtitle',
    fontSize=16,
    leading=22,
    alignment=TA_CENTER,
    textColor=ORANGE,
    fontName='Helvetica',
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name='CoverInfo',
    fontSize=13,
    leading=20,
    alignment=TA_CENTER,
    textColor=DARK,
    fontName='Helvetica',
    spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='SectionHeading',
    fontSize=18,
    leading=24,
    textColor=DARK,
    fontName='Helvetica-Bold',
    spaceBefore=20,
    spaceAfter=10,
    borderWidth=0,
    borderPadding=0,
))
styles.add(ParagraphStyle(
    name='SubHeading',
    fontSize=13,
    leading=18,
    textColor=ORANGE,
    fontName='Helvetica-Bold',
    spaceBefore=14,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name='BodyText2',
    fontSize=11,
    leading=16,
    alignment=TA_JUSTIFY,
    textColor=DARK,
    fontName='Helvetica',
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name='CodeBlock',
    fontSize=8.5,
    leading=12,
    fontName='Courier',
    textColor=DARK,
    backColor=LIGHT_GRAY,
    borderWidth=0.5,
    borderColor=HexColor("#dddddd"),
    borderPadding=8,
    spaceAfter=10,
    leftIndent=10,
    rightIndent=10,
))
styles.add(ParagraphStyle(
    name='Caption',
    fontSize=9,
    leading=13,
    alignment=TA_CENTER,
    textColor=gray,
    fontName='Helvetica-Oblique',
    spaceAfter=16,
    spaceBefore=4,
))
styles.add(ParagraphStyle(
    name='CheckItem',
    fontSize=10,
    leading=15,
    textColor=DARK,
    fontName='Helvetica',
    spaceAfter=2,
    leftIndent=20,
    bulletIndent=10,
))

story = []
page_width = A4[0] - 1.5*inch  # usable width

# ══════════════════════════════════════════════
# TITLE PAGE
# ══════════════════════════════════════════════
story.append(Spacer(1, 1.5*inch))

# University name
story.append(Paragraph("COMSATS University Islamabad", styles['CoverSubtitle']))
story.append(Paragraph("Wah Campus", styles['CoverInfo']))
story.append(Spacer(1, 0.3*inch))

# Orange line
story.append(HRFlowable(width="60%", thickness=3, color=ORANGE, spaceAfter=20, spaceBefore=10))

# Title
story.append(Paragraph("Web Technologies", styles['CoverTitle']))
story.append(Paragraph("Lab 3: CSS — Integrated Website Development", styles['CoverSubtitle']))
story.append(Spacer(1, 0.5*inch))

# Project name
story.append(Paragraph('<font color="#e67e22"><b>Project:</b></font> Food Corner Restaurant Website', styles['CoverInfo']))
story.append(Spacer(1, 0.6*inch))

# Student info
story.append(HRFlowable(width="50%", thickness=1, color=HexColor("#cccccc"), spaceAfter=15, spaceBefore=5))
story.append(Paragraph("<b>Name:</b> Muhammad Junaid", styles['CoverInfo']))
story.append(Paragraph("<b>Registration No:</b> FA24-BCS-167", styles['CoverInfo']))
story.append(Spacer(1, 0.4*inch))

# Date
story.append(Paragraph("<b>Date:</b> October 01, 2026", styles['CoverInfo']))
story.append(Spacer(1, 0.3*inch))
story.append(HRFlowable(width="50%", thickness=1, color=HexColor("#cccccc"), spaceAfter=15, spaceBefore=5))

# Live link
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(
    '<font color="#e67e22"><b>Live Demo:</b></font> '
    '<font color="#2980b9"><u><a href="https://food-corner-website-gilt.vercel.app">https://food-corner-website-gilt.vercel.app</a></u></font>',
    styles['CoverInfo']
))
story.append(Paragraph(
    '<font color="#e67e22"><b>GitHub:</b></font> '
    '<font color="#2980b9"><u><a href="https://github.com/junaid-devv/food-corner-website">https://github.com/junaid-devv/food-corner-website</a></u></font>',
    styles['CoverInfo']
))

story.append(PageBreak())

# ══════════════════════════════════════════════
# TABLE OF CONTENTS
# ══════════════════════════════════════════════
story.append(Paragraph("Table of Contents", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=15))

toc_items = [
    ("1.", "Introduction"),
    ("2.", "File Structure"),
    ("3.", "Website Screenshots"),
    ("4.", "CSS Types Demonstration"),
    ("5.", "CSS Selectors"),
    ("6.", "Pseudo-Classes & Pseudo-Elements"),
    ("7.", "Cascade, Specificity & Inheritance"),
    ("8.", "Fonts, Text, Colors & Backgrounds"),
    ("9.", "CSS Box Model"),
    ("10.", "Margin Collapsing"),
    ("11.", "Width, Height & Constraints"),
    ("12.", "Overflow Demonstration"),
    ("13.", "Display Properties"),
    ("14.", "Borders, Shadows & Spacing"),
    ("15.", "Requirements Checklist"),
    ("16.", "Live Deployment"),
]

for num, title in toc_items:
    story.append(Paragraph(
        f'<font face="Helvetica-Bold" color="#e67e22">{num}</font>  '
        f'<font face="Helvetica" color="#2c2c2c">{title}</font>',
        ParagraphStyle('TOC', fontSize=12, leading=22, leftIndent=20)
    ))

story.append(PageBreak())

# ══════════════════════════════════════════════
# 1. INTRODUCTION
# ══════════════════════════════════════════════
story.append(Paragraph("1. Introduction", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "This report documents the development of a <b>Food Corner</b> restaurant website as part of "
    "Web Technologies Lab 3. The project demonstrates comprehensive CSS knowledge by building "
    "a professional single-page website using only HTML and CSS. The website showcases all CSS "
    "concepts covered in the lab, including CSS types, selectors, pseudo-classes, pseudo-elements, "
    "cascade, specificity, inheritance, the box model, margin collapsing, overflow, display "
    "properties, and responsive design techniques.",
    styles['BodyText2']
))
story.append(Paragraph(
    "The website features a hero section with a background food image overlay, a menu section "
    "with four food item cards, an about section describing the restaurant, a contact form, "
    "and a footer. The design uses a warm color palette with orange (#e67e22), dark charcoal "
    "(#2c2c2c), cream (#faf3e0), and soft gray (#f5f5f5) to create an inviting restaurant feel.",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 2. FILE STRUCTURE
# ══════════════════════════════════════════════
story.append(Paragraph("2. File Structure", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "FoodCorner/<br/>"
    "├── index.html &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Main HTML page — 197 lines)<br/>"
    "├── style.css &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(External stylesheet — 320+ lines)<br/>"
    "└── images/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Image assets directory)",
    styles['CodeBlock']
))
story.append(Paragraph(
    "The project follows a clean structure with HTML content separated from CSS styling. "
    "Food images are sourced from Unsplash via direct URLs for high-quality visuals.",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 3. SCREENSHOTS
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("3. Website Screenshots", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

story.append(Paragraph("<b>3.1 Hero / Welcome Section</b>", styles['SubHeading']))
story.append(Paragraph(
    "The hero section features a full-viewport background image with a dark overlay, "
    "the restaurant's welcome heading (styled with inline CSS), a subtitle paragraph, "
    "and an 'Explore Menu' call-to-action button. The fixed navigation bar sits at the top.",
    styles['BodyText2']
))
if os.path.exists(HERO_IMG):
    img = Image(HERO_IMG, width=page_width, height=page_width * 9/16)
    img.hAlign = 'CENTER'
    story.append(img)
    story.append(Paragraph("Figure 1: Hero Section — Welcome to Food Corner", styles['Caption']))

story.append(PageBreak())

story.append(Paragraph("<b>3.2 Menu Section</b>", styles['SubHeading']))
story.append(Paragraph(
    "The menu section displays four food cards (Pizza, Burger, Sandwich, Pasta) in a responsive "
    "CSS Grid layout. Each card includes a food image, name, description, price, and an 'Order Now' "
    "button. The first card is styled differently using the :first-child pseudo-class with "
    "an orange border accent. The section heading uses ::before and ::after pseudo-elements.",
    styles['BodyText2']
))
if os.path.exists(MENU_IMG):
    img = Image(MENU_IMG, width=page_width, height=page_width * 9/16)
    img.hAlign = 'CENTER'
    story.append(img)
    story.append(Paragraph("Figure 2: Menu Section — Four Signature Food Cards", styles['Caption']))

story.append(PageBreak())

story.append(Paragraph("<b>3.3 About, Contact & Footer Sections</b>", styles['SubHeading']))
story.append(Paragraph(
    "The about section contains a constrained content box demonstrating width/height constraints "
    "(min-width, max-width, min-height, max-height). It includes an overflow demo box showing "
    "scrollable testimonials. The contact section has a styled form with attribute selectors "
    "for input styling. The footer displays the copyright notice.",
    styles['BodyText2']
))
if os.path.exists(ABOUT_IMG):
    img = Image(ABOUT_IMG, width=page_width, height=page_width * 9/16)
    img.hAlign = 'CENTER'
    story.append(img)
    story.append(Paragraph("Figure 3: About Section, Contact Form & Footer", styles['Caption']))

# ══════════════════════════════════════════════
# 4. CSS TYPES
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("4. CSS Types Demonstration", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

story.append(Paragraph("<b>4.1 Inline CSS</b>", styles['SubHeading']))
story.append(Paragraph(
    "Applied directly on the hero section's &lt;h1&gt; element using the style attribute:",
    styles['BodyText2']
))
story.append(Paragraph(
    '&lt;h1 style="color: #faf3e0; font-size: 4rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);"&gt;<br/>'
    '&nbsp;&nbsp;Welcome to Food Corner<br/>'
    '&lt;/h1&gt;',
    styles['CodeBlock']
))

story.append(Paragraph("<b>4.2 Internal CSS</b>", styles['SubHeading']))
story.append(Paragraph(
    "A &lt;style&gt; block in the HTML &lt;head&gt; defines the hero section's background properties:",
    styles['BodyText2']
))
story.append(Paragraph(
    '&lt;style&gt;<br/>'
    '&nbsp;&nbsp;#home {<br/>'
    '&nbsp;&nbsp;&nbsp;&nbsp;background-image: linear-gradient(...), url(...);<br/>'
    '&nbsp;&nbsp;&nbsp;&nbsp;background-size: cover;<br/>'
    '&nbsp;&nbsp;&nbsp;&nbsp;background-position: center;<br/>'
    '&nbsp;&nbsp;&nbsp;&nbsp;height: 100vh;<br/>'
    '&nbsp;&nbsp;}<br/>'
    '&lt;/style&gt;',
    styles['CodeBlock']
))

story.append(Paragraph("<b>4.3 External CSS</b>", styles['SubHeading']))
story.append(Paragraph(
    "The main stylesheet is linked via: <b>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</b>. "
    "This file contains the majority of the styling rules (320+ lines).",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 5. CSS SELECTORS
# ══════════════════════════════════════════════
story.append(Paragraph("5. CSS Selectors", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

selectors = [
    ("Element Selector", "body { font-family: 'Poppins', sans-serif; color: #2c2c2c; }"),
    ("Class Selector", ".container { max-width: 1200px; margin: 0 auto; }"),
    ("ID Selector", "#menu { background-color: #f5f5f5; }"),
    ("Attribute Selector", 'input[type="text"], input[type="email"] { padding: 12px 15px; }'),
    ("Grouping Selector", "h1, h2, h3, h4 { margin-top: 0; color: #1a1a1a; }"),
    ("Descendant Selector", "nav ul { list-style: none; display: flex; gap: 30px; }"),
]

for name, code in selectors:
    story.append(Paragraph(f"<b>{name}:</b>", styles['SubHeading']))
    story.append(Paragraph(code, styles['CodeBlock']))

# ══════════════════════════════════════════════
# 6. PSEUDO-CLASSES & PSEUDO-ELEMENTS
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("6. Pseudo-Classes & Pseudo-Elements", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

story.append(Paragraph("<b>6.1 :hover Pseudo-Class</b>", styles['SubHeading']))
story.append(Paragraph(
    "Applied to navigation links and food cards for interactive hover effects:",
    styles['BodyText2']
))
story.append(Paragraph(
    "nav a:hover { color: #e67e22; }<br/>"
    ".food-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }",
    styles['CodeBlock']
))

story.append(Paragraph("<b>6.2 :first-child Pseudo-Class</b>", styles['SubHeading']))
story.append(Paragraph(
    "The first food card receives a distinct orange border and cream background:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".menu-grid .food-card:first-child {<br/>"
    "&nbsp;&nbsp;border: 2px solid #e67e22;<br/>"
    "&nbsp;&nbsp;background-color: #fff9f0;<br/>}",
    styles['CodeBlock']
))

story.append(Paragraph("<b>6.3 ::before and ::after Pseudo-Elements</b>", styles['SubHeading']))
story.append(Paragraph(
    "Decorative symbols are added around the Menu section heading:",
    styles['BodyText2']
))
story.append(Paragraph(
    '#menu h2::before { content: "🍽 "; color: #e67e22; }<br/>'
    '#menu h2::after  { content: " ★"; color: #e67e22; }',
    styles['CodeBlock']
))

# ══════════════════════════════════════════════
# 7. CASCADE, SPECIFICITY & INHERITANCE
# ══════════════════════════════════════════════
story.append(Paragraph("7. Cascade, Specificity & Inheritance", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

story.append(Paragraph("<b>7.1 Inheritance</b>", styles['SubHeading']))
story.append(Paragraph(
    "The body element sets a common font-family and text color that all child elements inherit:",
    styles['BodyText2']
))
story.append(Paragraph(
    "body { font-family: 'Poppins', sans-serif; color: #2c2c2c; }",
    styles['CodeBlock']
))
story.append(Paragraph(
    "Specific elements like headings override the inherited color: "
    "<b>h1, h2, h3, h4 { color: #1a1a1a; }</b>",
    styles['BodyText2']
))

story.append(Paragraph("<b>7.2 Specificity</b>", styles['SubHeading']))
story.append(Paragraph(
    "An ID selector (#specific-btn) overrides a class selector (.btn-override) because "
    "ID selectors have higher specificity than class selectors:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".btn-override { background-color: red; }    /* LOSES */<br/>"
    "#specific-btn { background-color: rgb(230, 126, 34); }  /* WINS — higher specificity */",
    styles['CodeBlock']
))

story.append(Paragraph("<b>7.3 Cascade (Source Order)</b>", styles['SubHeading']))
story.append(Paragraph(
    "When two rules have the same specificity, the rule that appears later in the source wins:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".cascade-demo { color: blue; }     /* LOSES — appears first */<br/>"
    ".cascade-demo { color: #7f8c8d; }  /* WINS  — appears later */",
    styles['CodeBlock']
))

# ══════════════════════════════════════════════
# 8. FONTS, TEXT, COLORS & BACKGROUNDS
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("8. Fonts, Text, Colors & Backgrounds", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

story.append(Paragraph("<b>8.1 Font Properties</b>", styles['SubHeading']))
story.append(Paragraph(
    "• <b>font-family:</b> 'Poppins', sans-serif (Google Font via @import)<br/>"
    "• <b>font-size:</b> Various sizes (16px base, 36px headings, 4rem hero)<br/>"
    "• <b>font-weight:</b> 300 (light), 400 (regular), 600 (semibold), 700 (bold)<br/>"
    "• <b>font-style:</b> italic (used on the inline-elem span)",
    styles['BodyText2']
))

story.append(Paragraph("<b>8.2 Text Properties</b>", styles['SubHeading']))
story.append(Paragraph(
    "• <b>text-align:</b> center (section titles, hero, footer)<br/>"
    "• <b>text-decoration:</b> none (links reset), underline (cascade demo)<br/>"
    "• <b>line-height:</b> 1.6 (body), custom per element",
    styles['BodyText2']
))

story.append(Paragraph("<b>8.3 Color Types</b>", styles['SubHeading']))
story.append(Paragraph(
    "• <b>Named color:</b> white (header background)<br/>"
    "• <b>HEX color:</b> #2c2c2c (body text), #e67e22 (orange accents)<br/>"
    "• <b>RGB color:</b> rgb(230, 126, 34) (specificity demo button)",
    styles['BodyText2']
))

story.append(Paragraph("<b>8.4 Background Properties</b>", styles['SubHeading']))
story.append(Paragraph(
    "• <b>background-image:</b> Hero section uses a gradient overlay on Unsplash photo<br/>"
    "• <b>background-size:</b> cover (hero fills entire viewport)<br/>"
    "• <b>background-position:</b> center (hero image centered)<br/>"
    "• <b>background-repeat:</b> no-repeat (hero image not tiled)<br/>"
    "• <b>background-color:</b> #faf3e0 (body), #f5f5f5 (menu section), white (cards)",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 9. BOX MODEL
# ══════════════════════════════════════════════
story.append(Paragraph("9. CSS Box Model", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "The food cards clearly demonstrate the CSS Box Model hierarchy: "
    "<b>Content → Padding → Border → Margin</b>:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".food-card {<br/>"
    "&nbsp;&nbsp;width: 100%;          /* Content width */<br/>"
    "&nbsp;&nbsp;height: 100%;         /* Content height */<br/>"
    "&nbsp;&nbsp;padding: 20px;        /* Space inside border */<br/>"
    "&nbsp;&nbsp;border: 1px solid #ddd;  /* Visible border */<br/>"
    "&nbsp;&nbsp;border-radius: 12px;<br/>"
    "&nbsp;&nbsp;margin: 0;            /* Space outside border */<br/>"
    "&nbsp;&nbsp;box-sizing: border-box; /* Include padding+border in width */<br/>}",
    styles['CodeBlock']
))
story.append(Paragraph(
    "The <b>box-sizing: border-box</b> property is applied globally via the universal selector "
    "<b>* { box-sizing: border-box; }</b> to ensure consistent sizing across all elements.",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 10. MARGIN COLLAPSING
# ══════════════════════════════════════════════
story.append(Paragraph("10. Margin Collapsing", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "<b>Margin collapsing</b> occurs when the vertical margins of two adjacent block-level "
    "elements overlap. Instead of adding together, the browser uses only the <i>larger</i> "
    "of the two margins as the spacing between the elements.",
    styles['BodyText2']
))
story.append(Paragraph(
    "In the website, two stacked boxes are placed between the About and Contact sections. "
    "Box 1 has <b>margin-bottom: 60px</b> and Box 2 has <b>margin-top: 60px</b>. Due to "
    "margin collapsing, the actual space between them is <b>60px</b> (not 120px), because "
    "the margins collapse into the larger of the two values.",
    styles['BodyText2']
))
story.append(Paragraph(
    ".margin-collapse-1 { margin-bottom: 60px; }<br/>"
    ".margin-collapse-2 { margin-top: 60px; }<br/>"
    "/* Result: 60px gap between them, not 120px */",
    styles['CodeBlock']
))

# ══════════════════════════════════════════════
# 11. WIDTH, HEIGHT & CONSTRAINTS
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("11. Width, Height & Constraints", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "The About section's content box demonstrates all six constraint properties:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".about-content-box {<br/>"
    "&nbsp;&nbsp;width: 100%;          /* Flexible base width */<br/>"
    "&nbsp;&nbsp;max-width: 800px;     /* Cannot grow larger than 800px */<br/>"
    "&nbsp;&nbsp;min-width: 300px;     /* Cannot shrink smaller than 300px */<br/>"
    "&nbsp;&nbsp;height: auto;         /* Flexible based on content */<br/>"
    "&nbsp;&nbsp;min-height: 200px;    /* Minimum 200px tall */<br/>"
    "&nbsp;&nbsp;max-height: 2000px;   /* Maximum height constraint */<br/>}",
    styles['CodeBlock']
))
story.append(Paragraph(
    "When the browser window is resized, the content box respects these constraints — "
    "it won't stretch beyond 800px or shrink below 300px.",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 12. OVERFLOW
# ══════════════════════════════════════════════
story.append(Paragraph("12. Overflow Demonstration", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "A testimonial box inside the About section has a fixed height of 120px with more text "
    "than can fit. The <b>overflow: scroll</b> property adds scrollbars to access the hidden content:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".overflow-demo {<br/>"
    "&nbsp;&nbsp;overflow: scroll;     /* Always shows scrollbars */<br/>"
    "&nbsp;&nbsp;height: 120px;        /* Fixed, small height */<br/>"
    "&nbsp;&nbsp;background-color: #f9f9f9;<br/>"
    "&nbsp;&nbsp;border: 1px solid #ddd;<br/>"
    "&nbsp;&nbsp;padding: 15px;<br/>}",
    styles['CodeBlock']
))
story.append(Paragraph(
    "Other overflow values: <b>visible</b> (default — content spills out), "
    "<b>hidden</b> (clips content without scrollbar), "
    "<b>auto</b> (scrollbar only when needed).",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 13. DISPLAY PROPERTIES
# ══════════════════════════════════════════════
story.append(Paragraph("13. Display Properties", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

display_items = [
    ("display: block", "Applied to section headings (.block-elem). Takes full available width and starts on a new line."),
    ("display: inline", "Applied to a span (.inline-elem) within the About paragraph. Only takes the space needed by its content."),
    ("display: inline-block", "Applied to buttons and navigation links (.inline-block-elem). Sits inline but respects width, height, padding, and margin like a block element."),
    ("display: none", "Applied to a hidden promotional text (.hidden-elem) in the hero section. Completely removes the element from the document flow — it's invisible and takes no space."),
]

for prop, desc in display_items:
    story.append(Paragraph(f"<b>{prop}:</b> {desc}", styles['BodyText2']))

# ══════════════════════════════════════════════
# 14. BORDERS, SHADOWS & SPACING
# ══════════════════════════════════════════════
story.append(Paragraph("14. Borders, Shadows & Spacing", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "Food cards use a combination of border, border-radius, and box-shadow for a polished look:",
    styles['BodyText2']
))
story.append(Paragraph(
    ".food-card {<br/>"
    "&nbsp;&nbsp;border: 1px solid #ddd;<br/>"
    "&nbsp;&nbsp;border-radius: 12px;<br/>"
    "&nbsp;&nbsp;box-shadow: 0 5px 15px rgba(0,0,0,0.08);<br/>}<br/><br/>"
    ".food-card:hover {<br/>"
    "&nbsp;&nbsp;box-shadow: 0 10px 25px rgba(0,0,0,0.15);<br/>}",
    styles['CodeBlock']
))
story.append(Paragraph(
    "Consistent spacing is maintained throughout: sections use 100px vertical padding, "
    "the container has 20px horizontal padding, and cards use 30px grid gap.",
    styles['BodyText2']
))

# ══════════════════════════════════════════════
# 15. REQUIREMENTS CHECKLIST
# ══════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("15. Requirements Checklist", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))

checklist_data = [
    ["Requirement", "Status"],
    ["Inline CSS", "✓"],
    ["Internal CSS", "✓"],
    ["External CSS", "✓"],
    ["Element selector", "✓"],
    ["Class selector", "✓"],
    ["ID selector", "✓"],
    ["Attribute selector", "✓"],
    ["Grouping selector", "✓"],
    ["Descendant selector", "✓"],
    [":hover", "✓"],
    [":first-child", "✓"],
    ["::before", "✓"],
    ["::after", "✓"],
    ["Cascade", "✓"],
    ["Specificity", "✓"],
    ["Inheritance", "✓"],
    ["Font properties", "✓"],
    ["Text properties", "✓"],
    ["Color properties", "✓"],
    ["Background properties", "✓"],
    ["Padding", "✓"],
    ["Margin", "✓"],
    ["Border", "✓"],
    ["Margin collapsing", "✓"],
    ["box-sizing", "✓"],
    ["Width/Height", "✓"],
    ["Min/Max constraints", "✓"],
    ["Overflow", "✓"],
    ["Block", "✓"],
    ["Inline", "✓"],
    ["Inline-block", "✓"],
    ["None", "✓"],
    ["Box shadow", "✓"],
    ["Consistent spacing", "✓"],
]

table = Table(checklist_data, colWidths=[page_width * 0.75, page_width * 0.25])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), ORANGE),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#dddddd")),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
]))
story.append(table)

# ══════════════════════════════════════════════
# 16. LIVE DEPLOYMENT
# ══════════════════════════════════════════════
story.append(Spacer(1, 30))
story.append(Paragraph("16. Live Deployment", styles['SectionHeading']))
story.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=12))
story.append(Paragraph(
    "The website has been deployed to production via <b>Vercel</b> and the source code is "
    "hosted on <b>GitHub</b>:",
    styles['BodyText2']
))
story.append(Paragraph(
    '<b>Live Website:</b> <font color="#2980b9"><u>'
    '<a href="https://food-corner-website-gilt.vercel.app">'
    'https://food-corner-website-gilt.vercel.app</a></u></font>',
    styles['BodyText2']
))
story.append(Paragraph(
    '<b>GitHub Repository:</b> <font color="#2980b9"><u>'
    '<a href="https://github.com/junaid-devv/food-corner-website">'
    'https://github.com/junaid-devv/food-corner-website</a></u></font>',
    styles['BodyText2']
))
story.append(Spacer(1, 30))
story.append(HRFlowable(width="100%", thickness=2, color=ORANGE, spaceAfter=10))
story.append(Paragraph(
    "<i>End of Report — Muhammad Junaid (FA24-BCS-167)</i>",
    ParagraphStyle('EndNote', fontSize=10, alignment=TA_CENTER, textColor=gray, fontName='Helvetica-Oblique')
))

# ── Generate ──
doc.build(story)
print(f"PDF generated: {OUTPUT_PDF}")
