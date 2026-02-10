import kagglehub
import os
import shutil


src_path = kagglehub.dataset_download(
    "rohanrao/formula-1-world-championship-1950-2020"
)

DST = os.path.join("datasets", "raw")


os.makedirs(DST, exist_ok=True)


count = 0

for filename in os.listdir(src_path):
    if filename.endswith(".csv"):
        shutil.copy(
            os.path.join(src_path, filename),
            os.path.join(DST, filename)
        )
        count += 1


print(f"Copied {count} files")

