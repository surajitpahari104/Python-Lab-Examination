# Question 2: Online Mobile Store

def mobile_store(prices):
    print("Mobiles costing more than Rs. 20,000:",
          [price for price in prices if price > 20000])
    print("Total inventory value: Rs.", sum(prices))
    print("Most expensive mobile price: Rs.", max(prices))

mobile_store([15000, 22000, 35000, 18000, 48000])
