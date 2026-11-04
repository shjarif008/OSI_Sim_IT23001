#!/usr/bin/env python3
"""Simple terminal visualization of OSI encapsulation and decapsulation."""

import argparse
import time
from datetime import datetime

from colorama import Fore, Style, init

init(autoreset=True)

LAYERS = [
    (7, "Application", Fore.GREEN),
    (6, "Presentation", Fore.CYAN),
    (5, "Session", Fore.MAGENTA),
    (4, "Transport", Fore.YELLOW),
    (3, "Network", Fore.BLUE),
    (2, "Data Link", Fore.RED),
    (1, "Physical", Fore.WHITE),
]


def log_layer(number, name, message, color, animate, delay):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {color}Layer {number}: {name}{Style.RESET_ALL}")
    print(f"           {message}")
    if animate:
        time.sleep(delay)


def visualize(message, animate=False, delay=0.5):
    print("\n" + "=" * 48)
    print("             OSI 7-LAYER SIMULATION")
    print("=" * 48)

    print(f"\nOriginal message: {message!r}")

    print(f"\n{Fore.GREEN}{'=' * 15} ENCAPSULATION {'=' * 15}{Style.RESET_ALL}")
    print("Sender: Application -> Physical\n")

    send_messages = {
        7: f"Application creates the message: {message}",
        6: "Presentation formats the data.",
        5: "Session manages the communication session.",
        4: "Transport prepares data for end-to-end delivery.",
        3: "Network handles logical addressing and routing.",
        2: "Data Link prepares a frame for the local link.",
        1: "Physical transmits the data as bits.",
    }

    for number, name, color in LAYERS:
        log_layer(number, name, send_messages[number], color, animate, delay)

    print(f"\n{Fore.GREEN}Transmission complete.{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}{'=' * 15} DECAPSULATION {'=' * 15}{Style.RESET_ALL}")
    print("Receiver: Physical -> Application\n")

    receive_messages = {
        1: "Physical receives the transmitted bits.",
        2: "Data Link processes the received frame.",
        3: "Network processes logical addressing information.",
        4: "Transport processes transport information.",
        5: "Session handles the communication session.",
        6: "Presentation interprets the received data format.",
        7: f"Application receives the original message: {message}",
    }

    for number, name, color in reversed(LAYERS):
        log_layer(number, name, receive_messages[number], color, animate, delay)

    print(f"\n{Fore.GREEN}{'=' * 15} COMPLETE {'=' * 15}{Style.RESET_ALL}")
    print("The message has reached the receiving application.")
    print("=" * 48 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Simple terminal visualization of the OSI 7-layer model."
    )
    parser.add_argument(
        "--message",
        default="Hello OSI Model",
        help="Message to visualize (default: Hello OSI Model)",
    )
    parser.add_argument(
        "--animate",
        action="store_true",
        help="Add a short delay between layers",
    )
    args = parser.parse_args()

    visualize(args.message, animate=args.animate)


if __name__ == "__main__":
    main()
