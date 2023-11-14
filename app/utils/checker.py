import aiohttp


async def check_wallet(wallet):
    if wallet.startswith("0x"):
        chain = "evm"
    else:
        chain = "solana"

    url = f"https://airdrop.pyth.network/api/grant/v1/amount_and_proof?ecosystem={chain}&identity={wallet}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                result = f"<b> {wallet} </b> - ✅ <b> {int(data['amount']) / 1000000} </b>"
                print(result)
                return result
            elif response.status == 404 and "No result found" in await response.text():
                result = f"<b> {wallet} </b> - ❌"
                print(result)
                return result
            else:
                result = f"{wallet} - Something went wrong"
                print(result)
                return result