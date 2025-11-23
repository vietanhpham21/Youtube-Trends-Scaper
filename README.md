# YouTube Trends Scraper

Ein einfaches Python-Tool, um YouTube-Trending-Videos automatisch zu scrapen und zu analysieren.

## Was macht das Projekt?

Das Projekt besteht aus zwei Teilen:

1. **Scraper** - Sammelt automatisch Daten von YouTube-Trends
2. **Analyse** - Visualisiert die gesammelten Daten

## Features

**Data Collection:**
- Scraped Video-Infos: Titel, Views, Likes, Dislikes, Kommentare, Channel-Daten
- Speichert die Daten mit Timestamp in JSON-Dateien

**Data Analysis:**
- Entfernt automatisch Duplikate
- Berechnet Like-Rate und Dislike-Rate
- Analysiert Channel-Wachstum über Zeit (prozentuale View-Zunahme)
- Extrahiert und analysiert Hashtags aus Video-Beschreibungen
- Vergleicht Performance: Videos mit vs. ohne Hashtags

**Visualizations:**
- Bar-Charts: Like-Rates, Channel-Wachstum, Hashtag-Häufigkeit
- Interaktive Scatter-Plots (Plotly)
- Zeitreihenanalysen

## Tech Stack

- Python 3
- Selenium (Web Scraping)
- pandas (Datenverarbeitung)
- matplotlib & Plotly (Visualisierung)
- Jupyter Notebook

- Die Dislike-Zahlen kommen von einer Chrome-Extension (Return YouTube Dislike)
