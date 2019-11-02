#!/usr/bin/env python3

"""
IRSee -- a simple IRC sniffer over the local network
"""

__author__ = "Walker Griggs"
__version__ = "0.1.0"
__license__ = "MIT"

import pyshark
import sys
import os
import argparse

PERMISSIONS_MESSAGE = """
      === Permission Denied ===
      You need to run IRSee on an account with sufficient priviledges to
      capture, or need to give the account on which you're running IRSee
      sufficient privileges to capture.

      *Note* Do not run IRSee as root; TShark is inherently insecure.
      See: https://wiki.wireshark.org/CaptureSetup/CapturePrivileges for more
      info.

      tldr; Add your uesr to the `wireshark` group."""

EXIT_MESSAGE = "=== IRSee you later! ==="


def sniff(iface):
    """Capture IRC packets pass over the given interface"""
    cap = pyshark.LiveCapture(interface=iface, bpf_filter="tcp port 6667")

    try:
        capture(cap)
    except KeyboardInterrupt:
        cap.close()
        exit(0)


def capture(cap):
    """Capture packets continuously (until a keyboard interupt), and print message contents"""
    for pkt in cap.sniff_continuously():
        if "irc" in pkt:
            layer = pkt["irc"]

            if "response" in layer.field_names:
                print(layer.get_field_value("response"))
            else:
                print(layer.get_field_value("request"))

    cap.close()


def exit(code):
    """Gracefully exit"""
    print("\n" + EXIT_MESSAGE)
    try:
        sys.exit(code)
    except SystemExit:
        os._exit(code)


def main():
    parser = argparse.ArgumentParser(description="IRSee, a simple IRC sniffer")

    parser.add_argument(
        "iface", metavar="interface", type=str, nargs="+", help="the interface to sniff"
    )

    args = parser.parse_args()

    try:
        sniff(args.iface)
    except PermissionError as e:
        print(PERMISSIONS_MESSAGE)


if __name__ == "__main__":
    main()
