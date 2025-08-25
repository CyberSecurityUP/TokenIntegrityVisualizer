import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relation(self, process, privilege, status="Enabled"):
        """
        Adiciona uma relação processo → privilégio
        Apenas privilégios Enabled são adicionados (para reduzir poluição visual)
        """
        if status == "Enabled":
            self.graph.add_edge(process, privilege, label=status)

    def export_png(self, filename="graph.png"):
        """
        Exporta o grafo em formato PNG (para exibição no GUI)
        """
        if len(self.graph.nodes) == 0:
            return

        plt.figure(figsize=(20, 14))  # Aumenta o tamanho do gráfico
        pos = nx.spring_layout(self.graph, k=0.6, iterations=60)

        # Separar nós por categoria
        process_nodes = [n for n in self.graph.nodes if ".exe" in n]
        priv_nodes = [n for n in self.graph.nodes if n.startswith("Se")]

        # Desenhar nós
        nx.draw_networkx_nodes(self.graph, pos, nodelist=process_nodes,
                               node_color="lightgreen", node_size=2000, alpha=0.9)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=priv_nodes,
                               node_color="lightblue", node_size=1500, alpha=0.9)

        # Desenhar arestas
        nx.draw_networkx_edges(self.graph, pos, arrows=True, alpha=0.5)

        # Rótulos
        nx.draw_networkx_labels(self.graph, pos, font_size=8, font_family="monospace")

        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=7)

        plt.axis("off")
        plt.tight_layout()
        plt.savefig(filename, dpi=200)
        plt.close()

    def export_html(self, filename="graph.html"):
        if len(self.graph.nodes) == 0:
            return

        net = Network(height="800px", width="100%", directed=True, notebook=False)
        net.toggle_physics(True)  # ativa movimento e forças físicas

        for node in self.graph.nodes:
            color = "lightgreen" if ".exe" in node else "lightblue"
            net.add_node(node, label=node, color=color)

        for u, v, d in self.graph.edges(data=True):
            net.add_edge(u, v, label=d.get("label", ""))

        net.show(filename)

