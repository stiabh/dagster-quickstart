from pathlib import Path

import dagster as dg

# set up following the practices outlined here:
# https://docs.dagster.io/guides/build/projects/project-structure/combining-components-with-pythonic-definitions

defs = dg.load_from_defs_folder(path_within_project=Path(__file__).parent)
