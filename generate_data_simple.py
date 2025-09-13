"""
Generate sample marketing and business data using only standard library
"""
import csv
import random
import math
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

def generate_date_range(start_date='2024-01-01', days=120):
    """Generate date range for the datasets"""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    return [start + timedelta(days=x) for x in range(days)]

def normal_random(mean, std):
    """Simple normal distribution using Box-Muller transform"""
    if not hasattr(normal_random, "next_val"):
        normal_random.next_val = None
    
    if normal_random.next_val is not None:
        val = normal_random.next_val
        normal_random.next_val = None
        return val * std + mean
    
    u1 = random.random()
    u2 = random.random()
    
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    
    normal_random.next_val = z1
    return z0 * std + mean

def generate_facebook_data(dates):
    """Generate Facebook campaign data"""
    campaigns = ['Brand_Awareness_Q1', 'Conversion_Campaign_Jan', 'Retargeting_Feb', 'Product_Launch_Mar']
    states = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'MI', 'GA', 'NC']
    tactics = ['Video_Ads', 'Carousel_Ads', 'Single_Image', 'Collection_Ads']
    
    data = []
    for date in dates:
        for campaign in campaigns:
            # Generate 1-3 records per campaign per day
            num_records = random.randint(1, 3)
            for _ in range(num_records):
                state = random.choice(states)
                tactic = random.choice(tactics)
                
                # Base metrics with some seasonality
                day_of_year = date.timetuple().tm_yday
                seasonal_factor = 1 + 0.3 * math.sin(2 * math.pi * day_of_year / 365)
                
                impressions = int(normal_random(5000, 1500) * seasonal_factor)
                impressions = max(impressions, 100)
                
                ctr = normal_random(0.02, 0.005)  # 2% average CTR
                ctr = max(min(ctr, 0.08), 0.005)  # Cap between 0.5% and 8%
                
                clicks = int(impressions * ctr)
                
                cpc = normal_random(1.5, 0.5)  # Average $1.50 CPC
                cpc = max(cpc, 0.1)
                
                spend = clicks * cpc
                
                # Revenue attribution (conversion rate varies by campaign)
                conv_rate = {
                    'Brand_Awareness_Q1': 0.01,
                    'Conversion_Campaign_Jan': 0.025,
                    'Retargeting_Feb': 0.035,
                    'Product_Launch_Mar': 0.02
                }[campaign]
                
                conversions = sum(1 for _ in range(clicks) if random.random() < conv_rate)
                avg_order_value = normal_random(85, 25)
                avg_order_value = max(avg_order_value, 20)
                
                attributed_revenue = conversions * avg_order_value
                
                data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'tactic': tactic,
                    'state': state,
                    'campaign': campaign,
                    'impressions': impressions,
                    'clicks': clicks,
                    'spend': round(spend, 2),
                    'attributed_revenue': round(attributed_revenue, 2)
                })
    
    return data

def generate_google_data(dates):
    """Generate Google Ads campaign data"""
    campaigns = ['Search_Brand_Terms', 'Shopping_Campaigns', 'Display_Remarketing', 'YouTube_Video_Ads']
    states = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'MI', 'GA', 'NC']
    tactics = ['Search_Ads', 'Shopping_Ads', 'Display_Ads', 'Video_Ads']
    
    data = []
    for date in dates:
        for campaign in campaigns:
            num_records = random.randint(1, 2)
            for _ in range(num_records):
                state = random.choice(states)
                tactic = random.choice(tactics)
                
                day_of_year = date.timetuple().tm_yday
                seasonal_factor = 1 + 0.2 * math.sin(2 * math.pi * day_of_year / 365)
                
                impressions = int(normal_random(8000, 2000) * seasonal_factor)
                impressions = max(impressions, 200)
                
                # Google typically has higher CTR
                ctr = normal_random(0.035, 0.01)
                ctr = max(min(ctr, 0.12), 0.01)
                
                clicks = int(impressions * ctr)
                
                cpc = normal_random(2.1, 0.7)  # Higher CPC for Google
                cpc = max(cpc, 0.2)
                
                spend = clicks * cpc
                
                conv_rate = {
                    'Search_Brand_Terms': 0.04,
                    'Shopping_Campaigns': 0.028,
                    'Display_Remarketing': 0.015,
                    'YouTube_Video_Ads': 0.012
                }[campaign]
                
                conversions = sum(1 for _ in range(clicks) if random.random() < conv_rate)
                avg_order_value = normal_random(92, 30)
                avg_order_value = max(avg_order_value, 25)
                
                attributed_revenue = conversions * avg_order_value
                
                data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'tactic': tactic,
                    'state': state,
                    'campaign': campaign,
                    'impressions': impressions,
                    'clicks': clicks,
                    'spend': round(spend, 2),
                    'attributed_revenue': round(attributed_revenue, 2)
                })
    
    return data

def generate_tiktok_data(dates):
    """Generate TikTok campaign data"""
    campaigns = ['Gen_Z_Outreach', 'Trend_Challenge', 'Influencer_Collab', 'Product_Demo_Videos']
    states = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'MI', 'GA', 'NC']
    tactics = ['In_Feed_Ads', 'Spark_Ads', 'TopView_Ads', 'Branded_Hashtag']
    
    data = []
    for date in dates:
        for campaign in campaigns:
            if random.random() < 0.7:  # TikTok campaigns might not run every day
                state = random.choice(states)
                tactic = random.choice(tactics)
                
                day_of_year = date.timetuple().tm_yday
                seasonal_factor = 1 + 0.4 * math.sin(2 * math.pi * day_of_year / 365)
                
                impressions = int(normal_random(12000, 4000) * seasonal_factor)
                impressions = max(impressions, 500)
                
                # TikTok has high engagement but lower CTR to website
                ctr = normal_random(0.015, 0.008)
                ctr = max(min(ctr, 0.06), 0.005)
                
                clicks = int(impressions * ctr)
                
                cpc = normal_random(0.8, 0.3)  # Lower CPC for TikTok
                cpc = max(cpc, 0.1)
                
                spend = clicks * cpc
                
                conv_rate = {
                    'Gen_Z_Outreach': 0.018,
                    'Trend_Challenge': 0.022,
                    'Influencer_Collab': 0.025,
                    'Product_Demo_Videos': 0.02
                }[campaign]
                
                conversions = sum(1 for _ in range(clicks) if random.random() < conv_rate)
                avg_order_value = normal_random(65, 20)  # Lower AOV for younger audience
                avg_order_value = max(avg_order_value, 15)
                
                attributed_revenue = conversions * avg_order_value
                
                data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'tactic': tactic,
                    'state': state,
                    'campaign': campaign,
                    'impressions': impressions,
                    'clicks': clicks,
                    'spend': round(spend, 2),
                    'attributed_revenue': round(attributed_revenue, 2)
                })
    
    return data

def generate_business_data(dates):
    """Generate daily business performance data"""
    data = []
    
    # Initialize some baseline metrics
    base_orders = 450
    base_new_customers = 120
    
    for i, date in enumerate(dates):
        day_of_year = date.timetuple().tm_yday
        day_of_week = date.weekday()
        
        # Seasonal and weekly patterns
        seasonal_factor = 1 + 0.25 * math.sin(2 * math.pi * day_of_year / 365)
        weekend_factor = 1.2 if day_of_week in [5, 6] else 1.0  # Higher weekend sales
        
        # Growth trend over time
        growth_factor = 1 + (i / len(dates)) * 0.3  # 30% growth over 120 days
        
        total_factor = seasonal_factor * weekend_factor * growth_factor
        
        # Generate metrics with correlation to marketing spend
        orders = int(normal_random(base_orders * total_factor, 50))
        orders = max(orders, 50)
        
        new_orders_rate = normal_random(0.35, 0.05)  # 35% new orders
        new_orders_rate = max(min(new_orders_rate, 0.6), 0.2)
        new_orders = int(orders * new_orders_rate)
        
        new_customers = min(new_orders, int(normal_random(base_new_customers * total_factor, 20)))
        new_customers = max(new_customers, 20)
        
        avg_order_value = normal_random(78, 25)
        avg_order_value = max(avg_order_value, 20)
        
        total_revenue = orders * avg_order_value
        
        # COGS varies by product mix
        cogs_rate = normal_random(0.45, 0.05)  # 45% COGS
        cogs_rate = max(min(cogs_rate, 0.65), 0.3)
        cogs = total_revenue * cogs_rate
        
        gross_profit = total_revenue - cogs
        
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'orders': orders,
            'new_orders': new_orders,
            'new_customers': new_customers,
            'total_revenue': round(total_revenue, 2),
            'gross_profit': round(gross_profit, 2),
            'cogs': round(cogs, 2)
        })
    
    return data

def write_csv(filename, data, fieldnames):
    """Write data to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    """Generate all datasets and save to CSV files"""
    print("Generating sample data for Marketing Intelligence Dashboard...")
    
    # Generate date range
    dates = generate_date_range()
    print(f"Date range: {dates[0].strftime('%Y-%m-%d')} to {dates[-1].strftime('%Y-%m-%d')}")
    
    # Generate datasets
    print("Generating Facebook data...")
    facebook_data = generate_facebook_data(dates)
    write_csv('/home/runner/work/BI_Dasboard/BI_Dasboard/data/facebook.csv', facebook_data, 
              ['date', 'tactic', 'state', 'campaign', 'impressions', 'clicks', 'spend', 'attributed_revenue'])
    print(f"Facebook data: {len(facebook_data)} records")
    
    print("Generating Google data...")
    google_data = generate_google_data(dates)
    write_csv('/home/runner/work/BI_Dasboard/BI_Dasboard/data/google.csv', google_data,
              ['date', 'tactic', 'state', 'campaign', 'impressions', 'clicks', 'spend', 'attributed_revenue'])
    print(f"Google data: {len(google_data)} records")
    
    print("Generating TikTok data...")
    tiktok_data = generate_tiktok_data(dates)
    write_csv('/home/runner/work/BI_Dasboard/BI_Dasboard/data/tiktok.csv', tiktok_data,
              ['date', 'tactic', 'state', 'campaign', 'impressions', 'clicks', 'spend', 'attributed_revenue'])
    print(f"TikTok data: {len(tiktok_data)} records")
    
    print("Generating Business data...")
    business_data = generate_business_data(dates)
    write_csv('/home/runner/work/BI_Dasboard/BI_Dasboard/data/business.csv', business_data,
              ['date', 'orders', 'new_orders', 'new_customers', 'total_revenue', 'gross_profit', 'cogs'])
    print(f"Business data: {len(business_data)} records")
    
    print("\nData generation complete!")
    print("Files saved in /data/ directory:")
    print("- facebook.csv")
    print("- google.csv") 
    print("- tiktok.csv")
    print("- business.csv")

if __name__ == "__main__":
    main()