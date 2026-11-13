#!/usr/bin/env python3
"""
Free Google Maps B2B Lead Scraper & Contact Email Extractor
===========================================================
Extracts businesses, direct phone numbers, websites, physical addresses,
ratings, review counts, plus direct contact emails and social media links.

Powered by the Apify Actor: neon_innovation_lab/google-maps-b2b-lead-enricher
First 50 leads are 100% FREE (covered under Apify's $5.00/mo free tier).
"""

import os
import sys
import csv
import json
import argparse
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    from apify_client import ApifyClient
except ImportError:
    print("\n❌ Missing dependency: 'apify-client'")
    print("👉 Install it with: pip install apify-client python-dotenv\n")
    sys.exit(1)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Free Google Maps B2B Lead Scraper & Email Extractor",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        default="Roofers in Austin, TX",
        help="Search query combining niche and location (e.g. 'Coffee shops in Austin, TX', 'Plumbers in Dallas, TX')",
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=50,
        help="Max leads to extract (First 50 leads free tier!)",
    )
    parser.add_argument(
        "--country", "-c",
        type=str,
        default="us",
        help="Two-letter country code (e.g. 'us', 'gb', 'ca', 'au')",
    )
    parser.add_argument(
        "--enrich", "-e",
        action="store_true",
        default=True,
        help="Deep website visit to scrape contact emails and social profiles",
    )
    parser.add_argument(
        "--output-csv",
        type=str,
        default="leads.csv",
        help="Path to save output CSV file",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default="leads.json",
        help="Path to save output JSON file",
    )
    return parser.parse_args()


def export_to_csv(leads: List[Dict[str, Any]], filepath: str) -> None:
    if not leads:
        return

    fieldnames = [
        "title",
        "category",
        "address",
        "phone",
        "website",
        "emails",
        "rating",
        "reviewsCount",
        "linkedin",
        "instagram",
        "facebook",
        "twitter",
        "youtube",
        "googleMapsUrl",
        "query",
        "scrapedAt",
    ]

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for lead in leads:
            socials = lead.get("socials") or {}
            row = {
                "title": lead.get("title", ""),
                "category": lead.get("category", ""),
                "address": lead.get("address", ""),
                "phone": lead.get("phone", ""),
                "website": lead.get("website", ""),
                "emails": "; ".join(lead.get("emails") or []),
                "rating": lead.get("rating", ""),
                "reviewsCount": lead.get("reviewsCount", ""),
                "linkedin": socials.get("linkedin", ""),
                "instagram": socials.get("instagram", ""),
                "facebook": socials.get("facebook", ""),
                "twitter": socials.get("twitter", ""),
                "youtube": socials.get("youtube", ""),
                "googleMapsUrl": lead.get("googleMapsUrl", ""),
                "query": lead.get("query", ""),
                "scrapedAt": lead.get("scrapedAt", ""),
            }
            writer.writerow(row)


def main() -> None:
    args = parse_arguments()

    api_token = os.getenv("APIFY_TOKEN")
    if not api_token or api_token == "your_apify_api_token_here":
        print("\n" + "=" * 70)
        print("⚠️  APIFY_TOKEN NOT FOUND!")
        print("To run this scraper with the First 50 Leads Free Tier:")
        print("1. Sign up for a free account at: https://console.apify.com/")
        print("2. Copy your API token from: https://console.apify.com/account/integrations")
        print("3. Export it in your terminal:")
        print("   export APIFY_TOKEN=\"your_token_here\"")
        print("   Or add it to a .env file:")
        print("   APIFY_TOKEN=your_token_here")
        print("=" * 70 + "\n")
        sys.exit(1)

    print("\n🚀 Starting Free Google Maps Lead Scraper...")
    print(f"🔍 Search Query : '{args.query}'")
    print(f"📊 Target Limit : {args.limit} leads (First 50 leads free tier)")
    print(f"🌍 Country Code : {args.country}")
    print(f"✉️  Deep Enrich  : {args.enrich} (visiting company websites for emails & socials)\n")

    client = ApifyClient(api_token)

    run_input = {
        "searchQueries": [args.query],
        "maxResultsPerQuery": args.limit,
        "extractEmailsAndSocials": args.enrich,
        "countryCode": args.country,
    }

    actor_id = "neon_innovation_lab/google-maps-b2b-lead-enricher"

    try:
        print(f"⏳ Calling Apify Actor ({actor_id})...")
        run = client.actor(actor_id).call(run_input=run_input)

        if not run or run.get("status") != "SUCCEEDED":
            print(f"❌ Actor run ended with status: {run.get('status') if run else 'UNKNOWN'}")
            sys.exit(1)

        dataset_id = run["defaultDatasetId"]
        dataset_items = list(client.dataset(dataset_id).iterate_items())

        total_extracted = len(dataset_items)
        leads_with_email = [l for l in dataset_items if l.get("emails") and len(l["emails"]) > 0]
        leads_with_phone = [l for l in dataset_items if l.get("phone")]

        print("\n" + "=" * 70)
        print(f"🎉 EXTRACTION COMPLETE! Successfully scraped {total_extracted} businesses.")
        print(f"✉️  Leads with verified contact emails: {len(leads_with_email)}")
        print(f"📞 Leads with phone numbers:          {len(leads_with_phone)}")
        print("=" * 70 + "\n")

        # Export files
        export_to_csv(dataset_items, args.output_csv)
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump(dataset_items, f, indent=2, ensure_ascii=False)

        print(f"💾 Saved leads to CSV : {args.output_csv}")
        print(f"💾 Saved leads to JSON: {args.output_json}\n")

        # Print top 5 preview
        print("📋 Preview of first 3 leads:")
        for idx, item in enumerate(dataset_items[:3], 1):
            emails = ", ".join(item.get("emails") or []) or "None"
            phone = item.get("phone") or "None"
            rating = f"{item.get('rating')} ⭐ ({item.get('reviewsCount')} reviews)" if item.get("rating") else "N/A"
            print(f"\n  #{idx} {item.get('title')}")
            print(f"     Category: {item.get('category')}")
            print(f"     Phone   : {phone}")
            print(f"     Emails  : {emails}")
            print(f"     Website : {item.get('website') or 'None'}")
            print(f"     Rating  : {rating}")
            print(f"     Address : {item.get('address')}")

        print("\n" + "-" * 70)
        print("⭐ Like this tool? Star the repo & leave a review on Apify Store:")
        print("👉 https://apify.com/neon_innovation_lab/google-maps-b2b-lead-enricher")
        print("-" * 70 + "\n")

    except Exception as e:
        print(f"\n❌ Error during extraction: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
