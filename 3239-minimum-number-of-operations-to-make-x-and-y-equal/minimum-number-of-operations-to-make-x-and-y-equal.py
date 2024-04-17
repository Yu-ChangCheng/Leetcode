class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        queue = deque([(x, 0)]) # Queue to store (current value, steps taken)
        visited = set()
        visited.add(x)

        while queue:
            curr, step = queue.popleft()

            if curr == y:
                return step
            
            next_states = []
            if curr % 11 == 0:
                next_states.append(curr // 11)
            if curr % 5 == 0:
                next_states.append(curr // 5)
            next_states.append(curr - 1)
            next_states.append(curr + 1)

            for next_state in next_states:
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, step + 1))

        return -1