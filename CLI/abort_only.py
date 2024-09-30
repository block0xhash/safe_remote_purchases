# Import the 'boa' library for interacting with Vyper smart contracts.
# The '# type: ignore' comment is used here to bypass any type-checking issues that might arise if 'boa'
# is not properly recognized by type-checkers like MyPy, ensuring that this line does not cause errors.
import boa  # type: ignore

# Set up the seller's address as the externally owned account (EOA) from the default boa environment.
seller = boa.env.eoa

# Set the seller's balance to 100 ether (100 * 10^18 wei) in the simulated boa environment.
boa.env.set_balance(seller, 100 * 10**18)

# Print out the seller's address and current balance.
print(f"1. Seller: {seller} balance: {boa.env.get_balance(seller)}")

# Define the value of the item for sale as 2 ether (2 * 10^18 wei).
value = 2 * 10**18

# Load the contract from the specified Vyper source file, passing in the value (2 ether).
contract = boa.load("../contracts/escrow.vy", value=value)

# Print the seller's balance after loading the contract.
print(f"2. Seller: {seller} balance: {boa.env.get_balance(seller)}")

# Print the contract's address and its balance (after deployment).
print(f"Contract: {contract.address} balance: {boa.env.get_balance(contract.address)}")

# Print the seller's balance again to reflect any changes due to the contract deployment.
print(f"3. Deployer (seller): {seller} now has balance of: {boa.env.get_balance(contract.address)}")

# Call the 'abort' function of the contract, which should refund the seller's deposit.
contract.abort()

# Print a message indicating that the sale has been aborted and the deposit refunded.
print("Sale aborted and seller's deposit refunded.")

# Print the contract's balance after the 'abort' function is called, which should be 0 if refunded.
print(f"Contract: {contract.address} balance: {boa.env.get_balance(contract.address)}")

# Print the seller's balance after the 'abort' function, showing the refund.
print(f"Seller: {seller} balance: {boa.env.get_balance(seller)}")
