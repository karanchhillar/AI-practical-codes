class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, parents=None, probabilities=None):
        if parents is None:
            parents = []
        if probabilities is None:
            probabilities = []

        self.nodes[name] = {
            'parents': parents,
            'probabilities': probabilities
        }

    def get_probability(self, node, evidence):
        if not self.nodes[node]['parents']:
            return self.nodes[node]['probabilities'][0]

        parent_values = [evidence[parent] for parent in self.nodes[node]['parents']]
        index = sum([val * 2 ** i for i, val in enumerate(parent_values)])
        return self.nodes[node]['probabilities'][index]

    def query(self, target, evidence):
        probability_true = self.get_probability(target, evidence)
        evidence_false = evidence.copy()
        evidence_false[target] = 0
        probability_false = self.get_probability(target, evidence_false)

        normalization = probability_true + probability_false
        return probability_true / normalization

# Example usage with a more complex Bayesian network
bn = BayesianNetwork()

# Weather node with no parents
bn.add_node('Weather', probabilities=[0.3, 0.7])

# Traffic node influenced by Weather
bn.add_node('Traffic', parents=['Weather'], probabilities=[0.2, 0.8, 0.7, 0.3])

# Late node influenced by both Weather and Traffic
bn.add_node('Late', parents=['Weather', 'Traffic'], probabilities=[0.1, 0.9, 0.3, 0.7, 0.8, 0.2, 0.5, 0.5])

# Example query: P(Late | Weather=1, Traffic=0)
query_result = bn.query('Late', {'Weather': 1, 'Traffic': 0})
print(f"P(Late | Weather=1, Traffic=0) = {query_result}")
