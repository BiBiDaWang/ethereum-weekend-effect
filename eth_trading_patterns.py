"""
Ethereum Trading Patterns Analysis
Analyzes weekend/weekday and holiday effects on Ethereum blockchain activity

Author:Yuyan Kuang
Date: January 2026
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import time
import os

# Set up plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class EtherscanDataFetcher:
    """Fetches data from Etherscan API"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.etherscan.io/v2/api"
        self.chainid = '1'  # Ethereum mainnet
    
    def get_daily_transaction_count(self, date):
        """
        Get transaction count for a specific date
        
        Parameters:
        date (datetime): The date to fetch data for
        
        Returns:
        dict: Contains date and transaction count
        """
        # Convert date to unix timestamp (start and end of day)
        start_timestamp = int(date.replace(hour=0, minute=0, second=0).timestamp())
        end_timestamp = int(date.replace(hour=23, minute=59, second=59).timestamp())
        
        # Etherscan API parameters
        params = {
            'module': 'proxy',
            'action': 'eth_getBlockByNumber',
            'tag': 'latest',
            'boolean': 'true',
            'apikey': self.api_key
        }
        
        # Note: This is a simplified approach. For accurate daily counts,
        # we'll actually fetch block data and count transactions
        # We'll get the block number for start and end of day, then count transactions
        
        try:
            # Get block number at start of day
            start_block = self._get_block_by_timestamp(start_timestamp, 'after')
            # Get block number at end of day
            end_block = self._get_block_by_timestamp(end_timestamp, 'before')
            
            if start_block and end_block:
                # For simplicity, we'll estimate transaction count
                # In a real analysis, you'd sum up all transactions in blocks
                tx_count = self._estimate_tx_count(start_block, end_block)
                
                return {
                    'date': date.strftime('%Y-%m-%d'),
                    'tx_count': tx_count,
                    'start_block': start_block,
                    'end_block': end_block
                }
            
        except Exception as e:
            print(f"Error fetching data for {date.strftime('%Y-%m-%d')}: {str(e)}")
            return None
    
    def _get_block_by_timestamp(self, timestamp, closest='before'):
        """Get block number closest to a timestamp"""
        params = {
            'chainid': self.chainid,
            'module': 'block',
            'action': 'getblocknobytime',
            'timestamp': timestamp,
            'closest': closest,
            'apikey': self.api_key
        }
        
        response = requests.get(self.base_url, params=params)
        data = response.json()
        
        if data['status'] == '1':
            return int(data['result'])
        return None
    
    def _estimate_tx_count(self, start_block, end_block):
        """
        Estimate transaction count between two blocks
        This is a simplified version - samples a few blocks and estimates
        """
        # Sample 5 blocks evenly distributed
        sample_blocks = []
        step = max(1, (end_block - start_block) // 5)
        
        for i in range(5):
            block_num = start_block + (i * step)
            if block_num <= end_block:
                sample_blocks.append(block_num)
        
        total_tx = 0
        valid_samples = 0
        
        for block_num in sample_blocks:
            tx_count = self._get_block_tx_count(block_num)
            if tx_count is not None:
                total_tx += tx_count
                valid_samples += 1
            time.sleep(0.2)  # Rate limiting
        
        if valid_samples > 0:
            avg_tx_per_block = total_tx / valid_samples
            total_blocks = end_block - start_block + 1
            return int(avg_tx_per_block * total_blocks)
        
        return 0
    
    def _get_block_tx_count(self, block_num):
        """Get transaction count for a specific block"""
        params = {
            'chainid': self.chainid,
            'module': 'proxy',
            'action': 'eth_getBlockByNumber',
            'tag': hex(block_num),
            'boolean': 'false',
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if 'result' in data and data['result']:
                transactions = data['result'].get('transactions', [])
                return len(transactions)
        except:
            pass
        
        return None


class TradingPatternAnalyzer:
    """Analyzes trading patterns from transaction data"""
    
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        if not self.df.empty:
            self.df['date'] = pd.to_datetime(self.df['date'])
            self.df['day_of_week'] = self.df['date'].dt.dayofweek
            self.df['day_name'] = self.df['date'].dt.day_name()
            self.df['is_weekend'] = self.df['day_of_week'].isin([5, 6])
            self.df['month'] = self.df['date'].dt.month
    
    def analyze_weekend_effect(self):
        """Analyze differences between weekend and weekday trading"""
        if self.df.empty:
            print("No data to analyze")
            return
        
        weekend_avg = self.df[self.df['is_weekend']]['tx_count'].mean()
        weekday_avg = self.df[~self.df['is_weekend']]['tx_count'].mean()
        
        print("\n" + "="*50)
        print("WEEKEND vs WEEKDAY ANALYSIS")
        print("="*50)
        print(f"Average weekday transactions: {weekday_avg:,.0f}")
        print(f"Average weekend transactions: {weekend_avg:,.0f}")
        print(f"Difference: {weekend_avg - weekday_avg:,.0f} ({((weekend_avg/weekday_avg - 1) * 100):.2f}%)")
        print("="*50 + "\n")
    
    def analyze_day_of_week_effect(self):
        """Analyze patterns by day of week"""
        day_stats = self.df.groupby('day_name')['tx_count'].agg(['mean', 'std', 'count'])
        
        # Reorder to start with Monday
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_stats = day_stats.reindex([day for day in day_order if day in day_stats.index])
        
        print("\n" + "="*50)
        print("DAY OF WEEK ANALYSIS")
        print("="*50)
        print(day_stats.to_string())
        print("="*50 + "\n")
        
        return day_stats
    
    def plot_weekend_comparison(self):
        """Create visualization comparing weekend vs weekday"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Box plot
        self.df['Period'] = self.df['is_weekend'].map({True: 'Weekend', False: 'Weekday'})
        sns.boxplot(data=self.df, x='Period', y='tx_count', ax=axes[0])
        axes[0].set_title('Transaction Count: Weekday vs Weekend', fontsize=14, fontweight='bold')
        axes[0].set_ylabel('Transaction Count')
        axes[0].set_xlabel('')
        
        # Bar plot by day
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_avg = self.df.groupby('day_name')['tx_count'].mean().reindex(day_order)
        
        colors = ['#1f77b4']*5 + ['#ff7f0e']*2  # Blue for weekdays, orange for weekend
        day_avg.plot(kind='bar', ax=axes[1], color=colors)
        axes[1].set_title('Average Transaction Count by Day of Week', fontsize=14, fontweight='bold')
        axes[1].set_ylabel('Average Transaction Count')
        axes[1].set_xlabel('Day of Week')
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('outputs/weekend_effect_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Saved visualization: outputs/weekend_effect_analysis.png")
        plt.close()
    
    def plot_time_series(self):
        """Plot transaction counts over time"""
        plt.figure(figsize=(14, 6))
        
        # Plot all data
        plt.plot(self.df['date'], self.df['tx_count'], alpha=0.5, linewidth=1, label='Daily transactions')
        
        # Add 7-day moving average
        self.df['ma_7'] = self.df['tx_count'].rolling(window=7, center=True).mean()
        plt.plot(self.df['date'], self.df['ma_7'], linewidth=2, color='red', label='7-day moving average')
        
        # Highlight weekends
        weekend_data = self.df[self.df['is_weekend']]
        plt.scatter(weekend_data['date'], weekend_data['tx_count'], color='orange', 
                   alpha=0.6, s=30, label='Weekend', zorder=5)
        
        plt.title('Ethereum Transaction Count Over Time (2025)', fontsize=14, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Transaction Count')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('outputs/transaction_timeseries.png', dpi=300, bbox_inches='tight')
        print("✓ Saved visualization: outputs/transaction_timeseries.png")
        plt.close()


def main():
    """Main execution function"""
    print("\n" + "="*50)
    print("ETHEREUM TRADING PATTERN ANALYSIS")
    print("="*50 + "\n")
    
    # Create outputs directory if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Get API key from environment variable or user input
    api_key = os.getenv('ETHERSCAN_API_KEY')
    
    if not api_key:
        print("Please enter your Etherscan API key:")
        print("(You can get one free at https://etherscan.io/myapikey)")
        api_key = input("API Key: ").strip()
    
    # Initialize fetcher
    fetcher = EtherscanDataFetcher(api_key)
    
    # Define date range
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    
    print(f"\nFetching data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print("This may take a while due to API rate limits...\n")
    
    # Fetch data for each day
    all_data = []
    current_date = start_date
    
    while current_date <= end_date:
        print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}...", end='\r')
        
        data = fetcher.get_daily_transaction_count(current_date)
        if data:
            all_data.append(data)
        
        current_date += timedelta(days=1)
        time.sleep(0.25)  # Rate limiting: ~4 requests per second
    
    print("\n✓ Data fetch complete!                              \n")
    
    # Save raw data
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv('outputs/eth_transaction_data_2025.csv', index=False)
        print(f"✓ Saved raw data: outputs/eth_transaction_data_2025.csv ({len(all_data)} days)\n")
        
        # Analyze patterns
        analyzer = TradingPatternAnalyzer(all_data)
        analyzer.analyze_weekend_effect()
        analyzer.analyze_day_of_week_effect()
        
        # Create visualizations
        analyzer.plot_weekend_comparison()
        analyzer.plot_time_series()
        
        print("\n" + "="*50)
        print("ANALYSIS COMPLETE!")
        print("="*50)
        print("\nCheck the outputs folder for:")
        print("  • Raw data CSV")
        print("  • Weekend effect visualization")
        print("  • Time series plot")
        print("\n")
    else:
        print("No data was fetched. Please check your API key and try again.")


if __name__ == "__main__":
    main()
