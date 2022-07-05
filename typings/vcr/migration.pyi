"""
This type stub file was generated by pyright.
"""

"""
Migration script for old 'yaml' and 'json' cassettes

.. warning:: Backup your cassettes files before migration.

It merges and deletes the request obsolete keys (protocol, host, port, path)
into new 'uri' key.
Usage::

    python -m vcr.migration PATH

The PATH can be path to the directory with cassettes or cassette itself
"""
def preprocess_yaml(cassette):
    ...

PARTS = ...
def build_uri(**parts): # -> str:
    ...

def migrate_json(in_fp, out_fp): # -> bool:
    ...

def migrate_yml(in_fp, out_fp): # -> bool:
    ...

def migrate(file_path, migration_fn): # -> bool:
    ...

def try_migrate(path): # -> bool:
    ...

def main(): # -> None:
    ...

if __name__ == "__main__":
    ...
