import asyncio

from src.extractor.extractor import extract


async def main():

    response = await extract(
        "uploads/Report.pdf"
    )

    print("\n")
    print("=" * 50)
    print("LLM RESPONSE")
    print("=" * 50)

    print(response)


if __name__ == "__main__":
    asyncio.run(main())