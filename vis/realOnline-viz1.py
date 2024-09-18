import json
import networkx as nx
import plotly.graph_objects as go
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Load JSON data
with open('C:/Users/Chrisi/Downloads/graph_stube_obj.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Initialize graph
G = nx.Graph()

# Parsing rooms and objects
for entry in data:
    room = entry['e']['properties']['name'][0]
    building = entry['e']['properties']['gebaeude'][0]
    room_type = entry['e']['properties'].get('raumtyp', ["Unknown Room Type"])[0]
    
    # Add room node with room type
    G.add_node(room, label='room', building=building, room_type=room_type)

    # Iterate over objects
    if 'o' in entry:
        obj_name = entry['o']['properties'].get('bezeichnung', ["Unnamed Object"])[0]
        obj_date = entry['o']['properties'].get('datierung_exakt', ["Unknown date"])[0]
        obj_quantity = entry['o']['properties'].get('anzahl', [1])[0]
        obj_type = entry['o']['properties'].get('objektgattung', ["Unknown Type"])[0]
        
        # Add object node with object type
        G.add_node(obj_name, label='object', date=obj_date, quantity=obj_quantity, obj_type=obj_type)
        
        # Create relationship (edge) between room and object
        G.add_edge(room, obj_name, relationship="hat Objekt")


def plot_graph(G):
    # Get positions for the nodes
    pos = nx.spring_layout(G)

    # Extract edge and node information for Plotly
    edge_x = []
    edge_y = []
    edge_text = []
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        edge_text.append(f"Relationship: {G.edges[edge]['relationship']}")

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='text',
        text=edge_text,
        mode='lines',
        visible=True)

    # Separate room and object nodes
    room_x, room_y, room_text, room_color, room_size = [], [], [], [], []
    object_x, object_y, object_text, object_color, object_size = [], [], [], [], []
    
    degrees = dict(G.degree())

    # Assign unique colors to buildings
    buildings = set([G.nodes[node]['building'] for node in G.nodes() if G.nodes[node]['label'] == 'room'])
    building_color_map = {building: cm.jet(i / len(buildings)) for i, building in enumerate(buildings)}

    for node in G.nodes():
        x, y = pos[node]
        if G.nodes[node]['label'] == 'room':
            room_x.append(x)
            room_y.append(y)
            room_text.append(f"Room: {node}<br>Building: {G.nodes[node]['building']}")
            room_color.append(mcolors.to_hex(building_color_map[G.nodes[node]['building']]))
            room_size.append(degrees[node] * 5)  # Scale node size based on degree
        else:
            object_x.append(x)
            object_y.append(y)
            object_text.append(f"Object: {node}<br>Date: {G.nodes[node]['date']}<br>Quantity: {G.nodes[node]['quantity']}")
            object_color.append('#FF6347')  # Use a consistent color for objects
            object_size.append(degrees[node] * 5)  # Scale node size based on degree

    # Create room trace
    room_trace = go.Scatter(
        x=room_x, y=room_y,
        mode='markers',
        hoverinfo='text',
        text=room_text,
        marker=dict(
            size=room_size,
            color=room_color,
            showscale=True,
            colorscale='YlGnBu',
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2),
        visible=True)

    # Create object trace
    object_trace = go.Scatter(
        x=object_x, y=object_y,
        mode='markers',
        hoverinfo='text',
        text=object_text,
        marker=dict(
            size=object_size,
            color=object_color,
            showscale=False,  # Objects have a consistent color
            line_width=2),
        visible=True)

    # Create Plotly figure with filters
    fig = go.Figure(data=[edge_trace, room_trace, object_trace],
                    layout=go.Layout(
                        title='<br>Interactive Room-Object Graph with Filters',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=50),
                        updatemenus=[{
                            'buttons': [
                                {'label': 'All', 'method': 'update', 'args': [{'visible': [True, True, True]}, {'title': 'All Nodes and Edges'}]},
                                {'label': 'Only Rooms', 'method': 'update', 'args': [{'visible': [True, True, False]}, {'title': 'Only Rooms Visible'}]},
                                {'label': 'Only Objects', 'method': 'update', 'args': [{'visible': [True, False, True]}, {'title': 'Only Objects Visible'}]},
                            ],
                            'direction': 'down',
                            'showactive': True,
                        }],
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


# Call the function to plot the graph
plot_graph(G)
