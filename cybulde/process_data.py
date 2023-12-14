from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.gcp_utils import access_secret_version


@get_config(config_path="../configs", config_name="config")
def process_data(config: Config) -> None:
    print(config)
    github_access_token = access_secret_version(project_id="applied-craft-406304",
                                                secret_id="dvc_github_access_token")
    print(github_access_token)

    
if __name__ == "__main__":
    process_data()  # type: ignore
