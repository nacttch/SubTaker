# SubTaker - Subdomain Enumeration Toolkit

![SubTaker](SubTaker.png)

## Overview

**SubTaker** is a professional and interactive command-line toolkit designed for subdomain enumeration. It allows you to test single subdomains, load from a custom file, or use the built-in wordlist. Results are neatly stored in JSON format for easy integration into further workflows.

**Disclaimer:** Use this toolkit only on domains and networks for which you have explicit written permission. Unauthorized scanning or probing of systems you do not own is illegal.

## Features

* **Interactive Menu:** Choose between manual input, file input, or default wordlist.
* **JSON Reports:** Clean output saved in `report.json`.
* **Colorful CLI:** ASCII art banner and colored terminal interface.
* **Flexible Input:**

  * Option 1 — Enter a single subdomain manually.
  * Option 2 — Provide a file containing subdomains.
  * Option 3 — Use the default `subdomains.txt` wordlist inside the tool.
  * Option 4 — Exit.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/USERNAME/SubTaker.git
cd SubTaker
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Usage

```bash
python3 main.py
```

1. Enter the target domain (e.g., `example.com`).
2. Select one of the modes from the interactive menu.
3. Wait for the enumeration to complete.
4. View results in `report.json`.

### CLI Example

```
                                                                                                                                                                                                                                           
.▄▄ · ▄• ▄▌▄▄▄▄· ▄▄▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .▄▄▄                                                                                                                                                                                                  
▐█ ▀. █▪██▌▐█ ▀█▪•██  ▐█ ▀█ █▌▄▌▪▀▄.▀·▀▄ █·                                                                                                                                                                                                
▄▀▀▀█▄█▌▐█▌▐█▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐▀▀▄                                                                                                                                                                                                 
▐█▄▪▐█▐█▄█▌██▄▪▐█ ▐█▌·▐█▪ ▐▌▐█.█▌▐█▄▄▌▐█•█▌                                                                                                                                                                                                
 ▀▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀ .▀  ▀                                                                                                                                                                                                
                                                                                                                                                                                                                                           
           SubTaker - by Nactch                     

--------------------------------------------------
Enter target domain: example.com
Choose option:
1 - Single subdomain
2 - Subdomains from file
3 - Default wordlist
4 - Exit
Choice: 3
```

## Report Output

Reports are saved in the tool’s folder:

* `report.json` — machine-readable JSON report.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
