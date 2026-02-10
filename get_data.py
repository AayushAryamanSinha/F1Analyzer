import kagglehub
import os
import shutil

#Downloading datasets to the path
src_path = kagglehub.dataset_download(
    "rohanrao/formula-1-world-championship-1950-2020"
)

#Defining path 
DST = os.path.join("datasets", "raw")


#Checking if it exists or needs to be made
os.makedirs(DST, exist_ok=True)


count = 0

#Copying from src to DST 
for filename in os.listdir(src_path):
    if filename.endswith(".csv"):
        shutil.copy(
            os.path.join(src_path, filename),
            os.path.join(DST, filename)
        )
        count += 1

#Confirmation
print(f"Copied {count} files")


