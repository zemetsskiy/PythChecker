import asyncio
from dataclasses import dataclass

from aiogram import types
from aiogram.types import ParseMode

from app.create_bot import dp
from app.utils.checker import check_wallet


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.answer("<b> Enter list of Solana or Evm wallets each with a new line (15 max at a time)</b>", parse_mode=types.ParseMode.HTML)


@dp.message_handler(lambda message: not message.text.startswith('/'))
async def handle_wallets(message: types.Message):
    max_wallet = 15
    wallets = message.text.split("\n")[:max_wallet]
    results = []

    for wallet in wallets:
        await asyncio.sleep(2)
        # if len(wallet) != 42:
        #     results.append(f"<b> {wallet} </b> <u> Invalid wallet address </u>\n")
        #     continue

        result = await check_wallet(wallet=wallet)

        results.append(f"{result}\n")

    await message.answer("\n".join(results), parse_mode=ParseMode.HTML)