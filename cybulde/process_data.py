from cybulde.config_schemas.data_processing_config_schema import DataProcessingConfig
from cybulde.utils.config_utils import get_config
from cybulde.utils.gcp_utils import access_secret_version
from cybulde.utils.data_utils import get_raw_data_with_version
from omegaconf import OmegaConf
from hydra.utils import instantiate

@get_config(config_path="../configs", config_name="data_processing_config")
def process_data(config: DataProcessingConfig) -> None:
    print(OmegaConf.to_yaml(config))
    return
    github_access_token = access_secret_version(project_id=config.infrastructure.project_id,
                                                secret_id=config.github_access_token_secret_id)

    get_raw_data_with_version(version=config.version,
                              data_local_save_dir=config.data_local_save_dir,
                              github_user_name=config.github_user_name,
                              dvc_data_folder=config.dvc_data_folder,
                              dvc_remote_repo=config.dvc_remote_repo,
                              github_access_token=github_access_token)
    
    dataset_reader_manager = instantiate(config.dataset_reader_manager)
    df = dataset_reader_manager.read_data()
    print(df.head())


if __name__ == "__main__":
    process_data()  # type: ignore
