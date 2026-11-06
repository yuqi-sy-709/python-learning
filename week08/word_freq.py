from pathlib import Path
import string

path = Path(__file__).parent / "novel.txt" 
if path.exists():
    text = path.read_text(encoding= "utf-8" ) 
else :
    text = """The quick brown fox jumps over the lazy dog. 
The dog barks, and the fox runs away. 
Foxes are quick, dogs are loyal, and the forest is quiet at night. 
The quick fox and the lazy dog meet again tomorrow."""


clean=text.lower().translate(str.maketrans("","",string.punctuation))

words=clean.split()

freq={}
for w in words:
    freq[w]=freq.get(w,0)+1

top20=sorted(freq.items(),key=lambda x:x[1],reverse=True)[:20]

for word,count in top20:
    print(f"{word}: {count}")