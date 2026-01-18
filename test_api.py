"""
Simple test script to verify Etherscan API connection
Run this first to make sure everything is working!
"""

import requests
import os

def test_etherscan_api():
    """Test if your Etherscan API key works"""
    
    print("\n" + "="*50)
    print("ETHERSCAN API CONNECTION TEST")
    print("="*50 + "\n")
    
    # Get API key
    api_key = os.getenv('ETHERSCAN_API_KEY')
    
    
    # Test 1: Check API key is valid
    print("Test 1: Checking if API key is valid...")
    url = "https://api.etherscan.io/v2/api"
    params = {
        'chainid': '1',  # Ethereum mainnet
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == '1':
            print("✓ API key is valid!")
            print(f"  Current ETH price: ${data['result']['ethusd']}")
        else:
            print("✗ API key test failed")
            print(f"  Error: {data.get('message', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"✗ Connection error: {str(e)}")
        return False
    
    # Test 2: Fetch a sample block
    print("\nTest 2: Fetching latest block data...")
    params = {
        'chainid': '1',  # Ethereum mainnet
        'module': 'proxy',
        'action': 'eth_blockNumber',
        'apikey': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'result' in data:
            block_num = int(data['result'], 16)
            print(f"✓ Successfully fetched latest block: {block_num:,}")
        else:
            print("✗ Failed to fetch block data")
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False
    
    # Test 3: Get transaction count from a block
    print("\nTest 3: Fetching transaction count from a block...")
    params = {
        'chainid': '1',  # Ethereum mainnet
        'module': 'proxy',
        'action': 'eth_getBlockByNumber',
        'tag': hex(block_num),
        'boolean': 'false',
        'apikey': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'result' in data and data['result']:
            tx_count = len(data['result'].get('transactions', []))
            print(f"✓ Block {block_num:,} has {tx_count} transactions")
        else:
            print("✗ Failed to fetch transaction count")
            return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False
    
    # All tests passed!
    print("\n" + "="*50)
    print("✓ ALL TESTS PASSED!")
    print("="*50)
    print("\nYour setup is working correctly!")
    print("You can now run the main analysis script:")
    print("  python eth_trading_patterns.py")
    print("\n")
    
    return True


if __name__ == "__main__":
    test_etherscan_api()
