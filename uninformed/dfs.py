from source import COLOR_VISITING, COLOR_GOAL, COLOR_VISITED
from source import BaseSearchLogic

class DFSLogic(BaseSearchLogic):
    def dfs(self, start_node, goal_node=None):
        stack = [start_node]
        visited = set()
        parents = {start_node: None}

        while stack:
            current_node = stack.pop()

            if current_node not in visited:
                print(f"Visiting: {current_node}")
                self.update_node_color(current_node, COLOR_VISITING)

            if current_node == goal_node:
                # When the goal is reached, print the path
                path = self.reconstruct_path(parents, goal_node)
                print("Path found:", " -> ".join(path))
                
                print(f"Goal: {current_node}")
                self.update_node_color(current_node, COLOR_GOAL) 
                self.show_goal_message(goal_node) 
                return

            visited.add(current_node)  
            print(f"Visited: {current_node}")
            self.update_node_color(current_node, COLOR_VISITED) 

            for neighbor in reversed(self.get_neighbors(current_node)): 
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
                    parents[neighbor] = current_node
                    print(f"Visiting neighbor: {neighbor}")
                    self.update_node_color(neighbor, COLOR_VISITING) 

    def reconstruct_path(self, parents, goal_node):

        path = []
        current_node = goal_node

        while current_node is not None:
            path.append(current_node)
            current_node = parents[current_node]
        
        path.reverse()
        return path
