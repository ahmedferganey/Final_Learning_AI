# torch set seed
def set_seed(seed: int=42):
  """Sets random sets for torch operations.
  Args:
      seed (int, optional): Random seed to set. Defaults to 42.
  """  
  torch.manual_seed(seed)
  torch.cuda.manual_seed(seed)
#######################################################################
import os 
import zipfile
from pathlib import Path
import requests
def download_data(source: str,
                 destination: str,
                 remove_source: bool = True) -> Path:
  """Downloads a zipped dataset from source and unzips to destination.

  Args:
      source (str): A link to a zipped file containing data.
      destination (str): A target directory to unzip data to.
      remove_source (bool): Whether to remove the source after downloading and extracting.
  
  Returns:
      pathlib.Path to downloaded data.
    
  Example usage:
      download_data(source="https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip",
                    destination="pizza_steak_sushi")
  """   
  data_path = Path("data/")
  image_path = data_path / destination

    # If the image folder doesn't exist, download it and prepare it... 
  if image_path.is_dir():
    print(f"[INFO] {image_path} directory exists, skipping download")
  else:
    print(f"[INFO] Did not find {image_path} directory, creating one...")
    image_path.mkdir(parents=True, exist_ok=True)

    target_file = Path(source).name
    with open(data_path / target_file, "wb") as f:
      request = requests.get(source)
      print(f"[INFO] Downloading {target_file} from {source}...")
      f.write(request.content)
    
    with zipfile.ZipFile(data_path / target_file, "r") as zip_ref:
      print(f"[INFO] Unzipping {target_file} data...") 
      zip_ref.extractall(image_path)      
    if remove_source:
      os.remove(data_path / target_file)
  return image_path
#######################################################################
%%time
from going_modular.going_modular.utils import save_model

# 1. Set the random seeds
set_seeds(seed=42)

# 2. Keep track of experiment numbers
experiment_number = 0

# 3. Loop through each DataLoader
for dataloader_name, train_dataloader in train_dataloaders.items():

    # 4. Loop through each number of epochs
    for epochs in num_epochs: 

        # 5. Loop through each model name and create a new model based on the name
        for model_name in models:

            # 6. Create information print outs
            experiment_number += 1
            print(f"[INFO] Experiment number: {experiment_number}")
            print(f"[INFO] Model: {model_name}")
            print(f"[INFO] DataLoader: {dataloader_name}")
            print(f"[INFO] Number of epochs: {epochs}")  

            # 7. Select the model
            if model_name == "effnetb0":
                model = create_effnetb0() # creates a new model each time (important because we want each experiment to start from scratch)
            else:
                model = create_effnetb2() # creates a new model each time (important because we want each experiment to start from scratch)
            
            # 8. Create a new loss and optimizer for every model
            loss_fn = nn.CrossEntropyLoss()
            optimizer = torch.optim.Adam(params=model.parameters(), lr=0.001)

            # 9. Train target model with target dataloaders and track experiments
            train(model=model,
                  train_dataloader=train_dataloader,
                  test_dataloader=test_dataloader, 
                  optimizer=optimizer,
                  loss_fn=loss_fn,
                  epochs=epochs,
                  device=device,
                  writer=create_writer(experiment_name=dataloader_name,
                                       model_name=model_name,
                                       extra=f"{epochs}_epochs"))
            
            # 10. Save the model to file so we can get back the best model
            save_filepath = f"07_{model_name}_{dataloader_name}_{epochs}_epochs.pth"
            save_model(model=model,
                       target_dir="models",
                       model_name=save_filepath)
            print("-"*50 + "\n")
#######################################################################
# s            

