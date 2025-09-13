# Marketing Intelligence Dashboard

A comprehensive BI dashboard for analyzing marketing campaign performance and business outcomes across multiple platforms (Facebook, Google, TikTok).

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BI_Dasboard
   ```

2. **Generate sample data** (optional - data already included)
   ```bash
   python3 generate_data_simple.py
   ```

3. **Process data for dashboard**
   ```bash
   python3 data_processor.py
   ```

4. **Start the dashboard server**
   ```bash
   python3 server.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8000/dashboard.html`

## 📊 Dashboard Features

### Key Metrics Tracked
- **Total Marketing Spend**: $736,527 across all platforms
- **Attributed Revenue**: $834,304 from marketing campaigns  
- **Overall ROAS**: 1.13x (profitable campaigns)
- **Total Orders**: 76,636 during tracking period
- **New Customers**: 20,615 acquired customers
- **Customer Acquisition Cost**: $36 average CPA
- **Marketing Attribution**: 14% of total business revenue
- **Average CPC**: $2.14 cost per click

### Platform Performance
1. **TikTok** - Best performing with 1.64x ROAS
   - Spend: $66,680 | Revenue: $109,360
   - CTR: 1.54% | CPC: $1

2. **Facebook** - Strong performance with 1.23x ROAS
   - Spend: $184,623 | Revenue: $226,685
   - CTR: 2.02% | CPC: $2

3. **Google** - Largest spend with 1.03x ROAS
   - Spend: $485,225 | Revenue: $498,259
   - CTR: 3.49% | CPC: $2

### Visualizations
- **Summary KPI Cards**: 8 key performance indicators
- **Platform Performance Charts**: Visual comparison of spend vs revenue
- **Daily Trends**: 30-day trend analysis
- **Campaign Performance Table**: Top 10 campaigns by spend
- **Platform Summary Table**: Comprehensive platform metrics
- **Key Insights**: AI-generated business insights and recommendations

## 🏗️ Technical Architecture

### Data Pipeline
1. **Raw Data**: CSV files for each platform (facebook.csv, google.csv, tiktok.csv, business.csv)
2. **Data Processing**: Python script aggregates and calculates metrics
3. **Output**: JSON file with processed dashboard data
4. **Visualization**: HTML/CSS/JavaScript dashboard with responsive design

### Files Structure
```
BI_Dasboard/
├── data/
│   ├── facebook.csv      # Facebook campaign data
│   ├── google.csv        # Google Ads campaign data  
│   ├── tiktok.csv        # TikTok campaign data
│   └── business.csv      # Daily business metrics
├── dashboard.html        # Main dashboard interface
├── dashboard_data.json   # Processed data for dashboard
├── data_processor.py     # Data aggregation and processing
├── generate_data_simple.py # Sample data generation
├── server.py            # HTTP server for dashboard
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

### Data Schema

#### Marketing Data (Facebook, Google, TikTok)
- `date`: Campaign date (YYYY-MM-DD)
- `tactic`: Ad format/type
- `state`: Geographic state
- `campaign`: Campaign name
- `impressions`: Ad impressions
- `clicks`: Ad clicks
- `spend`: Ad spend in USD
- `attributed_revenue`: Revenue attributed to ads

#### Business Data
- `date`: Business date (YYYY-MM-DD)
- `orders`: Total daily orders
- `new_orders`: New customer orders
- `new_customers`: Newly acquired customers
- `total_revenue`: Total daily revenue
- `gross_profit`: Daily gross profit
- `cogs`: Cost of goods sold

## 📈 Key Insights & Recommendations

### 💰 Profitability Analysis
- **Overall profitable**: 1.13x ROAS indicates positive ROI
- **Every $1 spent generates $1.13 in revenue**
- Campaigns are above the 1.0 breakeven threshold

### 🏆 Platform Performance
- **TikTok outperforms**: Highest ROAS at 1.64x despite lowest spend
- **Google has scale**: Largest spend but lowest ROAS at 1.03x
- **Facebook balanced**: Good middle ground with 1.23x ROAS

### 💡 Optimization Opportunities
1. **Reallocate budget**: Shift spend from Google to TikTok for better ROI
2. **Improve attribution**: Current 14% attribution suggests measurement gaps
3. **Campaign optimization**: Focus on high-performing campaigns like "Retargeting_Feb" (1.95x ROAS)

### 📊 Attribution Insights
- Marketing directly attributes to **14%** of total business revenue
- Remaining **86%** comes from:
  - Organic traffic
  - Repeat customers  
  - Word-of-mouth
  - Other unmeasured channels

## 🔧 Technical Implementation

### Dashboard Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Data**: Loads from JSON data file
- **Interactive Elements**: Hover effects and visual feedback
- **Performance Optimized**: No external dependencies, fast loading
- **Accessibility**: Proper semantic HTML and color contrast

### Visualization Approach
- **Simple Charts**: Custom CSS-based charts (no external libraries)
- **Color Coding**: Red for spend, green for revenue, consistent throughout
- **Data Tables**: Sortable and responsive tables for detailed data
- **Insights Cards**: AI-generated insights with trend indicators

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- No external CDN dependencies
- Graceful degradation for older browsers

## 🚀 Deployment Options

### Local Development
```bash
python3 server.py
# Dashboard available at http://localhost:8000/dashboard.html
```

### Production Deployment
The dashboard can be deployed to any web hosting service:

1. **Static Hosting** (Recommended)
   - Netlify, Vercel, GitHub Pages
   - Upload HTML, JSON, and assets
   - No server-side processing required

2. **Traditional Web Server**
   - Apache, Nginx, IIS
   - Serve static files from document root

3. **Cloud Platforms**
   - AWS S3 + CloudFront
   - Google Cloud Storage
   - Azure Static Web Apps

### Environment Setup
```bash
# No external dependencies required for dashboard
# Optional: Python for data processing
pip install -r requirements.txt  # Only needed for data processing
```

## 📊 Data Sources & Attribution

### Sample Data Characteristics
- **120 days** of marketing and business data
- **Realistic metrics** based on industry benchmarks
- **Seasonal patterns** built into data generation
- **Platform-specific** performance characteristics

### Marketing Attribution Model
- **Last-click attribution** for simplicity
- **Direct revenue tracking** from campaign to conversion
- **Conservative estimates** to avoid over-attribution

## 🔮 Future Enhancements

### Short-term Improvements
- [ ] Date range filters
- [ ] Platform filtering
- [ ] Export functionality (PDF/Excel)
- [ ] Campaign deep-dive pages

### Advanced Features
- [ ] Forecasting and trend analysis
- [ ] Multi-touch attribution modeling  
- [ ] Real-time data integration
- [ ] A/B testing framework
- [ ] Automated alerting and reporting

### Technical Enhancements
- [ ] Database integration
- [ ] API endpoints for data updates
- [ ] User authentication and permissions
- [ ] Mobile app companion

## 📝 Data Methodology

### Metrics Definitions
- **ROAS**: Return on Ad Spend (Revenue ÷ Spend)
- **CTR**: Click-through Rate (Clicks ÷ Impressions × 100)
- **CPC**: Cost per Click (Spend ÷ Clicks)
- **CPA**: Customer Acquisition Cost (Spend ÷ New Customers)

### Attribution Windows
- **7-day click**: Revenue attributed within 7 days of ad click
- **1-day view**: Revenue attributed within 1 day of ad impression
- **Conservative approach**: Avoids double-counting across platforms

---

**Built for data-driven marketing decisions** 📊💡