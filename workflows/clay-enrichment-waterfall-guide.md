# Clay Table Waterfall Enrichment Guide

How to integrate **`neon_innovation_lab/google-maps-b2b-lead-enricher`** directly into your **Clay** tables as a custom HTTP API enrichment column.

---

## Why Connect via HTTP API in Clay?

Native Clay enrichment waterfalls charge 1 to 2 Clay credits per row (equivalent to **$0.05 to $0.10 per contact**). 

By connecting our synchronous Apify endpoint directly inside Clay:
- You pay only **$0.007 per lead** (90% savings).
- You get verified company emails, direct phones, and full social media profiles (LinkedIn, Facebook, Instagram) injected directly into your Clay table columns.

---

## Step-by-Step Setup in Clay

### 1. In your Clay Table, Add an Action Column
- Click **Add Column** -> **Enrich Data** -> Select **HTTP API**.

### 2. Configure HTTP Settings:
- **Method**: `POST`
- **URL**:
  ```text
  https://api.apify.com/v2/acts/neon_innovation_lab~google-maps-b2b-lead-enricher/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN
  ```
  *(Replace `YOUR_APIFY_TOKEN` with your personal Apify token from [console.apify.com/account/integrations](https://console.apify.com/account/integrations))*

### 3. Configure Headers:
- `Content-Type`: `application/json`

### 4. Configure Body (JSON Payload):
```json
{
  "searchQueries": ["{{/Niche/}} in {{/City/}}"],
  "maxResultsPerQuery": 10,
  "extractEmailsAndSocials": true,
  "countryCode": "us"
}
```

### 5. Map the Output Columns:
Clay will automatically parse the returned JSON array. Map the following fields to new columns:
- `data[0].emails` -> **Company Emails**
- `data[0].phone` -> **Direct Phone**
- `data[0].socials.linkedin` -> **Company LinkedIn URL**
- `data[0].website` -> **Official Website**
- `data[0].rating` -> **Google Star Rating**
- `data[0].reviewsCount` -> **Total Reviews**

---

## 🚀 Pro Tip for Outbound Sequences

Filter your Clay table for rows where `Company Emails` is not empty, and pass them directly to the **Smartlead** or **Instantly** integration in Clay to run hyper-targeted, high-reply cold email campaigns!
