# Finanças Inteligentes — Relatório do Projeto
**Atualizado em:** 25 de Junho de 2026  
**Objetivo:** Sistema de renda passiva automatizado com blog de finanças pessoais

---

## 🌐 LINKS IMPORTANTES

| Recurso | URL |
|---|---|
| **Site (Blog)** | https://colunas0428.github.io/financas-inteligentes/ |
| **Página Mercados** | https://colunas0428.github.io/financas-inteligentes/mercados.html |
| **Página Artigos** | https://colunas0428.github.io/financas-inteligentes/articles/index.html |
| **GitHub Repositório** | https://github.com/colunas0428/financas-inteligentes |
| **GitHub Actions** | https://github.com/colunas0428/financas-inteligentes/actions |
| **GitHub Secrets** | https://github.com/colunas0428/financas-inteligentes/settings/secrets/actions |
| **Google Analytics** | https://analytics.google.com |
| **Google Search Console** | https://search.google.com/search-console |
| **Google AdSense** | https://adsense.google.com (ainda não aprovado) |
| **Instagram** | https://www.instagram.com/contascontas0428/ |
| **Make.com** | https://www.make.com |
| **Gemini API** | https://aistudio.google.com/app/apikey |

---

## 🔑 CREDENCIAIS E CHAVES (GUARDAR COM SEGURANÇA)

| Serviço | Conta / Projeto |
|---|---|
| GitHub | colunas0428 |
| Google (Analytics / Search Console) | colunas0428@gmail.com |
| Instagram | colunas0428@gmail.com / @contascontas0428 |
| Gemini API | Projeto: **freecontas** |
| Unsplash (não usado ativamente) | colunas0428@gmail.com |

> ⚠️ NUNCA partilhes as chaves API publicamente.

---

## ✅ O QUE ESTÁ FEITO

### 1. Site / Blog (GitHub Pages)
- [x] Site online e gratuito em GitHub Pages
- [x] Design verde profissional com navegação completa
- [x] 3 artigos iniciais publicados manualmente
- [x] Página de Mercados com dados em tempo real (crypto, bolsa, commodities, forex)
- [x] Página de Artigos com listagem
- [x] Sitemap.xml submetido ao Google Search Console
- [x] Google Analytics instalado (ID: G-5DK6M614ME)
- [x] Google Search Console verificado
- [x] RSS Feed criado (para automação Make.com)

### 2. Geração Automática de Artigos (GitHub Actions)
- [x] Workflow configurado para correr todos os dias às 9h UTC
- [x] Script Python que gera artigos em português com Gemini AI
- [x] 30 tópicos de finanças pessoais pré-definidos
- [x] Artigos guardados automaticamente no repositório
- [⚠️] **PENDENTE:** Quota Gemini API ainda não ativa no projeto "freecontas" (aguardar 24-48h)

### 3. Instagram Automático (Make.com)
- [x] Conta Instagram criada: @contascontas0428
- [x] Página Facebook Business criada
- [x] Make.com configurado com cenário RSS → Instagram
- [x] Publicação automática quando novo artigo é detetado no RSS
- [x] 20 imagens de finanças aleatórias configuradas
- [x] Logo/foto de perfil criada

### 4. Monetização (em preparação)
- [ ] Google AdSense — aguarda 20-30 artigos (~semana 3-4)
- [ ] Amazon Afiliados — aguarda tráfego real (~mês 2-3)

---

## 📊 PÁGINA DE MERCADOS — DADOS EM TEMPO REAL

| Secção | Estado |
|---|---|
| Criptomoedas (10 moedas em EUR) | ✅ Funcional |
| Bolsa Lisboa PSI — ações individuais | ✅ (dados em horário de mercado) |
| Gráfico PSI 20 interativo | ✅ (símbolo: INDEX:PSI20) |
| Índices Mundiais (PSI20, DAX, CAC40, S&P500, Nasdaq) | ✅ Funcional |
| Commodities (Ouro, Prata, Petróleo, Cobre, Gás) | ✅ Funcional |
| Câmbios (EUR/USD, EUR/GBP, etc.) | ✅ Funcional |
| Fear & Greed Index | ✅ Funcional |

---

## 🗓️ PRÓXIMOS PASSOS

### Semana 1-2 (Agora)
1. **Confirmar que o workflow Gemini funciona** — testar amanhã após quota ativar
2. **Verificar artigos novos** em https://colunas0428.github.io/financas-inteligentes/articles/
3. **Partilhar o site** em grupos de finanças no Facebook, Reddit (r/financaspessoais), LinkedIn

### Semana 3-4 (Quando tiveres 20+ artigos)
4. **Candidatar ao Google AdSense**
   - Vai a https://adsense.google.com
   - Adiciona o site colunas0428.github.io/financas-inteligentes
   - Aguarda aprovação (5-14 dias)
   - Após aprovação, substitui os espaços "Espaco Publicitario" no site pelo código AdSense

### Mês 2
5. **Candidatar ao Amazon Afiliados Portugal/Brasil**
   - https://programas.amazon.es/afiliados (Espanha/Portugal)
   - Criar artigos com recomendações de livros de finanças
   - Adicionar links de afiliado nos artigos

6. **Melhorar SEO**
   - Adicionar meta descriptions em todos os artigos
   - Criar artigos sobre tópicos com alta pesquisa no Google Portugal

### Mês 3+
7. **Newsletter** (gratuito com Mailchimp)
   - Capturar emails dos visitantes
   - Enviar resumo semanal automático

8. **Parcerias com brokers/seguradoras**
   - Programas de afiliados de brokers portugueses (XTB, eToro, Trading 212)
   - Comissões por cada cliente referenciado

---

## 💰 PROJEÇÃO DE RENDIMENTO MENSAL

| Fase | Artigos | Visitas/mês | Receita Estimada |
|---|---|---|---|
| **Mês 1-2** | 30-60 | 100-500 | €0-5 |
| **Mês 3-4** | 90-120 | 500-2.000 | €5-50 (AdSense ativo) |
| **Mês 6** | 180 | 2.000-8.000 | €50-200 |
| **Mês 12** | 365 | 8.000-30.000 | €200-800 |
| **Mês 24** | 700+ | 30.000-100.000 | €800-3.000+ |

> Nota: Os valores dependem do tráfego orgânico do Google (SEO). Quanto mais artigos e partilhas, mais rápido o crescimento.

---

## ⚙️ COMO O SISTEMA FUNCIONA (AUTOMATICAMENTE)

```
Todo os dias às 9h UTC:
  1. GitHub Actions acorda
  2. Escolhe um tópico de finanças aleatório
  3. Pede ao Gemini AI para escrever artigo de 1000 palavras em português
  4. Guarda artigo como HTML no site
  5. Atualiza a página inicial com o novo artigo
  6. Publica automaticamente no GitHub Pages
  7. Make.com deteta novo item no RSS feed
  8. Publica automaticamente no Instagram com imagem aleatória
```

**Intervenção humana necessária:** Zero (após setup completo)

---

## 🚨 PROBLEMAS CONHECIDOS / A RESOLVER

1. **Quota Gemini API** — projeto "freecontas" aguarda ativação (24-48h)
2. **Gráfico PSI 20** — símbolo `INDEX:PSI20` pode não mostrar gráfico interativo
3. **S&P 500 / Nasdaq nos índices** — símbolos podem precisar ajuste
4. **Página "Sobre"** — pode estar a mostrar conteúdo errado

---

## 📁 FICHEIROS DO PROJETO

| Ficheiro | Função |
|---|---|
| `index.html` | Página principal do blog |
| `mercados.html` | Dados de mercado em tempo real |
| `sobre.html` | Página sobre o projeto |
| `articles/index.html` | Listagem de artigos |
| `articles/*.html` | Artigos individuais gerados |
| `generate_article.py` | Script Python de geração de artigos |
| `.github/workflows/daily_content.yml` | Automação GitHub Actions |
| `feed.xml` | RSS Feed para Make.com |
| `sitemap.xml` | Mapa do site para Google |

---

*Relatório gerado automaticamente — Projeto Finanças Inteligentes*
