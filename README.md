# Stock Market Trading API
### Written by Sam Burba

---
### About:
stock\_ai is an AI that predicts to buy or sell stocks. It uses a viterbi algorithm with backtracking to decide to buy or sell stocks depending on the stocks trend within the provided timeframe.

### To install:
```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
``` 
### To run:
```bash
python run.py [TICKER SYMBOL] [START DATE] [END DATE]
```
*Note: all dates must be MM/DD/YYYY format*
There are three additional tests provided. To run the tests:
```bash
tests/[NUMBER]
```
[NUMBER] = 1, 2, or 3
