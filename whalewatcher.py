import os
import requests
import streamlit as st

# Function to fetch Ethereum wallet balances from Etherscan API
def fetch_wallet_balances(api_key, addresses):
    url = f"https://api.etherscan.io/api?module=account&action=balancemulti&address={','.join(addresses)}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            return data['result']
    return None

# Streamlit app
def main():
    # Title of the Streamlit app
    st.title('Highrise Ecommerce LLC: Cryptocurrency Whale Watcher')

    # Ethereum wallet addresses to fetch balances for
    addresses = [
        "0x66E092fD00c4E4eb5BD20F5392C1902d738aE7bC",
        "0x3E46a9EC06b3A9824C306f13785EEcCdf6e21eb9",
        "0x21E27a5E5513D6e65C4f830167390997aA84843a",
        "0x97d54945Fa681EFBDE3D8a73b79E38EA1C47e22F",
        "0xa29E963992597B21bcDCaa969d571984869C4FF5",
        "0xcbdB19D4F21368B87c2c8f43CE5D463dDc788f4D",
        "0x18E24850FDEceee577da1e08C63B260cCf69B962",
        "0x0A4F6ecB214Dc1d9aCdd99743B4DCc58ccc088b9",
        "0xEae7380dD4CeF6fbD1144F49E4D1e6964258A4F4",
        "0xCFFAd3200574698b78f32232aa9D63eABD290703",
        "0xcc6FcfB8b3988043E382a481d6BF482D68897024",
        "0xceB69F6342eCE283b2F5c9088Ff249B5d0Ae66ea",
        "0xb0E62712d08d246C03EF19076dfbA56C355b4022",
        "0xC44b7316936E2F004E688fD53a95e060Df1811C3",
        "0x004c26816dA9219CF3408e84eDD9716Df4B5739A",
        "0x0e747EB2ff0F26fB77c3a1eA67EE07FAc2DbB783",
        "0xb5d85CBf7cB3EE0D56b3bB207D5Fc4B82f43F511",
        "0xBFCd86e36D947A9103A7D4a95d178A432723d6aD",
        "0xcc6FcfB8b3988043E382a481d6BF482D68897024",
        "0xC5caAe9CBEfADBb6eC748cB13CD8Ad31a44aEfBB"
    ]

    # Fetch the API key from environment variable
    api_key = os.getenv("ETHERSCAN_API_KEY")

    if not api_key:
        st.error("API key not found. Please set the ETHERSCAN_API_KEY environment variable.")
        return

    # Fetch wallet balances
    balances = fetch_wallet_balances(api_key, addresses)
    if balances is not None:
        st.write("Ethereum Wallet Balances:")
        for i, balance_data in enumerate(balances, start=1):
            address = balance_data['account']
            balance_ether = int(balance_data['balance']) / 10**18
            st.write(f"{i}. Address: {address}, Balance: {balance_ether} Ether")
        
        # Create a bar chart
        balances_dict = {balance_data['account']: float(balance_data['balance']) / 10**18 for balance_data in balances}
        st.bar_chart(balances_dict)
    else:
        st.error("Failed to fetch wallet balances. Please check your API key and try again later.")

if __name__ == '__main__':
    main()