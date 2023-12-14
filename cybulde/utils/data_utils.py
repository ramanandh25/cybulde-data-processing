from shutil import rmtree
from cybulde.utils.utils import run_shell_command


def get_cmd_to_get_raw_data(
        version: str,
        data_local_save_dir: str,
        dvc_remote_repo: str,
        dvc_data_folder: str,
        github_user_name: str,
        github_access_token: str,
) -> str:
    """
    get shell command to download the rawdata from dvc store
    :param version: data version
    :param data_local_save_dir: where to save the downloaded data locally
    :param dvc_remote_repo: dvc remote repository that holds the info about data
    :param dvc_data_folder:location where the remote data is stored
    :param github_user_name: GitHub useer name
    :param github_access_token: GitHub access token
    :return:shell command to download raw data
    """
    # dvc_remote_repo = https://github.com/ramanandh25/cybulde-data.git
    # modified dvc repo required = https://<username>:<access-token>@github.com/ramanandh25/cybulde-data.git
    without_https = dvc_remote_repo.replace("https://", "")
    dvc_remote_repo = f"https://{github_user_name}:{github_access_token}@{without_https}"
    command = f"dvc get {dvc_remote_repo} {dvc_data_folder} --rev {version} -o {data_local_save_dir}"
    return command


def get_raw_data_with_version(
        version: str,
        data_local_save_dir: str,
        dvc_remote_repo: str,
        dvc_data_folder: str,
        github_user_name: str,
        github_access_token: str,
) -> None:
    rmtree(data_local_save_dir,ignore_errors=True)
    command = get_cmd_to_get_raw_data(version=version,
                                      data_local_save_dir=data_local_save_dir,
                                      dvc_remote_repo=dvc_remote_repo,
                                      dvc_data_folder=dvc_data_folder,
                                      github_user_name=github_user_name,
                                      github_access_token=github_access_token)
    run_shell_command(command)