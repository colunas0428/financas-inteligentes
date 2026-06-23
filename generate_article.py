#!/usr/bin/env python3
import sys
import os
import requests
import json
import re
from datetime import datetime

def generate_article(topic):
    api_key = os.environ.get('GEMINI_API_KEY', '')
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    prompt = f"""Escreva um artigo completo em portugues brasileiro sobre "{topic}" relacionado a financas pessoais.
O artigo deve ter exatamente 1000 palavras, ser educativo, pratico e acessivel ao publico brasileiro.
Inclua: titulo principal, introducao, 3-4 secoes com subtitulos, dicas praticas e conclusao.
Formate em HTML completo com tags h1, h2, p, ul, li. Use uma linguagem amigavel e motivadora."""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2048}
    }
    
    response = requests.post(url, json=payload, timeout=60)
    data = response.json()
    
    if 'candidates' not in data:
        raise Exception(f"API Error: {data}")
    
    content = data['candidates'][0]['content']['parts'][0]['text']
    
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower().replace('c','c').replace('a','a').replace('e','e').replace('e','e').replace('o','o').replace('u','u').replace('a','a').replace('i','i'))
    slug = slug.strip('-')
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"articles/{slug}.html"
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
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
</head>
<body>
<header><a href="/">Financas Inteligentes</a></header>
<div class="date">Publicado em {date_str}</div>
<!-- ADSENSE CODE HERE -->
<div class="adsense">Espaco Publicitario</div>
{content}
<div class="adsense"><!-- ADSENSE CODE HERE --></div>
<footer><p>2024 Financas Inteligentes</p></footer>
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
<div class="card-img">article</div>
<div class="card-body">
<h3>{topic}</h3>
<p>Artigo publicado em {date_str}. Aprenda tudo sobre {topic.lower()} e melhore suas financas.</p>
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
