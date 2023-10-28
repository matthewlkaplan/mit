#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bot skeleton
"""

import random
import math
timestep = 0
def submit_market(state, symbols, my_history, period_history, cur_position):



    sigma = 0
    k = 1
    gamma = 0.1
    timestep += 1
    t = timestep / 50
    q = cur_position
    market = []

    r_a = period_history["A"]["price"] - q * gamma * sigma**2 * (50 - t)
    delta_a = gamma * sigma**2 * (50 - t) + 2 / gamma * math.log(1 + gamma / k)


    r_b = period_history["B"]["price"] - q * gamma * sigma**2 * (50 - t)
    delta_b = gamma * sigma**2 * (50 - t) + 2 / gamma * math.log(1 + gamma / k)
    

    r_c = period_history["C"]["price"] - q * gamma * sigma**2 * (50 - t)
    delta_c = gamma * sigma**2 * (50 - t) + 2 / gamma * math.log(1 + gamma / k)

    """
    Given user defined state and history of the trades you executed 
    last round, come up with a new market for this round.
    
    `state` is initially an empty dictionary
    `symbols` is a list of symbol names

    `my_history` is a dict that maps a symbol name to a list of your trades for that symbol
    Each trade in `my_history[symbol]` is a dict of the format
    {
         "size": volume traded,
         "price": price traded at,
         "dir": either "buy" or "sell",
         "id_against": the type of party traded against, either "team"
                         or "customer"
    }

    `period_history` is a dict that maps a symbol name to a list of all trades for that symbol
    Each trade in `period_history[symbol]` is a dict of the format
    {
        "size": volume traded (will always be 1),
        "price": price traded at,
        "dir": either "buy" or "sell" depending on the team's action (not the customer's),
        "id_against": "customer",
    }
    """

    """
    Example of state you might want to keep track of are the last buy and sell prices
    you submitted to the market
    """
    state["buy_price"] = 1250
    state["sell_price"] = 1750

    """
    Example code to keep track of round number
    """
    if "round" not in state:
        state["round"] = 0
    state["round"] += 1
    

    """
    Example code to count number of buys and sells you
    executed last round in symbol A
    """
    my_num_buys = 0
    my_num_sells = 0
    for trade in my_history["A"]:
        if trade["dir"] == "buy":
            my_num_buys += 1
        elif trade["dir"] == "sell":
            my_num_sells += 1
    
    num_buys = 0
    num_sells = 0
    for trade in period_history["C"]:
        if trade["dir"] == "buy":
            num_buys += 1
        elif trade["dir"] == "sell":
            num_sells += 1
    
    return {
        "A": {
            "buy": {
                    "price": state["buy_price"] + delta_a,
                    "size": 1
                    },
            "sell": {
                    "price": state["sell_price"] - delta_a,
                    "size": 1
                    },
            },
        "B": {
            "buy": {
                    "price": state["buy_price"] + delta_b,
                    "size": 2
                    },
            "sell": {
                    "price": state["sell_price"] - delta_b,
                    "size": 2
                    },
            },
        "C": {
            "buy": {
                    "price": state["buy_price"] + delta_c,
                    "size": 3
                    },
            "sell": {
                    "price": state["sell_price"] - delta_c,
                    "size": 3
                    },
            }
    }


# Run this code to check that your bot handles the input parameters correctly.
# Please DO NOT have this statement in your submission!
print(submit_market(
    {},
    ['A', 'B', 'C'],
    {
        'A': [{'size': 1, 'price': 1285, 'dir': 'buy', 'id_against': 'customer'}], 
        'B': [], 
        'C': [{'size': 1, 'price': 1766, 'dir': 'sell', 'id_against': 'customer'}, {'size': 1, 'price': 1766, 'dir': 'sell', 'id_against': 'customer'}]
    },
    {
        'A': [{'size': 1, 'price': 1246, 'dir': 'buy', 'id_against': 'customer'}, {'size': 1, 'price': 1250, 'dir': 'buy', 'id_against': 'customer'}], 
        'B': [{'size': 1, 'price': 1763, 'dir': 'sell', 'id_against': 'customer'}, {'size': 1, 'price': 1763, 'dir': 'sell', 'id_against': 'customer'}, {'size': 1, 'price': 1652, 'dir': 'sell', 'id_against': 'customer'}, {'size': 1, 'price': 1652, 'dir': 'sell', 'id_against': 'customer'}], 
        'C': [{'size': 1, 'price': 1758, 'dir': 'sell', 'id_against': 'customer'}, {'size': 1, 'price': 1758, 'dir': 'sell', 'id_against': 'customer'}]
    },
    {'A': 1, 'B': -2, 'C': -9},
))

