# Getting Your `urpn`
To get your `urpn` navigate to the [RBWM website](https://forms.rbwm.gov.uk/bincollections) and enter your address. The `urpn` can be found in the url.

# Usage
Modify `bin_collection.py` and add your `urpn`.

```
cd /path/to/repo/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 bin_collection.py
```

For subsequent uses:

```
cd /path/to/repo/
source .venv/bin/activate
python3 bin_collection.py
```
