#!/usr/bin/env node
/**
 * Free Google Maps B2B Lead Scraper & Contact Email Extractor (Node.js)
 * ====================================================================
 * Extracts businesses, direct phone numbers, websites, physical addresses,
 * ratings, review counts, plus direct contact emails and social media links.
 *
 * Powered by Apify Actor: neon_innovation_lab/google-maps-b2b-lead-enricher
 * First 50 leads are 100% FREE (covered under Apify's $5.00/mo free credit).
 */

import fs from 'node:fs';
import path from 'node:path';
import { ApifyClient } from 'apify-client';
import dotenv from 'dotenv';

dotenv.config();

const APIFY_TOKEN = process.env.APIFY_TOKEN;

if (!APIFY_TOKEN || APIFY_TOKEN === 'your_apify_api_token_here') {
  console.log('\n' + '='.repeat(70));
  console.log('⚠️  APIFY_TOKEN NOT FOUND!');
  console.log('To run this scraper with the First 50 Leads Free Tier:');
  console.log('1. Sign up for a free account at: https://console.apify.com/');
  console.log('2. Copy your API token from: https://console.apify.com/account/integrations');
  console.log('3. Set it in your terminal:');
  console.log('   export APIFY_TOKEN="your_token_here"');
  console.log('   Or add it to a .env file:');
  console.log('   APIFY_TOKEN=your_token_here');
  console.log('='.repeat(70) + '\n');
  process.exit(1);
}

// Parse simple CLI flags
const args = process.argv.slice(2);
function getArg(flag, defaultValue) {
  const index = args.indexOf(flag);
  if (index !== -1 && args[index + 1]) {
    return args[index + 1];
  }
  return defaultValue;
}

const query = getArg('--query', 'Coffee shops in Austin, TX');
const limit = parseInt(getArg('--limit', '50'), 10);
const country = getArg('--country', 'us');
const outputCsv = getArg('--output-csv', 'leads.csv');
const outputJson = getArg('--output-json', 'leads.json');

console.log('\n🚀 Starting Free Google Maps Lead Scraper (Node.js)...');
console.log(`🔍 Search Query : "${query}"`);
console.log(`📊 Target Limit : ${limit} leads (First 50 leads free tier)`);
console.log(`🌍 Country Code : ${country}`);
console.log(`✉️  Deep Enrich  : true (visiting company websites for emails & socials)\n`);

const client = new ApifyClient({ token: APIFY_TOKEN });

const runInput = {
  searchQueries: [query],
  maxResultsPerQuery: limit,
  extractEmailsAndSocials: true,
  countryCode: country,
};

const actorId = 'neon_innovation_lab/google-maps-b2b-lead-enricher';

try {
  console.log(`⏳ Calling Apify Actor (${actorId})...`);
  const run = await client.actor(actorId).call(runInput);

  if (!run || run.status !== 'SUCCEEDED') {
    console.error(`❌ Actor run ended with status: ${run ? run.status : 'UNKNOWN'}`);
    process.exit(1);
  }

  const { items } = await client.dataset(run.defaultDatasetId).listItems();

  const totalExtracted = items.length;
  const leadsWithEmail = items.filter((l) => Array.isArray(l.emails) && l.emails.length > 0);
  const leadsWithPhone = items.filter((l) => Boolean(l.phone));

  console.log('\n' + '='.repeat(70));
  console.log(`🎉 EXTRACTION COMPLETE! Successfully scraped ${totalExtracted} businesses.`);
  console.log(`✉️  Leads with verified contact emails: ${leadsWithEmail.length}`);
  console.log(`📞 Leads with phone numbers:          ${leadsWithPhone.length}`);
  console.log('='.repeat(70) + '\n');

  // 1. Export JSON
  fs.writeFileSync(outputJson, JSON.stringify(items, null, 2), 'utf-8');

  // 2. Export CSV
  const headers = [
    'title',
    'category',
    'address',
    'phone',
    'website',
    'emails',
    'rating',
    'reviewsCount',
    'linkedin',
    'instagram',
    'facebook',
    'twitter',
    'youtube',
    'googleMapsUrl',
    'query',
    'scrapedAt',
  ];

  const escapeCsv = (str) => {
    if (str === null || str === undefined) return '""';
    const clean = String(str).replace(/"/g, '""');
    return `"${clean}"`;
  };

  const csvRows = [headers.join(',')];
  for (const item of items) {
    const socials = item.socials || {};
    const row = [
      escapeCsv(item.title),
      escapeCsv(item.category),
      escapeCsv(item.address),
      escapeCsv(item.phone),
      escapeCsv(item.website),
      escapeCsv((item.emails || []).join('; ')),
      escapeCsv(item.rating),
      escapeCsv(item.reviewsCount),
      escapeCsv(socials.linkedin),
      escapeCsv(socials.instagram),
      escapeCsv(socials.facebook),
      escapeCsv(socials.twitter),
      escapeCsv(socials.youtube),
      escapeCsv(item.googleMapsUrl),
      escapeCsv(item.query),
      escapeCsv(item.scrapedAt),
    ];
    csvRows.push(row.join(','));
  }

  fs.writeFileSync(outputCsv, csvRows.join('\n'), 'utf-8');

  console.log(`💾 Saved leads to CSV : ${outputCsv}`);
  console.log(`💾 Saved leads to JSON: ${outputJson}\n`);

  console.log('📋 Preview of first 3 leads:');
  items.slice(0, 3).forEach((item, idx) => {
    const emails = (item.emails || []).join(', ') || 'None';
    const rating = item.rating ? `${item.rating} ⭐ (${item.reviewsCount} reviews)` : 'N/A';
    console.log(`\n  #${idx + 1} ${item.title}`);
    console.log(`     Category: ${item.category || 'N/A'}`);
    console.log(`     Phone   : ${item.phone || 'None'}`);
    console.log(`     Emails  : ${emails}`);
    console.log(`     Website : ${item.website || 'None'}`);
    console.log(`     Rating  : ${rating}`);
    console.log(`     Address : ${item.address || 'N/A'}`);
  });

  console.log('\n' + '-'.repeat(70));
  console.log('⭐ Like this tool? Star the repo & leave a review on Apify Store:');
  console.log('👉 https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher');
  console.log('-'.repeat(70) + '\n');
} catch (err) {
  console.error('\n❌ Error during extraction:', err.message);
  process.exit(1);
}
