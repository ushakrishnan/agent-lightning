# Azure OpenAI Installation Guide````markdown

# Complete Installation Guide for Agent Lightning with Azure OpenAI

This comprehensive guide walks you through setting up Agent Lightning with Azure OpenAI integration, from initial prerequisites to running your first APO-optimized agent.

This guide provides comprehensive installation instructions for Agent Lightning with Azure OpenAI support using both **Conda** and **UV** package managers.

## 🎯 Overview

## Prerequisites

This installation enables:

- **Agent Lightning 0.2.2+** with APO (Automatic Prompt Optimization) capabilities- **Windows 11 with WSL2 Ubuntu 22.04 LTS** (recommended) or Linux/macOS

- **Azure OpenAI** integration with gpt-4o-mini and other models- **Python 3.10+** (tested with 3.10-3.12)

- **Production-ready patterns** with error handling, logging, and persistence- **Conda** or **UV** package manager

- **Cross-platform support** with optimized WSL2 configuration- **Azure OpenAI account** with API keys



## 📋 Prerequisites## Installation Methods



### System Requirements### Method 1: UV Installation (Recommended - Modern & Fast)

- **Operating System**: Windows 11 with WSL2, macOS 10.15+, or Linux

- **Python**: 3.8 or higher (3.11+ recommended)#### 1. Install with UV (All Extras)

- **Memory**: 4GB RAM minimum, 8GB recommended

- **Storage**: 2GB free space for dependencies and training data```bash

# Navigate to agent-lightning directory

### Azure Requirementscd /path/to/agent-lightning

- **Azure Subscription** with access to Azure OpenAI Service

- **Azure OpenAI Resource** deployed in a supported region# Install with all extras for complete functionality

- **Model Deployment** of gpt-4o-mini or compatible modeluv sync --frozen \

- **API Keys** with appropriate permissions    --extra apo \

    --extra verl \

### Development Environment    --group dev \

- **Git** for version control    --group torch-cpu \

- **Code Editor** (VS Code recommended)    --group torch-stable \

- **Terminal** with bash support (WSL2 for Windows)    --group trl \

    --group agents \

## 🚀 Installation Steps    --no-default-groups

```

### Step 1: Python Environment Setup

#### 2. Verify UV Installation

#### Option A: Using UV (Recommended)

```bash```bash

# Install UV package manager# Option 1: Use uv run (recommended)

curl -LsSf https://astral.sh/uv/install.sh | shuv run python -c "import agentlightning; print('✅ Agent Lightning installed')"



# Create project environment# Option 2: Activate virtual environment

cd agent-lightningsource .venv/bin/activate

uv venvpython -c "import agentlightning; print('✅ Agent Lightning installed')"

source .venv/bin/activate  # Linux/macOS```

# or .venv\Scripts\activate  # Windows

#### 3. UV Installation Results

# Install Agent Lightning with APO support

uv add "agentlightning[apo]==0.2.2"**✅ Successfully Installed Components:**

```- **agentlightning**: 0.2.2 (installed as editable from source)

- **torch**: 2.8.0+cpu (CPU-optimized version)

#### Option B: Using Conda- **verl**: 0.6.0 (VERL algorithm support)

```bash- **poml**: 0.0.8 (APO algorithm support)

# Create conda environment- **Dependencies**: agentops, aiohttp, fastapi, flask, openai, etc.

conda create -n agentlightning python=3.11

conda activate agentlightning**✅ Virtual Environment:**

- **Location**: `.venv/` folder in project root

# Install Agent Lightning- **Python**: 3.12.12 (or your system Python version)

pip install "agentlightning[apo]==0.2.2"- **Activation**: `source .venv/bin/activate` or use `uv run`

```

### Method 2: Conda Installation (Traditional - Reliable)

#### Option C: Using pip + venv

```bash#### 1. Create Conda Environment

# Create virtual environment

python -m venv agentlightning-env```bash

source agentlightning-env/bin/activate  # Linux/macOS# Create a new conda environment with Python 3.10

# or agentlightning-env\Scripts\activate  # Windowsconda create -n agentlightning python=3.10 -y

conda activate agentlightning

# Upgrade pip```

pip install --upgrade pip

#### 2. Install PyTorch (CPU Version for WSL Compatibility)

# Install Agent Lightning with APO support

pip install "agentlightning[apo]==0.2.2"```bash

```# Install CPU-only PyTorch for WSL compatibility

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### Step 2: Azure OpenAI Setup```



#### Create Azure OpenAI Resource#### 3. Install Agent Lightning

1. **Azure Portal**: Navigate to [portal.azure.com](https://portal.azure.com)

2. **Create Resource**: Search for "OpenAI" and select "Azure OpenAI"```bash

3. **Configure Resource**:# Navigate to agent-lightning directory

   - **Subscription**: Select your Azure subscriptioncd /path/to/agent-lightning

   - **Resource Group**: Create new or use existing

   - **Region**: Choose supported region (e.g., East US, West Europe)# Install agent-lightning in development mode with all extras

   - **Name**: Choose unique resource namepip install -e .[apo,verl,dev,agents]

   - **Pricing Tier**: Standard S0```



#### Deploy Model#### 4. Install Additional Dependencies

1. **Navigate to Resource**: Go to your Azure OpenAI resource

2. **Model Deployments**: Click "Model deployments" in the left menu```bash

3. **Create Deployment**:# Install OpenAI SDK for Azure OpenAI

   - **Model**: Select `gpt-4o-mini` or `gpt-4`pip install openai python-dotenv

   - **Model version**: Use latest available```

   - **Deployment name**: `gpt-4o-mini` (or your preference)

   - **Content filter**: Use default or customize as needed## Post-Installation Verification



#### Get API Credentials### 1. Basic Installation Test

1. **Keys and Endpoint**: Navigate to "Keys and Endpoint" section

2. **Copy Values**:```bash

   - **Key 1** or **Key 2**: Your API key# Activate your environment

   - **Endpoint**: Your resource endpoint URLconda activate agentlightning  # for conda

   - **Region**: Note the region for reference# OR

source .venv/bin/activate      # for UV

### Step 3: Environment Configuration

# Check agent-lightning version

#### Create Environment Filepip show agentlightning

```bash

# Create .env file in your project directory# Test core imports

cat > .env << 'EOF'python -c "import agentlightning; print('✅ Agent Lightning')"

# Azure OpenAI Configurationpython -c "import torch; print(f'✅ PyTorch {torch.__version__}')"

AZURE_OPENAI_API_KEY=your_api_key_herepython -c "import openai; print('✅ OpenAI SDK')"

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/```

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini

AZURE_OPENAI_API_VERSION=2024-02-15-preview### 2. Environment Verification



# Optional: AgentOps Integration#### For UV Installation:

AGENTOPS_API_KEY=your_agentops_key_here```bash

AGENTOPS_ENABLED=true# Check UV environment status

uv run pip list | grep -E "(agentlightning|torch|openai)"

# Optional: Logging Configuration

LOG_LEVEL=INFO# Verify all extras are installed

ENABLE_TRACE_LOGGING=trueuv run python -c "

EOFimport sys

```try:

    import agentlightning

#### Set Environment Variables    import torch

```bash    import openai

# Load environment variables    from agentlightning.algorithm.apo import APO

export $(cat .env | xargs)    print('✅ All components verified')

except ImportError as e:

# Verify configuration    print(f'❌ Missing: {e}')

echo "Endpoint: $AZURE_OPENAI_ENDPOINT""

echo "Deployment: $AZURE_OPENAI_DEPLOYMENT_NAME"```

```

#### For Conda Installation:

### Step 4: Verify Installation```bash

# Check conda environment

#### Test Basic Installationconda info --envs

```pythonconda list | grep -E "(agentlightning|torch|openai)"

# test_installation.py

import sys# Verify installation

print(f"Python version: {sys.version}")python -c "

try:

try:    import agentlightning

    import agentlightning    import torch  

    print(f"Agent Lightning version: {agentlightning.__version__}")    import openai

    print("✅ Agent Lightning installed successfully")    from agentlightning.algorithm.apo import APO

except ImportError as e:    print('✅ All components verified')

    print(f"❌ Agent Lightning installation failed: {e}")except ImportError as e:

    print(f'❌ Missing: {e}')

try:"

    from agentlightning.algorithm.apo import APO```

    print("✅ APO algorithm available")

except ImportError as e:## Package Versions (Verified Working)

    print(f"❌ APO algorithm not available: {e}")

| Package | Version | Purpose |

try:|---------|---------|---------|

    from openai import AzureOpenAI| **agentlightning** | 0.2.2 | Core framework |

    print("✅ Azure OpenAI SDK available")| **torch** | 2.7.1+cpu / 2.8.0+cpu | PyTorch for ML |

except ImportError as e:| **openai** | Latest | Azure OpenAI SDK |

    print(f"❌ Azure OpenAI SDK not available: {e}")| **verl** | 0.6.0 | VERL algorithm support |

```| **poml** | 0.0.8 | APO algorithm support |

| **python-dotenv** | Latest | Environment variable loading |

```bash

python test_installation.py## Usage Instructions

```

### UV Usage (Recommended)

#### Test Azure OpenAI Connection```bash

```python# Method 1: Use uv run (no activation needed)

# test_azure_connection.pyuv run python examples/apo/room_selector_apo_persistent.py

import os

from openai import AzureOpenAI# Method 2: Activate environment first

source .venv/bin/activate

def test_azure_connection():python examples/apo/room_selector_apo_persistent.py

    try:deactivate  # when done

        client = AzureOpenAI(```

            api_key=os.getenv("AZURE_OPENAI_API_KEY"),

            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),### Conda Usage

            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")```bash

        )# Activate environment

        conda activate agentlightning

        # Test API call

        response = client.chat.completions.create(# Run your scripts

            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini"),python examples/apo/room_selector_apo_persistent.py

            messages=[{"role": "user", "content": "Hello, Azure OpenAI!"}],

            max_tokens=50# Deactivate when done

        )conda deactivate

        ```

        print("✅ Azure OpenAI connection successful")

        print(f"Response: {response.choices[0].message.content}")## Troubleshooting

        return True

        ### WSL PyTorch Issues

    except Exception as e:**Problem**: PyTorch hangs on import in WSL2

        print(f"❌ Azure OpenAI connection failed: {e}")

        return False**Solution**:

```bash

if __name__ == "__main__":# Uninstall and reinstall CPU-only version

    test_azure_connection()pip uninstall torch torchvision torchaudio

```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

```

```bash

python test_azure_connection.py### Import Errors

```**Problem**: `ModuleNotFoundError` for agentlightning



### Step 5: Download Examples**Solution**:

```bash

#### Clone Agent Lightning Repository# For UV: Ensure you're using uv run or activated .venv

```bashsource .venv/bin/activate

# Clone the repository

git clone https://github.com/ushakrishnan/agent-lightning.git# For Conda: Ensure environment is activated

cd agent-lightningconda activate agentlightning



# Navigate to Azure OpenAI examples# Reinstall in development mode

cd examples/apo/AOAIpip install -e .[apo,verl,dev,agents]

``````



#### Test Room Selector Demo### UV Sync Issues

```bash**Problem**: UV sync fails with dependency conflicts

# Run interactive demo

python room_selector_azure.py**Solution**:

``````bash

# Clear UV cache and retry

Expected output:uv cache clean

```uv sync --frozen --extra apo --extra verl --group dev --group torch-cpu --group torch-stable --group trl --group agents --no-default-groups

🏨 Azure OpenAI Room Selector Agent```

==================================================

🚀 Initializing Room Selector Agent...### Azure OpenAI Connection Issues

✅ Agent initialized successfully!**Problem**: Authentication or endpoint errors



💬 Interactive Mode (type 'quit' to exit)**Solution**:

Enter your room selection requirements:1. Check environment variables in `.env` file

```2. Verify API keys and endpoint URLs  

3. Test with: `uv run python -c "import openai; print('SDK ready')"`

#### Run APO Training

```bash## Quick Installation Commands

# Execute APO training session

python room_selector_apo_persistent.py### For New Projects (UV - Recommended):

``````bash

git clone https://github.com/ushakrishnan/agent-lightning.git

Expected output:cd agent-lightning

```uv sync --frozen --extra apo --extra verl --group dev --group torch-cpu --group torch-stable --group trl --group agents --no-default-groups

🧠 Agent Lightning APO Training with Azure OpenAIuv run python -c "import agentlightning; print('✅ Ready to go!')"

============================================================```

🚀 Starting new training session...

📊 Average Score: 0.87### For New Projects (Conda - Traditional):

🏆 Best Score Ever: 0.87```bash

⏱️  Duration: 45.2 secondsgit clone https://github.com/ushakrishnan/agent-lightning.git

```cd agent-lightning

conda create -n agentlightning python=3.10 -y

## 🔧 Advanced Configurationconda activate agentlightning

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### Performance Optimizationpip install -e .[apo,verl,dev,agents]

pip install openai python-dotenv

#### Token Usage Optimizationpython -c "import agentlightning; print('✅ Ready to go!')"

```bash```

# Environment variables for cost control

export AZURE_OPENAI_MAX_TOKENS=1000## Next Steps

export AZURE_OPENAI_TEMPERATURE=0.7

export AZURE_OPENAI_TIMEOUT=301. **Environment Setup**: Configure Azure OpenAI credentials using `AZURE_ENV_SETUP.md`

```2. **APO Training**: Try persistent optimization with `examples/apo/room_selector_apo_persistent.py`

3. **Documentation**: Read `examples/apo/AOAI/docs/APO_PERSISTENCE.md` for advanced optimization techniques

#### Caching Configuration

```python## Support Resources

# Add to your .env file

ENABLE_RESPONSE_CACHING=true- **WSL Setup**: See `WSL_SETUP_GUIDE.md` for detailed WSL configuration

CACHE_TTL_SECONDS=3600- **Environment Variables**: Check `AZURE_ENV_SETUP.md` for Azure configuration

CACHE_MAX_SIZE=1000- **APO Training**: See `examples/apo/AOAI/docs/APO_PERSISTENCE.md` for optimization techniques

```````

### Monitoring and Observability

#### AgentOps Integration
```bash
# Sign up at agentops.ai and get your API key
export AGENTOPS_API_KEY=your_agentops_key
export AGENTOPS_ENABLED=true
export AGENTOPS_AUTO_START_SESSION=true
```

#### Structured Logging
```python
# logging_config.py
import logging
import os

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('agent_lightning.log'),
            logging.StreamHandler()
        ]
    )
    
    # Configure specific loggers
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

setup_logging()
```

### Security Best Practices

#### API Key Management
```bash
# Use Azure Key Vault for production
# Never commit API keys to version control

# Add to .gitignore
echo ".env" >> .gitignore
echo "*.log" >> .gitignore
echo "apo_training_history.json" >> .gitignore
```

#### Network Security
```python
# Configure firewall rules for Azure OpenAI
# Restrict access to specific IP ranges
# Use Azure Private Endpoints for enhanced security
```

## 🚨 Troubleshooting

### Common Installation Issues

#### ModuleNotFoundError: agentlightning
**Problem**: Package not found after installation
**Solution**:
```bash
# Verify you're in the correct environment
which python
pip list | grep agentlightning

# Reinstall if necessary
pip uninstall agentlightning
pip install "agentlightning[apo]==0.2.2"
```

#### Azure OpenAI Authentication Errors
**Problem**: `AuthenticationError` or `403 Forbidden`
**Solutions**:
1. **Verify API Key**: Check key is correct and not expired
2. **Check Endpoint**: Ensure endpoint URL format is correct
3. **Verify Deployment**: Confirm deployment name matches Azure configuration
4. **Region Access**: Ensure your subscription has access to the region

#### Package Dependency Conflicts
**Problem**: Version conflicts during installation
**Solution**:
```bash
# Create fresh environment
conda create -n agentlightning-fresh python=3.11
conda activate agentlightning-fresh

# Install with specific versions
pip install "agentlightning[apo]==0.2.2" --no-cache-dir
```

### Performance Issues

#### Slow Response Times
**Possible Causes**:
- Network latency to Azure region
- Large token limits in requests
- Rate limiting from Azure OpenAI

**Solutions**:
```python
# Optimize for faster responses
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    timeout=30,  # Reduce timeout
    max_retries=2  # Limit retries
)
```

#### Memory Usage Issues
**Solutions**:
```python
# Optimize memory usage
import gc

def optimize_memory():
    # Clear caches periodically
    gc.collect()
    
    # Limit conversation history
    max_history_length = 10
    
    # Use streaming for large responses
    stream=True
```

### WSL-Specific Issues

#### File Permission Errors
```bash
# Fix WSL file permissions
sudo chmod +x /mnt/c/usha/GHOrgs/agent-lightning/examples/apo/AOAI/*.py
```

#### Path Issues
```bash
# Use WSL paths, not Windows paths
cd /mnt/c/usha/GHOrgs/agent-lightning
# Not: cd C:\usha\GHOrgs\agent-lightning
```

## 📚 Next Steps

### 1. Explore Examples
- **Basic Usage**: Run the room selector demo
- **APO Training**: Execute persistent training sessions
- **Custom Scenarios**: Modify training tasks for your domain

### 2. Development Workflow
- **Code Organization**: Structure your agent implementations
- **Testing Strategy**: Implement comprehensive test coverage
- **Deployment Planning**: Design production deployment strategy

### 3. Advanced Features
- **Custom Algorithms**: Implement domain-specific APO variants
- **Integration Patterns**: Connect with external APIs and databases
- **Monitoring**: Implement comprehensive observability

### 4. Production Considerations
- **Scaling**: Design for multiple concurrent users
- **Security**: Implement proper authentication and authorization
- **Monitoring**: Set up alerting and performance tracking
- **Cost Management**: Optimize token usage and API costs

## 🔗 Additional Resources

### Documentation
- [Azure Environment Setup](AZURE_ENV_SETUP.md)
- [WSL Setup Guide](WSL_SETUP_GUIDE.md)
- [APO Persistence Guide](../examples/apo/AOAI/docs/APO_PERSISTENCE.md)

### External Resources
- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Agent Lightning GitHub](https://github.com/ushakrishnan/agent-lightning)
- [AgentOps Platform](https://agentops.ai/)

---

*This installation guide provides a complete foundation for Azure OpenAI integration with Agent Lightning. Follow the steps sequentially for the smoothest setup experience.*