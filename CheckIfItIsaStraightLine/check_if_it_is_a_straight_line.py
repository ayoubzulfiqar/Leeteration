class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        # Calculate the change in x and y for the first two points
        # This will be used as the reference slope (dy/dx)
        # We use cross-multiplication to avoid division and floating-point issues:
        # (y_i - y_0) / (x_i - x_0) == (y_1 - y_0) / (x_1 - x_0)
        # becomes:
        # (y_i - y_0) * (x_1 - x_0) == (y_1 - y_0) * (x_i - x_0)
        
        # Let dx_ref = x_1 - x_0
        # Let dy_ref = y_1 - y_0
        dx_ref = x1 - x0
        dy_ref = y1 - y0

        # Iterate through the remaining points starting from the third point
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]

            # Calculate the change in x and y relative to the first point
            dx_current = xi - x0
            dy_current = yi - y0

            # Check if the "slope" (dy/dx) is consistent using cross-multiplication
            # If dy_current * dx_ref != dy_ref * dx_current,
            # it means the current point does not lie on the same line
            if dy_current * dx_ref != dy_ref * dx_current:
                return False

        # If all points satisfy the condition, they form a straight line
        return True