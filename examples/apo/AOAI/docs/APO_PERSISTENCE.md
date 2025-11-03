# APO Persistence and Scoring System

This document provides a comprehensive guide to the APO (Automatic Prompt Optimization) persistence system and scoring mechanisms used in the Azure OpenAI room selector agent.

## � Environment Setup and Testing

### Development Environment Preparation

#### 1. Conda Environment Activation
```bash
# Ensure you're using the correct conda environment
conda activate torchfix  # or your Agent Lightning environment

# Verify environment setup
conda list | grep -E "(agentlightning|torch|openai)" 
python -c "import agentlightning, torch; print('✅ Environment ready')"
```

#### 2. Azure OpenAI Configuration
```bash
# Navigate to working directory
cd examples/apo/AOAI

# Configure environment variables
export AZURE_OPENAI_API_KEY="your_api_key"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o-mini"
export AZURE_OPENAI_API_VERSION="2024-02-15-preview"

# Test connection
python -c "
from openai import AzureOpenAI
import os
client = AzureOpenAI(
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
)
print('✅ Azure OpenAI connection verified')
"
```

### APO Training Environment Testing

#### 1. Persistence System Validation
```bash
# Test checkpoint loading/saving
python -c "
from room_selector_apo_persistent import PersistentAPOTrainer
trainer = PersistentAPOTrainer('test_checkpoint.json')

# Test save operation
trainer.training_history = [{'test': 'data'}]
trainer.save_checkpoint()
print('✅ Checkpoint save test passed')

# Test load operation  
trainer.load_checkpoint()
print('✅ Checkpoint load test passed')
print(f'History loaded: {len(trainer.training_history)} entries')
"
```

#### 2. Scoring System Validation
```bash
# Test scoring algorithm
python -c "
from room_selector_apo_persistent import PersistentAPOTrainer
trainer = PersistentAPOTrainer()

# Test scoring with sample data
task = {
    'id': 'test_business',
    'expected_features': ['wifi', 'workspace', 'budget']
}
recommendation = 'I recommend the Business Room with excellent WiFi, dedicated workspace, and fits your budget perfectly.'

score = trainer.evaluate_room_selection(task, recommendation)
print(f'✅ Scoring test completed: {score:.2f}')
print('Expected score: 0.8-1.0 for good recommendation')
"
```

#### 3. Training Pipeline Testing
```bash
# Run minimal training session
python -c "
from room_selector_apo_persistent import PersistentAPOTrainer
trainer = PersistentAPOTrainer('test_training.json')

print('🧪 Running test training session...')
trainer.run_training_session(num_iterations=1)
print('✅ Training pipeline test completed')
"
```

### Performance Monitoring

#### Training Metrics Validation
```bash
# Monitor training performance
python -c "
import json
import os

if os.path.exists('apo_training_history.json'):
    with open('apo_training_history.json', 'r') as f:
        data = json.load(f)
    
    print('📊 Training History Analysis:')
    print(f'Total sessions: {len(data.get(\"history\", []))}')
    print(f'Best score: {data.get(\"best_score\", 0):.2f}')
    
    if data.get('history'):
        recent = data['history'][-1]
        print(f'Latest session score: {recent.get(\"average_score\", 0):.2f}')
        print(f'Latest duration: {recent.get(\"duration_seconds\", 0):.1f}s')
else:
    print('No training history found. Run training first.')
"
```

---

APO (Automatic Prompt Optimization) is Agent Lightning's sophisticated algorithm for automatically improving prompts through iterative optimization. It learns from performance feedback to enhance agent responses over time.

### Key Features
- **Automatic Optimization**: Continuously improves prompts based on performance metrics
- **Persistent State**: Saves and loads optimization progress across sessions
- **Multi-dimensional Scoring**: Evaluates multiple aspects of agent performance
- **Adaptive Learning**: Adjusts optimization strategies based on task patterns

## 💾 Persistence Architecture

### Training History Management
The persistence system maintains comprehensive training history with the following structure:

```json
{
  "history": [
    {
      "timestamp": "2024-11-02T15:30:00",
      "duration_seconds": 45.2,
      "iterations": 5,
      "scores": [0.85, 0.87, 0.89, 0.92, 0.94],
      "average_score": 0.894,
      "best_score_updated": true,
      "task_count": 5
    }
  ],
  "best_score": 0.94,
  "last_updated": "2024-11-02T15:30:45",
  "total_sessions": 12
}
```

### Checkpoint Files
- **`apo_training_history.json`** - Main persistence file
- **`apo.log`** - Detailed training logs
- **`agentops.log`** - AgentOps integration logs
- **`pomltrace/`** - POML trace files for debugging

### State Recovery
The system automatically recovers from interruptions:
```python
def load_checkpoint(self):
    """Load training history from checkpoint file."""
    if os.path.exists(self.checkpoint_file):
        with open(self.checkpoint_file, 'r') as f:
            data = json.load(f)
            self.training_history = data.get('history', [])
            self.current_best_score = data.get('best_score', 0.0)
```

## 📊 Scoring System

### Multi-dimensional Evaluation
The scoring system evaluates agent performance across four key dimensions:

#### 1. Feature Alignment (40% weight)
Measures how well the recommendation addresses user requirements:
```python
def evaluate_feature_alignment(self, task, recommendation):
    feature_score = 0.0
    for feature in task["expected_features"]:
        if feature.lower() in recommendation.lower():
            feature_score += 1.0
    return min(feature_score / len(task["expected_features"]), 1.0)
```

**Scoring criteria:**
- ✅ **1.0**: All expected features mentioned
- ⚠️ **0.75**: Most features addressed  
- ❌ **0.5**: Some features missing
- 🚫 **0.0**: Major features ignored

#### 2. Room Selection Clarity (20% weight)
Evaluates whether a specific room was clearly recommended:
```python
room_indicators = ["room", "suite", "deluxe", "standard", "penthouse", "business"]
if any(indicator in recommendation.lower() for indicator in room_indicators):
    score += 0.2
```

**Examples:**
- ✅ "I recommend the Ocean View Deluxe Room"
- ✅ "The Business Suite would be perfect"
- ❌ "You might want to consider various options"

#### 3. Reasoning Quality (20% weight)
Assesses the quality of explanation provided:
```python
reasoning_indicators = ["because", "since", "due to", "reason", "suitable", "ideal"]
if any(indicator in recommendation.lower() for indicator in reasoning_indicators):
    score += 0.2
```

**Quality levels:**
- ✅ **High**: Clear cause-and-effect reasoning
- ⚠️ **Medium**: Basic justification provided
- ❌ **Low**: Minimal or unclear reasoning

#### 4. Budget Consideration (20% weight)
Evaluates financial awareness and budget alignment:
```python
budget_indicators = ["budget", "cost", "price", "$", "affordable", "expensive"]
if any(indicator in recommendation.lower() for indicator in budget_indicators):
    score += 0.2
```

### Scoring Examples

#### Excellent Response (Score: 0.95)
```
User: "Business trip, need WiFi and workspace, budget $200-250"
Agent: "I recommend the Business Room ($200/night) because it perfectly matches 
your requirements with fast WiFi, dedicated workspace, and falls within your 
budget range. The room also includes meeting room credits ideal for business travelers."
```

**Score breakdown:**
- Feature alignment: 1.0 (WiFi ✓, workspace ✓, budget ✓)
- Room clarity: 0.2 (Business Room clearly specified)
- Reasoning: 0.2 ("because it perfectly matches...")
- Budget: 0.2 (specific price mentioned)
- **Total: 0.95**

#### Poor Response (Score: 0.35)
```
User: "Romantic getaway, ocean view, budget flexible up to $400"
Agent: "There are several rooms available. You might like some of them."
```

**Score breakdown:**
- Feature alignment: 0.0 (no features addressed)
- Room clarity: 0.0 (no specific room)
- Reasoning: 0.0 (no reasoning provided)
- Budget: 0.0 (no budget consideration)
- **Total: 0.0**

## 📈 Performance Tracking

### Training Metrics
The system tracks multiple performance indicators:

#### Session-level Metrics
- **Average Score**: Mean performance across all tasks in a session
- **Score Variance**: Consistency of performance
- **Duration**: Time taken for optimization
- **Iteration Count**: Number of optimization rounds

#### Historical Metrics
- **Best Score Ever**: Highest score achieved across all sessions
- **Improvement Trend**: Performance trajectory over time
- **Session Success Rate**: Percentage of successful training sessions
- **Convergence Rate**: Speed of optimization convergence

### Performance Visualization
```python
def print_training_history(self):
    """Print complete training history with trends."""
    recent_scores = [s['average_score'] for s in self.training_history[-5:]]
    trend = "📈" if recent_scores[-1] > recent_scores[0] else "📉"
    print(f"Recent trend: {trend} (last 5 sessions)")
```

## 🎯 Optimization Strategies

### Adaptive Learning
The APO system adapts its optimization strategy based on:

#### Performance Patterns
- **High Variance**: Focus on consistency improvements
- **Low Scores**: Emphasize fundamental capability enhancement
- **Plateau**: Introduce exploration to escape local optima

#### Task-specific Optimization
Different room selection scenarios require different optimization approaches:

**Business Travel Tasks**
- Priority: Feature alignment and practical considerations
- Weight: Efficiency and professional amenities

**Leisure Travel Tasks**  
- Priority: Experience quality and preference matching
- Weight: Emotional satisfaction and luxury features

**Budget-focused Tasks**
- Priority: Cost optimization and value delivery
- Weight: Price sensitivity and essential features

### Learning Rate Adaptation
```python
def calculate_learning_rate(self, performance_history):
    """Adapt learning rate based on recent performance."""
    if len(performance_history) < 3:
        return 0.1  # Default rate for new training
    
    recent_improvement = performance_history[-1] - performance_history[-3]
    if recent_improvement > 0.05:
        return 0.15  # Increase rate for good progress
    elif recent_improvement < -0.02:
        return 0.05  # Decrease rate for regression
    else:
        return 0.1   # Maintain current rate
```

## 🔧 Configuration Options

### Training Parameters
```python
class APOConfig:
    """Configuration for APO training parameters."""
    
    # Training session settings
    ITERATIONS_PER_SESSION = 5
    MAX_SESSIONS = 50
    CONVERGENCE_THRESHOLD = 0.95
    
    # Scoring weights
    FEATURE_WEIGHT = 0.4
    CLARITY_WEIGHT = 0.2
    REASONING_WEIGHT = 0.2
    BUDGET_WEIGHT = 0.2
    
    # Persistence settings
    CHECKPOINT_INTERVAL = 1  # Save after each session
    MAX_HISTORY_SIZE = 100   # Keep last 100 sessions
    BACKUP_ENABLED = True    # Create backup checkpoints
```

### Environment Variables
```bash
# APO Training Configuration
APO_CHECKPOINT_FILE=apo_training_history.json
APO_LOG_LEVEL=INFO
APO_MAX_ITERATIONS=10
APO_CONVERGENCE_THRESHOLD=0.90

# Performance Monitoring
ENABLE_AGENTOPS=true
AGENTOPS_API_KEY=your_agentops_key
PERFORMANCE_TRACKING=detailed
```

## 🚨 Troubleshooting

### Common Issues

#### Low Scores Persisting
**Symptoms**: Scores remain below 0.5 after multiple sessions
**Solutions**:
1. Review task expectations vs agent capabilities
2. Adjust scoring weights for specific domain
3. Examine training data quality
4. Consider prompt engineering refinements

#### Training Not Converging
**Symptoms**: High variance in scores, no clear improvement trend
**Solutions**:
1. Reduce learning rate for stability
2. Increase iterations per session
3. Review task diversity and complexity
4. Check for data quality issues

#### Checkpoint Corruption
**Symptoms**: Training history lost or inconsistent
**Solutions**:
1. Enable automatic backups
2. Validate JSON structure regularly
3. Implement checkpoint verification
4. Use versioned checkpoint files

### Debugging Tools

#### Trace Analysis
```python
def analyze_training_traces(self):
    """Analyze POML traces for optimization insights."""
    trace_files = glob.glob("pomltrace/*.poml")
    for trace_file in trace_files:
        # Analyze prompt evolution and performance correlation
        pass
```

#### Performance Profiling
```python
def profile_training_session(self):
    """Profile training performance and identify bottlenecks."""
    import cProfile
    profiler = cProfile.Profile()
    profiler.enable()
    # Run training session
    profiler.disable()
    profiler.print_stats()
```

## 🎓 Best Practices

### Training Strategy
1. **Start Simple**: Begin with clear, unambiguous tasks
2. **Gradual Complexity**: Introduce edge cases progressively  
3. **Regular Checkpoints**: Save progress frequently
4. **Monitor Trends**: Track performance patterns over time
5. **Validate Results**: Test optimized prompts on unseen data

### Scoring Design
1. **Balanced Weights**: Ensure no single dimension dominates
2. **Clear Criteria**: Define measurable success indicators
3. **Domain Alignment**: Match scoring to business objectives
4. **Regular Review**: Update criteria based on performance insights

### Persistence Management
1. **Backup Strategy**: Maintain multiple checkpoint versions
2. **Cleanup Policy**: Remove old traces and logs regularly
3. **Monitoring**: Track checkpoint file sizes and integrity
4. **Recovery Plan**: Test restoration procedures regularly

## 📚 References

- [Agent Lightning APO Documentation](../../docs/algorithm-zoo/apo.md)
- [Azure OpenAI Best Practices](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [POML Trace Format Specification](../../docs/deep-dive/traces.md)
- [AgentOps Integration Guide](../../docs/reference/instrumentation.md)

---

*This persistence system provides the foundation for continuous improvement in AI agent performance, enabling sophisticated optimization strategies while maintaining comprehensive training history and robust error recovery capabilities.*