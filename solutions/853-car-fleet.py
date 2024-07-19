class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            arrival_time = (target - pos) / spd
            stack.append(arrival_time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


# There are n cars travelling on a 1-lane road, towards a finish line at
# distance target.
#
# If one car catches up to another, they form a fleet and travel together, at
# the speed of the slower car.
#
# Given two arrays describing the positions of the cars on the road and their
# speeds, return the number of fleets that reach the target.
#
# NOTICE that if two cars form a fleet, they must occupy the same position
# at some time before reaching the target -- on the graph of car position
# against time, fleets are formed when lines intersect.
#
# NOTICE that this is the same as car x starting before car y, but having an
# earlier arrival time (imagining cars keep travelling and don't form fleets).
#
# So for any car, if an earlier car has a sooner arrival time, they will form
# a fleet.
#
# When a fleet is formed, it travels at the speed of the slower car. Other cars
# may join the fleet later.
#
# Track fleets with a stack. Sort the cars by position, in reverse. For each
# car, push its arrival time to the stack. If the last value on the stack is
# less than or equal to the second-last value, then an EARLIER car has a
# SOONER arrival time then a later one, so they form a fleet.
#
# If so, pop the stack, so the arrival time of the earlier car is removed,
# and the arrival time of the fleet (slower) is the new head of the stack.
#
# NOTICE this works because only adjacent cars can form a fleet--there is
# no scenario where cars are ordered x, y, z, and x + z form a fleet without
# y. So the head of the stack (fleet arriving latest) is the only fleet that
# the next car in the iteration can join.
