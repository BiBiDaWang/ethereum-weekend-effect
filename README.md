# Ethereum Weekend Effect: An Empirical Analysis of Blockchain Activity Patterns

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This project investigates whether Ethereum blockchain activity exhibits systematic differences between weekdays and weekends, drawing on behavioral finance literature documenting calendar anomalies in traditional financial markets. Using transaction-level data from the Ethereum mainnet in 2025, I find statistically significant evidence that weekday activity exceeds weekend activity by approximately 16%, suggesting that institutional and professional participants continue to exert substantial influence on blockchain ecosystems despite their 24/7 operational nature.

## Research Question

**Do Ethereum transaction patterns differ between weekdays and weekends?**

Traditional financial markets exhibit well-documented calendar anomalies, including the "weekend effect" where trading volume and returns patterns differ systematically by day of the week. This analysis tests whether decentralized blockchain networks—which operate continuously without traditional market hours—display similar behavioral patterns, potentially indicating that legacy financial market structures continue to influence cryptocurrency markets.

## Key Findings

### Primary Results
- **Weekend Effect Magnitude:** 15.66% reduction in transaction volume on weekends relative to weekdays
- **Statistical Significance:** Highly significant (p < 0.001) using both parametric (t-test) and non-parametric (Mann-Whitney U) tests
- **Effect Size:** Medium-to-large (Cohen's d = 0.745), indicating practical as well as statistical significance
- **95% Confidence Interval:** True difference lies between 187,229 and 330,304 fewer transactions per weekend day

### Day-of-Week Patterns
- **Monday:** Highest activity (1,699,381 transactions) - potential "Monday effect" from weekend backlog
- **Gradual Decline:** Monotonic decrease from Monday through Friday
- **Weekend Drop:** Sharp decline on Saturday (1,419,819) and Sunday (1,368,132)
- **ANOVA Results:** Significant differences across all seven days (F = 7.15, p < 0.001)

### Economic Interpretation
These findings suggest:
1. **Institutional Dominance:** Professional and institutional participants account for ~16% of daily activity
2. **Business Cycle Influence:** Despite 24/7 operations, Ethereum activity follows traditional business patterns
3. **Market Structure:** Crypto markets are not fully separated from traditional finance rhythms
4. **Arbitrage Opportunities:** Systematic weekend volume reduction may create predictable liquidity variations

## Data

### Source
- **Provider:** Etherscan API (v2)
- **Blockchain:** Ethereum Mainnet (Chain ID: 1)
- **Period:** January 1, 2025 - December 31, 2025 (365 days)
- **Sample Size:** 261 weekdays, 104 weekend days

### Metrics
- **Primary Variable:** Daily transaction count
- **Transaction Definition:** All on-chain operations including:
  - ETH transfers
  - Smart contract interactions (DeFi, NFTs, DAOs)
  - Token transfers (ERC-20, ERC-721, ERC-1155)
  - Contract deployments
  - Failed transactions

### Data Collection Methodology
Transaction counts are estimated using a stratified sampling approach:
1. Identify block range for each calendar day (UTC timezone)
2. Sample 5 blocks evenly distributed across each day
3. Calculate average transactions per block
4. Estimate daily total: avg_tx_per_block × blocks_per_day

**Limitations:** 
- Sampling rate of 0.07% (5 blocks from ~7,200 daily blocks) may introduce estimation error
- Day-to-day estimates may be noisy, though large sample size (365 days) helps average out random variation
- Methodology is consistent across all days, so relative comparisons (weekday vs. weekend) remain valid
- Future work should validate estimates against complete block data or use pre-aggregated statistics

## Methodology

### Statistical Tests Employed

1. **Shapiro-Wilk Test:** Assess normality of distributions
2. **Independent Samples t-test:** Parametric test comparing weekday vs. weekend means
3. **Mann-Whitney U Test:** Non-parametric alternative robust to non-normality
4. **One-way ANOVA:** Test for differences across all seven days of the week
5. **Cohen's d:** Standardized effect size measure
6. **Bootstrap Confidence Intervals:** 95% CI for mean difference

### Why Multiple Tests?
- **Robustness:** Convergent evidence from parametric and non-parametric approaches
- **Assumption Checking:** Shapiro-Wilk results guide test selection
- **Effect Magnitude:** Cohen's d distinguishes statistical from practical significance
- **Comprehensive View:** ANOVA reveals finer day-of-week granularity

## Repository Structure

```
ethereum-weekend-effect/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── eth_trading_patterns.py             # Main data collection and analysis
├── statistical_tests.py                # Statistical significance testing
├── test_api.py                         # API connection testing
├── test_api_debug.py                   # Detailed API diagnostics
├── outputs/
│   ├── eth_transaction_data_2025.csv   # Raw daily transaction counts
│   ├── weekend_effect_analysis.png     # Box plots and bar charts
│   ├── transaction_timeseries.png      # Time series visualization
│   ├── statistical_analysis.png        # Distribution and Q-Q plots
│   └── statistical_results.txt         # Summary of test results
└── docs/
    └── research_note.pdf               # Detailed research writeup
```

## Installation and Usage

### Prerequisites
- Python 3.12 or higher
- Etherscan API key (free tier sufficient) - obtain at https://etherscan.io/myapikey

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ethereum-weekend-effect.git
cd ethereum-weekend-effect
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Test API connection:
```bash
python test_api.py
# Enter your Etherscan API key when prompted
```

### Running the Analysis

**Step 1: Collect Data**
```bash
python eth_trading_patterns.py
# Runtime: ~15 minutes for full year due to API rate limits
# Output: CSV file with daily transaction counts and initial visualizations
```

**Step 2: Statistical Testing**
```bash
python statistical_tests.py
# Runtime: <1 second (reads from existing CSV)
# Output: Comprehensive statistical test results and additional visualizations
```

### Modifying the Analysis

**Analyze a different time period:**
```python
# In eth_trading_patterns.py, lines 269-270:
start_date = datetime(2024, 1, 1)  # Change year or date range
end_date = datetime(2024, 12, 31)
```

**Increase sampling precision:**
```python
# In eth_trading_patterns.py, line 77:
for i in range(50):  # Increase from 5 to 50 blocks per day
```

## Limitations and Future Work

### Current Limitations

1. **Sampling Methodology**
   - Small sample size per day (5 blocks from ~7,200)
   - May miss intraday volatility spikes or unique events
   - Future: Validate against complete block data or use aggregated APIs

2. **Scope**
   - Single metric (transaction count) doesn't capture full market dynamics
   - One blockchain (Ethereum) may not generalize to all cryptocurrencies
   - One year of data limits ability to test persistence of patterns

3. **Transaction Heterogeneity**
   - All transactions weighted equally regardless of economic significance
   - No distinction between retail vs. institutional participants
   - Failed transactions counted alongside successful ones

### Proposed Extensions

1. **Multi-Metric Analysis**
   - Gas prices (proxy for network congestion and urgency)
   - Transaction values (economic magnitude vs. count)
   - Unique active addresses (user participation vs. bot activity)
   - DeFi-specific metrics (DEX volume, TVL flows, liquidations)

2. **Temporal Analysis**
   - Holiday effects (major holidays vs. regular weekends)
   - Intraday patterns (hourly transaction distribution)
   - Seasonal variations (quarterly or monthly patterns)
   - Multi-year comparison (2023 vs. 2024 vs. 2025)

3. **Cross-Blockchain Comparison**
   - Bitcoin (Layer 1, different use case)
   - Polygon, Arbitrum, Optimism (Layer 2 scaling solutions)
   - Solana, Binance Smart Chain (alternative Layer 1s)
   - Test whether weekend effect is universal or Ethereum-specific

4. **Causal Analysis**
   - Granger causality with traditional markets (S&P 500, Nasdaq)
   - Event studies around major announcements or market shocks
   - Regression discontinuity around market structure changes

5. **Economic Mechanisms**
   - Identify transaction types driving the weekend effect
   - Analyze gas price elasticity differences by day
   - Test for strategic timing of large transactions

## Academic Context

This analysis contributes to the growing literature on cryptocurrency market microstructure and behavioral finance in decentralized systems. Key related work includes:

- **Calendar Anomalies:** French (1980), Gibbons & Hess (1981) document day-of-week effects in stock returns
- **Crypto Market Efficiency:** Urquhart (2016), Aharon & Qadan (2019) find calendar effects persist in Bitcoin
- **Blockchain Activity Patterns:** Makarov & Schoar (2020) analyze flow of funds across exchanges
- **DeFi Microstructure:** Lehar & Parlour (2021), Park (2021) study decentralized exchange dynamics

This project demonstrates that despite the technological promise of "always-on" markets, behavioral and institutional patterns from traditional finance continue to shape blockchain ecosystems.

## Requirements

See `requirements.txt` for full dependencies. Key packages:
- `pandas >= 2.1.4` - Data manipulation
- `matplotlib >= 3.8.2` - Visualization
- `seaborn >= 0.13.0` - Statistical plotting
- `scipy >= 1.11.0` - Statistical tests
- `requests >= 2.31.0` - API calls

## Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Etherscan for providing free API access to Ethereum blockchain data
- The broader cryptocurrency research community for methodological guidance
- [Prof. Antoinette Schoar's research](https://mitsloan.mit.edu/faculty/directory/antoinette-schoar) on fintech and blockchain for motivating this analysis

## Citation

If you use this code or analysis in your work, please cite:

```bibtex
@misc{yourname2025ethereum,
  author = {Your Name},
  title = {Ethereum Weekend Effect: An Empirical Analysis of Blockchain Activity Patterns},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/yourusername/ethereum-weekend-effect}
}
```

---

**Questions or suggestions?** Open an issue or submit a pull request!
