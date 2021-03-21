import sys
import os


def load_allowed_file_extensions(allowed_file_path):
    with open(os.path.join(sys.path[0], allowed_file_path)) as allowed_file:
        return set([s.strip() for s in allowed_file.read().splitlines()])


def is_format_potentially_changed(filePath1, filePath2, allowed_file_ext):
    assert filePath1.split(".")[-1] == filePath2.split(".")[
        -1]  # assert file extensions are the same
    file_ext = filePath1.split(".")[-1]

    if file_ext not in allowed_file_ext:
        return False

    with open(filePath1, "r") as file_1:
        file_1_stripped = "".join(file_1.read().split())
    with open(filePath2, "r") as file_2:
        file_2_stripped = "".join(file_2.read().split())
    return file_1_stripped == file_2_stripped


if __name__ == "__main__":
    starting_path = sys.argv[1]
    repo_root_1 = sys.argv[2]
    repo_root_2 = sys.argv[3]

    format_changed = []

    repo_1_starting_path = os.path.join(repo_root_1, starting_path)
    repo_2_starting_path = os.path.join(repo_root_2, starting_path)

    allowed_file_extensions = load_allowed_file_extensions(
        "allowed_file_extensions.txt")

    for curr_root_repo_1, dirs, files in os.walk(repo_1_starting_path):

        path_from_root = curr_root_repo_1.replace(repo_root_1, "")
        curr_root_repo_2 = repo_root_2 + path_from_root

        for file_name in files:
            file_path_repo_1 = os.path.join(curr_root_repo_1, file_name)
            file_path_repo_2 = os.path.join(curr_root_repo_2, file_name)
            if not os.path.isfile(file_path_repo_2):
                continue
            if is_format_potentially_changed(file_path_repo_1,
                                             file_path_repo_2,
                                             allowed_file_extensions):
                format_changed.append(file_path_repo_1)

    for file_potentially_reformatted in format_changed:
        print(file_potentially_reformatted)
