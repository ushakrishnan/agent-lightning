# Azure OpenAI APO Integration# APO Room Selector - Azure OpenAI Edition



This folder contains a complete Azure OpenAI integration for Agent Lightning's APO (Automatic Prompt Optimization) algorithm, featuring a room selection agent with persistent optimization.This directory contains the APO (Automatic Prompt Optimization) room selector implementation optimized for Azure OpenAI, featuring persistent optimization and comprehensive documentation.



## 🚀 Quick Start## 🗂️ **Directory Structure**



1. **Environment Setup**: Follow the [AOAI Installation Guide](../../docs/AOAI/INSTALLATION_GUIDE.md)```

2. **Configure Azure OpenAI**: Set your environment variables (see [Azure Environment Setup](../../docs/AOAI/AZURE_ENV_SETUP.md))examples/apo/AOAI/

3. **Run APO Training**: Execute the persistent training example├── docs/

4. **Test the Agent**: Use the optimized room selector│   ├── APO_PERSISTENCE.md          # Comprehensive APO guide

│   └── MODULES_OVERVIEW.md         # Detailed module documentation

## 📁 Files Overview├── room_selector_azure.py          # Core Azure OpenAI room selector

├── room_selector_apo_persistent.py # APO training with persistence

### Core Implementation├── room_tasks.jsonl                # Training dataset

- **`room_selector_module.py`** - Core room selection logic and Azure OpenAI integration└── README.md                       # This file

- **`room_selector_azure.py`** - Executable script for testing the room selector agent```

- **`room_selector_apo_persistent.py`** - APO training with persistent optimization

- **`room_tasks.jsonl`** - Training dataset with room selection scenarios## 📚 **Documentation**



### Documentation### Core Documentation

- **`docs/APO_PERSISTENCE.md`** - Detailed guide on APO persistence and scoring- **[APO_PERSISTENCE.md](docs/APO_PERSISTENCE.md)** - Complete guide to APO scoring, persistence, and optimization

- **`docs/MODULES_OVERVIEW.md`** - Architecture and module documentation- **[MODULES_OVERVIEW.md](docs/MODULES_OVERVIEW.md)** - Comprehensive module documentation with architecture details



## 🎯 Features### Related Documentation

- **[Installation Guide](../../../docs/AOAI/INSTALLATION_GUIDE.md)** - Complete installation with UV and Conda

### Room Selection Agent- **[Azure Environment Setup](../../../docs/AOAI/AZURE_ENV_SETUP.md)** - Azure OpenAI configuration guide

- **Smart Reasoning**: Analyzes user preferences, room features, and context

- **Flexible Criteria**: Handles budget, size, amenities, location preferences## 🔧 **Core Implementation**

- **Real-world Scenarios**: Supports business trips, family vacations, romantic getaways

- **Detailed Explanations**: Provides clear rationale for recommendations### Main Modules

- **`room_selector_azure.py`** - Core room selector agent with Azure OpenAI integration

### APO Training  - Structured task processing with Pydantic models

- **Persistent Optimization**: Saves and loads training progress across sessions  - Intelligent room scoring and selection logic

- **Performance Tracking**: Monitors average scores and improvement trends  - Comprehensive error handling and logging

- **Automatic Logging**: Comprehensive logs with AgentOps integration  

- **Configurable Training**: Adjustable parameters for different optimization goals- **`room_selector_apo_persistent.py`** - APO training orchestrator with persistence

  - Persistent optimization across training runs

### Azure OpenAI Integration  - Automatic best-configuration loading

- **Production Ready**: Full error handling and retry logic  - Comprehensive training history tracking

- **Secure Authentication**: Environment-based API key management

- **Optimized Models**: Uses gpt-4o-mini for cost-effective performance### Data Files

- **Comprehensive Logging**: Detailed request/response tracking- **`room_tasks.jsonl`** - Training dataset with diverse room booking scenarios

- **Generated files**: `apo_training_history.json`, `apo.log`, `pomltrace/`

## 🛠️ Usage Examples

## 🚀 **Quick Start**

### Basic Room Selection

```bash### Prerequisites

cd examples/apo/AOAI1. **Environment Setup**: Configure your `.env` file in the parent APO directory:

python room_selector_azure.py```bash

```# Copy example and edit with your Azure OpenAI credentials

cp ../env.example ../.env

### APO Training Sessionnano ../.env

```bash```

cd examples/apo/AOAI

python room_selector_apo_persistent.pyRequired variables:

``````bash

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

### Interactive TestingAZURE_OPENAI_API_KEY=your_api_key_here

```pythonAZURE_OPENAI_API_VERSION=2024-12-01-preview

from room_selector_module import RoomSelectorAgentAZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o  # Your Azure deployment name

```

agent = RoomSelectorAgent()

result = agent.select_room({2. **Installation**: Ensure Agent Lightning is installed with APO support:

    "user_preferences": "romantic getaway, ocean view",```bash

    "budget_range": "$200-400 per night",# Using UV (recommended)

    "dates": "weekend in December"uv sync --extra apo --extra verl --group dev

})

print(result)# Using Conda

```conda activate agentlightning

pip install -e .[apo,verl,dev,agents]

## 📊 Performance Results```



Our APO training achieves excellent performance:### Run APO Training

- **Average Score**: 90%+ after optimization```bash

- **Training Efficiency**: Rapid convergence with persistent checkpoints# Navigate to AOAI directory

- **Real-world Accuracy**: High-quality room recommendations validated against user preferencescd examples/apo/AOAI



## 🔧 Configuration# Execute APO training with persistence

python room_selector_apo_persistent.py

### Environment Variables```

```bash

AZURE_OPENAI_API_KEY=your_api_key_here### Expected Output

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/```bash

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-miniHotel Room Selector with APO - Azure OpenAI Version with Persistence

AZURE_OPENAI_API_VERSION=2024-02-15-preview======================================================================

```✅ Azure OpenAI client created successfully

✅ Using deployment: gpt-4o

### APO Parameters✅ Loaded datasets: 4 training, 4 validation tasks

- **Training Rounds**: Configurable optimization iterations📈 Using optimal config from best run (score: 0.876)

- **Persistence**: Automatic checkpoint saving/loading🚀 Starting APO training with persistence...

- **Scoring**: Multi-dimensional evaluation metrics🎉 APO training completed!

- **Logging**: Comprehensive performance tracking📊 Final score: 0.923

💾 Training history saved for future optimization runs.

## 🏗️ Architecture```



```## 🎯 **Features**

room_selector_module.py     # Core agent implementation

    ├── RoomSelectorAgent   # Main agent class### Core Capabilities

    ├── Azure OpenAI client # LLM integration- **Azure OpenAI Integration**: Seamless integration with Azure deployments

    └── Logging system     # Performance monitoring- **Persistent Learning**: Saves training history and automatically loads optimal configurations

- **Room Selection Intelligence**: AI agent that learns to select optimal rooms based on requirements

room_selector_apo_persistent.py  # APO training- **Performance Tracking**: Monitors and improves decision quality over time

    ├── APO algorithm       # Automatic prompt optimization- **Comprehensive Logging**: Detailed logs for debugging and analysis

    ├── Persistence layer  # Training state management

    └── Performance tracking # Metrics and evaluation### Advanced Features

```- **Configuration Optimization**: Automatically tunes APO parameters based on historical performance

- **Multi-Environment Support**: Separate configurations for development and production

## 📋 Requirements- **Error Resilience**: Graceful handling of network issues and API failures

- **Rich Monitoring**: Console output with progress indicators and performance metrics

- **Agent Lightning**: 0.2.2+ with APO extras

- **Azure OpenAI**: Valid subscription and deployment## 📊 **Performance Metrics**

- **Python**: 3.8+ with required dependencies

- **Environment**: WSL2, Linux, or macOS recommended### Latest Results

- **Average Success Rate**: 87.6% with baseline prompts

## 🔍 Troubleshooting- **Optimal Configuration**: 

  - Validation batch size: 5

### Common Issues  - Gradient batch size: 2

1. **API Key Errors**: Verify environment variables are set correctly  - Beam width: 2

2. **Deployment Not Found**: Ensure your Azure OpenAI deployment name matches  - Best deployment: `gpt-4.1-mini` (cost-effective choice)

3. **Rate Limiting**: Implement exponential backoff for high-volume usage

4. **Training Persistence**: Check file permissions for checkpoint saving### Training Evolution

```

### Getting HelpRun 1: Default config → Score: 0.650

- Review the [installation guide](../../docs/AOAI/INSTALLATION_GUIDE.md)Run 2: Optimized → Score: 0.750

- Check the [troubleshooting section](../../docs/AOAI/AZURE_ENV_SETUP.md#troubleshooting)Run 3: Fine-tuned → Score: 0.876  ← Current best

- Examine logs in `apo.log` and `agentops.log````



## 🚀 Next Steps## 🔍 **Analysis and Debugging**



1. **Scale Training**: Experiment with larger datasets and longer training sessions### Generated Files

2. **Custom Domains**: Adapt the pattern for your specific use cases- **`apo_training_history.json`** - Training scores and configurations

3. **Production Deployment**: Implement proper monitoring and error handling- **`apo.log`** - Detailed APO training logs

4. **Integration**: Connect with real hotel booking APIs or databases- **`pomltrace/`** - POML optimization traces for analysis

- **`agentops.log`** - Agent operations monitoring

## 📖 Additional Resources

### Monitoring Commands

- [APO Algorithm Documentation](../../docs/algorithm-zoo/apo.md)```bash

- [Agent Lightning Documentation](../../docs/)# View training progress

- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)tail -f apo.log



---# Analyze score evolution

grep "score" apo.log

*This implementation demonstrates production-ready patterns for Azure OpenAI integration with Agent Lightning's APO algorithm, providing a complete foundation for building optimized AI agents.*
# Check optimization traces
ls pomltrace/ && cat pomltrace/latest_trace.json

# Review training history
python -c "
import json
with open('apo_training_history.json') as f:
    h = json.load(f)
    print(f'Runs: {len(h[\"runs\"])}, Best: {h[\"best_score\"]:.3f}')
"
```

## 🛠️ **Development**

### Adding New Scenarios
1. Edit `room_tasks.jsonl` with new booking scenarios
2. Test with `python room_selector_azure.py`
3. Run APO training to optimize for new tasks

### Configuration Tuning
1. Backup `apo_training_history.json`
2. Modify parameters in `get_optimal_config_from_history()`
3. Monitor performance improvements

### Testing
```bash
# Test Azure connectivity
python -c "from room_selector_azure import create_azure_client; print('✅ Azure client ready')"

# Validate task format
python -c "from room_selector_azure import load_room_tasks; print(f'✅ Loaded {len(load_room_tasks())} tasks')"
```

## 📋 **Troubleshooting**

### Common Issues
| Issue | Solution |
|-------|----------|
| Authentication failed | Check `AZURE_OPENAI_API_KEY` in `.env` |
| Model not found | Verify `AZURE_OPENAI_DEPLOYMENT_NAME` matches deployment |
| Training fails | Reduce batch sizes in configuration |
| No history found | Normal for first run; defaults will be used |

### Support Resources
- **[APO Persistence Guide](docs/APO_PERSISTENCE.md)** - Detailed troubleshooting
- **[Modules Overview](docs/MODULES_OVERVIEW.md)** - Architecture and debugging
- **[Azure Setup Guide](../../../docs/AOAI/AZURE_ENV_SETUP.md)** - Environment configuration

---

**Version**: 2.0  
**Last Updated**: November 2, 2025  
**Maintainer**: Agent Lightning AOAI Examples Team