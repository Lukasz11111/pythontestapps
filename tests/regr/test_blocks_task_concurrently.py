import asyncio

async def factorial(name, number):
    revdebug.block()
    f = 1
    for i in range(0, 3):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        # revdebug.block(True)
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    revdebug.snapshot(f'block {name}')
    a=1
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())