


def conversion():
  import os
  import yaml
  import pandas as pd

  
  os_make_dir="stocks"
  os.makedirs(os_make_dir, exist_ok=True)
  dir_path ="C:\\Users\\Rama Kumar\\Downloads\\data"         
 
  data = [] # Initialize an empty list to store data
    
  for folder_name in os.listdir(dir_path):

    folder_path = os.path.join(dir_path, folder_name)
    for filename in os.listdir(folder_path):
   
     if filename.endswith('.yaml') or filename.endswith('.yml'):  # Filter YAML files
        
        #Join the file name along with the folder path to get the path of each yaml file
       
        final_path = os.path.join(folder_path, filename)
        
        # Open and read each YAML file 
 
        with open(final_path, 'r') as file:
            try:
              yaml_data = yaml.safe_load(file) 
              if yaml_data is None :
                 print("There is no data in the yanl file:",final_path)
                 continue
            except Exception as e:
                 print(f"There is an error in loading the yaml file{final_path}:error code is {e}")
                 continue
             # Parse YAML content
            
            # Ensure it's in a compatible format (e.g., list of dictionaries)
            if isinstance(yaml_data, list):  # If the YAML file contains a list of records
                
                data.extend(yaml_data)  # Append each record to the main list
            elif isinstance(yaml_data, dict):  # If it's a single dictionary
                
                data.append(yaml_data)  # Treat it as one record

# Convert the combined data into a DataFrame
  df = pd.DataFrame(data,index=None)

# Display the DataFrame
  print(df)
  print("conversion program ends here")
  return df,os_make_dir

   
