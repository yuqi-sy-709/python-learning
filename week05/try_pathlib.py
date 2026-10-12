from pathlib import Path
import shutil
folder = Path("D:/学习/学习手册-Trae版/.trae/python-learning/week05/test")
print(folder.exists())
for f in folder.iterdir():
    print(f.name,f.suffix)
new_dir=folder/"txt"
new_dir.mkdir(exist_ok=True)
shutil.move(str(f),new_dir/f.name)
