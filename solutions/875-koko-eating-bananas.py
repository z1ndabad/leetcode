class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        
        while min_speed < max_speed:
            current_speed = min_speed + (max_speed - min_speed) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / current_speed)
        
            if h < total_hours:
                min_speed = current_speed + 1
                
            else:
                max_speed = current_speed
        
        return min_speed

# Given an array piles describing the sizes of piles of bananas to eat,
# and a time limit h in which one can eat bananas, return the minimum hourly
# eating speed (bananas/hr) with which one could consume all piles.
# If a given pile contains fewer bananas than the current eating speed K,
# eating K bananas from the pile will empty the pile and consume no additional
# bananas.
#
# NOTICE that the number of hours it takes to eat a pile is:
#
# [pile size] / [eating speed] rounded up
#
# NOTICE that, because a max of 1 pile can be finished per hour regardless of 
# the eating speed, the ORDER piles are eaten in does not matter, AND the
# maximum eating speed that makes a difference is the size of the largest
# pile.
#
# Now we have:
# - A sorted search space -- all possible eating speeds from 1-??
# - Bounds on the space -- 1,max(piles)
# - Criteria to find a value -- sum(ceil([pile size] / [eating speed])) <= h
#
# Run a binary search on the array of possible speeds from 1 to max. Search
# for the smallest speed where total hours == h
