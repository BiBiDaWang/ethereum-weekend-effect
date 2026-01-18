"""
Statistical Significance Testing for Weekend Effect
Tests whether the weekend vs weekday difference is statistically significant

Author: Yuyan Kuang
Date: January 2026
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set up plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)


def load_data():
    """Load the transaction data from CSV"""
    try:
        df = pd.read_csv('outputs/eth_transaction_data_2025.csv')
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_week'] = df['date'].dt.dayofweek
        df['day_name'] = df['date'].dt.day_name()
        df['is_weekend'] = df['day_of_week'].isin([5, 6])
        return df
    except FileNotFoundError:
        print("Error: Could not find outputs/eth_transaction_data_2025.csv")
        print("Make sure you've run eth_trading_patterns.py first!")
        return None


def calculate_effect_size(weekday_data, weekend_data):
    """Calculate Cohen's d effect size"""
    n1, n2 = len(weekday_data), len(weekend_data)
    var1, var2 = np.var(weekday_data, ddof=1), np.var(weekend_data, ddof=1)
    
    # Pooled standard deviation
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    # Cohen's d
    cohens_d = (np.mean(weekday_data) - np.mean(weekend_data)) / pooled_std
    
    return cohens_d


def interpret_cohens_d(d):
    """Interpret Cohen's d effect size"""
    d_abs = abs(d)
    if d_abs < 0.2:
        return "negligible"
    elif d_abs < 0.5:
        return "small"
    elif d_abs < 0.8:
        return "medium"
    else:
        return "large"


def perform_statistical_tests(df):
    """Perform comprehensive statistical tests"""
    
    # Separate weekend and weekday data
    weekday_tx = df[~df['is_weekend']]['tx_count'].values
    weekend_tx = df[df['is_weekend']]['tx_count'].values
    
    print("\n" + "="*70)
    print("STATISTICAL SIGNIFICANCE TESTING - WEEKEND EFFECT")
    print("="*70)
    
    # Descriptive statistics
    print("\n1. DESCRIPTIVE STATISTICS:")
    print("-" * 70)
    print(f"Weekday samples: {len(weekday_tx)} days")
    print(f"  Mean: {np.mean(weekday_tx):,.0f}")
    print(f"  Median: {np.median(weekday_tx):,.0f}")
    print(f"  Std Dev: {np.std(weekday_tx, ddof=1):,.0f}")
    print(f"  Min: {np.min(weekday_tx):,.0f}")
    print(f"  Max: {np.max(weekday_tx):,.0f}")
    
    print(f"\nWeekend samples: {len(weekend_tx)} days")
    print(f"  Mean: {np.mean(weekend_tx):,.0f}")
    print(f"  Median: {np.median(weekend_tx):,.0f}")
    print(f"  Std Dev: {np.std(weekend_tx, ddof=1):,.0f}")
    print(f"  Min: {np.min(weekend_tx):,.0f}")
    print(f"  Max: {np.max(weekend_tx):,.0f}")
    
    difference = np.mean(weekday_tx) - np.mean(weekend_tx)
    pct_difference = (difference / np.mean(weekend_tx)) * 100
    print(f"\nDifference: {difference:,.0f} ({pct_difference:.2f}%)")
    
    # Test for normality (Shapiro-Wilk test)
    print("\n2. NORMALITY TESTS (Shapiro-Wilk):")
    print("-" * 70)
    _, p_weekday = stats.shapiro(weekday_tx)
    _, p_weekend = stats.shapiro(weekend_tx)
    
    print(f"Weekday p-value: {p_weekday:.4f}", end="")
    if p_weekday > 0.05:
        print(" → Data is normally distributed ✓")
    else:
        print(" → Data may not be normally distributed")
    
    print(f"Weekend p-value: {p_weekend:.4f}", end="")
    if p_weekend > 0.05:
        print(" → Data is normally distributed ✓")
    else:
        print(" → Data may not be normally distributed")
    
    # Independent samples t-test (parametric)
    print("\n3. INDEPENDENT SAMPLES T-TEST (Parametric):")
    print("-" * 70)
    t_stat, p_value_t = stats.ttest_ind(weekday_tx, weekend_tx)
    
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_value_t:.6f}")
    
    if p_value_t < 0.001:
        print("Result: *** HIGHLY SIGNIFICANT (p < 0.001) ***")
    elif p_value_t < 0.01:
        print("Result: ** VERY SIGNIFICANT (p < 0.01) **")
    elif p_value_t < 0.05:
        print("Result: * SIGNIFICANT (p < 0.05) *")
    else:
        print("Result: NOT SIGNIFICANT (p ≥ 0.05)")
    
    # Mann-Whitney U test (non-parametric alternative)
    print("\n4. MANN-WHITNEY U TEST (Non-parametric):")
    print("-" * 70)
    u_stat, p_value_u = stats.mannwhitneyu(weekday_tx, weekend_tx, alternative='two-sided')
    
    print(f"U-statistic: {u_stat:.4f}")
    print(f"p-value: {p_value_u:.6f}")
    
    if p_value_u < 0.001:
        print("Result: *** HIGHLY SIGNIFICANT (p < 0.001) ***")
    elif p_value_u < 0.01:
        print("Result: ** VERY SIGNIFICANT (p < 0.01) **")
    elif p_value_u < 0.05:
        print("Result: * SIGNIFICANT (p < 0.05) *")
    else:
        print("Result: NOT SIGNIFICANT (p ≥ 0.05)")
    
    # Effect size (Cohen's d)
    print("\n5. EFFECT SIZE (Cohen's d):")
    print("-" * 70)
    cohens_d = calculate_effect_size(weekday_tx, weekend_tx)
    interpretation = interpret_cohens_d(cohens_d)
    
    print(f"Cohen's d: {cohens_d:.4f}")
    print(f"Interpretation: {interpretation.upper()} effect size")
    print("\nEffect size guide:")
    print("  • 0.0 - 0.2: Negligible")
    print("  • 0.2 - 0.5: Small")
    print("  • 0.5 - 0.8: Medium")
    print("  • 0.8+:      Large")
    
    # Confidence interval for the difference
    print("\n6. 95% CONFIDENCE INTERVAL FOR DIFFERENCE:")
    print("-" * 70)
    
    # Calculate standard error
    se_weekday = np.std(weekday_tx, ddof=1) / np.sqrt(len(weekday_tx))
    se_weekend = np.std(weekend_tx, ddof=1) / np.sqrt(len(weekend_tx))
    se_diff = np.sqrt(se_weekday**2 + se_weekend**2)
    
    # 95% CI
    ci_lower = difference - 1.96 * se_diff
    ci_upper = difference + 1.96 * se_diff
    
    print(f"Difference: {difference:,.0f}")
    print(f"95% CI: [{ci_lower:,.0f}, {ci_upper:,.0f}]")
    print("\nInterpretation: We are 95% confident that the true difference")
    print(f"in transaction counts lies between {ci_lower:,.0f} and {ci_upper:,.0f}.")
    
    # One-way ANOVA across all days of week
    print("\n7. ONE-WAY ANOVA (All Days of Week):")
    print("-" * 70)
    
    # Group by day of week
    days = [df[df['day_name'] == day]['tx_count'].values 
            for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
    
    f_stat, p_value_anova = stats.f_oneway(*days)
    
    print(f"F-statistic: {f_stat:.4f}")
    print(f"p-value: {p_value_anova:.6f}")
    
    if p_value_anova < 0.001:
        print("Result: *** HIGHLY SIGNIFICANT (p < 0.001) ***")
        print("There are significant differences among days of the week.")
    elif p_value_anova < 0.01:
        print("Result: ** VERY SIGNIFICANT (p < 0.01) **")
        print("There are significant differences among days of the week.")
    elif p_value_anova < 0.05:
        print("Result: * SIGNIFICANT (p < 0.05) *")
        print("There are significant differences among days of the week.")
    else:
        print("Result: NOT SIGNIFICANT (p ≥ 0.05)")
        print("No significant differences among days of the week.")
    
    print("\n" + "="*70)
    print("CONCLUSION:")
    print("="*70)
    
    if p_value_t < 0.05 and p_value_u < 0.05:
        print("✓ The weekend effect is STATISTICALLY SIGNIFICANT!")
        print(f"✓ Weekdays have significantly more transactions (p < {max(p_value_t, p_value_u):.4f})")
        print(f"✓ Effect size is {interpretation} (Cohen's d = {cohens_d:.2f})")
        print("\nThis suggests that:")
        print("  • Institutional/professional activity drives weekday transactions")
        print("  • Ethereum activity follows traditional business cycles")
        print("  • The difference is not due to random chance")
    else:
        print("✗ The weekend effect is NOT statistically significant")
        print("  The observed difference could be due to chance")
    
    print("="*70 + "\n")
    
    return {
        'weekday_mean': np.mean(weekday_tx),
        'weekend_mean': np.mean(weekend_tx),
        't_stat': t_stat,
        'p_value_t': p_value_t,
        'u_stat': u_stat,
        'p_value_u': p_value_u,
        'cohens_d': cohens_d,
        'f_stat': f_stat,
        'p_value_anova': p_value_anova
    }


def create_statistical_visualizations(df):
    """Create visualizations for statistical analysis"""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Distribution comparison (histogram)
    weekday_tx = df[~df['is_weekend']]['tx_count']
    weekend_tx = df[df['is_weekend']]['tx_count']
    
    axes[0, 0].hist(weekday_tx, bins=20, alpha=0.6, label='Weekday', color='blue', edgecolor='black')
    axes[0, 0].hist(weekend_tx, bins=20, alpha=0.6, label='Weekend', color='orange', edgecolor='black')
    axes[0, 0].axvline(weekday_tx.mean(), color='blue', linestyle='--', linewidth=2, label=f'Weekday mean: {weekday_tx.mean():,.0f}')
    axes[0, 0].axvline(weekend_tx.mean(), color='orange', linestyle='--', linewidth=2, label=f'Weekend mean: {weekend_tx.mean():,.0f}')
    axes[0, 0].set_xlabel('Transaction Count')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Distribution of Transaction Counts', fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Q-Q plot for normality check (Weekday)
    stats.probplot(weekday_tx, dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title('Q-Q Plot: Weekday Transactions', fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Q-Q plot for normality check (Weekend)
    stats.probplot(weekend_tx, dist="norm", plot=axes[1, 0])
    axes[1, 0].set_title('Q-Q Plot: Weekend Transactions', fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Violin plot
    df['Period'] = df['is_weekend'].map({True: 'Weekend', False: 'Weekday'})
    sns.violinplot(data=df, x='Period', y='tx_count', ax=axes[1, 1])
    axes[1, 1].set_title('Distribution Comparison (Violin Plot)', fontweight='bold')
    axes[1, 1].set_ylabel('Transaction Count')
    axes[1, 1].set_xlabel('')
    
    plt.tight_layout()
    plt.savefig('outputs/statistical_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved statistical visualization: outputs/statistical_analysis.png\n")
    plt.close()


def main():
    """Main execution function"""
    print("\n" + "="*70)
    print("STATISTICAL SIGNIFICANCE ANALYSIS")
    print("Ethereum Weekend Effect - 2025 Data")
    print("="*70)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    print(f"\nLoaded {len(df)} days of transaction data")
    
    # Perform statistical tests
    results = perform_statistical_tests(df)
    
    # Create visualizations
    create_statistical_visualizations(df)
    
    # Save results to file
    results_text = f"""
STATISTICAL ANALYSIS RESULTS - ETHEREUM WEEKEND EFFECT
{'='*70}

Data Period: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}
Total Days: {len(df)}

DESCRIPTIVE STATISTICS:
- Weekday mean: {results['weekday_mean']:,.0f} transactions
- Weekend mean: {results['weekend_mean']:,.0f} transactions
- Difference: {results['weekday_mean'] - results['weekend_mean']:,.0f} transactions

STATISTICAL TESTS:
- T-test p-value: {results['p_value_t']:.6f}
- Mann-Whitney U p-value: {results['p_value_u']:.6f}
- ANOVA p-value: {results['p_value_anova']:.6f}

EFFECT SIZE:
- Cohen's d: {results['cohens_d']:.4f} ({interpret_cohens_d(results['cohens_d'])} effect)

CONCLUSION:
The weekend effect is {'STATISTICALLY SIGNIFICANT' if results['p_value_t'] < 0.05 else 'NOT statistically significant'}.
"""
    
    with open('outputs/statistical_results.txt', 'w') as f:
        f.write(results_text)
    
    print("✓ Saved results summary: outputs/statistical_results.txt")
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
    print("\nGenerated files in outputs/ folder:")
    print("  • statistical_analysis.png - Visual distributions and Q-Q plots")
    print("  • statistical_results.txt - Summary of test results")
    print("\n")


if __name__ == "__main__":
    main()
