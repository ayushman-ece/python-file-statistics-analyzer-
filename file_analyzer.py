import os


class FileAnalyzer:

    def __init__(self, folder):
        self.folder = folder

    def analyze(self):
        if not os.path.exists(self.folder):
            print("Folder not found. ❌")
            return

        files = []

        for name in os.listdir(self.folder):
            path = os.path.join(self.folder, name)

            if os.path.isfile(path):
                size = os.path.getsize(path)
                extension = os.path.splitext(name)[1] or "No Extension"

                files.append({
                    "name": name,
                    "size": size,
                    "extension": extension
                })

        if not files:
            print("No files found. ❌")
            return

        print("\n===== FILE STATISTICS =====")
        print(f"Total Files: {len(files)}")

        total_size = sum(file["size"] for file in files)
        print(f"Total Size : {total_size / 1024:.2f} KB")

        print("\n===== FILE DETAILS =====")

        for file in files:
            print(
                f"{file['name']} → "
                f"{file['size'] / 1024:.2f} KB → "
                f"{file['extension']}"
            )

        largest = max(files, key=lambda file: file["size"])

        print("\n===== LARGEST FILE =====")
        print(f"Name: {largest['name']}")
        print(f"Size: {largest['size'] / 1024:.2f} KB")