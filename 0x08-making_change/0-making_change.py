#!/usr/bin/python3
"""This module contains a function that calculates the
minimum number of coins needed to make a given total.
"""


def makeChange(coins, total):
    """Calculate the minimum number of coins needed to make the given total.

    Args:
    coins (list): List of coin denominations.
    total (int): The total amount to make.

    Returns:
    int: The minimum number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to use the largest denominations first
    coins.sort(reverse=True)

    # Initialize the coin count and the remaining total
    coin_count = 0
    remaining_total = total

    # Iterate over each coin denomination
    for coin in coins:
        if remaining_total == 0:
            return coin_count
        # If the coin is less than or equal to the remaining total
        if coin <= remaining_total:
            # Calculate how many coins of this denomination can be used
            num_coins = remaining_total // coin
            # Update the total number of coins used
            coin_count += num_coins
            # Update the remaining amount
            remaining_total -= num_coins * coin

    # If there's any remaining total that couldn't be made, return -1
    if remaining_total > 0:
        return -1

    return coin_count
