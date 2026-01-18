# QUICK START GUIDE

Follow these steps in order:

## 1️⃣ First Time Setup

### Open VS Code
1. Launch VS Code
2. File → Open Folder
3. Create/select folder: `ethereum-analysis`

### Open Terminal in VS Code
- View → Terminal (or press Ctrl + `)

### Install Python Packages
```bash
pip install -r requirements.txt
```
If that doesn't work, try:
```bash
pip3 install -r requirements.txt
```

## 2️⃣ Get Your API Key

1. Go to: https://etherscan.io/myapikey
2. Sign up (free)
3. Create API key
4. Copy it (looks like: `ABCD1234EFGH5678...`)

## 3️⃣ Test Your Setup

```bash
python test_api.py
```
If that doesn't work, try:
```bash
python3 test_api.py
```

When prompted, paste your API key.

**Expected output:**
```
✓ API key is valid!
✓ Successfully fetched latest block
✓ Block XXX has XX transactions
✓ ALL TESTS PASSED!
```

## 4️⃣ Run the Full Analysis

### For the full year (takes ~15 minutes):
```bash
python eth_trading_patterns.py
```

### For just January (takes ~1 minute):
Edit `eth_trading_patterns.py` first:
- Find line: `end_date = datetime(2025, 12, 31)`
- Change to: `end_date = datetime(2025, 1, 31)`
- Save and run

## 5️⃣ View Results

After the script finishes, check the `outputs` folder for:
- `eth_transaction_data_2025.csv` - Raw data
- `weekend_effect_analysis.png` - Charts
- `transaction_timeseries.png` - Time series

## 🆘 Quick Troubleshooting

### "Python not found"
Try `python3` instead of `python`

### "pip not found"  
Try `pip3` instead of `pip`

### "No module named requests"
Run: `pip install requests pandas matplotlib seaborn`

### "Invalid API key"
- Make sure you copied the whole key
- Check it's activated on Etherscan
- Try pasting it again

### Script is slow
This is normal! API has rate limits.
- Full year: ~15 minutes
- One month: ~1 minute

### No outputs folder
The script creates it automatically.
Look in your project folder.

## 📊 Understanding Output

The terminal will show:
```
WEEKEND vs WEEKDAY ANALYSIS
Average weekday transactions: 1,234,567
Average weekend transactions: 987,654
Difference: -246,913 (-20.00%)
```

This means:
- Weekdays have MORE transactions
- About 20% more activity on weekdays
- This suggests institutional/professional activity dominates

## ✅ Checklist

Before running the full analysis:
- [ ] Python installed (check: `python --version`)
- [ ] Packages installed (check: run `test_api.py`)
- [ ] API key working (test script passes)
- [ ] Decided on date range (full year or just testing with one month)

## 🎯 Next Steps After Success

1. Open the CSV in Excel/Google Sheets
2. Look at the charts
3. Think about what you see
4. Modify the code to ask new questions
5. Try different date ranges
6. Add analysis for holidays

## 💡 Pro Tips

1. **Start small**: Test with 1 week first before running full year
2. **Save your API key**: Set environment variable so you don't need to type it each time
3. **Check the data**: Look at the CSV to see if numbers make sense
4. **Read the code**: Comments explain what each part does
5. **Experiment**: Change things and see what happens!

---

Good luck! 🚀
