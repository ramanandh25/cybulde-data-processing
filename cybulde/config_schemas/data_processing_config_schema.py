from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from cybulde.config_schemas.infrastructure import gcp_schema
from omegaconf import MISSING
from cybulde.config_schemas.data_processing import dataset_readers_schema, dataset_cleaners_schema


@dataclass
class DataProcessingConfig:
    version: str = MISSING
    data_local_save_dir: str = "./data/raw"
    dvc_remote_repo: str = "https://github.com/ramanandh25/cybulde-data.git"
    dvc_data_folder: str = "data/raw"
    github_user_name: str = "ramanandh25"
    github_access_token_secret_id: str = "dvc_github_access_token"
    infrastructure: gcp_schema.GCPConfig = gcp_schema.GCPConfig()
    dataset_reader_manager: dataset_readers_schema.DatasetReaderManagerConfig = MISSING
    dataset_cleaner_manager: dataset_cleaners_schema.DatasetCleanerManagerConfig = MISSING


def setup_config() -> None:
    gcp_schema.setup_config()
    dataset_readers_schema.setup_config()
    dataset_cleaners_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
