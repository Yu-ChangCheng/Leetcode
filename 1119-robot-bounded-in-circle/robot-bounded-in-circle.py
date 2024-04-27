class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # Initial direction is up (0, 1), right is (1, 0), down is (0, -1), left is (-1, 0)
        direction = (0, 1)
        position = (0, 0)

        # Define a rotation matrix for left and right turns
        left_rotation = { (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1) }
        right_rotation = { (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1) }
        
        for c in instructions:
            # Execute the command string
            if c == 'G':
                position = (position[0] + direction[0], position[1] + direction[1])
            elif c == 'L':
                direction = left_rotation[direction]
            elif c == 'R':
                direction = right_rotation[direction]

        # If the final position is the starting position, or if not facing the original direction, it's circular
        if position == (0, 0) or direction != (0, 1):
            return True
        else:
            return False

