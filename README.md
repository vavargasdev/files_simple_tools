# Files Simple Tools

Collection of small tools in class format to perform common file and folder tasks.

Prerequisite: Python 3

## Overview

This repository contains two simple utilities:

- `search_file_folder.py` — (SearchFilesFolder class) Quickly find files or folders locally, with optional recursion and extension filtering.
- `clean_files_names.py` — (CleanFilesNames class) Clean and rename filenames by removing accents and special characters, limiting length, normalizing case and avoiding name collisions.

## Requirements

- Python 3.x
- Standard library only (no external dependencies by default)

Recommendation:
- For reproducible environments, consider using a virtual environment:
  ```bash
  python -m venv .venv
  source .venv/bin/activate   # Linux/macOS
  .venv\Scripts\activate      # Windows
  pip install -r requirements-optional.txt
  ```

## search_file_folder.py

Search for files or directories by name and optional extension.

Usage example:
```py
from search_file_folder import SearchFilesFolder

# Search for files with "test" in the name and "jpg" extension, recursively
search = SearchFilesFolder("D:/ImageFiles", "file", "test", "jpg", True)
search.start()
```

Notes:
- `dir_or_file` accepts `"dir"`, `"folder"` or `"file"`.
- When `recursive=True`, the search traverses subdirectories using glob.

## clean_files_names.py

Clean filenames in a target directory:
- Remove accents
- Replace spaces and special characters with underscores
- Limit base name to 30 characters
- Convert to lowercase
- Preserve file extension
- If a cleaned name already exists, append `_1`, `_2`, ... to avoid collisions

Usage example:
```py
from clean_files_names import CleanFilesNames

renamer = CleanFilesNames("D:/ImageFiles")
renamer.rename_files()
```

Behavior notes:
- Only actual files are renamed (directories are skipped).
- Extensions are normalized to lowercase and preserved.
- The script returns a list of renamed pairs and prints progress and errors.

## License

MIT License — see the source file headers for author and version information.