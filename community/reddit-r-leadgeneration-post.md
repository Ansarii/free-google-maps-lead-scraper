# Reddit Community Post: r/leadgeneration & r/coldemail

**Target Subreddits**:
- `r/leadgeneration`
- `r/coldemail`
- `r/sales`
- `r/Entrepreneur`

---

## 📌 Post Title:
**Why 90% of Google Maps scrapers give you useless data (and a free script that actually finds emails)**

---

## 📝 Post Body:

If you’ve ever tried scraping Google Maps for local B2B lead gen (roofers, plumbers, dentists, accounting firms), you’ve probably noticed the exact same frustrating pattern:

You pay $50–$100 for an Outscraper or PhantomBuster subscription, run a search for "Plumbers in Chicago", and get back a spreadsheet with 500 rows... and **almost zero contact emails**. 

### The Problem: Google Maps Does NOT Store Emails
A lot of people don't realize this: Google Maps as a platform literally does not display or index business email addresses. It gives you:
- Business name
- Phone number
- Physical address
- Website URL
- Reviews & star rating

If a scraper only pulls data from Google Maps itself, you’re stuck with a phone list and zero cold email outreach capability.

To actually get inboxes, you have to write a second scraper that visits every single company website, parses the DOM, checks `mailto:` links, handles redirects, and filters out tracking assets (`.png`, Sentry, Wix tracking).

### I built and open-sourced a tool that handles both stages automatically:
1. **Stage 1**: Searches Google Maps for your niche + location and extracts verified listings.
2. **Stage 2**: Automatically visits each company's official website using high-speed HTML parsing to extract **contact emails, secondary phone numbers, and social links (LinkedIn, Facebook, Instagram)**.
3. **Stage 3**: Cleans the data and exports directly to a structured CSV and JSON file.

### Here's what the output looks like (Sample: Austin Roofing):
- **Business**: Greater Austin Roof Pros
- **Category**: Roofing contractor
- **Phone**: (512) 555-0199
- **Website**: https://www.austinroofpros.com
- **Emails**: contact@austinroofpros.com; estimates@austinroofpros.com
- **Socials**: LinkedIn, Facebook, Instagram links
- **Rating**: 4.9 ⭐ (218 reviews)

### How to use it for free:
I open-sourced the Python and Node.js code on GitHub, and configured a **free tier for the first 50 leads** (no credit card needed):

👉 **GitHub Repo**: https://github.com/Ansarii/free-google-maps-lead-scraper

If you don't want to run local code, you can also run it directly in your browser with 1 click on the Apify Store (every new account gets $5 free monthly credit which easily covers 50-100 leads free):
👉 **Cloud Runner**: https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher

If anyone needs help setting this up in n8n or Clay to automate daily lead lists, drop a comment below and I'll share the webhook JSON!
