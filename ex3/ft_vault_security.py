#!/usr/bin/env python3

from typing import Literal, TypeAlias

Read: TypeAlias = Literal["read"]
Write: TypeAlias = Literal["write"]
Action: TypeAlias = Read | Write

Content: TypeAlias = str
Error: TypeAlias = str
Success: TypeAlias = tuple[Literal[True], Content]
Failure: TypeAlias = tuple[Literal[False], Error]
ArchiveResult: TypeAlias = Success | Failure


def secure_archive(
    file_name: str, action: Action = "read", content: str = ""
) -> ArchiveResult:
    match action:
        case "read":
            try:
                with open(file_name, mode="r", encoding="utf-8") as reader:
                    lines = [line for line in reader]
                    return True, "".join(lines)
            except OSError as error:
                return False, f"{error}"
            except UnicodeDecodeError as error:
                return False, f"{error}"
        case "write":
            try:
                with open(file_name, mode="w", encoding="utf-8") as writer:
                    writer.writelines([content])
                return True, "Content successfully written to file"
            except OSError as error:
                return False, f"{error}"
            except UnicodeDecodeError as error:
                return False, f"{error}"


def main() -> None:
    print("=== Cyber Archives Security ==")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    file_name = "../ex2/ancient_fragment.txt"
    print("Using 'secure_archive' to read from a regular file:")
    result, content = secure_archive(file_name)
    print(result, content)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(file_name, action="write", content=content))


if __name__ == "__main__":
    main()
