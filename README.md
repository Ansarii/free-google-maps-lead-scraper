# 🚀 Free Google Maps Lead Scraper & B2B Contact Email Extractor

> **Extract unlimited verified local B2B leads from Google Maps with direct phone numbers, business websites, physical addresses, review counts, star ratings, and contact emails + social media profiles (LinkedIn, Instagram, Facebook, X, YouTube).**

[![Run on Apify](https://apify.com/actor-badge?actor=neon_innovation_lab/google-maps-b2b-lead-enricher)](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher)
[![GitHub stars](https://img.shields.io/github/stars/Ansarii/free-google-maps-lead-scraper.svg?style=social)](https://github.com/Ansarii/free-google-maps-lead-scraper/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-green.svg)](https://nodejs.org/)

---

## 🎁 First 50 Leads 100% Free

Stop paying \$49–\$149/month subscriptions before extracting a single lead. 

* **Zero Upfront Cost:** Every new Apify account receives **$5.00/month in free platform credits**.
* **$0 Custom Event Charges on Initial 50 Leads:** The underlying Actor [`neon_innovation_lab/google-maps-b2b-lead-enricher`](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher) waives custom lead enrichment fees for the first 50 leads of every run.
* **No Credit Card Required:** Run it directly via cloud console or using the Python and Node.js scripts in this repo.

---

## ⚡ Why Use This Lead Scraper?

| Feature | This Scraper | Outscraper / ScrapingBee | PhantomBuster | Apollo / ZoomInfo |
| :--- | :--- | :--- | :--- | :--- |
| **Free Tier** | 🎁 **First 50 Leads Free** | ⚠️ 10-25 leads trial | ❌ 14-day trial only | ❌ Paywalled |
| **Deep Contact Enrichment** | ✅ **Emails + Socials (LinkedIn, IG, FB)** | ⚠️ Basic phone only | ⚠️ Broken on dynamic sites | ⚠️ Stale directory data |
| **Monthly Subscription** | ❌ **$0 / month** | 💸 $29 – $99 / mo | 💸 $69 – $149 / mo | 💸 $1,200 – $10,000 / yr |
| **Cost per 1,000 Leads** | 💰 **~$7.00 / 1k leads** | 💸 $15 – $30 / 1k leads | 💸 $40 – $80 / 1k leads | 💸 $150 – $300 / 1k leads |
| **Anti-Bot & Proxy Rotation** | ✅ **Automated residential proxies** | ⚠️ Extra fee | ⚠️ Frequent IP blocks | N/A |
| **Output Formats** | 📁 **CSV, JSON, Excel** | CSV, XLSX | CSV, JSON | CRM export |

---

## 📊 Extracted Data Points

Each extracted lead includes:
* **Business Name (`title`)**
* **Google Maps Category (`category`)**
* **Direct Phone Number (`phone`)** (verified on Maps & official website)
* **Official Website (`website`)**
* **Contact Emails (`emails`)** (syntax-cleaned from company website)
* **Social Profiles (`socials`)**: LinkedIn, Instagram, Facebook, X (Twitter), YouTube
* **Physical Address (`address`)**
* **Google Star Rating (`rating`) & Total Reviews (`reviewsCount`)**
* **Google Maps URL (`googleMapsUrl`)**
* **Timestamp (`scrapedAt`)**

### Sample JSON Output

```json
{
  "title": "Greater Austin Roof Pros",
  "category": "Roofing contractor",
  "address": "1201 E 11th St, Austin, TX 78702",
  "phone": "(512) 555-0199",
  "website": "https://www.austinroofpros.com",
  "emails": [
    "contact@austinroofpros.com",
    "estimates@austinroofpros.com"
  ],
  "socials": {
    "linkedin": "https://www.linkedin.com/company/austin-roof-pros",
    "facebook": "https://www.facebook.com/austinroofpros",
    "instagram": "https://www.instagram.com/austinroofpros"
  },
  "rating": 4.9,
  "reviewsCount": 218,
  "googleMapsUrl": "https://www.google.com/maps/place/Greater+Austin+Roof+Pros",
  "query": "Roofers in Austin, TX",
  "scrapedAt": "2026-10-19T10:15:30.000Z"
}
```

---

## 🚀 Quickstart: Python

### 1. Clone & Install
```bash
git clone https://github.com/Ansarii/free-google-maps-lead-scraper.git
cd free-google-maps-lead-scraper
pip install -r requirements.txt
```

### 2. Configure Token
Get your free API token ($5 monthly free credit) at [https://console.apify.com/account/integrations](https://console.apify.com/account/integrations):
```bash
cp .env.example .env
# Edit .env and paste your APIFY_TOKEN
```
Or export directly:
```bash
export APIFY_TOKEN="your_token_here"
```

### 3. Run the Scraper
```bash
python scrape_leads.py --query "Roofers in Austin, TX" --limit 50
```

#### Custom Options:
```bash
python scrape_leads.py \
  --query "Dentists in Miami, FL" \
  --limit 50 \
  --country "us" \
  --output-csv "dentists_miami.csv" \
  --output-json "dentists_miami.json"
```

---

## ⚡ Quickstart: Node.js

### 1. Install Dependencies
```bash
npm install
```

### 2. Run the Script
```bash
node scrape_leads.js --query "Coffee shops in Seattle, WA" --limit 50
```

Results are immediately formatted and saved to `leads.csv` and `leads.json`!

---

## ☁️ 1-Click Cloud Execution (No Code Required)

Don't want to run local scripts? Run directly in your browser on Apify Cloud:

1. Open the Actor on the Apify Store:
   👉 **[neon_innovation_lab/google-maps-b2b-lead-enricher](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher)**
2. Enter your search query (e.g., `Plumbers in Chicago, IL`).
3. Click **Start**.
4. Download your enriched spreadsheet in **Excel, CSV, or JSON** with 1 click!

---

## 🔄 Automated Outbound Workflows

### 1. Clay Table Waterfall Integration
RevOps and outbound teams can enrich leads automatically in Clay:
1. Add an **Enrichment** column using **HTTP API**.
2. **Method**: `POST`
3. **URL**: `https://api.apify.com/v2/acts/neon_innovation_lab~google-maps-b2b-lead-enricher/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN`
4. **Body**:
   ```json
   {
     "searchQueries": ["{{Domain}} in {{City}}"],
     "maxResultsPerQuery": 10,
     "extractEmailsAndSocials": true
   }
   ```
5. Map extracted `emails`, `phone`, and `socials` directly to your outbound sequence columns!

### 2. n8n Automated CRM Sync
Build a hands-free prospecting cron job:
1. Add an **n8n Schedule Trigger** (e.g. Every Monday at 9:00 AM).
2. Call the Apify node with Actor `neon_innovation_lab/google-maps-b2b-lead-enricher`.
3. Filter leads where `emails.length > 0`.
4. Send directly to **Smartlead, Instantly, HubSpot, or Airtable**.

---

## 💰 Transparent Pay-Per-Event Pricing (After Free Tier)

| Metric | Cost | Details |
| :--- | :--- | :--- |
| **First 50 Leads** | **$0.00** | 🎁 Waived custom fee under $5/mo free credit |
| **Actor Start Fee** | $0.03 | Charged once when execution starts |
| **Per Enriched Lead (51+)** | $0.005 | Charged per verified lead extracted |
| **Dataset Item Storage** | $0.002 | Platform dataset storage per row |
| **Effective Cost / 1,000 Leads**| **~$7.03** | 100% pay-as-you-go, zero monthly subscription |

---

## 🛡️ Legal & Ethical Web Scraping

* This tool only collects publicly available business information published on Google Maps and public company websites.
* In the United States, scraping publicly accessible internet data is legal under federal case law (*hiQ Labs v. LinkedIn*).
* Users are responsible for complying with relevant local regulations (such as CAN-SPAM, GDPR, or CCPA) when conducting cold outreach.

---

## ⭐ Star the Repo & Support

If this free tool helped you generate sales leads and pipeline:
* ⭐ **Star this repository** on GitHub: [Ansarii/free-google-maps-lead-scraper](https://github.com/Ansarii/free-google-maps-lead-scraper)
* 🚀 **Leave a 5-star review** on the Apify Store: [neon_innovation_lab/google-maps-b2b-lead-enricher](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher)
* 💡 **Feature Requests & Issues**: Open an issue on GitHub!
