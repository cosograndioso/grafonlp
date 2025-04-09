import networkx as nx
import matplotlib.pyplot as plt
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

class KeywordGraph:
    def __init__(self, keywords):
        """
        Initialize the graph with a set of keywords.
        Each keyword can become a node in the graph.
        """
        self.keywords = set(keywords)
        self.graph = nx.Graph()

    def build(self, results):
        """
        Build the graph based on keyword co-occurrences within context windows.
        If two keywords appear in the same context, they are connected by an edge.
        """
        logger.info("Building keyword graph...")
        try:
            for word, context in results:
                # Ensure the keyword is added as a node
                self.graph.add_node(word)
                # Check for co-occurrence with other keywords in the context
                for other in self.keywords:
                    if other != word and other in context.lower():
                        self.graph.add_edge(word, other)

            logger.info(f"Graph built with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges.")
        except Exception as e:
            logger.error(f"Error building the keyword graph: {e}")
            raise e

    def show(self):
        """
        Display the graph using matplotlib if it contains edges.
        """
        try:
            if self.graph.number_of_edges() > 0:
                plt.figure(figsize=(10, 8))
                nx.draw(
                    self.graph,
                    with_labels=True,
                    node_color='blue',
                    node_size=2000,
                    font_size=12
                )
                plt.title("Keyword Graph – Environment")
                plt.tight_layout()
                plt.show()
            else:
                logger.warning("No connections found between keywords.")
        except Exception as e:
            logger.error(f"Error displaying the graph: {e}")
            raise e
