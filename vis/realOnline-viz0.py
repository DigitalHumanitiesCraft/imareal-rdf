import json
import networkx as nx

def load_realonline_data(file_path='C:/Users/Chrisi/Downloads/graph_stube_obj.json'):
    """
    Load and parse JSON data from the REALonline graph_stube_obj file.

    Parameters:
    file_path (str): Path to the JSON file. Defaults to 'graph_stube_obj.json'.

    Returns:
    list: Parsed JSON data as a Python list of dictionaries.

    Raises:
    FileNotFoundError: If the specified file is not found.
    json.JSONDecodeError: If there's an error decoding the JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def process_realonline_data(data):
    """
    Process REALonline data and create a NetworkX graph.

    Parameters:
    data (list): Parsed JSON data from load_realonline_data()

    Returns:
    nx.Graph: A NetworkX graph representing the room-object relationships
    """
    G = nx.Graph()

    for entry in data:
        # Process room (entity) data
        room = entry['e']['properties'].get('name', ["Unnamed Room"])[0]
        building = entry['e']['properties'].get('gebaeude', ["Unknown Building"])[0]
        room_type = entry['e']['properties'].get('raumtyp', ["Unknown Type"])[0]
        inventory_name = entry['e']['properties'].get('inventarname', "Unknown Inventory")
        room_id = entry['e']['properties'].get('id', "Unknown ID")

        G.add_node(room_id, label='room', name=room, building=building, 
                   room_type=room_type, inventory_name=inventory_name)

        # Process object data if present
        if 'o' in entry:
            obj_name = entry['o']['properties'].get('name', ["Unnamed Object"])[0]
            obj_label = entry['o']['properties'].get('bezeichnung', ["Unlabeled Object"])[0]
            obj_quantity = entry['o']['properties'].get('anzahl', [1])[0]
            obj_date = entry['o']['properties'].get('datierung_exakt', ["Unknown date"])[0]
            obj_category = entry['o']['properties'].get('objektgattung', ["Unknown category"])[0]
            obj_id = entry['o']['properties'].get('id', "Unknown ID")

            G.add_node(obj_id, label='object', name=obj_name, obj_label=obj_label,
                       quantity=obj_quantity, date=obj_date, category=obj_category)

            # Add edge representing the relationship
            relation = entry['eo']['properties'].get('RelationLabel', "Unknown Relation")
            G.add_edge(room_id, obj_id, relationship=relation)

        # Process thesaurus information
        if 'et' in entry and 't' in entry:
            thesaurus_name = entry['t']['properties'].get('ThesaurusName', "Unknown Thesaurus")
            thesaurus_short_name = entry['t']['properties'].get('ShortName', "Unknown Short Name")
            G.nodes[room_id][thesaurus_name] = thesaurus_short_name

    return G

def main():
    # Load the data
    file_path = 'C:/Users/Chrisi/Downloads/graph_stube_obj.json'  # Replace with your actual file path
    data = load_realonline_data(file_path)

    if data:
        # Process the data
        graph = process_realonline_data(data)
        print(f"Graph created with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # Example of accessing node information
        for node in graph.nodes(data=True):
            if node[1]['label'] == 'room':
                print(f"Room: {node[1]['name']}, Building: {node[1]['building']}")
            elif node[1]['label'] == 'object':
                print(f"Object: {node[1]['name']}, Category: {node[1]['category']}")
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
