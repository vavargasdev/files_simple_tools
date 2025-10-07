"""
Class to clean and rename file names in a directory.
Removes accents and special characters,
limits text to 30 characters,
converts to lowercase.

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

import os
import unicodedata
import re

DIRTARGET = "D:/Images"


class ClearFilesNames:
    """
    Attributes:
        target_dir (str): Path to the folder where files will be renamed.

    Methods:
        clean_text(text): Cleans the file name text.
        rename_files(): Renames all files in the folder.

    Usage example:
        renamer = ClearFilesNames("D:/ImageFiles")
        renamer.rename_files()
    """

    def __init__(self, target_dir):
        self.target_dir = target_dir

    @staticmethod
    def clean_text(text):
        # Remove accents
        text_no_accent = (
            unicodedata.normalize("NFKD", text)
            .encode("ASCII", "ignore")
            .decode("utf-8")
        )
        # Remove characters that are not letters, numbers, underscores or dots
        clean = re.sub(r"[^a-zA-Z0-9\.]", "_", text_no_accent)
        # Limit to 30 characters
        clean = clean[:30]
        # Lowercase
        clean = clean.lower()
        return clean

    def rename_files(self):
        if not os.path.exists(self.target_dir):
            print(f"The directory {self.target_dir} does not exist.")
            return []
        for filename in os.listdir(self.target_dir):
            new_name = self.clean_text(filename)
            old_path = os.path.join(self.target_dir, filename)
            new_path = os.path.join(self.target_dir, new_name)
            os.rename(old_path, new_path)
            print(f"{filename} renamed to {new_name}")


def main():
    target_dir = DIRTARGET
    renamer = ClearFilesNames(target_dir)
    renamer.rename_files()


if __name__ == "__main__":
    main()
