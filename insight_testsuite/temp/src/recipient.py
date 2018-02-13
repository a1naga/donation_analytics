from heapq import *
import math


class RecipientData:
    '''This class represents the running values of donation information for a recipient.
    It calculates percentile as donation amount is added. For percentile calculation a max
    heap and a min heap is used.
    '''

    def __init__(self,percentile):
        self.num_contributions = 0
        self.total_donation_amt = 0
        self.heaps = [], []
        self.percentile = percentile

    def get_num_cont(self):
        return self.num_contributions

    def get_total_donation(self):
        return self.round_num(self.total_donation_amt)

    def add_donation(self, amt):
        'Adding up the donation amount and pushing the values to minheap and maxheap'
        self.num_contributions += 1
        self.total_donation_amt += amt
        max_heap, min_heap = self.heaps

        'using the heapq as maxheap by negating the amt, by default heapq is minheap'
        if len(max_heap) > 0:
            if amt > float(-max_heap[0]):
                heappush(min_heap,amt)
            else:
                heappush(max_heap,-amt)
            self.balance_heap()
        else:
            heappush(max_heap, -amt)

    def balance_heap(self):
        'Balancing the heap based on the percentile value'
        maxheap,minheap = self.heaps
        index = math.ceil((self.percentile/100.0)*self.num_contributions)
        if len(maxheap) > index:
            heappush(minheap, -heappop(maxheap))
        elif len(maxheap) < index:
            heappush(maxheap, -heappop(minheap))

    def round_num(self,num):
        'Rounding up the total dollor amount and returning it'
        val = num - int(num)
        if val >= .50:
            return math.ceil(num)
        elif val < .50:
            return math.floor(num)

    def find_percentile(self):
        maxheap,minheap = self.heaps
        return self.round_num(-maxheap[0])
