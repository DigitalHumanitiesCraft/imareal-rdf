import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import networkx as nx
import plotly.graph_objects as go

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
DATA_FILE_PATH = 'C:/Users/Chrisi/Downloads/graph_stube_obj.json'
ROOM_COLOR = 'skyblue'
OBJECT_COLOR = 'lightcoral'
ROOM_SYMBOL = 'square'
OBJECT_SYMBOL = 'circle'
EDGE_COLOR = 'gray'
EDGE_OPACITY = 0.3
LABEL_FREQUENCY = 5  # Show label for every nth node


@dataclass
class NodeProperties:
    """Data class for storing node properties."""
    label: str
    color: str
    symbol: str
    size: int
    tooltip_text: str


def load_realonline_data(file_path: str) -> Optional[List[Dict[str, Any]]]:
    """
    Load and parse JSON data from the REALonline graph_stube_obj file.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        Optional[List[Dict[str, Any]]]: Parsed JSON data or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            logging.info(f"Data loaded successfully from {file_path}.")
            return data
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return None


def process_realonline_data(data: List[Dict[str, Any]]) -> nx.Graph:
    """
    Process REALonline data and create a NetworkX graph.

    Parameters:
        data (List[Dict[str, Any]]): Parsed JSON data from load_realonline_data().

    Returns:
        nx.Graph: A NetworkX graph representing the room-object relationships.
    """
    G = nx.Graph()

    for entry in data:
        # Process room data
        room_name = entry['e']['properties'].get('name', ["Unnamed Room"])[0]
        building = entry['e']['properties'].get('gebaeude', ["Unknown Building"])[0]

        # Add room node
        G.add_node(room_name, label='room', building=building)

        # Process object data if present
        if 'o' in entry:
            obj_name = entry['o']['properties'].get('bezeichnung', ["Unnamed Object"])[0]
            obj_date = entry['o']['properties'].get('datierung_exakt', ["Unknown date"])[0]
            obj_quantity = entry['o']['properties'].get('anzahl', [1])[0]

            # Add object node
            G.add_node(obj_name, label='object', date=obj_date, quantity=obj_quantity)

            # Create relationship (edge) between room and object
            G.add_edge(room_name, obj_name, relationship="hat Objekt")

    logging.info("Graph processing complete.")
    return G


def assign_node_positions(G: nx.Graph) -> Dict[Any, Tuple[float, float]]:
    """
    Assign positions to nodes for visualization.

    Parameters:
        G (nx.Graph): The graph containing nodes and edges.

    Returns:
        Dict[Any, Tuple[float, float]]: A dictionary mapping nodes to positions.
    """
    # Separate nodes by type
    rooms = [node for node in G.nodes() if G.nodes[node]['label'] == 'room']
    objects = [node for node in G.nodes() if G.nodes[node]['label'] == 'object']

    # Use spring layout for initial positions
    pos_spring = nx.spring_layout(G, k=0.15, iterations=50, seed=42)

    # Normalize x positions
    x_positions = [pos_spring[node][0] for node in G.nodes()]
    x_min = min(x_positions)
    x_max = max(x_positions)

    # Assign positions with rooms on top and objects on bottom
    positions = {}
    for node in G.nodes():
        x = pos_spring[node][0]
        x_norm = (x - x_min) / (x_max - x_min) * 2 - 1  # Normalize x to [-1,1]
        node_type = G.nodes[node]['label']
        y = 1 if node_type == 'room' else -1
        positions[node] = (x_norm, y)

    logging.info("Node positions assigned.")
    return positions


def create_node_traces(
    G: nx.Graph,
    pos: Dict[Any, Tuple[float, float]],
    label_frequency: int = LABEL_FREQUENCY
) -> go.Scatter:
    """
    Create node traces for Plotly visualization.

    Parameters:
        G (nx.Graph): The graph containing nodes and edges.
        pos (Dict[Any, Tuple[float, float]]): Positions of nodes.
        label_frequency (int): Frequency of labels to display.

    Returns:
        go.Scatter: A Plotly Scatter trace for nodes.
    """
    node_x = []
    node_y = []
    node_text = []
    hover_texts = []
    node_colors = []
    node_symbols = []
    node_sizes = []
    labels = []

    for i, node in enumerate(G.nodes()):
        x, y = pos[node]
        node_data = G.nodes[node]
        node_type = node_data['label']

        # Append positions
        node_x.append(x)
        node_y.append(y)

        # Determine node properties
        if node_type == 'room':
            color = ROOM_COLOR
            symbol = ROOM_SYMBOL
            size = 15
            tooltip_text = f"Room: {node}<br>Building: {node_data['building']}"
        else:
            color = OBJECT_COLOR
            symbol = OBJECT_SYMBOL
            try:
                size = 10 + int(node_data['quantity']) * 2
            except (ValueError, TypeError):
                size = 10  # Default size
            tooltip_text = (
                f"Object: {node}<br>Date: {node_data.get('date', 'Unknown date')}<br>"
                f"Quantity: {node_data.get('quantity', 'Unknown')}"
            )

        # Append properties
        node_colors.append(color)
        node_symbols.append(symbol)
        node_sizes.append(size)
        hover_texts.append(tooltip_text)

        # Append labels selectively to reduce clutter
        if i % label_frequency == 0:
            labels.append(node)
        else:
            labels.append('')

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=labels,
        textposition='top center',
        hoverinfo='text',
        hovertext=hover_texts,
        marker=dict(
            size=node_sizes,
            color=node_colors,
            symbol=node_symbols,
            line=dict(width=1, color='DarkSlateGrey')
        ),
        showlegend=False
    )

    logging.info("Node traces created.")
    return node_trace


def create_edge_traces(G: nx.Graph, pos: Dict[Any, Tuple[float, float]]) -> go.Scatter:
    """
    Create edge traces for Plotly visualization.

    Parameters:
        G (nx.Graph): The graph containing nodes and edges.
        pos (Dict[Any, Tuple[float, float]]): Positions of nodes.

    Returns:
        go.Scatter: A Plotly Scatter trace for edges.
    """
    edge_x = []
    edge_y = []
    edge_texts = []

    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_texts.append(f"{edge[0]} - {edge[2]['relationship']} - {edge[1]}")

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.0, color=EDGE_COLOR),
        opacity=EDGE_OPACITY,
        hoverinfo='text',
        text=edge_texts,
        mode='lines'
    )

    logging.info("Edge traces created.")
    return edge_trace


def create_legend_traces() -> List[go.Scatter]:
    """
    Create legend traces for rooms and objects.

    Returns:
        List[go.Scatter]: A list containing legend traces.
    """
    legend_traces = []

    legend_traces.append(
        go.Scatter(
            x=[None],
            y=[None],
            mode='markers',
            marker=dict(
                size=15,
                color=ROOM_COLOR,
                symbol=ROOM_SYMBOL,
                line=dict(width=1, color='DarkSlateGrey')
            ),
            legendgroup='Rooms',
            showlegend=True,
            name='Rooms'
        )
    )

    legend_traces.append(
        go.Scatter(
            x=[None],
            y=[None],
            mode='markers',
            marker=dict(
                size=15,
                color=OBJECT_COLOR,
                symbol=OBJECT_SYMBOL,
                line=dict(width=1, color='DarkSlateGrey')
            ),
            legendgroup='Objects',
            showlegend=True,
            name='Objects'
        )
    )

    logging.info("Legend traces created.")
    return legend_traces


def plot_graph(G: nx.Graph):
    """
    Plot the graph using Plotly.

    Parameters:
        G (nx.Graph): The graph containing nodes and edges.
    """
    # Assign positions
    pos = assign_node_positions(G)

    # Create traces
    node_trace = create_node_traces(G, pos)
    edge_trace = create_edge_traces(G, pos)
    legend_traces = create_legend_traces()

    # Create figure
    fig = go.Figure(
        data=[edge_trace, node_trace] + legend_traces,
        layout=go.Layout(
            title='Interactive Room-Object Graph',
            titlefont_size=16,
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=20, r=20, t=50),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )

    logging.info("Plotting graph.")
    fig.show()


def main():
    """Main function to execute the data loading, processing, and plotting."""
    data = load_realonline_data(DATA_FILE_PATH)
    if data:
        graph = process_realonline_data(data)
        logging.info(
            f"Graph created with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges."
        )
        plot_graph(graph)
    else:
        logging.error("Failed to load data.")


if __name__ == "__main__":
    main()
