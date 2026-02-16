from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load PDF
reader = PdfReader("sample2.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text()

print("Total characters in document:", len(text))

# 2. Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(text)

print("Total chunks created:", len(chunks))

# 3. Inspect a chunk
print("\n--- Sample Chunk ---\n")
print(chunks[0])