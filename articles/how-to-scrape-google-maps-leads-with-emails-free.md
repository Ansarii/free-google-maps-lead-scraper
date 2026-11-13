---
title: How to Scrape Google Maps Leads with Emails for Free (Python & Node.js)
published: true
tags: python, webscraping, leadgeneration, tutorial
canonical_url: https://github.com/Ansarii/free-google-maps-lead-scraper
---

# How to Scrape Google Maps Leads with Emails for Free (Python & Node.js)

If you've ever tried scraping Google Maps for local B2B leads, you know the major roadblock: **Google Maps never shows email addresses.** 

Google Maps listings give you business names, phone numbers, star ratings, and website links, but if you want to run cold email outreach or build a prospecting list, raw maps data leaves you stuck manually clicking through hundreds of websites to find contact inboxes.

In this guide, you will learn how to build an automated, zero-cost pipeline that:
1. **Searches Google Maps** for any target niche and location (e.g., *"Roofers in Austin, TX"*, *"Dentists in Miami, FL"*).
2. **Extracts verified business details**: Name, address, phone number, star rating, and website.
3. **Deep-crawls each company's website** to extract syntax-verified contact emails and social media profiles (LinkedIn, Instagram, Facebook).
4. **Exports cleanly to CSV and JSON**.

Best of all, you can run this **completely free for your first 50 leads** without needing a credit card or maintaining expensive residential proxy infrastructure.

---

## The Architecture: Why Most Scrapers Fail

Traditional Google Maps scrapers just pull the visible DOM on Google Maps. That gives you:
- Business Name: ✅
- Phone Number: ✅
- Physical Address: ✅
- Website: ✅
- **Contact Email: ❌ (NOT stored on Google Maps)**

To solve this, our pipeline deploys a **2-Stage Lead Enrichment Architecture**:

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  Stage 1: Google Maps  │ ───► │ Stage 2: Deep Website  │ ───► │  Stage 3: Data Export  │
│  Extract Listings &    │      │ Visit company site to  │      │ Clean CSV & JSON with  │
│  Official Website URLs │      │ scrape emails & socials│      │ verified B2B contacts  │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

Rather than managing headless browsers, anti-bot bypasses, and proxy pools yourself, we wrap this pipeline into an open-source client calling the cloud Actor [`neon_innovation_lab/google-maps-b2b-lead-enricher`](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher).

---

## Prerequisites

1. Python 3.8+ or Node.js 18+
2. A free Apify API token (Apify provides **$5.00/month in free credits**, and the first 50 leads incur **$0 in custom event fees**).
   - Sign up free: [https://console.apify.com/](https://console.apify.com/)
   - Copy your token from: [https://console.apify.com/account/integrations](https://console.apify.com/account/integrations)

---

## Method 1: Python Implementation

### 1. Install the SDK
```bash
pip install apify-client python-dotenv
```

### 2. The Python Script (`scrape_leads.py`)

```python
import os
import csv
import json
from apify_client import ApifyClient

# 1. Initialize client with your free API token
client = ApifyClient(os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN_HERE"))

# 2. Define search parameters
run_input = {
    "searchQueries": ["Roofers in Austin, TX"],
    "maxResultsPerQuery": 50,         # First 50 leads are 100% free!
    "extractEmailsAndSocials": True,  # Deep website visit for emails & socials
    "countryCode": "us"
}

print("🚀 Starting Google Maps Lead Extraction with Email Enrichment...")
run = client.actor("neon_innovation_lab/google-maps-b2b-lead-enricher").call(run_input=run_input)

# 3. Retrieve dataset items
dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"🎉 Successfully scraped {len(dataset_items)} enriched leads!\n")

# 4. Export to CSV
with open("leads.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Category", "Phone", "Website", "Emails", "Rating", "Address"])
    for lead in dataset_items:
        emails = "; ".join(lead.get("emails") or [])
        writer.writerow([
            lead.get("title"),
            lead.get("category"),
            lead.get("phone"),
            lead.get("website"),
            emails,
            lead.get("rating"),
            lead.get("address")
        ])

print("💾 Saved to leads.csv!")
```

Run it with:
```bash
export APIFY_TOKEN="your_token_here"
python scrape_leads.py
```

---

## Method 2: Node.js Implementation

### 1. Install the SDK
```bash
npm install apify-client dotenv
```

### 2. The Node.js Script (`scrape_leads.js`)

```javascript
import fs from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({
  token: process.env.APIFY_TOKEN || 'YOUR_APIFY_TOKEN_HERE',
});

const runInput = {
  searchQueries: ['Dentists in Miami, FL'],
  maxResultsPerQuery: 50,        // First 50 leads are free!
  extractEmailsAndSocials: true, // Collect emails & social profiles
  countryCode: 'us',
};

console.log('🚀 Running lead extraction...');
const run = await client.actor('neon_innovation_lab/google-maps-b2b-lead-enricher').call(runInput);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`✅ Extracted ${items.length} enriched businesses!`);

// Export to JSON
fs.writeFileSync('leads.json', JSON.stringify(items, null, 2));
console.log('💾 Saved to leads.json');
```

---

## Sample Extracted Output

Here is an example of what the returned JSON dataset looks like:

```json
{
  "title": "Austin Premier Roofing Co",
  "category": "Roofing contractor",
  "address": "1204 E 7th St, Austin, TX 78702",
  "phone": "(512) 555-0142",
  "website": "https://www.austinpremierroofing.com",
  "emails": [
    "contact@austinpremierroofing.com",
    "estimates@austinpremierroofing.com"
  ],
  "socials": {
    "linkedin": "https://www.linkedin.com/company/austin-premier-roofing",
    "facebook": "https://www.facebook.com/austinpremierroofing",
    "instagram": "https://www.instagram.com/austinroofingtx"
  },
  "rating": 4.9,
  "reviewsCount": 184,
  "googleMapsUrl": "https://www.google.com/maps/place/...",
  "query": "Roofers in Austin, TX",
  "scrapedAt": "2026-10-19T12:00:00.000Z"
}
```

---

## Cost Comparison: Why Pay-Per-Event Wins

| Tool | Monthly Subscription | Cost for 1,000 Leads | Free Trial |
| :--- | :--- | :--- | :--- |
| **This Tool (`free-google-maps-lead-scraper`)** | **$0 / month** | **~$7.00** | 🎁 **First 50 Leads Free** |
| Outscraper | $29 – $99 / mo | $15 – $30 | 25 leads |
| PhantomBuster | $69 – $149 / mo | $40 – $80 | 14-day limit |
| Apollo / ZoomInfo | $99 – $1,000+ / mo | $150 – $300 | Limited export |

By leveraging Apify's Pay-Per-Event (PPE) model, you only pay for what you actually extract:
- **First 50 leads**: $0.00 custom fee
- **Additional leads**: $0.005 per enriched lead + $0.002 dataset storage
- **Total effective cost**: ~$7.03 per 1,000 verified leads!

---

## Open-Source GitHub Repository

The complete open-source code with CLI options (`--query`, `--limit`, `--country`), automated CSV/JSON formatting, and sample data is available on GitHub:

👉 **[GitHub: Ansarii/free-google-maps-lead-scraper](https://github.com/Ansarii/free-google-maps-lead-scraper)**

If you don't even want to run local code, you can trigger the scraper directly in your browser with 1 click:
👉 **[Run on Apify Store: google-maps-b2b-lead-enricher](https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher)**

Happy prospecting! If you found this useful, don't forget to star the GitHub repo! ⭐
