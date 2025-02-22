import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import ollama
from dotenv import load_dotenv
import re
import os

load_dotenv()


def stream_response(response):
    """Generator to stream response like typing."""
    for word in response.split():
        yield word + " "


class SimpleRAG:
    def __init__(self, collection_name="documents", path="./sounds"):
        self.client = chromadb.PersistentClient(
            path=path)  # Persistent storage
        self.embedding_func = SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name=collection_name, embedding_function=self.embedding_func)
        self.is_loaded = False
        self.collection_name = collection_name

    def split_transcript(self, doc_text):
        """Splits the transcript into conversation-based segments."""
        segments = []
        current_segment = []
        last_time = None

        for line in doc_text.strip().split("\n"):
            match = re.match(r"(\d{2}:\d{2}) (.*)", line)
            if match:
                timestamp, text = match.groups()
                if last_time and int(timestamp.split(":")[0]) > int(last_time.split(":")[0]):
                    segments.append(" ".join(current_segment))
                    current_segment = []
                current_segment.append(f"[{timestamp}] {text}")
                last_time = timestamp

        if current_segment:
            segments.append("\n".join(current_segment))

        return segments

    def load_document(self, collection_name, doc_text):
        """Loads a transcript by splitting it into conversational contexts and adding to ChromaDB."""
        if self.is_loaded and self.collection_name == collection_name:
            print("Document already loaded, refresh the collection")
            self.client.delete_collection(self.collection_name)
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name, embedding_function=self.embedding_func)
        else:
            self.collection_name = collection_name
            if self.collection_name in self.client.list_collections():
                self.collection = self.client.get_collection(
                    name=self.collection_name)
                print(
                    f"Loaded cached conversation segments into the database.")
                return
            else:
                self.collection = self.client.create_collection(
                    name=self.collection_name, embedding_function=self.embedding_func)
        segments = self.split_transcript(doc_text)
        for i, segment in enumerate(segments):
            print("========= Segment", i, "=========")
            self.collection.add(ids=[str(i)], documents=[segment])
            print(segment)
        self.is_loaded = True
        print(
            f"Loaded {len(segments)} conversation segments into the database.")

    def retrieve_context(self, query, top_k=5):
        """Retrieves top-k relevant chunks from ChromaDB."""
        results = self.collection.query(query_texts=[query], n_results=top_k)
        return "\n".join(results["documents"][0]) if results["documents"] else ""

    def ask(self, query, chat_history=[], use_k_last_history=5):
        """Retrieves relevant info and queries Llama 3.2."""
        context = self.retrieve_context(query)
        if not context:
            return "No relevant information found."

        if len(chat_history):
            prev_chat_history = ""
            for sender, msg in chat_history[-use_k_last_history:]:
                prev_chat_history += f"{sender}: {msg}\n"
        else:
            prev_chat_history = "No previous chat history."

        prompt = f"""
        You are an assistant helping a doctor to recall his memory regarding his previous meeting with his patient. Here is your last conversation with him earlier (if any):
        {prev_chat_history}

        Now, the doctor is asking you another question.
        Current Question: {query}
        
        Here's retrieved context from the transcription of the meeting which in format of conversational segments that contains the timestamp and the conversation text:
        Context:
        {context}

        Please answer only the doctor's Current Question based on the context above. No need to intro or add further information that is not required, just answer the Current Question directly.
        
        Put a corresponding timestamp at the end of each point of your answer. The timestamp mention should be in "![hh:mm]" format.
        
        Here is a good example:
        Question: What is the patient's current medication?
        Answer: The patient is currently taking Paracetamol and Amoxicillin for his fever and cough. ![00:12] The patient is also taking Vitamin C for his immune system. ![00:15]
        """

        # print(prompt)

        response = ollama.chat(model=os.getenv("LLM_MODEL_NAME"), messages=[
                               {"role": "user", "content": prompt}])
        return response["message"]["content"]


# Example usage
if __name__ == "__main__":
    rag = SimpleRAG()
    doc_text = """Your long document text goes here..."""
    rag.load_document(doc_text)
    question = "What is the key information from the document?"
    print(rag.ask(question))
