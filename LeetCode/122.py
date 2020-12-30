# def maxProfit(prices) -> int:
#     profit = 0
#     for i in range(1, len(prices)):
#         if prices[i] - prices[i-1] > 0:
#             profit += prices[i] - prices[i-1]
#     return profit

def maxProfit(prices) -> int:
    return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

print(maxProfit([7,1,5,3,6,4]))
