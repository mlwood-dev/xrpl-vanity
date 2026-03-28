# XRP Vanity Wallet Finder (Beginner Guide)

This project helps you generate an XRP Ledger wallet address that matches text you choose.

Example goals:
- Address starts with `rNFT`
- Address starts with `rXRP`
- Address ends with `abc` (optional mode)

The script keeps generating new wallets until it finds a match, then stops.

## Important Safety Notes (Read First)

- The script prints a **seed** (your wallet secret key).
- Anyone who has this seed can control the wallet and funds.
- Never share the seed in chat, screenshots, email, cloud notes, or public posts.
- If a seed is exposed, treat the wallet as compromised and do not use it.
- This tool only creates wallets. It does **not** fund them or send transactions.

## What You Need

- A computer with internet access
- Python 3.10 or newer
- Terminal app (Command Prompt, PowerShell, or macOS Terminal)

No previous Python knowledge is required. Just copy/paste the commands below.

## 1) Download or Open This Project

If you already have the folder, open Terminal in this folder:

`xrpl-vanity`

If you are using Git:

```bash
git clone https://github.com/<your-username>/xrpl-vanity.git
cd xrpl-vanity
```

## 2) Check Python Is Installed

Run:

```bash
python3 --version
```

If that fails, try:

```bash
python --version
```

You want to see Python `3.10+` (for example `Python 3.11.8`).

If Python is missing:
- macOS: install from [python.org](https://www.python.org/downloads/macos/)
- Windows: install from [python.org](https://www.python.org/downloads/windows/) and check "Add Python to PATH"
- Linux: use your package manager or [python.org](https://www.python.org/downloads/source/)

## Chromebook Setup (ChromeOS)

Chromebooks can run this script using the built-in Linux environment.

### 1) Enable Linux on Chromebook

1. Open Chromebook **Settings**
2. Go to **Advanced** -> **Developers** -> **Linux development environment**
3. Click **Turn on** and finish setup

After setup, a Linux Terminal window opens.

### 2) Install tools in Linux Terminal

Run:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

### 3) Get this project and enter folder

```bash
git clone https://github.com/<your-username>/xrpl-vanity.git
cd xrpl-vanity
```

### 4) Install dependencies and run

```bash
python3 -m pip install -r requirements.txt
python3 vanity.py rNFT
```

### Chromebook performance tip

Many Chromebooks have lower-power CPUs. Start with fewer workers to keep the device responsive:

```bash
python3 vanity.py rNFT --jobs 2
```

If your Chromebook gets hot or slow, reduce `--jobs` to `1`.

## 3) Install Dependencies

From inside the project folder, run:

```bash
python3 -m pip install -r requirements.txt
```

If your system uses `python` instead of `python3`:

```bash
python -m pip install -r requirements.txt
```

This installs `xrpl-py`, the library used to create XRP wallets.

## 4) Run the Script

Basic command:

```bash
python3 vanity.py <pattern>
```

Example (address starts with `rNFT`):

```bash
python3 vanity.py rNFT
```

The script will:
1. Start searching
2. Use multiple CPU workers by default
3. Print the first matching address and seed
4. Exit automatically

## Common Examples

### A) Match one prefix (starts with text)

```bash
python3 vanity.py rXRP
```

### B) Match multiple possible prefixes

This matches if address starts with either `rNFT` or `rnft`:

```bash
python3 vanity.py rNFT rnft
```

### C) Match a suffix (ends with text)

```bash
python3 vanity.py abc --suffix
```

### D) Set worker count manually

Use fewer workers (example: 4):

```bash
python3 vanity.py rDOGE --jobs 4
```

### E) Print result only (quiet mode)

```bash
python3 vanity.py rVIP --quiet
```

## Full Command Options

```bash
python3 vanity.py pattern [pattern ...] [--suffix] [-j N] [-q]
```

- `pattern`: one or more strings to match (case-sensitive)
- `--suffix`: match at the end instead of the start
- `-j N`, `--jobs N`: number of worker processes
- `-q`, `--quiet`: only print final result lines

## How Long Will It Take?

Vanity search is brute force. Time is unpredictable.

General rule:
- Short patterns can be found quickly
- Longer or very specific patterns can take much longer

Also depends on:
- Your CPU speed
- Number of workers
- Whether you match start (`prefix`) or end (`suffix`)

## Example Output

```text
Searching for address starting with: rNFT
Using 8 worker(s).
Match found.
Address: rNFT7Y...
Seed (secret): sEd...
Keep the seed private. You can re-create this wallet with Wallet.from_seed(seed).
```

## Troubleshooting

### "python3: command not found" or "python: command not found"
- Install Python from [python.org](https://www.python.org/downloads/)
- Restart Terminal after installation

### "No module named xrpl"
- Dependency is missing. Run:
  - `python3 -m pip install -r requirements.txt`

### It runs for a long time without a match
- Try a shorter pattern
- Try fewer characters
- Check capitalization (matching is case-sensitive)

### How do I stop it?
- Press `Ctrl + C` in Terminal

## Security Best Practices

- Store the seed in a password manager or secure offline location
- Do not keep seeds in plain text files
- Do not commit seeds to Git repositories
- Test first with small amounts if you intend to use the wallet on mainnet

## Quick Start (Copy/Paste)

```bash
python3 -m pip install -r requirements.txt
python3 vanity.py rNFT
```

If that works, you are ready to search for your own vanity address.
