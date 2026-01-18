# Ethereum Trading Pattern Analysis

This project analyzes weekend vs. weekday trading patterns on the Ethereum blockchain using Etherscan API.

## 🎯 What This Does

- Fetches daily Ethereum transaction data from Etherscan
- Analyzes weekend vs. weekday trading patterns
- Identifies day-of-week effects (Monday effect, etc.)
- Creates visualizations of the findings

## 📋 Prerequisites

1. **Python 3.8 or higher** - Check by running: `python --version` or `python3 --version`
2. **Etherscan API Key** (free) - Get one at: https://etherscan.io/myapikey
3. **VS Code** (you already have this!)

## 🚀 Step-by-Step Setup Guide

### Step 1: Open VS Code and Create a Project Folder

1. Open VS Code
2. Click `File` → `Open Folder`
3. Create a new folder called `ethereum-analysis` and open it
4. In VS Code, open the Terminal: `View` → `Terminal` (or press Ctrl+` )

### Step 2: Download the Project Files

You have two options:

**Option A: Copy the files I created**
1. Download the files from Claude (I'll provide them)
2. Place them in your `ethereum-analysis` folder

**Option B: Create files manually in VS Code**
1. Click the "New File" icon in VS Code
2. Name it `eth_trading_patterns.py`
3. Copy the code I provided above
4. Repeat for `requirements.txt` and `README.md`

### Step 3: Install Python Dependencies

In the VS Code terminal, run:

```bash
# On Windows:
pip install -r requirements.txt

# On Mac/Linux:
pip3 install -r requirements.txt
```

This installs:
- `requests` - for making API calls
- `pandas` - for data analysis
- `matplotlib` - for creating charts
- `seaborn` - for prettier visualizations

### Step 4: Get Your Etherscan API Key

1. Go to: https://etherscan.io/myapikey
2. Sign up for a free account if you don't have one
3. Create a new API key
4. Copy the key (it looks like: `ABC123XYZ456...`)

### Step 5: Run the Script

In the terminal:

```bash
# On Windows:
python eth_trading_patterns.py

# On Mac/Linux:
python3 eth_trading_patterns.py
```

When prompted, paste your Etherscan API key and press Enter.

### Step 6: Wait for Results

The script will:
1. Fetch data for each day in 2025 (this takes ~10-15 minutes due to rate limits)
2. Save the raw data to a CSV file
3. Perform statistical analysis
4. Create visualizations

## 📊 Output Files

After running, you'll find in the `outputs` folder:

1. **eth_transaction_data_2025.csv** - Raw daily transaction counts
2. **weekend_effect_analysis.png** - Comparison charts
3. **transaction_timeseries.png** - Time series plot with trends

## 🔍 Understanding the Results

The script will print to your terminal:

```
WEEKEND vs WEEKDAY ANALYSIS
Average weekday transactions: XXX,XXX
Average weekend transactions: XXX,XXX
Difference: XXX,XXX (XX.XX%)
```

This tells you if there's a weekend effect!

## 💡 Tips for Beginners

### If you get "Python not found":
- Make sure Python is installed
- Try `python3` instead of `python`
- On Windows, you might need to install from python.org

### If you get "pip not found":
- Try `pip3` instead of `pip`
- Or: `python -m pip install -r requirements.txt`

### If the script is too slow:
- The free Etherscan API has rate limits
- The script already includes delays to respect these limits
- For a full year of data, expect 10-15 minutes

### To test with less data:
- Edit the script and change the date range to just one month:
  ```python
  start_date = datetime(2025, 1, 1)
  end_date = datetime(2025, 1, 31)  # Just January
  ```

## 🎓 Learning Path

Once this works, you can:

1. **Modify the analysis** - Look at different time periods
2. **Add holidays** - Mark US holidays and analyze those days
3. **Calculate statistics** - Add t-tests to see if differences are significant
4. **Fetch more data** - Get gas prices, transaction values, etc.
5. **Compare years** - Run for 2024 vs 2025

## 📚 Code Structure Explained

```python
EtherscanDataFetcher class:
├── Handles API communication
├── Converts dates to blockchain blocks
└── Counts transactions per day

TradingPatternAnalyzer class:
├── Processes the data
├── Calculates statistics
└── Creates visualizations

main() function:
├── Coordinates everything
├── Fetches data
└── Runs analysis
```

## ❓ Common Questions

**Q: Why is it slow?**
A: Free Etherscan API limits us to ~5 requests/second. We're being polite to their servers!

**Q: Can I get more data?**
A: Yes! Modify the date range, but remember: more days = more time.

**Q: The numbers seem high/low?**
A: We're estimating by sampling blocks. For precise counts, we'd need to query every single block (much slower).

**Q: How do I re-run with new dates?**
A: Just edit the `start_date` and `end_date` in the `main()` function.

## 🐛 Troubleshooting

**Error: "Invalid API key"**
- Double-check you copied the entire key
- Make sure you activated it on Etherscan

**Error: "Module not found"**
- Re-run: `pip install -r requirements.txt`
- Make sure you're in the right folder

**No data fetched:**
- Check your internet connection
- Verify your API key is active
- Try a shorter date range first

## 📞 Need Help?

If you get stuck:
1. Read the error message carefully
2. Check you followed each step
3. Try with a shorter date range (one week) first
4. Google the specific error message

## 🎉 Next Steps

Once you successfully run this:
1. Explore the CSV data in Excel or Google Sheets
2. Look at the visualizations
3. Try modifying the code to answer new questions
4. Share your findings!

---

**Author:** Your Name  
**Last Updated:** January 2026  
**License:** MIT
