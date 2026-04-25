class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair positions and speeds
        pairs = [(p, s) for p, s in zip(position, speed)]
        
        stack = []
        
        # 2. Sort the pairs in descending order (closest to target first)
        for p, s in sorted(pairs, reverse=True):
            # Calculate time to reach the target
            time = (target - p) / s
            
            # Add the current car's time to the stack
            stack.append(time)
            
            # 3. Check for a fleet
            # If there are at least 2 cars, and the car behind (top of stack) 
            # reaches the target faster than or at the same time as the car ahead,
            # they merge into a fleet. 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # The faster car is bottlenecked, so we discard its faster time
                
        return len(stack)
            
