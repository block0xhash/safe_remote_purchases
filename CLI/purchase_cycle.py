import boa  # type: ignore

# Set up the seller's address as the externally owned account (EOA) from the default boa environment.
seller = boa.env.eoa

# Set the seller's balance to 8 ether (8 * 10^18 wei) in the simulated boa environment.
boa.env.set_balance(seller, 8 * 10**18)

# Print out the seller's address and current balance.
print(f"Seller: {seller} balance: {boa.env.get_balance(seller)}")

# Generate a new address for the buyer in the simulated environment.
buyer = boa.env.generate_address()

# Set the buyer's balance to 5 ether (5 * 10^18 wei) in the simulated environment.
boa.env.set_balance(buyer, 5 * 10**18)

# Print out the buyer's address and current balance.
print(f"Buyer: {buyer} balance: {boa.env.get_balance(buyer)}")

# Define the value of the item for sale as 2 ether (2 * 10^18 wei).
item_value = 2 * 10**18

# Load the contract from the specified Vyper source file, deployed by the seller.
contract = boa.load("../contracts/escrow.vy", value=item_value)

# Print the contract's address and initial balance.
print(f"Contract: {contract.address} balance: {boa.env.get_balance(contract.address)}")

# Perform the purchase. The buyer sends 4 ether (2 * item_value) as the purchase deposit.
purchase_value = 2 * item_value

# Use 'prank' to simulate that the buyer is performing the purchase transaction.
with boa.env.prank(buyer):
    contract.purchase(value=purchase_value)
    
# Print a message indicating that the purchase was successful and the buyer's deposit was sent.
print("Item purchased by the buyer.")

# Print the contract's balance after the purchase.
print(f"Contract: {contract.address} balance: {boa.env.get_balance(contract.address)}")

# Print the buyer's balance after the purchase.
print(f"Buyer: {buyer} balance: {boa.env.get_balance(buyer)}")

# Print the seller's balance after the purchase.
print(f"Seller: {seller} balance: {boa.env.get_balance(seller)}")

# Simulate the buyer confirming receipt of the item.
with boa.env.prank(buyer):
    contract.received()

# Print a message indicating that the buyer confirmed receiving the item.
print("Buyer confirmed receiving the item.")

# Print the contract's balance after the receipt confirmation (should be zero since the funds are distributed).
print(f"Contract: {contract.address} balance: {boa.env.get_balance(contract.address)}")

# Print the buyer's balance after the receipt confirmation.
print(f"Buyer: {buyer} balance: {boa.env.get_balance(buyer)}")

# Print the seller's balance after the receipt confirmation.
print(f"Seller: {seller} balance: {boa.env.get_balance(seller)}")
