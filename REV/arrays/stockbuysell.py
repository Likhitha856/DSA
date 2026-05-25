nums = [5, 4, 3, 2, 1]
def stocks(nums):
    if not nums:
        return 0, -1, -1
    buy=sell=nums[0]
    dayToSell=-1
    dayToBuy=-1
    tempDayToBuy=0
    profit=0
    max_profit=profit
    for i in range(1,len(nums)):
        if nums[i]<buy:
            buy=nums[i]
            tempDayToBuy=i
        sell=nums[i]
        profit=sell-buy
        if profit>max_profit: #to prevent same day buy and sell avoid >=
            max_profit=profit
            dayToBuy=tempDayToBuy
            dayToSell=i
            
            
    return max_profit,dayToBuy,dayToSell
print(stocks(nums))