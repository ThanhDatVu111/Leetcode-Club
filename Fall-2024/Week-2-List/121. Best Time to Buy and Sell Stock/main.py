def maxProfit(prices: List[int]) -> int:
    minPrice = prices[0]
    result=0
    for i in range(1,len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        else:
            temp = prices[i] - minPrice
            if temp > result:
                result = temp
    return result

# Time Complexity: O(n)
# Space Complexity: O(1)

def main():
    print(f"this is the result: {maxProfit([7,1,5,3,6,4])}")
                                   
if __name__ == "__main__":
    main()