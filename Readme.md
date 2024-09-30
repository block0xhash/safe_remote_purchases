
# Verified Deployed contract

https://sepolia.scrollscan.com/address/0x9fe9fb0a65184b335c698a110cb5a6ece9c89245#code


# Safe Remote Purchase (Vyper on Scroll)

This project demonstrates the potential of [Vyper](https://vyper.readthedocs.io/en/stable/) as an alternative to Solidity for building smart contracts on the Scroll network. The included CLI folder provides a command-line interface for interacting with the contract.

## Contract Overview

This contract is a port of the original Solidity-based [Safe Remote Purchase](https://github.com/ethereum/solidity/blob/develop/docs/solidity-by-example.rst) example, rewritten and optimized in Vyper. It ensures secure transactions between buyers and sellers with deposit mechanisms that guarantee fairness.

### Transaction Flow:

1. **Seller posts an item for sale** and places a safety deposit (2x the item value).
   - Contract balance: `2 * item value`.
   - (Seller can reclaim the deposit and cancel the sale if no purchase is made.)
2. **Buyer purchases the item** by sending the item value and an additional deposit (equal to the item value).
   - Contract balance: `4 * item value`.
3. **Seller ships the item** to the buyer.
4. **Buyer confirms receipt**, and the following happens:
   - Buyer receives a refund of their deposit (item value).
   - Seller receives their deposit (2x item value) plus the item's value.
   - Contract balance: `0`.

## Project Structure

- **`deploy/deploy.py`**: Script to deploy the contract using Scroll's API.
- **CLI**: A command-line interface for interacting with the smart contract.

### Scroll Network API

The deployment script (`deploy/deploy.py`) uses the Scroll network API. Set up your environment using the `SCROLL_KEY` from your environment variables.

```python
SCROLL_KEY = os.getenv('SCROLL_KEY')
if SCROLL_KEY:
    SCROLL_URL = f"https://scroll-sepolia.g.alchemy.com/v2/{SCROLL_KEY}"
    boa.set_network_env(SCROLL_URL)
else:
    print("SCROLL_KEY environment variable not set. Exiting.")
    exit(1)
