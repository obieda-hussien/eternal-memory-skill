#!/usr/bin/env python3
"""
Search memories using semantic similarity.
Usage: python3 search_memory.py "your query"
"""

import sys
import json
from pathlib import Path

try:
    import chromadb
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Installing dependencies...")
    import os
    os.system("pip install chromadb sentence-transformers")
    import chromadb
    from sentence_transformers import SentenceTransformer

WORKSPACE = Path.home() / ".openclaw" / "workspace"
CHROMA_DIR = WORKSPACE / ".eternal-memory" / "chromadb"
CONFIG_FILE = WORKSPACE / ".eternal-memory" / "config.json"

def load_config():
    """Load configuration."""
    if not CONFIG_FILE.exists():
        print("❌ Memory system not initialized. Run: python3 scripts/setup_memory.py")
        sys.exit(1)
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def search_memories(query, n_results=5):
    """Search memories by semantic similarity."""
    config = load_config()
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection("eternal_memories")
    
    if collection.count() == 0:
        print("No memories stored yet!")
        return
    
    # Generate query embedding
    print(f"Searching for: '{query}'...\n")
    model = SentenceTransformer(config['embeddings']['model'])
    query_embedding = model.encode(query).tolist()
    
    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(n_results, collection.count())
    )
    
    # Display results
    print(f"Found {len(results['documents'][0])} relevant memories:\n")
    print("="*60)
    
    for i, (doc, metadata, distance) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ), 1):
        print(f"\n{i}. Similarity: {1 - distance:.2%}")
        print(f"   Time: {metadata.get('timestamp', 'Unknown')}")
        print(f"   Source: {metadata.get('source', 'Unknown')}")
        print(f"\n   {doc}")
        print("   " + "-"*56)
    
    print("\n" + "="*60)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search_memory.py 'your query'")
        print("\nExample:")
        print("  python3 search_memory.py 'programming languages'")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    search_memories(query)

if __name__ == "__main__":
    main()
