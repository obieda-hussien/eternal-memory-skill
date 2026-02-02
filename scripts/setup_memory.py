#!/usr/bin/env python3
"""
Setup script for eternal memory system.
Initializes ChromaDB locally and optionally Supabase cloud storage.
"""

import os
import sys
import json
from pathlib import Path

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("Installing ChromaDB...")
    os.system("pip install chromadb")
    import chromadb
    from chromadb.config import Settings

# Paths
WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
CHROMA_DIR = WORKSPACE / ".eternal-memory" / "chromadb"
CONFIG_FILE = WORKSPACE / ".eternal-memory" / "config.json"

def setup_local_storage():
    """Initialize ChromaDB for local vector storage."""
    print("Setting up local vector storage (ChromaDB)...")
    
    # Create directories
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR),
        settings=Settings(anonymized_telemetry=False)
    )
    
    # Create collection for memories
    try:
        collection = client.get_or_create_collection(
            name="eternal_memories",
            metadata={"description": "AI eternal memory storage"}
        )
        print(f"✅ ChromaDB initialized at {CHROMA_DIR}")
        print(f"   Collection: {collection.name}")
        print(f"   Count: {collection.count()} memories")
    except Exception as e:
        print(f"❌ Error initializing ChromaDB: {e}")
        return False
    
    return True

def setup_config():
    """Create configuration file."""
    print("\nCreating configuration...")
    
    config = {
        "storage": {
            "local": {
                "enabled": True,
                "path": str(CHROMA_DIR)
            },
            "cloud": {
                "enabled": False,
                "provider": "supabase",
                "url": "",
                "api_key": ""
            }
        },
        "embeddings": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "local": True
        },
        "auto_capture": {
            "enabled": True,
            "daily_logs": True
        },
        "auto_curation": {
            "enabled": True,
            "frequency": "daily"
        }
    }
    
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Configuration saved to {CONFIG_FILE}")
    return True

def prompt_cloud_setup():
    """Ask user if they want to configure cloud storage."""
    print("\n" + "="*60)
    print("CLOUD STORAGE (OPTIONAL)")
    print("="*60)
    print("Do you want to set up cloud backup with Supabase?")
    print("This allows you to access memories from anywhere.")
    print("Free tier: 500MB database + pgvector for semantic search")
    print("\nYou'll need:")
    print("1. Supabase account (free): https://supabase.com")
    print("2. Create a new project")
    print("3. Get your project URL and API key")
    
    setup_cloud = input("\nSet up cloud storage now? (y/n): ").lower().strip()
    
    if setup_cloud == 'y':
        print("\nGreat! Let's configure Supabase...")
        url = input("Supabase project URL: ").strip()
        api_key = input("Supabase API key (anon key): ").strip()
        
        if url and api_key:
            # Update config
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            
            config['storage']['cloud']['enabled'] = True
            config['storage']['cloud']['url'] = url
            config['storage']['cloud']['api_key'] = api_key
            
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=2)
            
            print("✅ Cloud storage configured!")
            print("   Run: python3 scripts/sync_to_cloud.py to upload existing memories")
        else:
            print("⚠️  Skipping cloud setup (missing credentials)")
    else:
        print("⚠️  Cloud storage skipped. You can configure it later in:")
        print(f"   {CONFIG_FILE}")

def main():
    """Main setup flow."""
    print("="*60)
    print("ETERNAL MEMORY SETUP")
    print("="*60)
    print("This will initialize the eternal memory system for AI agents.")
    print(f"Workspace: {WORKSPACE}\n")
    
    # Setup local storage
    if not setup_local_storage():
        print("\n❌ Setup failed. Check errors above.")
        sys.exit(1)
    
    # Create config
    if not setup_config():
        print("\n❌ Configuration failed.")
        sys.exit(1)
    
    # Optional cloud setup
    prompt_cloud_setup()
    
    print("\n" + "="*60)
    print("✅ SETUP COMPLETE!")
    print("="*60)
    print("\nNext steps:")
    print("1. Store your first memory:")
    print("   python3 scripts/store_memory.py 'Your memory here'")
    print("\n2. Search memories:")
    print("   python3 scripts/search_memory.py 'query'")
    print("\n3. Auto-curate daily logs:")
    print("   python3 scripts/curate_memory.py")
    print("\nEternal memory is ready! 🧠✨")

if __name__ == "__main__":
    main()
