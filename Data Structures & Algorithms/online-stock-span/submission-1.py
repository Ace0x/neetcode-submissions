import heapq
class StockSpanner:

    def __init__(self):
        self.h = []  # stack of (price, span)

    def next(self, price: int) -> int:
        span = 1

        while self.h and self.h[-1][0] <= price:
            old_price, old_span = self.h.pop()
            span += old_span

        self.h.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)