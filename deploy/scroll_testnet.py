import boa  # type: ignore # Import the boa library for interacting with Vyper contracts.
from eth_account import Account  # type: ignore # For handling Ethereum accounts and private keys securely.
import os  # For working with environment variables.
import subprocess  # To run shell commands like decrypting the private key using gpg.

# Set the network environment using the SCROLL_KEY from environment variables.
SCROLL_KEY = os.getenv('SCROLL_KEY')
if SCROLL_KEY:
    SCROLL_URL = f"https://scroll-sepolia.g.alchemy.com/v2/{SCROLL_KEY}"
    boa.set_network_env(SCROLL_URL)
else:
    print("SCROLL_KEY environment variable not set. Exiting.")
    exit(1)

# Function to decrypt and get the private key using gpg (or other secure methods).
def get_private_key():
    try:
        # Command to decrypt the private key from a GPG-encrypted file.
        private_key = subprocess.run(
            ["gpg", "--decrypt", os.path.expanduser("~/key.env.gpg")],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        ).stdout.decode('utf-8').strip()

        return private_key
    except subprocess.CalledProcessError as e:
        print(f"Error decrypting private key: {e.stderr.decode('utf-8')}")
        return None

# Decrypt the private key using GPG.
private_key = get_private_key()

if private_key:
    # Create an Ethereum account from the decrypted private key.
    deployer_account = Account.from_key(private_key)

    # Add the decrypted private key to the boa environment (for deployment purposes).
    boa.env.add_account(deployer_account)

    # Load the contract partially
    # deployer = boa.load_partial("../contracts/escrow.vy")
    deployer = boa.load_partial("contracts/escrow.vy")


    # Deploy the contract using the deployer account.
    contract = deployer.deploy()

    result = boa.verify(contract)
    result.wait_for_verification()

    # Print the contract address after successful deployment.
    print(f"Contract deployed at address: {contract.address}")
else:
    print("Failed to retrieve private key. Exiting.")
