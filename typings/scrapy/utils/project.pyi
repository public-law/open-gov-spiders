"""
This type stub file was generated by pyright.
"""

from scrapy.settings import Settings

ENVVAR = ...
DATADIR_CFG_SECTION = ...
def inside_project() -> bool:
    ...

def project_data_dir(project: str = ...) -> str:
    """Return the current project data dir, creating it if it doesn't exist"""
    ...

def data_path(path: str, createdir: bool = ...) -> str:
    """
    Return the given path joined with the .scrapy data directory.
    If given an absolute path, return it unmodified.
    """
    ...

def get_project_settings() -> Settings:
    ...

