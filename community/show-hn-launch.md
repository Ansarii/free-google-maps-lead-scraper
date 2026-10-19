# Hacker News Launch Guide (Show HN)

**Platform**: [news.ycombinator.com/submit](https://news.ycombinator.com/submit)

---

## 📌 Title:
`Show HN: Free Google Maps Lead Scraper with Website Contact Email Enrichment`

---

## 🔗 URL:
`https://github.com/Ansarii/free-google-maps-lead-scraper`

---

## 📝 First Comment (Post immediately after submitting):

Hi HN,

I built `free-google-maps-lead-scraper` to solve a common annoyance when gathering local B2B directory information: Google Maps listings give you business names, addresses, ratings, and phones, but they never include direct contact emails.

Most commercial tools charge $50–$150/month subscriptions for basic scraping, and still leave you with spreadsheets full of missing emails or junk image names (`logo@2x.png`).

Here’s how this works:
1. **Maps Crawler**: Uses Playwright to navigate Google Maps search queries, bypass cookie consent dialogs, and paginate through business listings.
2. **Deep Website Contact Enrichment**: Visits each discovered company website using fast HTTP/Cheerio parsing to extract syntax-verified contact emails, secondary phone numbers, and social media handles (LinkedIn, Instagram, Facebook, X).
3. **Data Sanitization**: Filters out false positives (tracking domains, Sentry/Wix assets, dummy templates) and formats everything into clean CSV and JSON.

You can run it locally with Python or Node.js:
- Python: `python scrape_leads.py --query "Roofers in Austin, TX" --limit 50`
- Node.js: `node scrape_leads.js --query "Dentists in Miami, FL" --limit 50`

For developers who don't want to run Chromium or manage IP rotation locally, there is also a 1-click cloud execution option hosted on Apify where the first 50 leads are 100% free (via Apify's $5 monthly credit and zero custom event fees).

Repo: https://github.com/Ansarii/free-google-maps-lead-scraper
Cloud Actor: https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher

Would appreciate any feedback on edge-case handling or features you'd find useful!
