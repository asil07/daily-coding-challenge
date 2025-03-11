import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter customers whose referee_id is either NULL (NaN in pandas) or not equal to 2
    result = customer[(customer['referee_id'].isna()) | (customer['referee_id'] != 2)]
    
    # Select only the 'name' column
    return result[['name']]
