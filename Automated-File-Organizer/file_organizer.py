import os
import shutil

from config import FILE_CATEGORIES
from logger import write_log


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def organize_files(folder_path):

    moved_files = 0

    try:
        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            if not os.path.isfile(file_path):
                continue

            extension = os.path.splitext(file)[1].lower()

            category_found = False

            for category, extensions in FILE_CATEGORIES.items():

                if extension in extensions:

                    destination_folder = os.path.join(
                        folder_path,
                        category
                    )

                    create_folder(destination_folder)

                    shutil.move(
                        file_path,
                        os.path.join(destination_folder, file)
                    )

                    print(f"Moved: {file} → {category}")

                    write_log(
                        f"Moved '{file}' to '{category}' folder"
                    )

                    moved_files += 1
                    category_found = True
                    break

            if not category_found:

                others_folder = os.path.join(
                    folder_path,
                    "Others"
                )

                create_folder(others_folder)

                shutil.move(
                    file_path,
                    os.path.join(others_folder, file)
                )

                print(f"Moved: {file} → Others")

                write_log(
                    f"Moved '{file}' to 'Others' folder"
                )

                moved_files += 1

        print("\nOrganization Completed Successfully")
        print(f"Total Files Moved: {moved_files}")

        write_log(
            f"Organization completed. {moved_files} files moved."
        )

    except Exception as e:
        print("Error:", e)
        write_log(f"ERROR: {e}")


def rename_files(folder_path):

    try:

        files = os.listdir(folder_path)

        counter = 1

        for file in files:

            old_path = os.path.join(folder_path, file)

            if not os.path.isfile(old_path):
                continue

            extension = os.path.splitext(file)[1]

            new_name = f"File_{counter}{extension}"

            new_path = os.path.join(
                folder_path,
                new_name
            )

            os.rename(old_path, new_path)

            print(f"Renamed: {file} → {new_name}")

            write_log(
                f"Renamed '{file}' to '{new_name}'"
            )

            counter += 1

        print("\nRenaming Completed Successfully")
        write_log("Renaming operation completed")

    except Exception as e:
        print("Error:", e)
        write_log(f"ERROR: {e}")


def delete_empty_folders(folder_path):

    try:

        deleted = 0

        for item in os.listdir(folder_path):

            item_path = os.path.join(
                folder_path,
                item
            )

            if os.path.isdir(item_path):

                if len(os.listdir(item_path)) == 0:

                    os.rmdir(item_path)

                    print(
                        f"Deleted Empty Folder: {item}"
                    )

                    write_log(
                        f"Deleted empty folder '{item}'"
                    )

                    deleted += 1

        print(
            f"\nTotal Empty Folders Deleted: {deleted}"
        )

    except Exception as e:
        print("Error:", e)
        write_log(f"ERROR: {e}")


def show_menu():

    print("\n" + "=" * 50)
    print("      AUTOMATED FILE ORGANIZER")
    print("=" * 50)

    print("\n1. Organize Files")
    print("2. Rename Files")
    print("3. Delete Empty Folders")
    print("4. Exit")


def main():

    folder_path = input(
        "\nEnter Folder Path: "
    ).strip()

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":
            organize_files(folder_path)

        elif choice == "2":
            rename_files(folder_path)

        elif choice == "3":
            delete_empty_folders(folder_path)

        elif choice == "4":
            print("\nThank You For Using File Organizer")
            write_log("Program exited")
            break

        else:
            print("Invalid Choice. Try Again.")


if __name__ == "__main__":
    main()