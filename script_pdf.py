import os.path

from pypdf import PdfReader

reader = PdfReader("tmp/Okken_Python-Testing-with-pytest.pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[4].extract_text())

assert "Simple, Rapid, Effective, and Scalable" in reader.pages[4]
print(os.path.getsize("tmp/Okken_Python-Testing-with-pytest.pdf"))
assert os.path.getsize("tmp/Okken_Python-Testing-with-pytest.pdf") == 9295550


