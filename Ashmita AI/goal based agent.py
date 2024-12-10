class GoalBasedAgent:
    def __init__(self, size):
        self.size = size
        self.world = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_location = (0, 0)
        self.agent_orientation = 'right'
        self.has_gold = False
        self.arrows = 1
        self.wumpus_alive = True

    def sense(self):
        perceptions = {}
        x, y = self.agent_location

        # Check for stench
        if (x > 0 and self.world[x-1][y] == 'W') or \
           (x < self.size-1 and self.world[x+1][y] == 'W') or \
           (y > 0 and self.world[x][y-1] == 'W') or \
           (y < self.size-1 and self.world[x][y+1] == 'W'):
            perceptions['stench'] = True
        else:
            perceptions['stench'] = False

        # Check for breeze
        if (x > 0 and self.world[x-1][y] == 'P') or \
           (x < self.size-1 and self.world[x+1][y] == 'P') or \
           (y > 0 and self.world[x][y-1] == 'P') or \
           (y < self.size-1 and self.world[x][y+1] == 'P'):
            perceptions['breeze'] = True
        else:
            perceptions['breeze'] = False

        # Check for glitter
        if self.world[x][y] == 'G':
            perceptions['glitter'] = True
        else:
            perceptions['glitter'] = False

        # Check for bump
        if (self.agent_orientation == 'right' and y == self.size - 1) or \
           (self.agent_orientation == 'left' and y == 0) or \
           (self.agent_orientation == 'up' and x == 0) or \
           (self.agent_orientation == 'down' and x == self.size - 1):
            perceptions['bump'] = True
        else:
            perceptions['bump'] = False

        # No screaming in this implementation
        perceptions['scream'] = False
        return perceptions

    def update_perceptions(self, perceptions):
        x, y = self.agent_location

        # Update perceptions based on agent's location
        for key, value in perceptions.items():
            if value:
                if key == 'stench':
                    self.world[x][y] = 'S'
                elif key == 'breeze':
                    self.world[x][y] = 'B'
                elif key == 'glitter':
                    self.world[x][y] = 'G'

    def plan(self, goals):
        # For simplicity, return the first goal that the agent can achieve
        for goal in goals:
            if goal in self.sense():
                return goal
        return None

    def act(self, goals):
        goal = self.plan(goals)
        if goal:
            print(f"Achieving goal: {goal}")
        else:
            print("No applicable goal")

# Example usage
agent = GoalBasedAgent(size=4)
agent.world[1][0] = 'P'  # Pit at (1, 0)
agent.world[2][1] = 'W'  # Wumpus at (2, 1)
agent.world[0][3] = 'G'  # Gold at (0, 3)
agent.act(goals=['glitter', 'stench'])  # Example goals
