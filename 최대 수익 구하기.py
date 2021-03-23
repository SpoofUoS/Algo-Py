def max_profit(prices):
    n = len(prices)
    
    max_profit = 0                         # 최대 수익은 항상 0이상
    min_price = prices[0]                  # 첫째 날의 주가를 최솟값으로 기억
    
    
    for i in range(1,n):                   # 1부터 n-1까지 반복
        profit = prices[i] - min_price     # 지금 까지의 최솟값에 주식을 사서 i날에 팔때의 수익
        
        if profit > max_profit:            # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            max_profit = profit
            
        if prices[i] < min_price:          # i날 주가가 최솟값보다 작으면 값으 고정
            min_price = prices[i]
    
    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(max_profit(stock))