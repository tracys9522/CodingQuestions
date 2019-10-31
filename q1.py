#calculate total profit from two directory examples
#Tracy Sun

#example 1
profit = {
"cost_price": 32.67,
"sell_price": 45.00,
"inventory": 1200
}

# total profit = sales - cost
total_profit = (profit['sell_price']-profit['cost_price']) * profit['inventory']
print profit
print "Profit = ", str(total_profit)

#example 2
profit = {
"cost_price": 225.89,
"sell_price": 550.00,
"inventory": 100
}

total_profit = (profit['sell_price']-profit['cost_price']) * profit['inventory']
print profit
print "Profit = ", str(total_profit)
