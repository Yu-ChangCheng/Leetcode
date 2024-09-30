class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [(p,s) for p,s in zip(position,speed)]
        s_pair = sorted(pair)[::-1] # nlogn + n

        pre_t = None
        count = 0

        for position, speed in s_pair:
            dist = target - position
            t = float(dist) / speed
            if not pre_t or t > pre_t:
                pre_t = t
                count += 1
        return count
