import asyncio
import telegram

async def main():
    bot = telegram.Bot("6471157961:AAGEUv0WAY8XsU7WsgwZC4Db3ZRp4K7P-Ds")
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=5832880157)
        


if __name__ == '__main__':
    asyncio.run(main())

