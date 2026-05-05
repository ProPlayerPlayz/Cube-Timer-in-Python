# Cube Timer Mark 4
# Program by S.Sakthi Swaroopan (modernized with async live timer)

import asyncio
import random
import time

MOVES = [
    "F", "R", "L", "U", "D", "B",
    "F'", "R'", "L'", "U'", "D'", "B'",
    "F2", "R2", "L2", "U2", "D2", "B2",
]


def generate_scramble(length=20):
    """Generate a scramble with no repeated face on consecutive moves."""
    scramble = []
    prev = "ZZ"

    while len(scramble) < length:
        current = random.choice(MOVES)
        if current[0] != prev[0]:
            scramble.append(current)
            prev = current

    return " ".join(scramble)


async def live_timer(stop_event):
    """Continuously render elapsed time on a single line until stopped."""
    start = time.perf_counter()

    while not stop_event.is_set():
        elapsed = time.perf_counter() - start
        print(f"\rTime: {elapsed:0.2f}s", end="", flush=True)
        await asyncio.sleep(0.05)

    return time.perf_counter() - start


async def wait_for_stop(stop_event):
    """Wait for Enter key to stop the timer without blocking the event loop."""
    await asyncio.to_thread(input, "\nPress [Enter] to stop timer...")
    stop_event.set()


async def run_solve_session():
    """Run one full solve attempt: scramble -> start -> live timer -> stop."""
    scramble = generate_scramble()
    print("\nScramble:", scramble)

    await asyncio.to_thread(input, "Press [Enter] to start timer...")

    stop_event = asyncio.Event()
    timer_task = asyncio.create_task(live_timer(stop_event))

    await wait_for_stop(stop_event)
    final_time = await timer_task

    print(f"\nFinal Time: {final_time:0.3f}s")


def main():
    print("==============================")
    print("  Cube Timer [Mark 4 - v1.0]  ")
    print("==============================")

    while True:
        asyncio.run(run_solve_session())

        code = input("Another solve? [Y/N] >>> ").strip().lower()
        if code not in ["y", "yes"]:
            print("Closing Program...")
            break

    print("==============================")
    print("          Thank You           ")
    print("==============================")


if __name__ == "__main__":
    main()
