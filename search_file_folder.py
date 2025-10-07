"""
Class with usage example to quickly locate files or folders locally.
You can define the extension, search for folders or files
recursively or only in the root of the given directory.

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

import glob
import os

# Configure here
DIRTARGET = "D:/Images"
DIRFILE = "file"  # Use "file" or "dir"
WORD = "test"
EXT = "jpg"
RECURSIVE = True  # True to search in subfolder, False to search only in root


class SearchFilesFolder:
    """
    Attributes:
        target_dir (str): The directory where the search will be performed.
        dir_or_file (str): Either 'dir' for searching directories or 'file' for files.
        keyword (str): The keyword to search for within file/folder names.
        extension (str): The file extension to filter (only applies when searching for files).
        recursive(bool): Whether to search recursively in subdirectories.

    Usage example:
        new_search = SearchFilesFolder("D:/ImageFiles", "file", "test", "jpg", True)
        new_search.start()
    """

    def __init__(self, target_dir, dir_or_file, keyword, extension, recursive):
        self.target_dir = target_dir
        self.dir_or_file = dir_or_file
        self.keyword = keyword
        self.extension = extension
        self.recursive = recursive

    def start(self):
        if self.dir_or_file not in ["dir", "folder", "file"]:
            raise ValueError("dir_or_file must be 'dir', 'folder', or 'file'.")

        if not os.path.exists(self.target_dir):
            print(f"The directory {self.target_dir} does not exist.")
            return []

        if self.dir_or_file == "dir" or self.dir_or_file == "folder":
            result = sorted(self.search_dir())
        else:
            result = sorted(self.search_files())

        if result:
            if self.dir_or_file == "dir" or self.dir_or_file == "folder":
                print("Subdirectories found, sorted by name:")
            else:
                print("Files found, sorted by name:")
            for file in result:
                print(file)
        else:
            print("No files or subdirectories found!")

    def search_files(self):
        if self.extension:
            dirs = os.path.join(
                self.target_dir, f"**/*{self.keyword}*.{self.extension}"
            )
        else:
            dirs = os.path.join(self.target_dir, f"**/*{self.keyword}*")
        return glob.glob(dirs, recursive=self.recursive)

    def search_dir(self):
        dirs = os.path.join(self.target_dir, f"**/*{self.keyword}*")
        return [
            directory
            for directory in glob.glob(dirs, recursive=self.recursive)
            if os.path.isdir(directory)
        ]


def main():
    new_search = SearchFilesFolder(DIRTARGET, DIRFILE, WORD, EXT, RECURSIVE)
    new_search.start()


if __name__ == "__main__":
    main()
