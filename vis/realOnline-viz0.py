import json
import networkx as nx
import plotly.graph_objects as go

# Load JSON data
with open('C:/Users/Chrisi/Downloads/graph_stube_obj.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Initialize graph
G = nx.Graph()

# Parsing rooms and objects
for entry in data:
    room = entry['e']['properties']['name'][0]
    building = entry['e']['properties']['gebaeude'][0]
    
    # Add room node
    G.add_node(room, label='room', building=building)

    # Iterate over objects
    if 'o' in entry:
        # Check for 'bezeichnung' key and set a default value if not found
        obj_name = entry['o']['properties'].get('bezeichnung', ["Unnamed Object"])[0]
        
        # Check for 'datierung_exakt' key and set a default value if not found
        obj_date = entry['o']['properties'].get('datierung_exakt', ["Unknown date"])[0]
        
        # Check for 'anzahl' key and set a default value if not found
        obj_quantity = entry['o']['properties'].get('anzahl', [1])[0]
        
        # Add object node
        G.add_node(obj_name, label='object', date=obj_date, quantity=obj_quantity)
        
        # Create relationship (edge) between room and object
        G.add_edge(room, obj_name, relationship="hat Objekt")


def plot_graph(G):
    # Get positions for the nodes
    pos = nx.spring_layout(G)

    # Extract edge and node information for Plotly
    edge_x = []
    edge_y = []
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        node_data = G.nodes[node]
        node_type = node_data['label']
        
        # Build tooltip text
        if node_type == 'room':
            node_text.append(f"Room: {node}<br>Building: {node_data['building']}")
        else:
            node_text.append(f"Object: {node}<br>Date: {node_data['date']}<br>Quantity: {node_data['quantity']}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        text=node_text,
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    # Create Plotly figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Interactive Room-Object Graph',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=50),
                        annotations=[dict(
                            text="Visualization of room-to-object relationships",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002
                        )],
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False))
                    )
    fig.show()

# Plot the graph
plot_graph(G)
