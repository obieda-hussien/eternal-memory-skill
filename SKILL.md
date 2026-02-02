---
name: eternal-memory
description: AI eternal memory system with semantic search, auto-curation, and multi-layer storage. Supports local and cloud storage for persistent, searchable memories.
---

# Eternal Memory

## Overview

This skill provides an eternal memory system for AI agents. It combines local files, vector databases, and cloud storage to ensure memories persist forever and can be semantically searched.

## Architecture

### Memory Layers

1. **Daily Logs** (`memory/YYYY-MM-DD.md`)
   - Raw conversation logs
   - Automatic daily capture
   - Timestamped entries

2. **Long-term Memory** (`MEMORY.md`)
   - Curated, distilled memories
   - Important events, decisions, preferences
   - Manually and auto-updated

3. **Vector Store**
   - Semantic embeddings for all memories
   - Fast similarity search
   - ChromaDB (local) + Supabase (cloud)

## Quick Start

### Setup

```bash
# Install dependencies
source venv/bin/activate
pip install chromadb supabase sentence-transformers

# Initialize memory database
python3 scripts/setup_memory.py
```

### Basic Usage

```python
# Store a memory
python3 scripts/store_memory.py "User prefers Python over JavaScript"

# Search memories
python3 scripts/search_memory.py "programming languages"

# Auto-curate from daily logs
python3 scripts/curate_memory.py --date 2026-02-02
```

## Features

### 1. Auto-Capture
Automatically captures conversations and important context to daily logs.

### 2. Semantic Search
Search memories by meaning, not just keywords. Uses embeddings to find relevant context.

### 3. Auto-Curation
Periodically reviews daily logs and updates MEMORY.md with important insights.

### 4. Privacy-First
- Local-first architecture (ChromaDB)
- Optional cloud backup (Supabase)
- All data encrypted

### 5. Export/Import
Easily export all memories to JSON or import from backups.

## Storage Options

### Local (ChromaDB)
- Free, unlimited storage
- Fast semantic search
- No internet required
- Data stays on your machine

### Cloud (Supabase)
- Free tier: 500MB database
- Accessible from anywhere
- Automatic backups
- PostgreSQL + pgvector

## Resources

### scripts/

- `setup_memory.py`: Initialize memory databases
- `store_memory.py`: Store new memories
- `search_memory.py`: Semantic search across memories
- `curate_memory.py`: Auto-curate from daily logs
- `export_memory.py`: Export all memories to JSON

### references/

- `chromadb_guide.md`: ChromaDB setup and usage
- `supabase_setup.md`: Supabase configuration
- `embedding_models.md`: Guide to choosing embedding models

### assets/

- `schema.sql`: Supabase database schema
- `config.template.json`: Configuration template

## Integration with OpenClaw

This skill integrates with OpenClaw's existing memory system:
- Reads from `memory/YYYY-MM-DD.md` and `MEMORY.md`
- Enhances `memory_search` with vector search
- Provides backup and export functionality

## Next Steps

1. Run setup script to initialize databases
2. Configure Supabase (optional, for cloud backup)
3. Let the AI auto-capture memories during conversations
4. Use heartbeats to auto-curate daily logs into MEMORY.md

---

**Build eternal memory. Never forget.** 🧠✨
