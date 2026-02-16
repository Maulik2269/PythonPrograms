from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Load PDF
#reader = PdfReader("sample2.pdf")
#reader = PdfReader("GenAIBrochure.pdf")
reader = PdfReader("DatabricksBigBookOfGenAIFINAL.pdf")
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

# 4. User question
#question = "What is this document about?"
#question = "What types of leave are available to employees?"
#question = "Compensation is paid monthly or yearly ?"
#question = "What topics are covered in this course?"
#question = "I am having 10 plus experience in MS SQL, is this course will be helpful to me ?"
question = "Give me some idea about this book."

# 5. Retrieve relevant chunks
docs = vectorstore.similarity_search(question, k=3)

context = "\n\n".join(doc.page_content for doc in docs)

# 6. Build grounded prompt
prompt = f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

# 7. Ask the LLM
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

# 8. Print answer
print("\n🤖 Answer:\n")
print(response.choices[0].message.content)