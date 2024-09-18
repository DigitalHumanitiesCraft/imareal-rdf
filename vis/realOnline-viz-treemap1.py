import json
import logging
from typing import Any, Dict, List, Optional

import pandas as pd
import plotly.express as px

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
DATA_FILE_PATH = 'C:/Users/Chrisi/Downloads/graph_stube_obj.json'  # Update this path as needed
COLOR_DISCRETE_SEQUENCE = px.colors.qualitative.Pastel  # Color palette for buildings

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

def prepare_treemap_data(data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Prepare data for treemap visualization.

    Parameters:
        data (List[Dict[str, Any]]): Parsed JSON data.

    Returns:
        pd.DataFrame: DataFrame structured for treemap visualization.
    """
    treemap_data = []

    for entry in data:
        # Extract room information
        room_name = entry['e']['properties'].get('name', ["Unnamed Room"])[0]
        building = entry['e']['properties'].get('gebaeude', ["Unknown Building"])[0]

        # If objects are present, extract object information
        if 'o' in entry:
            obj_name = entry['o']['properties'].get('bezeichnung', ["Unnamed Object"])[0]
            obj_quantity = entry['o']['properties'].get('anzahl', [1])[0]

            # Ensure quantity is numeric
            try:
                obj_quantity = int(obj_quantity)
            except (ValueError, TypeError):
                obj_quantity = 1

            treemap_data.append({
                'Building': building,
                'Room': room_name,
                'Object': obj_name,
                'Quantity': obj_quantity
            })

    # Create a DataFrame
    df = pd.DataFrame(treemap_data)

    # If Quantity is missing, set it to 1
    df['Quantity'] = df['Quantity'].fillna(1)

    logging.info("Treemap data prepared.")
    return df

def create_treemap(df: pd.DataFrame):
    """
    Create and display a treemap visualization with enhanced tooltips.

    Parameters:
        df (pd.DataFrame): DataFrame containing the treemap data.
    """
    # Calculate total quantity per room for sizing
    room_quantities = df.groupby('Room')['Quantity'].sum().reset_index()
    df = df.merge(room_quantities, on='Room', suffixes=('', '_RoomTotal'))

    # Calculate total quantity per building
    building_quantities = df.groupby('Building')['Quantity'].sum().reset_index()
    df = df.merge(building_quantities, on='Building', suffixes=('', '_BuildingTotal'))

    # Create treemap
    fig = px.treemap(
        df,
        path=['Building', 'Room', 'Object'],
        values='Quantity',
        color='Building',
        color_discrete_sequence=COLOR_DISCRETE_SEQUENCE,
        hover_data={
            'Building': True,
            'Room': True,
            'Object': True,
            'Quantity': True,
            'Quantity_RoomTotal': False,     # Exclude from automatic hover data
            'Quantity_BuildingTotal': False  # Exclude from automatic hover data
        },
        custom_data=['Quantity_RoomTotal', 'Quantity_BuildingTotal']
    )

    # Update hover template to include detailed information
    fig.update_traces(
        hovertemplate=(
            '<b>%{label}</b><br>'
            'Parent: %{parent}<br>'
            'Quantity: %{value}<br>'
            'Total in Room: %{customdata[0]}<br>'
            'Total in Building: %{customdata[1]}<br>'
            'Path: %{currentPath}'
        )
    )

    # Update layout
    fig.update_layout(
        title='Room-Object Treemap Visualization',
        margin=dict(t=50, l=25, r=25, b=25),
        uniformtext=dict(minsize=10, mode='hide'),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial")
    )

    logging.info("Treemap visualization created with enhanced tooltips.")
    fig.show()

def main():
    """Main function to execute the data loading, preparation, and visualization."""
    data = load_realonline_data(DATA_FILE_PATH)
    if data:
        df = prepare_treemap_data(data)
        if not df.empty:
            create_treemap(df)
        else:
            logging.error("DataFrame is empty. No data to display.")
    else:
        logging.error("Failed to load data.")

if __name__ == "__main__":
    main()
