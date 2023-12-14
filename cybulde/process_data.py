from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.gcp_utils import access_secret_version
from cybulde.utils.data_utils import get_raw_data_with_version


@get_config(config_path="../configs", config_name="config")
def process_data(config: Config) -> None:
    print(config)
    github_access_token = access_secret_version(project_id="applied-craft-406304",
                                                secret_id="dvc_github_access_token")
    github_user_name = "ramanandh25"
    version = "v9"
    dvc_remote_repo = "https://github.com/ramanandh25/cybulde-data.git"
    dvc_data_folder = "data/raw"
    data_local_save_dir = "./data/raw"

    get_raw_data_with_version(version=version,
                              data_local_save_dir=data_local_save_dir,
                              github_user_name=github_user_name,
                              dvc_data_folder=dvc_data_folder,
                              dvc_remote_repo=dvc_remote_repo,
                              github_access_token=github_access_token)
    

if __name__ == "__main__":
    process_data()  # type: ignore
