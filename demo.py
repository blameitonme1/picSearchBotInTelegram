import asyncio
import telegram


async def main():
    bot = telegram.Bot("6471157961:AAGEUv0WAY8XsU7WsgwZC4Db3ZRp4K7P-Ds")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())

