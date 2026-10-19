# Reddit Community Post: r/webscraping, r/Python & r/javascript

**Target Subreddits**:
- `r/webscraping`
- `r/Python`
- `r/javascript`
- `r/SaaS`

---

## 📌 Post Title:
**How we solved the Google Maps Consent Dialog + Infinite Feed pagination without burning 10GB of RAM (Free Python & Node.js scripts)**

---

## 📝 Post Body:

Hey r/webscraping,

Building a reliable Google Maps scraper usually runs into three frustrating engineering bottlenecks:
1. **The Google Consent Wall**: When querying Maps via headless browsers, Google throws localized consent modal overlays (`consent.google.com`) that block the feed from rendering.
2. **Infinite Scroll Virtualization**: The Google Maps results feed (`div[role="feed"]`) aggressively unmounts off-screen DOM nodes as you scroll down.
3. **The Browser Overhead Trap**: Launching 20 Chromium browser tabs to visit company websites for email scraping drains memory (2GB–4GB RAM) and takes minutes per batch.

### How we solved it:

#### 1. Forced Query Parameters for Consent Bypassing
Instead of relying on fragile `div > button:has-text("Accept All")` DOM selectors across 50 international Google domains, appending `&hl=en&gl=us` directly to the search URL standardizes the DOM structure and minimizes regional cookie modals.

#### 2. Decoupled Playwright + Cheerio Architecture
Rather than opening full Chromium instances to scrape company websites for contact details:
- We use a single, lightweight Playwright crawler strictly to scroll the Google Maps feed and collect place URLs.
- Once the URLs are collected, website email & social extraction is handled via asynchronous **Cheerio + Axios** HTTP requests with strict 3-second timeouts. 
- Memory usage drops from 2048 MB to **under 256 MB**, and execution speed is ~15x faster.

#### 3. RegEx & False-Positive Email Sanitization
Naive regex (`\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`) pulls tons of garbage from modern SPAs:
- Image filenames (`logo@2x.png`, `icon.svg`)
- Analytics/Crashlytics hashes (`sentry.io`, `wixpress.com`)
- Placeholder strings (`user@domain.com`, `example.com`)

Our scraper applies strict exclusion filters and also inspects `mailto:` attributes in the DOM.

### Free Open-Source Repository:
We packaged the entire pipeline into clean, ready-to-run Python and Node.js CLI scripts with direct CSV and JSON export:

👉 **GitHub**: https://github.com/Ansarii/free-google-maps-lead-scraper

For anyone who wants to run it in the cloud without configuring proxies locally, we set up a free tier for the first 50 leads:
👉 **Apify Store**: https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher

Would love to get feedback on the email filtering regex and edge cases you've encountered with Google Maps feeds!
