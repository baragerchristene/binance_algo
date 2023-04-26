# get live order book info from websocket
# decide which 5 assets have the highest trade volume 
# create a 'trading pair'object with each of those assets (so that the pairs that are being viewed are reusable later in the code)
# watch each of the trading pairs objects and wait for the right time to enter the trade 
# when market conditions permit, enter the trade (use pandas to create a csv file with every detail on the trade so that the bot handler (me) can view later and make adjustments )
# continue watching whilst in the trade to find the right time to exit

# gpt suggestions:
# implement risk management. have a "safeword" so to speak, a condition in place that would make the trade appear risky and the algorithm not enter the trade with the asset 
# implement a position sizing strategy to help the algorithm decide how much capital should be allocated to any given trading pair object# 