#source; reference from Geek Knapsack Problem
def _init_(self, profit, weight):
  self.profit=profit
  self.weight=weight

def knapsackProblem(w, arr):
  #profit = 
  arr.sort(key=lambda input:(input.profit/input.weight),reverse=True)
  result=0
  for i in arr:
    if i.weight<=w:
      w-=i.weight
      result+=i.profit
    else:
      result +=i.profit*(w/i.weight)
  return result

