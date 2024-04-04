class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [(p,s) for p,s in zip(position, speed)]
        s_pairs = sorted(pairs)[::-1]

        prev_t = None
        count = 0

        for position, speed in s_pairs:
            dist = target - position
            t = dist/float(speed)
            if not prev_t or t > prev_t:
                prev_t = t
                count += 1
        return count
