#!/usr/bin/env python3
import sys
import os
import requests
import json
import re
from datetime import datetime

def generate_article(topic):
    api_key = os.environ.get('GEMINI_API_KEY', '')
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)
    
    # Try models in order of preference
    models = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-2.0-flash']
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{models[0]}:generateContent?key={api_key}"
    
    prompt = f"""Escreve um artigo completo em portugues europeu sobre "{topic}" relacionado a financas pessoais.
O artigo deve ter aproximadamente 1000 palavras, ser educativo, pratico e acessivel.
Inclui: titulo principal, introducao, 3-4 seccoes com subtitulos, dicas praticas e conclusao.
Formata em HTML com tags h1, h2, p, ul, li. Usa linguagem amigavel e motivadora."""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2048}
    }
    
    print(f"Calling Gemini API for topic: {topic}")
    response = requests.post(url, json=payload, timeout=60)
    print(f"API response status: {response.status_code}")
    
    data = response.json()
    
    if 'candidates' not in data:
        print(f"API Error response: {json.dumps(data, indent=2)}")
        sys.exit(1)
    
    content = data['candidates'][0]['content']['parts'][0]['text']
    
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower())
    slug = slug.strip('-')
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"articles/{slug}.html"
    
    html = f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic} - Financas Inteligentes</title>
<style>
body{{font-family:'Segoe UI',sans-serif;max-width:800px;margin:0 auto;padding:20px;color:#333;line-height:1.7}}
header{{background:linear-gradient(135deg,#1a472a,#2d6a4f);color:white;padding:20px;border-radius:8px;margin-bottom:30px}}
header a{{color:#a8d5b5;text-decoration:none}}
h1{{color:#1a472a;font-size:2em;margin:20px 0}}
h2{{color:#2d6a4f;margin:25px 0 15px}}
.date{{color:#888;font-size:.9em;margin-bottom:20px}}
.adsense{{background:#f5f5f5;border:2px dashed #ccc;padding:30px;text-align:center;color:#999;margin:25px 0;border-radius:5px}}
footer{{background:#1a472a;color:#a8d5b5;padding:20px;text-align:center;border-radius:8px;margin-top:40px}}
</style>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-5DK6M614ME"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-5DK6M614ME');</script>
</head>
<body>
<header><a href="/financas-inteligentes/">Financas Inteligentes</a></header>
<div class="date">Publicado em {date_str}</div>
<div class="adsense">Espaco Publicitario</div>
{content}
<div class="adsense">Espaco Publicitario</div>
<footer><p>&copy; 2025 Financas Inteligentes</p></footer>
</body>
</html>"""
    
    os.makedirs('articles', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Article saved: {filename}")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            index = f.read()
        
        card = f"""
<div class="card">
<div class="card-img">&#128200;</div>
<div class="card-body">
<h3>{topic}</h3>
<p>Artigo publicado em {date_str}. Aprende tudo sobre {topic.lower()} e melhora as tuas financas.</p>
<a href="/financas-inteligentes/{filename}">Ler Artigo</a>
</div>
</div>"""
        
        index = index.replace('</div>\n<div class="adsense" style="margin-top:40px">', card + '\n</div>\n<div class="adsense" style="margin-top:40px">')
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index)
        print("index.html updated")
    except Exception as e:
        print(f"Warning: Could not update index.html: {e}")
    
    return filename

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_article.py 'topic'")
        sys.exit(1)
    topic = ' '.join(sys.argv[1:])
    generate_article(topic)
