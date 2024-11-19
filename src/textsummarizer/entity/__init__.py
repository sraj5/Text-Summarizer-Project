from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    #Defining the return type of variables in config.yaml updated earlier
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path