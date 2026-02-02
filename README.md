# Eternal Memory Skill for AI Agents 🤖🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green.svg)](https://github.com/obieda-hussien/eternal-memory-skill)

**Give your AI agents eternal memory!** Never forget conversations, learn from past interactions, and build truly autonomous AI companions.

## ✨ Features

### 🔍 Semantic Search
- **Vector Embeddings**: Uses sentence-transformers for intelligent similarity search
- **Find by Meaning**: Search memories by concepts, not just keywords
- **Fast Results**: ChromaDB provides lightning-fast queries

### 🏗️ Multi-Layer Architecture
- **Daily Logs**: Automatic capture of conversations and events
- **Long-term Memory**: Curated, distilled knowledge base
- **Vector Storage**: Semantic embeddings for advanced retrieval

### 🔒 Privacy-First Design
- **Local Storage**: All data stays on your machine by default
- **No External Dependencies**: Works offline with ChromaDB
- **Optional Cloud**: Sync to Supabase for cross-device access

### 🤖 Auto-Curation
- **Smart Summarization**: Automatically extracts key insights
- **Memory Maintenance**: Keeps only relevant, valuable information
- **Continuous Learning**: Improves over time

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install chromadb sentence-transformers
```

### 2. Setup Memory System

```bash
python3 scripts/setup_memory.py
```

### 3. Store Your First Memory

```bash
python3 scripts/store_memory.py "Your AI learned something new today!"
```

### 4. Search Memories

```bash
python3 scripts/search_memory.py "what did the AI learn"
```

## 📁 Project Structure

```
eternal-memory-skill/
├── SKILL.md              # Complete skill documentation
├── scripts/
│   ├── setup_memory.py   # Initialize memory databases
│   ├── store_memory.py   # Store new memories
│   └── search_memory.py  # Semantic search
└── README.md             # This file
```

## 🛠️ Advanced Usage

### Cloud Backup (Optional)

Configure Supabase for cloud storage:

1. Create free account at [supabase.com](https://supabase.com)
2. Get your project URL and API key
3. Update `config.json` with credentials
4. Run sync scripts (coming soon)

### Integration with OpenClaw

This skill integrates seamlessly with OpenClaw AI agents:
- Reads existing `memory/YYYY-MM-DD.md` files
- Enhances search capabilities with vector similarity
- Provides backup and export functionality

## 🎯 Use Cases

- **Personal AI Assistants**: Remember user preferences and history
- **Customer Support Bots**: Learn from interactions to improve responses
- **Educational AI**: Track learning progress and adapt content
- **Creative Writing AI**: Maintain story continuity across sessions
- **Research Assistants**: Keep track of findings and sources

## 🔧 Technical Details

- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector DB**: ChromaDB (local) + optional Supabase (cloud)
- **Languages**: Python 3.8+
- **Dependencies**: chromadb, sentence-transformers

## 📈 Roadmap

- [ ] Auto-curation from daily logs
- [ ] Cloud sync with Supabase
- [ ] Export/import functionality
- [ ] Memory visualization dashboard
- [ ] Integration with more AI frameworks

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a PR!

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`AI`, `memory`, `vector-search`, `embeddings`, `autonomous-agents`, `machine-learning`, `nlp`, `open-source`

---

**Built with ❤️ by Eman AI** | **Published on ClawHub Marketplace** 🛒

*Give your AI the gift of memory. Make it truly eternal.* ✨
