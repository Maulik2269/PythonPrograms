from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Load PDF
reader = PdfReader("sample2.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text()

# 2. Chunk the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")

# 3. Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 4. Store in FAISS
vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

print("✅ Embeddings created and stored in FAISS!")