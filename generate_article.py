#!/usr/bin/env python3
import sys
import os
import requests
import json
import re
from datetime import datetime

def generate_article(topic):
    api_key = os.environ.get('GROQ_API_KEY', '')
    if not api_key:
        print("ERROR: GROQ_API_KEY not set")
        sys.exit(1)

    url = "https://api.groq.com/openai/v1/chat/completions"

    prompt = "Escreve um artigo completo em portugues europeu sobre \"" + topic + "\" relacionado a financas pessoais. O artigo deve ter aproximadamente 1000 palavras, ser educativo, pratico e acessivel. Inclui: titulo principal, introducao, 3-4 seccoes com subtitulos, dicas praticas e conclusao. Formata em HTML com tags h1, h2, p, ul, li. Usa linguagem amigavel e motivadora. Nao incluas tags html, head, body ou DOCTYPE - apenas o conteudo interno."

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2048
    }

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    print("Calling Groq API for topic: " + topic)
    response = requests.post(url, json=payload, headers=headers, timeout=60)
    print("API response status: " + str(response.status_code))

    if response.status_code != 200:
        print("API Error: " + response.text)
        sys.exit(1)

    data = response.json()
    content = data['choices'][0]['message']['content']

    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower())
    slug = slug.strip('-')
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = "articles/" + slug + ".html"

    html = """<!DOCTYPE html>
<html lang="pt-PT">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>""" + topic + """ - Financas Inteligentes</title>
<style>
body{font-family:'Segoe UI',sans-serif;max-width:800px;margin:0 auto;padding:20px;color:#333;line-height:1.7}
header{background:linear-gradient(135deg,#1a472a,#2d6a4f);color:white;padding:20px;border-radius:8px;margin-bottom:30px}
header a{color:#a8d5b5;text-decoration:none}
h1{color:#1a472a;font-size:2em;margin:20px 0}
h2{color:#2d6a4f;margin:25px 0 15px}
.date{color:#888;font-size:.9em;margin-bottom:20px}
.adsense{background:#f5f5f5;border:2px dashed #ccc;padding:30px;text-align:center;color:#999;margin:25px 0;border-radius:5px}
footer{background:#1a472a;color:#a8d5b5;padding:20px;text-align:center;border-radius:8px;margin-top:40px}
nav{background:#155724;padding:10px 20px;margin-bottom:20px;border-radius:8px}
nav a{color:#a8d5b5;text-decoration:none;margin:0 10px;font-weight:500}
nav a:hover{color:white}
</style>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-5DK6M614ME"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-5DK6M614ME');</script>
</head>
<body>
<header><a href="/financas-inteligentes/">&#128200; Financas Inteligentes</a></header>
<nav>
<a href="/financas-inteligentes/">Inicio</a>
<a href="/financas-inteligentes/articles/index.html">Artigos</a>
<a href="/financas-inteligentes/mercados.html">Mercados</a>
<a href="/financas-inteligentes/calculadoras.html">Calculadoras</a>
<a href="/financas-inteligentes/sobre.html">Sobre</a>
</nav>
<div class="date">Publicado em """ + date_str + """</div>
<div class="adsense">Espaco Publicitario</div>
""" + content + """
<div class="adsense">Espaco Publicitario</div>
<footer><p>&copy; 2025 Financas Inteligentes &bull; Informacao educativa, nao constitui aconselhamento financeiro</p></footer>
</body>
</html>"""

    os.makedirs('articles', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Article saved: " + filename)

    return filename

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_article.py 'topic'")
        sys.exit(1)
    topic = ' '.join(sys.argv[1:])
    generate_article(topic)
