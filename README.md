# Stock Market Trading API
## Written by Sam Burba

---
### About:
stock\_ai is an AI that predicts to buy or sell stocks. It uses a viterbi algorithm with backtracking to come to decide at each point to buy or sell, depending on the stocks history of going up or down.

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
