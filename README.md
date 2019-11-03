# IRSee :eyes::nose:
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

IRSee is an IRC layer sniffer over the local network.

**Disclaimer: IRSee was developed with the intent of observing the IRC protocol in real time. It should be used for educational purposes only. Though the vast majority of IRC traffic is encrypted, sifting through other people's conversations is still morally questionable. Always sniff with consent**

## Dependencies

The only OS dependency necessary (outside of Python3 and pip) is `tshark`. If your package repository doesn't supply `tshark`, it should supply `wireshark-cli`, or, at the very least, `wireshark`. (although, if you're stuck downloading wireshark, you might as well use that)

Otherwise, a simple `pip install pyshark` or `pip install -r requirements.txt` will get the remaining Python packages.

## Usage

The first step is to identify which interface you want to sniff. A simple `ifconfig` or, better yet, `ipaddr` will list all available interfaces.

IRSee will, by default, listen over port `6667`. If your IRC client listens a network over a different port, say `6697`, specify the port with `--port` (or `-p`). If you're unsure of what port (and the default isn't working), try using the `--all` flag and narrowing down from there.
