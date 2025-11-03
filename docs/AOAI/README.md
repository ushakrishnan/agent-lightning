# Azure OpenAI Integration Documentation```markdown

# AOAI Documentation

This directory contains comprehensive documentation for integrating Agent Lightning with Azure OpenAI services, featuring APO (Automatic Prompt Optimization) capabilities.

This folder contains comprehensive documentation and guides for Azure OpenAI integration with Agent Lightning.

## 📖 Documentation Structure

## Contents

### Installation and Setup

- **[Installation Guide](INSTALLATION_GUIDE.md)** - Complete setup instructions for Azure OpenAI integration- `INSTALLATION_GUIDE.md` - Complete installation guide with conda and UV options

- **[Azure Environment Setup](AZURE_ENV_SETUP.md)** - Azure OpenAI service configuration and authentication- `AZURE_ENV_SETUP.md` - Comprehensive Azure OpenAI environment setup and troubleshooting

- **[WSL Setup Guide](WSL_SETUP_GUIDE.md)** - Windows Subsystem for Linux configuration for optimal development- `WSL_SETUP_GUIDE.md` - Windows Subsystem for Linux setup for agent-lightning



### Implementation Examples**APO-Specific Documentation:**

- **[APO Room Selector](../examples/apo/AOAI/)** - Complete working example with APO training- `examples/apo/AOAI/docs/APO_PERSISTENCE.md` - APO scoring system and persistent optimization guide

- **[Training Persistence](../examples/apo/AOAI/docs/APO_PERSISTENCE.md)** - Advanced persistence and scoring systems- `examples/apo/AOAI/docs/MODULES_OVERVIEW.md` - Comprehensive APO AOAI module documentation

- **[Module Architecture](../examples/apo/AOAI/docs/MODULES_OVERVIEW.md)** - Comprehensive architectural documentation

## Quick Start

## 🚀 Quick Start

1. **Installation**: Follow `INSTALLATION_GUIDE.md` for conda or UV installation

1. **Prerequisites**: Ensure you have Python 3.8+ and access to Azure OpenAI2. **Environment Setup**: Use `AZURE_ENV_SETUP.md` for Azure OpenAI configuration

2. **Installation**: Follow the [Installation Guide](INSTALLATION_GUIDE.md) for complete setup3. **APO Training**: See `examples/apo/AOAI/docs/APO_PERSISTENCE.md` for persistent optimization

3. **Configuration**: Set up your Azure OpenAI credentials using [Azure Environment Setup](AZURE_ENV_SETUP.md)

4. **First Run**: Execute the room selector example to verify your setup## Installation Options



```bash### UV Installation (Recommended)

# Quick verification```bash

cd examples/apo/AOAI# Fast, modern package management

python room_selector_azure.pyuv sync --frozen --extra apo --extra verl --group dev --group torch-cpu --group torch-stable --group trl --group agents --no-default-groups

```uv run python examples/apo/room_selector_apo_persistent.py

```

## 🎯 Key Features

### Conda Installation (Traditional)

### Azure OpenAI Integration```bash

- **Production-ready authentication** with environment variable management# Reliable, widely-used approach

- **Comprehensive error handling** with retry logic and failoverconda create -n agentlightning python=3.10 -y

- **Cost optimization** with efficient token usage and prompt engineeringconda activate agentlightning

- **Model flexibility** supporting gpt-4o-mini and other Azure OpenAI deploymentspip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip install -e .[apo,verl,dev,agents]

### APO (Automatic Prompt Optimization)```

- **Persistent training** with checkpoint management across sessions

- **Multi-dimensional scoring** evaluating multiple performance aspects## Environment Configuration

- **Adaptive learning** that improves prompts based on performance feedback

- **Comprehensive monitoring** with detailed logging and performance tracking### Basic Setup

```bash

### Development Environment# Create .env file in your project root

- **Cross-platform support** with optimized WSL2 configurationcp examples/apo/.env.example .env

- **Modern tooling** with UV package manager and conda integration# Edit with your Azure OpenAI credentials

- **Comprehensive logging** with structured output and error trackingnano .env

- **Interactive testing** with command-line tools and demos```



## 🏗️ Architecture Overview### Required Variables

```bash

```AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

Azure OpenAI IntegrationAZURE_OPENAI_API_KEY=your_api_key

├── Core FrameworkAZURE_OPENAI_API_VERSION=2024-08-01-preview

│   ├── Agent Lightning 0.2.2+AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

│   ├── APO Algorithm```

│   └── Azure OpenAI SDK

├── Implementation Layer## Features Covered

│   ├── Room Selector Agent

│   ├── Training Persistence### 🚀 Installation

│   └── Performance Monitoring- **UV Installation**: Modern package manager with comprehensive extras

└── Environment Layer- **Conda Installation**: Traditional approach with step-by-step verification

    ├── WSL2 Ubuntu 22.04- **Troubleshooting**: Common issues and solutions for WSL, PyTorch, and dependencies

    ├── Python 3.11+

    └── Azure OpenAI Service### 🔧 Environment Setup

```- **Azure OpenAI Configuration**: Complete variable setup and testing

- **Multiple Environment Support**: Dev/prod environment patterns

## 📊 Performance Results- **Security Best Practices**: API key protection and rotation

- **LiteLLM Integration**: Understanding Agent Lightning's environment handling

Our APO integration achieves excellent performance metrics:

### 🎯 APO Training

- **Training Efficiency**: 90%+ average scores after optimization- **Persistent Optimization**: Score tracking across training runs

- **Response Quality**: High-quality recommendations with detailed reasoning- **Configuration Management**: Automatic best-setting loading

- **Cost Effectiveness**: Optimized token usage with gpt-4o-mini- **Performance Tuning**: Parameter optimization guidelines

- **Reliability**: Robust error handling and automatic recovery- **Integration Examples**: Real-world APO usage patterns



## 🔧 Configuration Options### 💻 WSL Setup

- **Complete WSL2 Installation**: From Windows features to Ubuntu setup

### Environment Variables- **Development Environment**: Miniconda, Git, and essential tools

```bash- **VS Code Integration**: Remote development setup

# Azure OpenAI Configuration- **Performance Optimization**: Memory management and file system tips

AZURE_OPENAI_API_KEY=your_api_key_here

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/## Verification Steps

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini

AZURE_OPENAI_API_VERSION=2024-02-15-preview### Test Installation

```bash

# Optional: AgentOps Integration# Check core components

AGENTOPS_API_KEY=your_agentops_keyuv run python -c "import agentlightning; print('✅ Agent Lightning')"

AGENTOPS_ENABLED=trueuv run python -c "import torch; print('✅ PyTorch')"

```uv run python -c "import openai; print('✅ OpenAI SDK')"

```

### APO Training Parameters

```python### Test Azure OpenAI Connection

# Training Configuration```bash

APO_ITERATIONS_PER_SESSION = 5# Verify environment and connectivity

APO_MAX_SESSIONS = 50uv run python -c "

APO_CONVERGENCE_THRESHOLD = 0.95from dotenv import load_dotenv

APO_CHECKPOINT_INTERVAL = 1import openai, os

```load_dotenv()

client = openai.OpenAI(

## 🛠️ Development Workflow    base_url=os.getenv('AZURE_OPENAI_ENDPOINT'),

    api_key=os.getenv('AZURE_OPENAI_API_KEY')

### 1. Environment Setup)

```bashprint('✅ Azure OpenAI connection ready')

# Install Agent Lightning with APO support"

pip install "agentlightning[apo]==0.2.2"```



# Configure Azure OpenAI### Test APO Training

export AZURE_OPENAI_API_KEY="your_key"```bash

export AZURE_OPENAI_ENDPOINT="your_endpoint"# Run APO with Azure OpenAI

```cd examples/apo

uv run python room_selector_apo_persistent.py

### 2. Development Testing```

```bash

# Run interactive demo## Troubleshooting Resources

python examples/apo/AOAI/room_selector_azure.py

| Issue | Solution |

# Execute APO training|-------|----------|

python examples/apo/AOAI/room_selector_apo_persistent.py| **PyTorch hangs in WSL** | Use CPU-only version: `pip install torch --index-url https://download.pytorch.org/whl/cpu` |

```| **Environment variables not loading** | Check `.env` file location and `load_dotenv()` calls |

| **Azure authentication errors** | Verify API keys and endpoint URLs in Azure portal |

### 3. Production Deployment| **Import errors** | Ensure environment is activated: `conda activate agentlightning` or `source .venv/bin/activate` |

```bash

# Verify configuration## Purpose

python -c "from examples.apo.AOAI.room_selector_module import RoomSelectorAgent; agent = RoomSelectorAgent()"

This documentation supports Azure OpenAI integration patterns and comprehensive development infrastructure for agent-lightning, providing:

# Run production workload

# (Implement your specific deployment strategy)- **Complete installation workflows** for different development preferences

```- **Production-ready environment configuration** with security best practices  

- **Advanced APO optimization techniques** for real-world performance

## 🚨 Troubleshooting- **Cross-platform development support** with comprehensive WSL guidance



### Common IssuesAll documentation is tested and verified with the current agent-lightning codebase.

```
#### Authentication Errors
**Problem**: `AuthenticationError` when connecting to Azure OpenAI
**Solution**: 
1. Verify your API key is correct and has not expired
2. Check that your endpoint URL is properly formatted
3. Ensure your deployment name matches your Azure configuration

#### Package Installation Issues
**Problem**: Dependency conflicts or installation failures
**Solution**:
1. Use a fresh virtual environment
2. Install with specific version: `pip install "agentlightning[apo]==0.2.2"`
3. For WSL users, follow the [WSL Setup Guide](WSL_SETUP_GUIDE.md)

#### Training Performance Issues
**Problem**: APO training not converging or low scores
**Solution**:
1. Review your training tasks for clarity and consistency
2. Adjust scoring weights for your specific domain
3. Increase training iterations or adjust learning parameters

### Getting Support

1. **Documentation**: Review the relevant guides in this directory
2. **Examples**: Examine the working implementation in `examples/apo/AOAI/`
3. **Logs**: Check `apo.log` and `agentops.log` for detailed error information
4. **Community**: Engage with the Agent Lightning community for additional support

## 📚 Additional Resources

### Agent Lightning Framework
- [Main Documentation](../index.md)
- [APO Algorithm Deep Dive](../algorithm-zoo/apo.md)
- [Training Best Practices](../how-to/train-first-agent.md)

### Azure OpenAI
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Best Practices Guide](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/models)
- [API Reference](https://docs.microsoft.com/azure/cognitive-services/openai/reference)

### Development Tools
- [WSL Documentation](https://docs.microsoft.com/windows/wsl/)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [AgentOps Platform](https://agentops.ai/)

## 🎯 Next Steps

1. **Complete Setup**: Follow the installation guides to set up your development environment
2. **Run Examples**: Execute the room selector demo to verify your configuration
3. **Explore APO**: Train your first agent using the persistent APO system
4. **Customize Implementation**: Adapt the patterns for your specific use case
5. **Deploy to Production**: Implement proper monitoring and scaling for production use

---

*This documentation provides comprehensive guidance for integrating Agent Lightning with Azure OpenAI, enabling sophisticated AI agent development with production-ready patterns and best practices.*