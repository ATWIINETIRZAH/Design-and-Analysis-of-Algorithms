



from collections import deque

class SocialNetwork:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()

    def add_connection(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def mutual_friends(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            return "Invalid users"

        queue = deque([(user1, [])])
        visited = set()

        while queue:
            current_user, path = queue.popleft()

            if current_user == user2:
                return path

            for friend in self.graph[current_user]:
                if friend not in visited:
                    queue.append((friend, path + [friend]))
                    visited.add(friend)

        return "No mutual friends"

# Example usage:
social_network = SocialNetwork()
social_network.add_connection("Tirzah", "Diana")
social_network.add_connection("Diana", "Munji")
social_network.add_connection("Tirzah", "Ian")
social_network.add_connection("Ian", "Nina")

user1 = "Tirzah"
user2 = "Nina"
result = social_network.mutual_friends(user1, user2)
print(f"Mutual friends between {user1} and {user2}: {result}")


# Conclusion on Space/Time Complexity:
# The time complexity of the BFS algorithm implemented here is O(V + E), where V is the number of vertices (users) and E is the number of edges (connections) in the graph. 
# The space complexity is also O(V), as the algorithm uses a queue and a set to keep track of visited users.

# In the context of finding mutual friends between two users, the BFS algorithm efficiently explores the network, 
# and its time complexity scales well with the size of the social network. 
# The space complexity is reasonable as it depends on the number of users in the network. Overall, the BFS algorithm is a practical approach for identifying mutual friends in a social network.