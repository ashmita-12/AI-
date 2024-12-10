class UtilityBasedAgent:
    def __init__(self, size):
        self.size = size
        self.agent_location = (0, 0)
        self.agent_orientation = 'right'

    def sense(self, perceptions):
        # Get the perception for the current location
        x, y = self.agent_location
        perception = perceptions.get((x, y), {})

        return perception

    def calculate_utility(self, action, perception):
        # Calculate the utility of the action based on the perception
        # For simplicity, we'll use a simple heuristic here
        utility = 0

        if action == 'move forward':
            # Higher utility if no breeze or stench
            if not perception.get('breeze', False) and not perception.get('stench', False):
                utility += 1
            # Lower utility if there's a breeze or stench
            else:
                utility -= 1
        elif action == 'turn left' or action == 'turn right':
            # Higher utility for turning (no cost)
            utility += 0.5
        elif action == 'grab':
            # Higher utility if glitter is present
            if perception.get('glitter', False):
                utility += 2
        elif action == 'shoot':
            # Higher utility if there's a stench (assuming it's the Wumpus)
            if perception.get('stench', False):
                utility += 2

        return utility

    def decide_action(self, perceptions):
        max_utility = float('-inf')
        best_action = None

        for action in ['move forward', 'turn left', 'turn right', 'grab', 'shoot']:
            perception = self.sense(perceptions)
            utility = self.calculate_utility(action, perception)

            if utility > max_utility:
                max_utility = utility
                best_action = action

        return best_action

    def update_location(self, action):
        # Update agent's location based on the action
        x, y = self.agent_location

        if action == 'move forward':
            if self.agent_orientation == 'right' and y < self.size - 1:
                self.agent_location = (x, y + 1)
            elif self.agent_orientation == 'left' and y > 0:
                self.agent_location = (x, y - 1)
            elif self.agent_orientation == 'up' and x > 0:
                self.agent_location = (x - 1, y)
            elif self.agent_orientation == 'down' and x < self.size - 1:
                self.agent_location = (x + 1, y)
        elif action == 'turn left':
            if self.agent_orientation == 'right':
                self.agent_orientation = 'up'
            elif self.agent_orientation == 'up':
                self.agent_orientation = 'left'
            elif self.agent_orientation == 'left':
                self.agent_orientation = 'down'
            elif self.agent_orientation == 'down':
                self.agent_orientation = 'right'
        elif action == 'turn right':
            if self.agent_orientation == 'right':
                self.agent_orientation = 'down'
            elif self.agent_orientation == 'down':
                self.agent_orientation = 'left'
            elif self.agent_orientation == 'left':
                self.agent_orientation = 'up'
            elif self.agent_orientation == 'up':
                self.agent_orientation = 'right'

    def act(self, perceptions):
        action = self.decide_action(perceptions)
        self.update_location(action)
        print(f"Action: {action}")

# Example usage
agent = UtilityBasedAgent(size=4)

# Example perceptions for each location
perceptions = {
    (0, 0): {'glitter': True},
    (1, 0): {'breeze': True},
    (2, 1): {'stench': True},
    # Other locations have no perceptions
}

agent.act(perceptions)
