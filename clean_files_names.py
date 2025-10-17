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


class CleanFilesNames:
    """
    Attributes:
        target_dir (str): Path to the folder where files will be renamed.

    Methods:
        clean_text(text): Cleans the file name text.
        rename_files(): Renames all files in the folder.

    Usage example:
        renamer = CleanFilesNames("D:/ImageFiles")
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
        renamed = []
        for filename in os.listdir(self.target_dir):
            old_path = os.path.join(self.target_dir, filename)
            # Skip directories (files only)
            if not os.path.isfile(old_path):
                continue
            # Split name and extension; clean only the base name
            name_root, ext = os.path.splitext(filename)
            clean_root = self.clean_text(name_root)
            ext = ext.lower()
            new_name = f"{clean_root}{ext}"
            new_path = os.path.join(self.target_dir, new_name)
            # If destination already exists, add suffix _1, _2, ...
            if os.path.exists(new_path) and os.path.abspath(
                old_path
            ) != os.path.abspath(new_path):
                counter = 1
                while True:
                    candidate = f"{clean_root}_{counter}{ext}"
                    candidate_path = os.path.join(self.target_dir, candidate)
                    if not os.path.exists(candidate_path):
                        new_name = candidate
                        new_path = candidate_path
                        break
                    counter += 1
            # If it's the same name, skip
            if os.path.abspath(old_path) == os.path.abspath(new_path):
                continue
            # Try to rename
            try:
                os.rename(old_path, new_path)
                print(f"{filename} renamed to {new_name}")
                renamed.append((filename, new_name))
            except Exception as e:
                print(f"Failed to rename {filename} -> {new_name}: {e}")
        return renamed


def main():
    target_dir = DIRTARGET
    renamer = CleanFilesNames(target_dir)
    renamed_files = renamer.rename_files()
    if not renamed_files:
        print("No files were renamed.")


if __name__ == "__main__":
    main()
