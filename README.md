# htbPicker
Search engine for Hack The Box machines using filters. It also selects a random machine for you.

## Usage

1. Clone repo `git clone https://github.com/thegoodhackertv/htbPicker.git`
2. Install requirements `pip3 install -r requirements.txt`
3. Export Hack The Box API Key: `export HTBKEY="key-here"` (https://app.hackthebox.com/profile/settings to create an App Token)
4. Download machine list `python3 htbPicker.py --update` this will update allmachines.json
5. Apply filters `python3 htbPicker.py -d Medium -os Windows -s 4.2 --random`

## Todo
- Enable single filters
- Search by name
- Print machine avatar
- Add colors

## Support
[<img width=300 alt="patreon" src="https://pbs.twimg.com/media/DC4gjLRUMAAyQ92?format=jpg">](https://www.patreon.com/thegoodhacker)
[<img width=250 alt="buymeacoffe" src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png">](https://www.buymeacoffee.com/thegoodhacker)
