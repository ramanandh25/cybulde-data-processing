from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from pydantic.dataclasses import dataclass


@dataclass
class DatasetReaderConfig:
    __target__: str = MISSING
    dataset_dir: str = MISSING
    dataset_name: str = MISSING


@dataclass
class GHCDatasetReaderConfig(DatasetReaderConfig):
    __target__: str = "cybulde.data_processing.dataset_readers.GHCDatasetReader"
    dev_split_ratio: float = MISSING


@dataclass
class JTCDatasetReaderConfig(DatasetReaderConfig):
    __target__: str = "cybulde.data_processing.dataset_readers.JigsawToxicCommentsDatasetReader"
    dev_split_ratio: float = MISSING


@dataclass
class TwitterDatasetReaderConfig(DatasetReaderConfig):
    __target__: str = "cybulde.data_processing.dataset_readers.TwitterDatasetReader"
    dev_split_ratio: float = MISSING
    test_split_ratio: float = MISSING


@dataclass
class DatasetReaderManagerConfig:
    __target__: str = "cybulde.data_processing.dataset_readers.DatasetReaderManager"
    dataset_readers: dict[str, DatasetReaderConfig] = MISSING


def setup_config()->None:
    cs = ConfigStore.instance()
    cs.store(name="ghc_dataset_reader_schema",
             node=GHCDatasetReaderConfig,
             group="dataset_reader_manager/dataset_reader")
    cs.store(name="jtc_dataset_reader_schema",
             node=JTCDatasetReaderConfig,
             group="dataset_reader_manager/dataset_reader")
    cs.store(name="twitter_dataset_reader_schema",
             node=TwitterDatasetReaderConfig,
             group="dataset_reader_manager/dataset_reader")
    cs.store(name="dataset_reader_manager_schema",
             node=DatasetReaderManagerConfig,
             group="dataset_reader_manager")
