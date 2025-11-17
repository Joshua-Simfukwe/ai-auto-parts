from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """
    Generate a vector embedding (list of floats) for input text.
    """
    if not text or text.strip() == "":
        return None

    vector = model.encode([text])[0]   # returns numpy array
    return vector.tolist()             # convert to Python list for JSONField