"""
Marketing Intelligence Dashboard - Data Processing Module
This module loads and processes the marketing and business data for the dashboard
"""
import csv
import json
from datetime import datetime
from collections import defaultdict, OrderedDict
import os

class DataProcessor:
    def __init__(self, data_dir="/home/runner/work/BI_Dasboard/BI_Dasboard/data"):
        self.data_dir = data_dir
        self.facebook_data = []
        self.google_data = []
        self.tiktok_data = []
        self.business_data = []
        
    def load_data(self):
        """Load all CSV data files"""
        self.facebook_data = self._load_csv("facebook.csv")
        self.google_data = self._load_csv("google.csv")
        self.tiktok_data = self._load_csv("tiktok.csv")
        self.business_data = self._load_csv("business.csv")
        
    def _load_csv(self, filename):
        """Load a CSV file and return data as list of dictionaries"""
        filepath = os.path.join(self.data_dir, filename)
        data = []
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    
    def get_combined_marketing_data(self):
        """Combine all marketing platform data with platform column"""
        combined = []
        
        for row in self.facebook_data:
            row_copy = row.copy()
            row_copy['platform'] = 'Facebook'
            combined.append(row_copy)
            
        for row in self.google_data:
            row_copy = row.copy()
            row_copy['platform'] = 'Google'
            combined.append(row_copy)
            
        for row in self.tiktok_data:
            row_copy = row.copy()
            row_copy['platform'] = 'TikTok'
            combined.append(row_copy)
            
        return combined
    
    def calculate_daily_metrics(self):
        """Calculate key daily metrics for dashboard"""
        marketing_data = self.get_combined_marketing_data()
        
        # Group marketing data by date
        daily_marketing = defaultdict(lambda: {
            'impressions': 0,
            'clicks': 0,
            'spend': 0.0,
            'attributed_revenue': 0.0,
            'facebook_spend': 0.0,
            'google_spend': 0.0,
            'tiktok_spend': 0.0,
            'facebook_revenue': 0.0,
            'google_revenue': 0.0,
            'tiktok_revenue': 0.0
        })
        
        for row in marketing_data:
            date = row['date']
            platform = row['platform'].lower()
            
            daily_marketing[date]['impressions'] += int(row['impressions'])
            daily_marketing[date]['clicks'] += int(row['clicks'])
            daily_marketing[date]['spend'] += float(row['spend'])
            daily_marketing[date]['attributed_revenue'] += float(row['attributed_revenue'])
            daily_marketing[date][f'{platform}_spend'] += float(row['spend'])
            daily_marketing[date][f'{platform}_revenue'] += float(row['attributed_revenue'])
        
        # Combine with business data
        business_dict = {row['date']: row for row in self.business_data}
        
        result = []
        for date in sorted(daily_marketing.keys()):
            marketing = daily_marketing[date]
            business = business_dict.get(date, {})
            
            # Calculate derived metrics
            ctr = (marketing['clicks'] / marketing['impressions']) * 100 if marketing['impressions'] > 0 else 0
            cpc = marketing['spend'] / marketing['clicks'] if marketing['clicks'] > 0 else 0
            roas = marketing['attributed_revenue'] / marketing['spend'] if marketing['spend'] > 0 else 0
            
            total_revenue = float(business.get('total_revenue', 0))
            marketing_attribution = (marketing['attributed_revenue'] / total_revenue) * 100 if total_revenue > 0 else 0
            
            result.append({
                'date': date,
                'impressions': marketing['impressions'],
                'clicks': marketing['clicks'],
                'spend': round(marketing['spend'], 2),
                'attributed_revenue': round(marketing['attributed_revenue'], 2),
                'ctr': round(ctr, 3),
                'cpc': round(cpc, 2),
                'roas': round(roas, 2),
                'orders': int(business.get('orders', 0)),
                'new_customers': int(business.get('new_customers', 0)),
                'total_revenue': round(total_revenue, 2),
                'gross_profit': round(float(business.get('gross_profit', 0)), 2),
                'marketing_attribution': round(marketing_attribution, 1),
                'facebook_spend': round(marketing['facebook_spend'], 2),
                'google_spend': round(marketing['google_spend'], 2),
                'tiktok_spend': round(marketing['tiktok_spend'], 2),
                'facebook_revenue': round(marketing['facebook_revenue'], 2),
                'google_revenue': round(marketing['google_revenue'], 2),
                'tiktok_revenue': round(marketing['tiktok_revenue'], 2)
            })
            
        return result
    
    def get_platform_performance(self):
        """Get platform-level performance metrics"""
        marketing_data = self.get_combined_marketing_data()
        
        platform_metrics = defaultdict(lambda: {
            'impressions': 0,
            'clicks': 0,
            'spend': 0.0,
            'attributed_revenue': 0.0,
            'campaigns': set()
        })
        
        for row in marketing_data:
            platform = row['platform']
            platform_metrics[platform]['impressions'] += int(row['impressions'])
            platform_metrics[platform]['clicks'] += int(row['clicks'])
            platform_metrics[platform]['spend'] += float(row['spend'])
            platform_metrics[platform]['attributed_revenue'] += float(row['attributed_revenue'])
            platform_metrics[platform]['campaigns'].add(row['campaign'])
        
        result = []
        for platform, metrics in platform_metrics.items():
            ctr = (metrics['clicks'] / metrics['impressions']) * 100 if metrics['impressions'] > 0 else 0
            cpc = metrics['spend'] / metrics['clicks'] if metrics['clicks'] > 0 else 0
            roas = metrics['attributed_revenue'] / metrics['spend'] if metrics['spend'] > 0 else 0
            
            result.append({
                'platform': platform,
                'impressions': metrics['impressions'],
                'clicks': metrics['clicks'],
                'spend': round(metrics['spend'], 2),
                'attributed_revenue': round(metrics['attributed_revenue'], 2),
                'ctr': round(ctr, 3),
                'cpc': round(cpc, 2),
                'roas': round(roas, 2),
                'campaigns': len(metrics['campaigns'])
            })
        
        return sorted(result, key=lambda x: x['spend'], reverse=True)
    
    def get_campaign_performance(self):
        """Get campaign-level performance metrics"""
        marketing_data = self.get_combined_marketing_data()
        
        campaign_metrics = defaultdict(lambda: {
            'impressions': 0,
            'clicks': 0,
            'spend': 0.0,
            'attributed_revenue': 0.0,
            'platform': ''
        })
        
        for row in marketing_data:
            campaign = row['campaign']
            campaign_metrics[campaign]['impressions'] += int(row['impressions'])
            campaign_metrics[campaign]['clicks'] += int(row['clicks'])
            campaign_metrics[campaign]['spend'] += float(row['spend'])
            campaign_metrics[campaign]['attributed_revenue'] += float(row['attributed_revenue'])
            campaign_metrics[campaign]['platform'] = row['platform']
        
        result = []
        for campaign, metrics in campaign_metrics.items():
            ctr = (metrics['clicks'] / metrics['impressions']) * 100 if metrics['impressions'] > 0 else 0
            cpc = metrics['spend'] / metrics['clicks'] if metrics['clicks'] > 0 else 0
            roas = metrics['attributed_revenue'] / metrics['spend'] if metrics['spend'] > 0 else 0
            
            result.append({
                'campaign': campaign,
                'platform': metrics['platform'],
                'impressions': metrics['impressions'],
                'clicks': metrics['clicks'],
                'spend': round(metrics['spend'], 2),
                'attributed_revenue': round(metrics['attributed_revenue'], 2),
                'ctr': round(ctr, 3),
                'cpc': round(cpc, 2),
                'roas': round(roas, 2)
            })
        
        return sorted(result, key=lambda x: x['spend'], reverse=True)
    
    def get_summary_metrics(self):
        """Get overall summary metrics"""
        daily_data = self.calculate_daily_metrics()
        
        if not daily_data:
            return {}
        
        total_spend = sum(row['spend'] for row in daily_data)
        total_attributed_revenue = sum(row['attributed_revenue'] for row in daily_data)
        total_revenue = sum(row['total_revenue'] for row in daily_data)
        total_orders = sum(row['orders'] for row in daily_data)
        total_new_customers = sum(row['new_customers'] for row in daily_data)
        total_impressions = sum(row['impressions'] for row in daily_data)
        total_clicks = sum(row['clicks'] for row in daily_data)
        
        avg_ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
        avg_cpc = total_spend / total_clicks if total_clicks > 0 else 0
        overall_roas = total_attributed_revenue / total_spend if total_spend > 0 else 0
        cpa = total_spend / total_new_customers if total_new_customers > 0 else 0
        
        return {
            'total_spend': round(total_spend, 2),
            'total_attributed_revenue': round(total_attributed_revenue, 2),
            'total_revenue': round(total_revenue, 2),
            'total_orders': total_orders,
            'total_new_customers': total_new_customers,
            'total_impressions': total_impressions,
            'total_clicks': total_clicks,
            'avg_ctr': round(avg_ctr, 3),
            'avg_cpc': round(avg_cpc, 2),
            'overall_roas': round(overall_roas, 2),
            'cpa': round(cpa, 2),
            'attribution_rate': round((total_attributed_revenue / total_revenue) * 100, 1) if total_revenue > 0 else 0
        }
    
    def export_dashboard_data(self, output_file="/home/runner/work/BI_Dasboard/BI_Dasboard/dashboard_data.json"):
        """Export processed data for dashboard"""
        data = {
            'summary': self.get_summary_metrics(),
            'daily_metrics': self.calculate_daily_metrics(),
            'platform_performance': self.get_platform_performance(),
            'campaign_performance': self.get_campaign_performance(),
            'last_updated': datetime.now().isoformat()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        return data

def main():
    """Process data and generate dashboard JSON"""
    processor = DataProcessor()
    processor.load_data()
    
    print("Processing marketing and business data...")
    data = processor.export_dashboard_data()
    
    print(f"Dashboard data exported successfully!")
    print(f"Summary metrics:")
    summary = data['summary']
    print(f"- Total Spend: ${summary['total_spend']:,}")
    print(f"- Total Attributed Revenue: ${summary['total_attributed_revenue']:,}")
    print(f"- Overall ROAS: {summary['overall_roas']}")
    print(f"- Total Orders: {summary['total_orders']:,}")
    print(f"- Marketing Attribution Rate: {summary['attribution_rate']}%")

if __name__ == "__main__":
    main()