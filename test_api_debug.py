"""
Improved test script with better debugging
Run this to diagnose the API connection issue
"""

import requests
import json

def test_etherscan_api():
    """Test if your Etherscan API key works"""
    
    print("\n" + "="*50)
    print("ETHERSCAN API CONNECTION TEST (DEBUG MODE)")
    print("="*50 + "\n")
    
    # Get API key
    print("Please enter your Etherscan API key:")
    api_key = input("API Key: ").strip()
    
    print(f"\nAPI key length: {len(api_key)} characters")
    print(f"First 8 chars: {api_key[:8]}")
    print(f"Last 4 chars: {api_key[-4:]}\n")
    
    # Test 1: Simple API call
    print("Test 1: Checking API connection...")
    url = "https://api.etherscan.io/v2/api"
    params = {
        'chainid': '1',  # Ethereum mainnet
        'module': 'stats',
        'action': 'ethsupply',
        'apikey': api_key
    }
    
    try:
        print(f"  Making request to: {url}")
        print(f"  Parameters: module=stats, action=ethsupply")
        
        response = requests.get(url, params=params)
        print(f"  HTTP Status Code: {response.status_code}")
        
        data = response.json()
        print(f"  Response: {json.dumps(data, indent=2)}\n")
        
        if data.get('status') == '1':
            print("✓ API key is working!")
            supply = int(data['result']) / 1e18
            print(f"  Current ETH supply: {supply:,.0f} ETH\n")
        else:
            print("✗ API returned an error")
            print(f"  Status: {data.get('status')}")
            print(f"  Message: {data.get('message')}")
            print(f"  Result: {data.get('result')}\n")
            
            # Give specific advice based on error
            if data.get('result') == 'Invalid API Key':
                print("DIAGNOSIS: The API key format is invalid")
                print("  → Copy the key again from Etherscan")
                print("  → Make sure there are no spaces")
            elif data.get('result') == 'Max rate limit reached':
                print("DIAGNOSIS: Rate limit hit")
                print("  → Wait a few seconds and try again")
            else:
                print("DIAGNOSIS: Unknown error")
                print("  → Check https://etherscan.io/myapikey")
                print("  → Ensure the API key is active")
            
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Network error: {str(e)}\n")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {str(e)}")
        print(f"  Raw response: {response.text}\n")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}\n")
        return False
    
    # Test 2: Fetch latest block number
    print("Test 2: Fetching latest block number...")
    params = {
        'chainid': '1',  # Ethereum mainnet
        'module': 'proxy',
        'action': 'eth_blockNumber',
        'apikey': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        print(f"  Response: {json.dumps(data, indent=2)}\n")
        
        if 'result' in data:
            block_num = int(data['result'], 16)
            print(f"✓ Latest block number: {block_num:,}\n")
        else:
            print("✗ Failed to fetch block number")
            print(f"  Response: {data}\n")
            return False
            
    except Exception as e:
        print(f"✗ Error: {str(e)}\n")
        return False
    
    # Test 3: Get block details
    print("Test 3: Fetching block transaction count...")
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
        
        if 'result' in data and data['result'] and 'transactions' in data['result']:
            tx_count = len(data['result']['transactions'])
            print(f"✓ Block {block_num:,} has {tx_count} transactions\n")
        else:
            print("✗ Failed to fetch block details")
            print(f"  Response keys: {data.keys() if isinstance(data, dict) else 'Not a dict'}\n")
            return False
            
    except Exception as e:
        print(f"✗ Error: {str(e)}\n")
        return False
    
    # All tests passed!
    print("="*50)
    print("✓✓✓ ALL TESTS PASSED! ✓✓✓")
    print("="*50)
    print("\nYour API key is working correctly!")
    print("You can now run the main analysis:")
    print("  python eth_trading_patterns.py\n")
    
    # Save API key for convenience
    save = input("Would you like to save this API key to a file? (y/n): ").strip().lower()
    if save == 'y':
        with open('api_key.txt', 'w') as f:
            f.write(api_key)
        print("✓ API key saved to api_key.txt")
        print("  (Keep this file private! Don't share it)\n")
    
    return True


if __name__ == "__main__":
    test_etherscan_api()
