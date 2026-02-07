#!/usr/bin/env python3
"""
Simple XRP Ledger vanity wallet finder using xrpl-py.
Generates wallets until one matches a desired pattern, then prints it and exits.
Supports multiple patterns and multiprocessing.
"""

import argparse
import multiprocessing
import sys

from xrpl.wallet import Wallet


def _worker(
    patterns: list[str],
    suffix: bool,
    stop: multiprocessing.Event,
    result_queue: multiprocessing.Queue,
) -> None:
    while not stop.is_set():
        wallet = Wallet.create()
        address = wallet.address
        if suffix:
            matches = any(address.endswith(p) for p in patterns)
        else:
            matches = any(address.startswith(p) for p in patterns)
        if matches:
            result_queue.put((address, wallet.seed))
            stop.set()
            return


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find an XRP Ledger vanity address. Generates wallets until one matches, then stops."
    )
    parser.add_argument(
        "pattern",
        nargs="+",
        help="One or more strings the address must start with (e.g. rNFT rnft). Case-sensitive.",
    )
    parser.add_argument(
        "--suffix",
        action="store_true",
        help="Match pattern at end of address instead of start.",
    )
    parser.add_argument(
        "-j", "--jobs",
        type=int,
        default=multiprocessing.cpu_count(),
        metavar="N",
        help="Number of worker processes (default: CPU count).",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only print the result; no progress or extra output.",
    )
    args = parser.parse_args()

    patterns = [p for p in args.pattern if p]
    if not patterns:
        parser.error("at least one non-empty pattern is required")

    if not args.quiet:
        mode = "ending" if args.suffix else "starting"
        pattern_str = ", ".join(patterns)
        print(f"Searching for address {mode} with: {pattern_str}")
        print(f"Using {args.jobs} worker(s).")

    stop = multiprocessing.Event()
    result_queue = multiprocessing.Queue()

    workers = [
        multiprocessing.Process(
            target=_worker,
            args=(patterns, args.suffix, stop, result_queue),
        )
        for _ in range(args.jobs)
    ]
    for w in workers:
        w.start()

    address, seed = result_queue.get()
    stop.set()
    for w in workers:
        w.join(timeout=1)
        if w.is_alive():
            w.terminate()

    if not args.quiet:
        print("Match found.")
    print("Address:", address)
    print("Seed (secret):", seed)
    print("Keep the seed private. You can re-create this wallet with Wallet.from_seed(seed).")


if __name__ == "__main__":
    main()
