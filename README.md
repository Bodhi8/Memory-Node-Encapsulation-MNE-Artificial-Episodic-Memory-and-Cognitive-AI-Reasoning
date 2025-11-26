# Memory-Node Encapsulation (MNE): Artificial Episodic Memory for Cognitive AI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Research](https://img.shields.io/badge/Research-Vector1%20Lab-green.svg)](https://vector1.ai/)

##  Overview

**Memory-Node Encapsulation (MNE)** is a revolutionary data structure that enables artificial intelligence systems to develop genuine episodic memory—the ability to remember and learn from lived experiences. Unlike traditional RAG systems that fragment memories into text chunks, or embeddings that compress meaning while discarding context, MNE captures **complete experiential memories** as multidimensional objects.

### Core Thesis
> *"Embeddings enabled AI to understand language. MNE will enable AI to understand life."*

This repository contains the research, implementation, and tools for building memory-driven cognitive AI systems using MNE and the NeoCortex-M architecture.

##  Key Features

- **Holistic Experience Capture**: Store complete memories with sensory data, emotional weight, temporal context, and relational links
- **Emotional Weighting**: Prioritize important memories based on emotional significance
- **Dynamic Graph Relationships**: Connect memories through typed relationships (causal, temporal, semantic, contradictory, confirmatory)
- **Knowledge Distillation**: Extract abstract principles from specific experiences
- **Memory Consolidation**: Sleep-like processes that strengthen patterns and prune irrelevant connections
- **Autobiographical Causality**: Learn causal relationships through direct experience rather than statistical inference
- **Cognitive Retrieval**: Relevance-weighted memory access that mimics human recall

##  Research Papers

This project is based on a series of research papers:

1. **[Memory-Node Encapsulation (MNE): A Revolutionary Data Structure for Artificial Episodic Memory](papers/01_MNE_Core_Paper.md)**  
   *Introduces the MNE data structure, NeoCortex-M architecture, and experimental validation*

2. **[Autobiographical Causality: How Episodic Memory Enables Lived Causal Understanding](papers/02_Autobiographical_Causality.md)**  
   *Explores how MNE enables AI to learn causality through direct experience*

3. **[The Living Memory Graph: Multi-Dimensional Self-Reorganization](papers/03_Living_Memory_Graph.md)** *(Coming Soon)*  
   *Details the dynamic graph reorganization and spreading activation mechanisms*

4. **[Implementation Guide and Best Practices](papers/04_Implementation_Guide.md)** *(Coming Soon)*  
   *Practical guidance for deploying MNE systems in production*

##  Architecture

```
┌─────────────────────────────────────┐
│    Perception Encoder (LLM/Vision)  │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ Memory Encoder (Creates MNE capsules)│
│ - Semantic representation           │
│ - Emotional weight computation      │
│ - Relationship identification       │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Memory Graph Store (Vector + Graph) │
│  - Weaviate / Neo4j / Custom        │
│  - HNSW vector search               │
│  - Graph relationships              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│   Cognitive Retrieval Engine        │
│   - Semantic similarity             │
│   - Emotional weighting             │
│   - Temporal relevance              │
│   - Graph connectivity              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│   Reflective Reasoning Layer        │
│   - Pattern identification          │
│   - Principle extraction            │
│   - Belief updates                  │
│   - Contradiction resolution        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Memory Consolidation Engine        │
│  - Compress redundant memories      │
│  - Strengthen important patterns    │
│  - Prune weak connections           │
│  - Archive low-priority MNEs        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│   LLM Decoder / Response Generator  │
└─────────────────────────────────────┘
```

##  Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mne-project.git
cd mne-project

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Basic Usage

```python
from mne_core import MemorySystem, MNE, ConsolidationConfig

# Initialize memory system
memory_system = MemorySystem(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    vector_db="weaviate",
    consolidation_config=ConsolidationConfig(
        schedule_hours=6,
        compression_threshold=0.8
    )
)

# Encode a new experience
mne = memory_system.encode_experience(
    text="User prefers vegetarian restaurants for dinner",
    emotional_weight=0.4,
    memory_type="episodic"
)

# Retrieve relevant memories
query = "Where should we go for dinner tonight?"
relevant_memories = memory_system.retrieve(
    query=query,
    top_k=5,
    min_relevance=0.6
)

# Generate response using memory context
response = memory_system.generate_response(
    query=query,
    retrieved_memories=relevant_memories
)

print(response)
```

### Advanced: Autobiographical Causality

```python
from mne_core import CausalMNE, CausalEncoder

# Create causal encoder
causal_encoder = CausalEncoder(memory_system)

# Experience a causal event
experience = causal_encoder.encode_causal_experience(
    action="touched_hot_stove",
    outcome="immediate_pain",
    emotional_weight=-0.95,
    prediction_error=0.98  # Highly surprising
)

# System learns: hot_stove → pain (single trial learning!)

# Later: planning with counterfactual simulation
plan = memory_system.plan_action(
    goal="move_hot_pan",
    options=["grab_directly", "use_pot_holder", "wait_to_cool"]
)
# Returns: "use_pot_holder" (highest utility, prevents pain)
```

##  Experimental Results

Comparison against traditional RAG systems:

| Task | RAG Baseline | MNE System | Improvement |
|------|--------------|------------|-------------|
| User Preference Recall | 14% | 92% | +78% |
| Narrative Consistency | 27% | 88% | +61% |
| Zero-Shot Learning | 6% | 74% | +68% |
| Reasoning Explanation | 0% | 63% | +63% |

##  Core Data Structure

```python
@dataclass
class MemoryNodeEncapsulation:
    # Core Identity
    id: UUID
    timestamp: DateTime
    memory_type: Literal["episodic", "semantic", "procedural", "associative"]
    
    # Content Layers
    raw_input: MultimodalContent
    compressed_representation: Float32Array  # Embedding vector
    
    # Affective Computing
    emotional_weight: float  # [-1.0, 1.0]
    valence: Literal["positive", "negative", "neutral", "mixed"]
    arousal: float  # [0.0, 1.0]
    
    # Dynamic Relevance
    relevance_score: float
    access_count: int
    last_accessed: DateTime
    
    # Graph Connectivity
    graph_connections: List[GraphConnection]
    
    # Meta-Learning
    distilled_knowledge: List[DistilledInsight]
    
    # Consolidation Metadata
    consolidation_state: Literal["fresh", "consolidating", "consolidated", "archived"]
    replay_count: int
    integration_score: float
```

##  Use Cases

1. **Personal AI Assistants**: True preference learning and personalization
2. **Healthcare AI**: Patient history with emotional context and causal understanding
3. **Education**: Adaptive tutoring that remembers each student's learning journey
4. **Autonomous Systems**: Robots and vehicles that learn from operational experience
5. **Research Assistants**: Scientific reasoning grounded in accumulated knowledge
6. **Customer Service**: Context-aware support that remembers user history

##  Documentation

- [Installation Guide](docs/installation.md)
- [API Reference](docs/api_reference.md)
- [Architecture Deep Dive](docs/architecture.md)
- [Memory Consolidation Guide](docs/consolidation.md)
- [Causal Learning](docs/causal_learning.md)
- [Best Practices](docs/best_practices.md)
- [Contributing](CONTRIBUTING.md)

##  Development Roadmap

### Phase 1: Core Implementation (Current)
- [x] Basic MNE data structure
- [x] Memory encoding and retrieval
- [x] Graph relationship management
- [ ] Consolidation engine
- [ ] Production-ready APIs

### Phase 2: Advanced Features (Q1-Q2 2025)
- [ ] Multimodal memory (images, audio, video)
- [ ] Distributed memory graphs
- [ ] Multi-agent memory sharing
- [ ] Dream-based insight generation
- [ ] Causal discovery algorithms

### Phase 3: Research Extensions (Q3-Q4 2025)
- [ ] Consciousness and qualia exploration
- [ ] Long-term deployment studies
- [ ] Biological validation experiments
- [ ] AGI integration research

##  Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Areas We Need Help
- **Core Development**: Python implementation of MNE components
- **Database Integration**: Weaviate, Neo4j, Qdrant adapters
- **Performance Optimization**: Scaling to millions of MNEs
- **Documentation**: Examples, tutorials, use cases
- **Research**: Experimental validation, benchmarking
- **Testing**: Unit tests, integration tests, performance tests

##  Citation

If you use MNE in your research, please cite:

```bibtex
@article{curry2024mne,
  title={Memory-Node Encapsulation (MNE): A Revolutionary Data Structure for Artificial Episodic Memory and Cognitive AI Reasoning},
  author={Curry, Brian},
  journal={Vector1 AI Economics Lab},
  year={2024},
  url={https://github.com/yourusername/mne-project}
}

@article{curry2024autobiographical,
  title={Autobiographical Causality: How Episodic Memory Enables Lived Causal Understanding in Artificial Intelligence},
  author={Curry, Brian},
  journal={Vector1 AI Economics Lab},
  year={2024}
}
```

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Vector1 AI Economics Lab for supporting this research
- The open-source community for tools including Weaviate, NetworkX, and the broader AI ecosystem
- The neuroscience community for insights into biological memory consolidation
- Early adopters and contributors who are helping shape this framework

##  Contact

**Brian Curry**  
Founder, Vector1 AI Economics Lab  
Email: brian@vector1.ai  
Website: [https://vector1.ai](https://vector1.ai)  
Medium: [@brian-curry-research](https://medium.com/@brian-curry-research)

##  Star History

If you find MNE useful, please consider starring the repository to help others discover it!

---

**"Intelligence is not primarily about pattern matching sophistication. It's about the ability to store experiences, retrieve relevant experiences, learn from experiences, and build models of the world from accumulated experiences. MNE provides the architectural foundation for all four."**
