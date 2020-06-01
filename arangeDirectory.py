import shutil
from pathlib import Path

org_img_path = Path("/Users/tanimotoryou/Documents/lab/imageData/Abdomen/RawData/Training/img")
org_lab_path = Path("/Users/tanimotoryou/Documents/lab/imageData/Abdomen/RawData/Training/label")

img_glob = sorted(org_img_path.glob("*"))
lab_glob = sorted(org_lab_path.glob("*"))

for x, y in zip(img_glob, lab_glob):
    print(str(x), str(y))



