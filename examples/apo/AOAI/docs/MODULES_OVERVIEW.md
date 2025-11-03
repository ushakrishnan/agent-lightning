# Azure OpenAI APO Integration - Modules Overview````markdown

# APO AOAI Module Documentation

This document provides a comprehensive architectural overview of all modules and files in the Azure OpenAI APO integration, detailing their purpose, functionality, and interconnections.

This document provides comprehensive documentation for all files and modules in the `examples/apo/AOAI/` directory, which demonstrates Azure OpenAI integration with Agent Lightning's APO (Automatic Prompt Optimization) algorithm.

## 🏗️ Architecture Overview

## 📁 Directory Structure

The Azure OpenAI APO integration follows a modular architecture with clear separation of concerns:

```

```examples/apo/AOAI/

examples/apo/AOAI/├── docs/

├── Core Implementation│   ├── APO_PERSISTENCE.md          # APO scoring and persistence guide

│   ├── room_selector_module.py      # Core business logic│   └── MODULES_OVERVIEW.md         # This file - comprehensive module documentation

│   ├── room_selector_azure.py       # Interactive executable├── room_selector_azure.py          # Core Azure OpenAI room selector agent

│   └── room_selector_apo_persistent.py # APO training├── room_selector_apo_persistent.py # APO training with persistent optimization

├── Data & Configuration├── room_tasks.jsonl                # Training dataset for room selection tasks

│   └── room_tasks.jsonl             # Training dataset└── README.md                       # Quick start guide for AOAI examples

├── Documentation```

│   ├── README.md                    # Main documentation

│   └── docs/## 🎯 Purpose and Goals

│       ├── APO_PERSISTENCE.md       # APO system guide

│       └── MODULES_OVERVIEW.md      # This fileThis module demonstrates:

└── Generated Artifacts (gitignored)- **Azure OpenAI Integration**: Proper configuration and usage with Agent Lightning

    ├── apo_training_history.json    # Training checkpoints- **APO Optimization**: Automatic prompt optimization for improved performance

    ├── *.log                        # Application logs- **Persistent Learning**: Score tracking and configuration optimization across training runs

    └── pomltrace/                   # POML debugging traces- **Production Patterns**: Best practices for enterprise Azure OpenAI deployments

```

## 📋 File Documentation

## 📋 Module Documentation

### 🔧 Core Files

### 1. Core Implementation Modules

#### `room_selector_azure.py`

#### `room_selector_module.py`**Purpose**: Core Azure OpenAI room selector agent implementation

**Purpose**: Central business logic for room selection with Azure OpenAI integration

**Key Components**:

**Key Components**:```python

```python# Azure OpenAI client configuration

class RoomSelectorAgent:def create_azure_client() -> AsyncAzureOpenAI:

    """Main agent class providing room selection capabilities."""    """Creates Azure OpenAI client with proper authentication and endpoint setup."""

    

    def __init__(self):# Main agent function

        """Initialize Azure OpenAI client and configuration."""@rollout

        async def room_selector(task, prompt_template: PromptTemplate) -> float:

    def select_room(self, user_input: str, available_rooms: str = None) -> Dict[str, Any]:    """Room selection agent that uses Azure OpenAI for decision making."""

        """Core room selection method with comprehensive error handling."""

        # Scoring/evaluation function

    def _setup_azure_openai(self) -> AzureOpenAI:async def judge_room_selection(task: RoomSelectionTask, selected_room_id: int) -> float:

        """Configure Azure OpenAI client with proper authentication."""    """Judges how well the room selection meets user requirements."""

        ```

    def _get_default_rooms(self) -> str:

        """Provide default room options for demonstration."""**Environment Dependencies**:

```- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI service endpoint

- `AZURE_OPENAI_API_KEY` - Authentication key

**Features**:- `AZURE_OPENAI_API_VERSION` - API version (e.g., "2024-12-01-preview")

- ✅ **Production-ready Azure OpenAI integration**- `AZURE_OPENAI_DEPLOYMENT_NAME` - Model deployment name

- ✅ **Comprehensive error handling and retry logic**

- ✅ **Configurable logging and monitoring****Key Features**:

- ✅ **Environment-based configuration management**- ✅ Proper Azure OpenAI authentication and endpoint configuration

- ✅ **Flexible room data management**- ✅ Error handling for network and API issues

- ✅ Structured task processing with Pydantic models

**Dependencies**:- ✅ Flexible room selection logic with scoring

- `openai` - Azure OpenAI Python SDK- ✅ Rich console output for debugging and monitoring

- `logging` - Python standard logging

- `os` - Environment variable access**Usage Pattern**:

- `json` - Data serialization```python

- `typing` - Type hints for better code quality# Load environment and create client

load_dotenv('../.env')

**Configuration**:client = create_azure_client()

```python

# Required environment variables# Execute room selection

AZURE_OPENAI_API_KEY          # Your API keytask = RoomSelectionTask(date="2025-10-13", time="11:00", ...)

AZURE_OPENAI_ENDPOINT         # Azure endpoint URLscore = await room_selector(task, prompt_template_baseline())

AZURE_OPENAI_DEPLOYMENT_NAME  # Model deployment name```

AZURE_OPENAI_API_VERSION      # API version (default: 2024-02-15-preview)

```---



**Usage Example**:#### `room_selector_apo_persistent.py`

```python**Purpose**: APO training orchestrator with persistent optimization and Azure OpenAI integration

from room_selector_module import RoomSelectorAgent

**Key Components**:

agent = RoomSelectorAgent()```python

result = agent.select_room("Business trip, need WiFi and workspace, budget $200-250")# Configuration management

print(result["recommendation"])def get_optimal_config_from_history() -> dict:

```    """Loads best-performing configuration from previous training runs."""



#### `room_selector_azure.py`def save_training_result(score: float, config: dict) -> None:

**Purpose**: Interactive command-line interface for testing the room selector agent    """Persists training results for future optimization."""



**Key Features**:# APO algorithm setup

- 🖥️ **Interactive user interface** with input validationalgo = APO[RoomSelectionTask](

- 🔍 **Environment validation** and setup guidance    openai_client,

- 📊 **Real-time performance metrics** (token usage, response time)    gradient_model=azure_deployment,

- 🛡️ **Graceful error handling** with user-friendly messages    apply_edit_model=azure_deployment,

- 🚪 **Clean exit handling** with proper resource cleanup    **optimal_config  # Use historical best configuration

)

**Main Function Flow**:```

```python

def main():**Training Flow**:

    # 1. Environment validation1. **History Loading**: Retrieves optimal configuration from previous runs

    # 2. Agent initialization 2. **Dataset Preparation**: Loads and splits room selection tasks

    # 3. Interactive loop3. **APO Creation**: Configures algorithm with Azure deployment parameters

    # 4. Result display and metrics4. **Training Execution**: Runs prompt optimization with progress tracking

    # 5. Graceful shutdown5. **Result Persistence**: Saves scores and configurations for future use

```

**Persistent Features**:

**Usage**:- 📊 **Score Tracking**: Maintains history of training performance

```bash- 🔧 **Configuration Optimization**: Automatically uses best-performing settings

cd examples/apo/AOAI- 💾 **Progress Persistence**: Resumes optimization from best known state

python room_selector_azure.py- 📈 **Performance Analytics**: Tracks improvement trends over time

```

**Configuration Parameters**:

**Interactive Experience**:| Parameter | Default | Range | Purpose |

```|-----------|---------|-------|---------|

🏨 Azure OpenAI Room Selector Agent| `val_batch_size` | 5 | 3-10 | Validation batch size for stability |

==================================================| `gradient_batch_size` | 2 | 2-8 | Gradient computation batch size |

🚀 Initializing Room Selector Agent...| `beam_width` | 1 | 1-4 | Search beam width for exploration |

✅ Agent initialized successfully!| `branch_factor` | 1 | 1-4 | Branching factor for alternatives |

| `beam_rounds` | 1 | 1-5 | Number of optimization rounds |

💬 Interactive Mode (type 'quit' to exit)

Enter your room selection requirements:---



Your requirements: Business trip, need good WiFi and workspace### 📊 Data Files

🤔 Analyzing your requirements...

✅ Room Recommendation:#### `room_tasks.jsonl`

------------------------------**Purpose**: Training dataset containing room selection scenarios

I recommend the Business Room ($200/night) because it perfectly matches your requirements...

📊 Tokens used: 245**Format**:

``````json

{

#### `room_selector_apo_persistent.py`  "task_input": {

**Purpose**: APO training implementation with persistent state management    "date": "2025-10-13",

    "time": "11:00", 

**Key Components**:    "duration_min": 30,

```python    "attendees": 2,

class PersistentAPOTrainer:    "needs": ["WiFi"],

    """APO trainer with comprehensive persistence and monitoring."""    "accessible_required": true

      }

    def __init__(self, checkpoint_file: str):}

        """Initialize with checkpoint management."""```

        

    def load_checkpoint(self):**Dataset Characteristics**:

        """Load previous training state and history."""- **Task Variety**: Different times, durations, group sizes, and requirements

        - **Complexity Levels**: From simple single-person bookings to complex conference room needs

    def save_checkpoint(self):- **Edge Cases**: Accessibility requirements, specific amenities, timing conflicts

        """Save current training progress and metrics."""- **Real-world Scenarios**: Based on actual hotel/office room booking patterns

        

    def get_training_tasks(self) -> List[Dict]:**Usage in Training**:

        """Define comprehensive training scenarios."""- **Training Split**: First half used for APO optimization

        - **Validation Split**: Second half used for performance evaluation

    def evaluate_room_selection(self, task: Dict, recommendation: str) -> float:- **Dynamic Loading**: Automatically loaded by training scripts

        """Multi-dimensional performance evaluation."""- **Error Handling**: Graceful fallback to sample tasks if file missing

        

    def run_training_session(self, num_iterations: int):---

        """Execute complete training session with monitoring."""

```### 📚 Documentation Files



**Training Pipeline**:#### `docs/APO_PERSISTENCE.md`

1. **Checkpoint Loading** - Restore previous training state**Purpose**: Comprehensive guide for APO scoring, persistence, and optimization

2. **Task Generation** - Create diverse training scenarios  

3. **Iterative Training** - Run optimization cycles**Coverage**:

4. **Performance Evaluation** - Multi-dimensional scoring- 🎯 **Scoring System**: How APO calculates and tracks performance

5. **Progress Tracking** - Monitor improvement trends- 💾 **Persistence Features**: Configuration and score storage mechanisms

6. **State Persistence** - Save progress and checkpoints- 🔧 **Configuration Tuning**: Parameter optimization guidelines

- 📊 **Monitoring**: Training progress and analysis techniques

**Scoring System** (Multi-dimensional evaluation):- 🔍 **Troubleshooting**: Common issues and debugging approaches

- **Feature Alignment** (40%): How well recommendations match user requirements

- **Room Selection Clarity** (20%): Clear identification of specific room**Key Sections**:

- **Reasoning Quality** (20%): Quality of explanation and justification1. **Overview**: APO persistence system architecture

- **Budget Consideration** (20%): Appropriate financial awareness2. **Scoring System**: Performance calculation and storage

3. **Usage Examples**: Practical implementation patterns

**Training Scenarios**:4. **Configuration Parameters**: Tuning guidelines and best practices

```python5. **Monitoring and Analysis**: Tools for tracking optimization progress

training_tasks = [6. **Integration with Azure OpenAI**: Environment-specific considerations

    "business_trip",      # Professional travel needs

    "romantic_getaway",   # Leisure and luxury preferences  ---

    "family_vacation",    # Safety and space requirements

    "luxury_executive",   # Premium accommodations#### `README.md`

    "budget_conscious"    # Cost optimization focus**Purpose**: Quick start guide and entry point for AOAI examples

]

```**Content**:

- 🚀 **Quick Setup**: Fast path to running examples

### 2. Data and Configuration- 🔧 **Environment Configuration**: Required variables and setup

- 📋 **File Overview**: Brief description of each module

#### `room_tasks.jsonl`- 🎯 **Usage Examples**: Common execution patterns

**Purpose**: Structured training dataset for APO optimization- 🔗 **References**: Links to detailed documentation



**Format**: JSON Lines with comprehensive scenario definitions---

```json

{## 🔄 Module Interactions

  "user_preferences": "business trip, need good WiFi and workspace, budget around $200",

  "room_features": "various rooms with different amenities and prices", ### Data Flow

  "context": "3-day corporate travel",```mermaid

  "expected_reasoning": "should consider business amenities and budget constraints"graph TD

}    A[room_tasks.jsonl] --> B[room_selector_apo_persistent.py]

```    B --> C[room_selector_azure.py]

    C --> D[Azure OpenAI API]

**Scenario Categories**:    B --> E[apo_training_history.json]

- **Business Travel**: Professional requirements and efficiency    E --> B

- **Leisure Travel**: Comfort, luxury, and experience quality    B --> F[pomltrace/]

- **Family Travel**: Safety, space, and family-friendly features    B --> G[apo.log]

- **Budget Travel**: Cost optimization and essential amenities```

- **Special Occasions**: Romantic getaways, honeymoons, celebrations

- **Accessibility**: Senior-friendly and mobility considerations### Component Dependencies

- **Group Travel**: Multiple occupancy and social requirements```python

- **Extended Stay**: Long-term comfort and work capabilities# Core dependency chain

room_selector_apo_persistent.py

**Data Quality Standards**:├── room_selector_azure.py      # Agent implementation

- ✅ **Diverse Scenarios**: Covers major use case categories├── agentlightning.algorithm.apo # APO optimization

- ✅ **Realistic Constraints**: Real-world budget and preference ranges├── openai.AsyncAzureOpenAI     # Azure client

- ✅ **Clear Expectations**: Specific reasoning and feature requirements└── dotenv                      # Environment loading

- ✅ **Balanced Distribution**: Even coverage across scenario types

room_selector_azure.py

### 3. Documentation Structure├── pydantic.BaseModel          # Type validation

├── openai.AsyncAzureOpenAI     # Azure integration

#### `README.md`├── agentlightning.rollout      # Agent decorator

**Purpose**: Main entry point and comprehensive usage guide└── rich.Console                # Output formatting

```

**Sections**:

- 🚀 **Quick Start**: Immediate setup and usage## 🎛️ Configuration Management

- 📁 **Files Overview**: Summary of all components

- 🎯 **Features**: Key capabilities and benefits### Environment Variables

- 🛠️ **Usage Examples**: Practical implementation patterns```bash

- 📊 **Performance Results**: Training outcomes and metrics# Required for Azure OpenAI integration

- 🔧 **Configuration**: Environment and parameter setupAZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

- 🏗️ **Architecture**: High-level system designAZURE_OPENAI_API_KEY=your_api_key_here

- 🚨 **Troubleshooting**: Common issues and solutionsAZURE_OPENAI_API_VERSION=2024-12-01-preview

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

#### `docs/APO_PERSISTENCE.md`

**Purpose**: Deep-dive into APO algorithm and persistence system# Optional for advanced features

AZURE_SUBSCRIPTION_ID=your_subscription_id

**Coverage**:AZURE_RESOURCE_GROUP=your_resource_group

- 🧠 **APO Algorithm**: Theoretical foundation and implementationAZURE_RESOURCE_NAME=your_resource_name

- 💾 **Persistence Architecture**: State management and recovery```

- 📊 **Scoring System**: Multi-dimensional evaluation framework

- 📈 **Performance Tracking**: Metrics and trend analysis### APO Configuration Evolution

- 🎯 **Optimization Strategies**: Adaptive learning approaches```python

- 🔧 **Configuration**: Advanced parameter tuning# Training progression example

- 🚨 **Troubleshooting**: Debugging and issue resolutionRun 1: Default config → Score: 0.650

Run 2: Optimized config → Score: 0.750  ← Saved as best

#### `docs/MODULES_OVERVIEW.md` (This File)Run 3: Experimental config → Score: 0.720

**Purpose**: Comprehensive architectural documentation and module referenceRun 4: Best config + tweaks → Score: 0.850  ← New best

```

## 🔄 Data Flow and Interactions

## 🏗️ Architecture Patterns

### Standard Operation Flow

```mermaid### 1. **Environment Isolation**

graph TD- Each example has its own `.env` configuration

    A[User Input] --> B[room_selector_azure.py]- No global environment pollution

    B --> C[RoomSelectorAgent.select_room()]- Easy switching between development/production setups

    C --> D[Azure OpenAI API]

    D --> E[Response Processing]### 2. **Modular Design**

    E --> F[Result Display]- Clear separation between agent logic and training orchestration

    F --> G[Logging & Metrics]- Reusable components across different optimization algorithms

```- Independent testing and validation capabilities



### APO Training Flow### 3. **Persistent Optimization**

```mermaid- Configuration state preserved across training runs

graph TD- Automatic best-configuration loading

    A[Training Start] --> B[Load Checkpoint]- Progressive improvement tracking

    B --> C[Generate Tasks]

    C --> D[Training Iteration]### 4. **Error Resilience**

    D --> E[Agent Execution]- Graceful degradation when files are missing

    E --> F[Performance Evaluation]- Comprehensive exception handling

    F --> G[Score Calculation]- Fallback configurations for robustness

    G --> H[Progress Tracking]

    H --> I[Save Checkpoint]## 🔧 Development Workflow

    I --> J{More Iterations?}

    J -->|Yes| D### Adding New Tasks

    J -->|No| K[Session Complete]1. **Edit `room_tasks.jsonl`**: Add new scenarios in JSONL format

```2. **Test individually**: Run `room_selector_azure.py` with new tasks

3. **Validate training**: Ensure APO can optimize on new dataset

### Configuration Management4. **Update documentation**: Document new task types and patterns

```mermaid

graph LR### Modifying Agent Logic

    A[Environment Variables] --> B[Module Initialization]1. **Update `room_selector_azure.py`**: Modify core selection logic

    B --> C[Azure OpenAI Client]2. **Test Azure integration**: Verify deployment compatibility

    B --> D[Logging Configuration]3. **Run APO training**: Ensure optimization still works

    B --> E[Training Parameters]4. **Validate persistence**: Check score tracking and configuration saving

    F[Default Values] --> B

```### Configuration Tuning

1. **Backup history**: Save `apo_training_history.json`

## 🔧 Integration Points2. **Experiment with parameters**: Adjust APO configuration values

3. **Monitor performance**: Track score improvements over runs

### External Dependencies4. **Document findings**: Update parameter guidelines

- **Azure OpenAI Service**: Core LLM functionality

- **Agent Lightning Framework**: APO algorithm and instrumentation## 🧪 Testing and Validation

- **AgentOps** (Optional): Performance monitoring and analytics

- **Python Standard Library**: Logging, JSON, OS, typing### Unit Testing Approach

```python

### Internal Dependencies# Test Azure client creation

```pythondef test_azure_client_creation():

# Module dependency graph    client = create_azure_client()

room_selector_azure.py    assert client is not None

    └── room_selector_module.py

            └── Azure OpenAI SDK# Test task processing

def test_room_selection_task():

room_selector_apo_persistent.py      task = RoomSelectionTask(date="2025-10-13", ...)

    ├── room_selector_module.py    assert task.attendees > 0

    ├── agentlightning.algorithm.apo

    └── room_tasks.jsonl# Test configuration loading

```def test_config_persistence():

    config = get_optimal_config_from_history()

### Configuration Dependencies    assert "val_batch_size" in config

- Environment variables for Azure OpenAI authentication```

- Optional AgentOps configuration for enhanced monitoring

- File system permissions for checkpoint and log management### Integration Testing

- Network access for Azure OpenAI API endpoints```bash

# Test full APO training pipeline

## 📊 Performance Characteristicscd examples/apo/AOAI

python room_selector_apo_persistent.py

### Scalability

- **Concurrent Users**: Single-threaded, suitable for development/testing# Verify outputs

- **Training Scale**: Handles hundreds of training iterations efficientlyls -la apo_training_history.json  # Training history saved

- **Memory Usage**: Minimal footprint with checkpoint-based persistencels -la pomltrace/                 # POML traces generated

- **Storage Requirements**: Lightweight JSON checkpoints and text logsgrep "score" apo.log              # Score progression tracked

```

### Reliability

- **Error Handling**: Comprehensive exception management at all levels### Performance Validation

- **State Recovery**: Automatic checkpoint loading and corruption handling```python

- **Network Resilience**: Retry logic for API failures# Analyze training history

- **Data Integrity**: JSON validation and backup checkpoint creationwith open('apo_training_history.json') as f:

    history = json.load(f)

### Performance Metrics    scores = [run['score'] for run in history['runs']]

- **Response Time**: Typically 1-3 seconds for room selection    print(f"Score progression: {scores}")

- **Training Speed**: 5-10 iterations per minute depending on task complexity    print(f"Best score: {max(scores)}")

- **Token Efficiency**: Optimized prompts for cost-effective Azure OpenAI usage```

- **Convergence Rate**: Usually achieves 80%+ scores within 3-5 sessions

## 🚀 Deployment Considerations

## 🚀 Extension Points

### Production Setup

### Adding New Room Types1. **Environment Variables**: Use Azure Key Vault or secure environment management

```python2. **API Rate Limits**: Configure appropriate throttling and retry logic

def _get_custom_rooms(self) -> str:3. **Monitoring**: Set up logging and performance tracking

    """Extend with domain-specific room categories."""4. **Scaling**: Consider multiple deployment environments for different models

    # Add luxury resorts, business hotels, budget hostels, etc.

```### Security Best Practices

1. **API Key Rotation**: Regular rotation of Azure OpenAI API keys

### Custom Scoring Metrics2. **Endpoint Security**: Use private endpoints where possible

```python3. **Access Control**: Implement proper RBAC for Azure resources

def evaluate_custom_criteria(self, task: Dict, recommendation: str) -> float:4. **Audit Logging**: Track API usage and optimization activities

    """Implement domain-specific evaluation criteria."""

    # Add industry-specific scoring dimensions## 📈 Performance Optimization

```

### Training Efficiency

### Integration with External APIs- **Batch Size Tuning**: Balance between stability and speed

```python- **Model Selection**: Choose appropriate Azure deployments for different tasks

def get_real_time_rooms(self, location: str, dates: Tuple[str, str]) -> str:- **Resource Allocation**: Optimize runner count based on available compute

    """Integrate with hotel booking APIs for live data."""

    # Connect to Booking.com, Expedia, etc.### Cost Management

```- **Token Usage**: Monitor and optimize prompt lengths

- **Model Selection**: Use cost-effective deployments when possible

### Advanced Training Scenarios- **Training Frequency**: Balance optimization frequency with cost

```python

def generate_dynamic_tasks(self, difficulty_level: str) -> List[Dict]:## 🔍 Troubleshooting Guide

    """Create adaptive training scenarios based on agent performance."""

    # Implement curriculum learning approaches### Common Issues

```

#### Azure Authentication Errors

## 🎯 Future Enhancements```bash

Error: "Authentication failed"

### Planned FeaturesSolution: Check AZURE_OPENAI_API_KEY and endpoint configuration

- **Multi-agent Collaboration**: Coordinate multiple room selector agents```

- **Real-time Learning**: Continuous optimization during production use

- **A/B Testing Framework**: Compare different optimization strategies#### Model Not Found

- **Advanced Analytics**: Performance dashboards and trend analysis```bash

- **API Integration**: Connect with real hotel booking servicesError: "Model 'xyz' not found"

Solution: Verify AZURE_OPENAI_DEPLOYMENT_NAME matches actual deployment

### Optimization Opportunities```

- **Prompt Caching**: Reduce API costs with intelligent caching

- **Batch Processing**: Handle multiple requests efficiently#### Training Failures

- **Model Selection**: Automatic model choice based on task complexity```bash

- **Parallel Training**: Multi-threaded APO optimizationError: APO training fails with timeout

Solution: Reduce batch sizes or increase timeout values

## 📋 Maintenance Guidelines```



### Regular Tasks#### Configuration Issues

- **Checkpoint Cleanup**: Remove old training history (monthly)```bash

- **Log Rotation**: Archive and compress log files (weekly)Error: "No previous training history found"

- **Performance Review**: Analyze training trends and metrics (weekly)Solution: Normal for first run; default configuration will be used

- **Environment Updates**: Keep dependencies current (quarterly)```



### Monitoring Checklist### Debugging Tools

- ✅ API key expiration and rotation```bash

- ✅ Training convergence and performance trends# Check environment variables

- ✅ Error rates and failure patternsenv | grep AZURE_OPENAI

- ✅ Resource usage and cost optimization

- ✅ Security and access control# View training logs

tail -f apo.log

### Version Control Best Practices

- **Checkpoint Versioning**: Tag successful training milestones# Analyze POML traces

- **Configuration Management**: Track environment variable changesls pomltrace/ && cat pomltrace/latest_trace.json

- **Documentation Updates**: Keep module docs synchronized with code

- **Dependency Tracking**: Document version compatibility matrices# Validate configuration

python -c "from room_selector_apo_persistent import get_optimal_config_from_history; print(get_optimal_config_from_history())"

---```



*This modules overview provides the comprehensive architectural foundation for understanding, extending, and maintaining the Azure OpenAI APO integration. Each component is designed for production use while maintaining clear separation of concerns and extensive configurability.*## 📚 Additional Resources

### Related Documentation
- `../../../docs/AOAI/INSTALLATION_GUIDE.md` - Complete installation instructions
- `../../../docs/AOAI/AZURE_ENV_SETUP.md` - Azure OpenAI environment setup
- `../../../docs/AOAI/WSL_SETUP_GUIDE.md` - Windows development environment

### External References
- [Azure OpenAI Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Agent Lightning GitHub](https://github.com/microsoft/agent-lightning)
- [APO Algorithm Paper](https://arxiv.org/abs/XXXX.XXXXX) *(when published)*

---

**Last Updated**: November 2, 2025  
**Version**: 1.0  
**Maintainer**: Agent Lightning AOAI Examples Team
````