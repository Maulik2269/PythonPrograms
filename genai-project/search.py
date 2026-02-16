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

# 3. Create embeddings + vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

# 4. Ask a question
query = "What types of leave are available to employees?"

# 5. Similarity search
docs = vectorstore.similarity_search(query, k=3)

# 6. Print results
print("\n🔍 Top matching chunks:\n")
for i, doc in enumerate(docs, 1):
    print(f"--- Chunk {i} ---")
    print(doc.page_content)
    print()