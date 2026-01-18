# The Weekend Effect in Ethereum Blockchain Activity: Evidence from 2025 Transaction Data

**Author:** [Yuyan Kuang]  
**Date:** January 2026  
**Affiliation:** [University of California, Davis]

---

## Abstract

This study examines whether Ethereum blockchain transaction patterns exhibit systematic day-of-week effects similar to those documented in traditional financial markets. Using daily transaction counts from the Ethereum mainnet throughout 2025, I find that weekday activity exceeds weekend activity by 15.66% (p < 0.001, Cohen's d = 0.745). The effect is robust to multiple statistical tests and shows a monotonic decline from Monday (highest) through Sunday (lowest). These findings suggest that despite operating continuously without traditional market hours, blockchain ecosystems remain substantially influenced by institutional participants who follow conventional business schedules. The results contribute to our understanding of cryptocurrency market microstructure and raise questions about the extent to which decentralized systems can escape the behavioral and institutional patterns of legacy financial markets.

**Keywords:** Blockchain, Ethereum, Calendar anomaly, Weekend effect, Cryptocurrency, Market microstructure, Behavioral finance

---

## 1. Introduction

### 1.1 Motivation

Calendar anomalies—systematic patterns in financial returns or trading activity associated with specific days, months, or seasons—have been extensively documented in traditional asset markets. Among the most robust findings is the "weekend effect," where stock returns and trading volumes differ systematically between weekdays and weekends (French, 1980; Gibbons & Hess, 1981). These patterns are typically attributed to institutional trading rhythms, information processing delays, and behavioral biases among market participants.

Cryptocurrency markets present a natural laboratory to test whether such calendar effects persist in markets that operate continuously, without the institutional constraints of traditional exchanges. Blockchain networks like Ethereum run 24 hours per day, 7 days per week, with no official market hours, holidays, or trading halts. If calendar anomalies emerge even in these "always-on" systems, it would suggest that human behavioral patterns and institutional structures exert influence independent of market design.

### 1.2 Research Question

This study investigates a simple but fundamental question: **Do Ethereum transaction patterns differ between weekdays and weekends?**

Specifically, I test the null hypothesis that average daily transaction counts are equal across all days of the week against the alternative that systematic differences exist. I further explore whether these differences follow predictable patterns (e.g., monotonic decline through the week, Monday effects).

### 1.3 Preview of Findings

Using 365 days of Ethereum mainnet data from 2025, I document a statistically significant and economically meaningful weekend effect: weekday transaction volumes exceed weekend volumes by approximately 16%. This effect is:
- **Highly significant** statistically (p < 0.001 across multiple tests)
- **Medium-to-large** in magnitude (Cohen's d = 0.745)
- **Monotonic** across the week (Monday > Tuesday > ... > Sunday)
- **Robust** to both parametric and non-parametric tests

These results suggest that institutional and professional participants, who operate primarily during business hours, account for a substantial fraction of Ethereum activity.

---

## 2. Literature Review

### 2.1 Calendar Anomalies in Traditional Markets

The weekend effect in stock markets is one of the most studied anomalies in finance. French (1980) and Gibbons and Hess (1981) documented that U.S. stock returns are systematically lower on Mondays than other weekdays. Subsequent research has identified potential mechanisms including:

- **Institutional trading patterns:** Professional traders concentrate activity during business hours
- **Information arrival:** Corporate announcements and economic data releases occur primarily on weekdays
- **Settlement conventions:** Many transactions settle on specific business days
- **Behavioral biases:** Individual investors may exhibit different risk preferences on weekends

### 2.2 Calendar Effects in Cryptocurrency Markets

The cryptocurrency literature has examined whether these traditional market patterns persist in decentralized systems. Urquhart (2016) found day-of-week effects in Bitcoin returns, though these weakened over time. Aharon and Qadan (2019) documented similar patterns across multiple cryptocurrencies, suggesting calendar anomalies are not unique to Bitcoin.

However, most existing work focuses on **price returns** rather than **transaction activity**. This distinction matters: returns reflect market outcomes (price changes), while transaction counts measure market participation directly. The present study contributes by examining blockchain activity patterns rather than price movements.

### 2.3 Blockchain Market Microstructure

Recent research has begun to characterize the unique microstructure of blockchain-based markets. Makarov and Schoar (2020) analyze Bitcoin flows across exchanges and document substantial price dispersion and arbitrage opportunities. Lehar and Parlour (2021) and Park (2021) study decentralized exchange (DEX) dynamics on Ethereum, finding that automated market makers exhibit different properties than traditional order book markets.

This study complements this literature by examining the temporal dimension of blockchain activity, testing whether legacy financial market patterns persist even in technologically decentralized systems.

---

## 3. Data and Methodology

### 3.1 Data Source

I obtain Ethereum mainnet transaction data via the Etherscan API (v2) for the full calendar year 2025 (January 1 - December 31). Etherscan provides comprehensive blockchain data aggregation and is widely used in academic and industry research.

**Blockchain Specifications:**
- **Network:** Ethereum Mainnet (Chain ID: 1)
- **Block Time:** Approximately 12 seconds per block (~7,200 blocks per day)
- **Consensus:** Proof-of-Stake (post-Merge as of September 2022)

### 3.2 Transaction Definition

An Ethereum "transaction" represents any state-changing operation recorded on the blockchain. This includes:

1. **ETH Transfers:** Sending native Ether between addresses
2. **Smart Contract Calls:** Interacting with deployed contracts
   - DeFi protocols (Uniswap, Aave, Compound)
   - NFT platforms (OpenSea, Blur)
   - DAO governance systems
3. **Token Transfers:** ERC-20, ERC-721, ERC-1155 token movements
4. **Contract Deployments:** Publishing new smart contracts
5. **Failed Transactions:** Transactions that reverted but still paid gas fees

This broad definition captures the full spectrum of blockchain activity, not just speculative trading.

### 3.3 Sampling Methodology

Due to API rate limits and computational constraints, I employ a stratified sampling approach rather than querying every block:

1. For each calendar day (00:00:00 to 23:59:59 UTC):
   - Identify the first and last block numbers
   - Divide the day into 5 equal time segments
   - Sample one block from each segment
   - Count transactions in each sampled block
   - Estimate daily total: `avg_tx_per_block × total_blocks_per_day`

**Sampling Rate:** 5 blocks from ~7,200 daily blocks = 0.07% sampling rate

**Justification and Limitations:**

*Advantages:*
- Consistent methodology applied to all days
- Captures variation throughout the day (not just a single snapshot)
- Computationally feasible within API constraints
- Temporal stratification reduces bias from time-of-day effects

*Limitations:*
- Small sample size may introduce estimation error for individual days
- May miss extreme events (e.g., large NFT drops, liquidation cascades)
- Assumes transaction rates are relatively stable within each 5-hour segment

*Robustness Considerations:*
- Large sample size (365 days) helps average out day-specific noise
- Consistent methodology means any bias affects weekdays and weekends equally
- Primary interest is *relative* comparison (weekday vs. weekend), not absolute levels
- Future work should validate estimates against complete block data

### 3.4 Variable Construction

**Primary Variables:**
- `tx_count`: Estimated daily transaction count
- `day_of_week`: Integer 0-6 (Monday = 0, Sunday = 6)
- `day_name`: String day name for clarity
- `is_weekend`: Boolean indicator (Saturday or Sunday)

**Descriptive Statistics:**

| Variable | N | Mean | Std Dev | Min | Max |
|----------|---|------|---------|-----|-----|
| Transaction Count (All Days) | 365 | 1,577,012 | 362,045 | 747,009 | 3,125,496 |
| Transaction Count (Weekdays) | 261 | 1,652,742 | 367,182 | 747,009 | 3,125,496 |
| Transaction Count (Weekends) | 104 | 1,393,976 | 291,242 | 886,212 | 2,596,216 |

**Key Observation:** Weekend standard deviation is lower than weekday (291K vs. 367K), suggesting weekends may have less volatility or fewer extreme events.

---

## 4. Empirical Results

### 4.1 Primary Finding: Weekend Effect

**Table 1: Mean Transaction Counts by Period**

| Period | N | Mean | Median | Std Dev | Min | Max |
|--------|---|------|--------|---------|-----|-----|
| Weekdays | 261 | 1,652,742 | 1,628,705 | 367,182 | 747,009 | 3,125,496 |
| Weekends | 104 | 1,393,976 | 1,368,080 | 291,242 | 886,212 | 2,596,216 |
| **Difference** | | **258,767** | | | | |
| **% Difference** | | **15.66%** | | | | |

The raw difference of 258,767 transactions per day represents a substantial reduction in weekend activity—roughly equivalent to removing one transaction every 0.3 seconds throughout the entire weekend.

### 4.2 Statistical Significance Tests

To ensure robustness, I conduct multiple complementary statistical tests:

**Test 1: Shapiro-Wilk Normality Test**

| Group | W-statistic | p-value | Conclusion |
|-------|-------------|---------|------------|
| Weekdays | 0.976 | 0.0002 | Non-normal |
| Weekends | 0.954 | <0.0001 | Non-normal |

While the distributions deviate slightly from perfect normality, visual inspection (Q-Q plots) shows the deviations are minor. Nevertheless, I employ both parametric and non-parametric tests for robustness.

**Test 2: Independent Samples t-test (Parametric)**

- **Null Hypothesis:** μ_weekday = μ_weekend
- **t-statistic:** 6.4248
- **p-value:** < 0.000001
- **Conclusion:** Reject null at any conventional significance level

**Test 3: Mann-Whitney U Test (Non-parametric)**

- **Null Hypothesis:** Distributions are identical
- **U-statistic:** 19,655
- **p-value:** < 0.000001
- **Conclusion:** Reject null; weekday distribution is stochastically larger

**Interpretation:** Both parametric and non-parametric tests yield identical conclusions, providing strong evidence against the null hypothesis of equal transaction counts.

### 4.3 Effect Size Analysis

Statistical significance alone does not indicate practical importance. I therefore calculate Cohen's d, a standardized measure of effect magnitude:

**Cohen's d = 0.7450**

**Interpretation Guide:**
- |d| < 0.2: Negligible
- 0.2 ≤ |d| < 0.5: Small
- 0.5 ≤ |d| < 0.8: Medium
- |d| ≥ 0.8: Large

The observed effect (d = 0.745) falls at the upper end of "medium" and approaches "large," indicating the weekend reduction is not just statistically detectable but economically meaningful.

**95% Confidence Interval for Difference:**
- Point estimate: 258,767 transactions
- 95% CI: [187,229, 330,304]
- Interpretation: With 95% confidence, true weekend reduction is between 187K and 330K transactions per day

### 4.4 Day-of-Week Analysis

**Table 2: Transaction Counts by Individual Day**

| Day | N | Mean | Std Dev |
|-----|---|------|---------|
| Monday | 52 | 1,699,381 | 342,115 |
| Tuesday | 52 | 1,658,352 | 374,608 |
| Wednesday | 53 | 1,642,576 | 366,830 |
| Thursday | 52 | 1,640,080 | 387,859 |
| Friday | 52 | 1,623,518 | 372,732 |
| **Saturday** | 52 | **1,419,819** | 331,237 |
| **Sunday** | 52 | **1,368,132** | 245,412 |

**Observations:**
1. **Monotonic Decline:** Mean activity decreases steadily from Monday to Sunday
2. **Monday Peak:** Highest activity occurs on Mondays, possibly reflecting a "weekend backlog"
3. **Sharp Weekend Drop:** Transition from Friday to Saturday shows largest day-to-day decline
4. **Sunday Minimum:** Lowest activity occurs on Sundays (19.5% below Monday)

**One-Way ANOVA Test:**
- **Null Hypothesis:** μ_Mon = μ_Tue = ... = μ_Sun
- **F-statistic:** 7.1549
- **p-value:** < 0.000001
- **Conclusion:** At least one day differs significantly from others

**Post-hoc Tukey HSD tests** (not shown for brevity) confirm that weekdays cluster together and weekends cluster together, with significant differences between these groups but less significant differences within groups.

### 4.5 Visualizations

The empirical patterns are visualized in three key figures (included in `outputs/` directory):

1. **weekend_effect_analysis.png:** Box plots and bar charts comparing weekday vs. weekend distributions
2. **transaction_timeseries.png:** Daily transaction counts over the full year with 7-day moving average
3. **statistical_analysis.png:** Distribution histograms and Q-Q plots for normality assessment

Visual inspection confirms:
- Clear separation between weekday and weekend distributions
- No obvious outliers driving the results
- Approximate normality despite formal test rejections
- Consistent pattern throughout the year (no obvious seasonal break)

---

## 5. Discussion and Interpretation

### 5.1 Economic Mechanisms

What explains the observed weekend effect in a 24/7 market? I consider several potential mechanisms:

**Hypothesis 1: Institutional Activity**

Cryptocurrency markets are increasingly institutionalized. Hedge funds, trading firms, and corporate treasuries now hold significant positions in digital assets. These entities typically operate during business hours and may reduce activity on weekends. If institutional participants account for ~16% of transaction volume, their weekend absence would generate the observed pattern.

**Supporting Evidence:**
- Monotonic weekly decline consistent with gradual institution withdrawal
- Monday peak consistent with "catch-up" activity after weekend
- Lower weekend volatility (smaller std dev) consistent with less professional trading

**Hypothesis 2: DeFi Protocol Management**

Many Ethereum transactions involve DeFi protocols that require active management:
- Adjusting collateral ratios to avoid liquidations
- Rebalancing liquidity pools
- Claiming rewards and compounding yields

Protocol teams and sophisticated users may perform these operations during working hours, reducing weekend activity.

**Hypothesis 3: Correlation with Traditional Markets**

Some cryptocurrency trading is driven by macroeconomic news and traditional market movements. With stock markets closed on weekends, related crypto activity may decline.

**Hypothesis 4: Reduced Bot Activity**

Automated trading systems and arbitrage bots may be monitored and adjusted by human operators during business hours. Reduced human oversight on weekends could lead to lower bot activity.

### 5.2 Alternative Explanations Considered

**Gas Price Effects:** One might hypothesize that high weekend gas prices discourage transactions. However, this would only explain the pattern if gas prices systematically increase on weekends. Preliminary analysis (not shown) suggests gas prices actually *decrease* on weekends, consistent with reduced demand rather than supply constraints.

**Network Congestion:** Could weekend network congestion limit transaction throughput? This seems unlikely given Ethereum's dynamic block size and priority fee mechanism. More likely, reduced demand leads to *less* congestion on weekends.

**Measurement Error:** Could sampling bias explain the findings? While possible, the consistency across 365 days, robustness to multiple statistical tests, and large effect size make sampling error an unlikely complete explanation.

### 5.3 Comparison to Prior Literature

My findings align with prior research documenting calendar effects in cryptocurrency markets:

- **Urquhart (2016):** Found day-of-week effects in Bitcoin returns, though diminishing over time
- **Aharon & Qadan (2019):** Documented calendar anomalies across multiple cryptocurrencies
- **Caporale & Plastun (2019):** Found significant day-of-week effects in Bitcoin and other cryptocurrencies

However, this study contributes by:
1. Examining *transaction activity* rather than *price returns*
2. Focusing on Ethereum (smart contract platform) rather than Bitcoin (primarily payment/store of value)
3. Using recent 2025 data, testing persistence of effects as markets mature
4. Providing transparent methodology and code for replication

### 5.4 Implications

**For Market Efficiency:**
The persistence of predictable calendar patterns in blockchain activity challenges the notion that cryptocurrency markets are informationally efficient. If transaction patterns are predictable, sophisticated participants could potentially exploit this for:
- Optimal trade timing (e.g., execute large transactions on weekends when prices may be less efficient)
- Liquidity provision strategies (adjust market making intensity by day of week)
- Risk management (adjust positions before weekends when activity declines)

**For Blockchain Scalability:**
Understanding activity patterns can inform network capacity planning. If demand systematically declines by 16% on weekends, resources could be reallocated (e.g., reduced validator requirements, optimized gas mechanisms).

**For Institutional Participation:**
The findings suggest institutional participants already exert substantial influence on Ethereum activity. As institutions increase their cryptocurrency exposure, we might expect:
- Strengthening of weekend effects over time
- Emergence of additional calendar patterns (e.g., end-of-month, end-of-quarter effects)
- Greater correlation with traditional market patterns

---

## 6. Limitations and Future Research

### 6.1 Limitations of Current Study

**Data and Methodology:**
1. **Sampling Approach:** 0.07% sampling rate may introduce noise, though large sample size mitigates this
2. **Single Metric:** Transaction count doesn't capture transaction value, complexity, or economic importance
3. **One Blockchain:** Results may not generalize to other blockchains with different user bases
4. **One Year:** Cannot test persistence across multiple years or regime changes

**Interpretation:**
1. **Correlation vs. Causation:** Cannot definitively identify mechanisms driving the weekend effect
2. **Heterogeneous Transactions:** Treat all transactions equally despite varying economic significance
3. **Failed Transactions:** Include failed transactions, which may follow different patterns

### 6.2 Extensions for Future Research

**1. Multi-Metric Analysis**
- Incorporate gas prices (network congestion proxy)
- Analyze transaction values (economic magnitude)
- Track unique active addresses (participant count)
- Examine specific DeFi protocols (e.g., Uniswap volume by day)

**2. Causal Identification**
- Event studies around major announcements (do they trigger weekend trading?)
- Regression discontinuity around daylight saving time changes
- Granger causality tests with traditional market hours

**3. Cross-Chain Comparison**
- Bitcoin: Payment-focused blockchain
- Solana: High-throughput alternative
- Polygon/Arbitrum: Layer 2 scaling solutions
- Do all blockchains show similar calendar effects?

**4. Time Variation**
- Test for structural breaks (e.g., around major DeFi launches, regulatory events)
- Compare 2023 vs. 2024 vs. 2025 (is effect strengthening or weakening?)
- Examine intraday patterns (hourly transaction distribution)

**5. Machine Learning Approaches**
- Predict transaction volume using day-of-week and lagged variables
- Cluster days by transaction patterns (unsupervised learning)
- Neural network forecasting of blockchain activity

### 6.3 Practical Applications

**For Traders:**
- Optimal execution timing (weekends may offer different liquidity)
- Fee management (lower gas prices on weekends)
- Arbitrage strategies (exploit predictable volume patterns)

**For Researchers:**
- Benchmark for testing market efficiency
- Framework for studying institutional participation
- Template for blockchain activity analysis

**For Protocol Designers:**
- Inform gas pricing mechanisms
- Optimize validator requirements
- Design better incentives for stable activity

---

## 7. Conclusion

This study documents a statistically significant and economically meaningful weekend effect in Ethereum blockchain activity. Weekday transaction volumes exceed weekend volumes by 15.66% (p < 0.001, Cohen's d = 0.745), with a monotonic decline from Monday (highest) through Sunday (lowest). These patterns suggest that institutional and professional participants, who operate primarily during traditional business hours, account for a substantial fraction of blockchain activity.

The findings contribute to our understanding of cryptocurrency market microstructure and raise important questions about market efficiency and institutional influence. Despite Ethereum's technological capacity for 24/7 operation, human behavioral patterns and institutional structures continue to shape activity patterns. As cryptocurrency markets mature and institutional participation grows, we might expect these calendar effects to strengthen rather than disappear.

The code and data for this analysis are publicly available, and I encourage replication and extension to other blockchains, time periods, and metrics. Understanding the temporal dynamics of blockchain activity is essential for both academic research and practical applications in the rapidly evolving cryptocurrency ecosystem.

---

## References

Aharon, D. Y., & Qadan, M. (2019). Bitcoin and the day-of-the-week effect. *Finance Research Letters*, 31, 415-424.

Caporale, G. M., & Plastun, A. (2019). The day of the week effect in the cryptocurrency market. *Finance Research Letters*, 31, 258-269.

French, K. R. (1980). Stock returns and the weekend effect. *Journal of Financial Economics*, 8(1), 55-69.

Gibbons, M. R., & Hess, P. (1981). Day of the week effects and asset returns. *Journal of Business*, 54(4), 579-596.

Lehar, A., & Parlour, C. A. (2021). Systemic fragility in decentralized markets. Working paper.

Makarov, I., & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets. *Journal of Financial Economics*, 135(2), 293-319.

Park, A. (2021). The conceptual flaws of decentralized automated market making. Working paper.

Urquhart, A. (2016). The inefficiency of Bitcoin. *Economics Letters*, 148, 80-82.

---

## Appendix: Code Availability

All code used in this analysis is available at:
[https://github.com/BiBiDaWang/ethereum-weekend-effect](https://github.com/BiBiDaWang/ethereum-weekend-effect)

The repository includes:
- Data collection scripts (`eth_trading_patterns.py`)
- Statistical analysis code (`statistical_tests.py`)
- API testing utilities
- Complete documentation
- Raw and processed data files

Researchers are encouraged to replicate and extend this work. Please cite this study if using the code or methodology.
