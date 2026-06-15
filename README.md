# Meter Internet Bandwidth

Python script to measure internet download and upload speed, using the `speedtest-cli` library.

## 

## Features

* Automatically selects the nearest test server
* Measures download speed in Mbps
* Measures upload speed in Mbps
* Displays formatted results in the terminal

## 

## Requirements

* Python 3.x
* "speedtest-cli" library

## 

## Installation

bash
pip install speedtest-cli


## Usage

bash
python speed-test-bandwidth.py


## Example output


🛰️  Connecting to test servers... Please wait.
📥 Testing DOWNLOAD speed...
📤 Testing UPLOAD speed...

==============================
          TEST RESULTS          
==============================
⚡ Download: 87.34 Mbps
⚡ Upload:   23.12 Mbps
==============================


## Roadmap

* \[ ] Save results history to CSV
* \[ ] Add command-line options (argparse)
* \[ ] Evaluate migration to the official Ookla Speedtest CLI, since the `speedtest-cli` library is no longer actively maintained

