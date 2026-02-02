#!/usr/bin/env python3
"""
Store a memory in the eternal memory system.
Usage: python3 store_memory.py "Your memory text here"
"""

import sys
import json
from pathlib import Path
from datetime import datetime

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

def store_memory(text, metadata=None):
    """Store a memory with embeddings."""
    config = load_config()
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection("eternal_memories")
    
    # Generate embedding
    print("Generating embedding...")
    model = SentenceTransformer(config['embeddings']['model'])
    embedding = model.encode(text).tolist()
    
    # Create metadata
    mem_metadata = {
        "timestamp": datetime.now().isoformat(),
        "source": "manual",
        **(metadata or {})
    }
    
    # Store in ChromaDB
    memory_id = f"mem_{datetime.now().timestamp()}"
    collection.add(
        ids=[memory_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[mem_metadata]
    )
    
    print(f"✅ Memory stored! (ID: {memory_id})")
    print(f"   Total memories: {collection.count()}")
    
    # Also append to daily log
    today = datetime.now().strftime("%Y-%m-%d")
    daily_log = WORKSPACE / "memory" / f"{today}.md"
    daily_log.parent.mkdir(parents=True, exist_ok=True)
    
    with open(daily_log, 'a') as f:
        f.write(f"\n## {datetime.now().strftime('%H:%M')} - Manual Memory\n")
        f.write(f"{text}\n")
    
    print(f"   Also logged to: {daily_log}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 store_memory.py 'Your memory text'")
        print("\nExample:")
        print("  python3 store_memory.py 'User prefers Python over JavaScript'")
        sys.exit(1)
    
    memory_text = " ".join(sys.argv[1:])
    store_memory(memory_text)

if __name__ == "__main__":
    main()
