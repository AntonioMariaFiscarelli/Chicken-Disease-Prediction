from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


#congif.yaml:
""" 
artifacts_root: artifacts


data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion    
"""