
## Project Name
**Fine-Tuning Large Language Models for Arabic News Processing**

---

## Project Description
Developed an end-to-end NLP pipeline for fine-tuning Large Language Models (LLMs) to perform advanced Arabic news text processing tasks, including entity extraction and translation. The project utilized parameter-efficient fine-tuning techniques (LoRA) on the Qwen2.5-1.5B-Instruct model using LLaMA-Factory framework, achieving optimized performance for structured data extraction from Arabic news articles. Implemented production-grade inference optimization using vLLM for high-throughput model serving.

---

## Key Implementation Points

### 1. **LoRA-Based Model Fine-Tuning with LLaMA-Factory**
   - Fine-tuned Qwen2.5-1.5B-Instruct model on 2,700+ training samples using Low-Rank Adaptation (LoRA) technique with rank-64 configuration targeting all model layers for parameter-efficient training
   - Designed structured Pydantic schemas for multi-task learning including entity extraction (13 entity types: person, location, organization, time, money, etc.), news categorization (8 categories), and Arabic-to-English translation
   - Implemented custom data preprocessing pipeline with formatted instruction-following templates for supervised fine-tuning (SFT), optimizing for 3,500 token context length with multi-worker parallel processing

### 2. **Production-Grade Deployment with vLLM and Advanced Inference Optimization**
   - Deployed the fine-tuned model using vLLM serving framework with LoRA adapter integration, achieving 80% GPU memory utilization for optimized throughput and reduced inference latency
   - Developed custom logits processors for controlled text generation, implementing character-level filtering to ensure output quality and language constraints during inference
   - Integrated experiment tracking using Weights & Biases (WandB) for monitoring training metrics, loss curves, and model performance evaluation across training checkpoints

---

## Technical Stack
- **Frameworks**: LLaMA-Factory, Hugging Face Transformers, vLLM, PyTorch
- **Model**: Qwen2.5-1.5B-Instruct (1.5B parameters)
- **Techniques**: LoRA (Low-Rank Adaptation), Supervised Fine-Tuning (SFT), Parameter-Efficient Fine-Tuning
- **Languages**: Python, Arabic NLP
- **Libraries**: Pydantic, Datasets, Optimum, WandB
- **Platform**: Google Colab with GPU acceleration

---

## Project Outcomes
- Successfully trained a specialized Arabic NLP model capable of extracting structured information from news articles
- Achieved efficient fine-tuning with <5% of model parameters updated through LoRA technique
- Deployed production-ready inference server supporting concurrent requests with optimized memory management
- Created reusable data schemas and preprocessing pipelines for Arabic text processing tasks

---

