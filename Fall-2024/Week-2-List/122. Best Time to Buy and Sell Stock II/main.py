def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for i in range (1,len(prices)):
        if prices[i] > min_price: #shaw opporturnity
            max_profit += prices[i] - min_price
        min_price = prices[i] #min price always one index after prices[i], sell stock rapidly to find highest profit.
    return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)

def main():
    print(f"this is the result: {maxProfit([7,1,5,3,6,4])}")
                                   
if __name__ == "__main__":
    main()