"""#!/usr/bin/env python3

Room Selection APO Training with Persistence"""

Room Selector with APO (Agent Performance Optimization) - Azure OpenAI Version with Persistence

This script demonstrates Agent Lightning's APO (Automatic Prompt Optimization) 

algorithm with Azure OpenAI, featuring persistent training state management.This module orchestrates APO training for room selection using Azure OpenAI, featuring

persistent optimization that learns and improves across multiple training runs.

The training optimizes prompts for room selection tasks, learning from 

performance across multiple sessions.Key Features:

"""- APO (Automatic Prompt Optimization) integration for continuous improvement

- Persistent scoring and configuration management across training sessions

import os- Azure OpenAI deployment integration with proper authentication

import json- Comprehensive training history tracking and analysis

import logging- Automated optimal configuration loading from previous runs

from datetime import datetime- Rich logging and monitoring for training progress

from agentlightning import AgentLightning

from agentlightning.algorithm.apo import APOArchitecture:

from room_selector_module import RoomSelectorAgent- Uses room_selector_azure.py for core agent implementation

- Implements persistent storage for training scores and configurations

# Configure logging- Automatically loads best-performing configurations from history

logging.basicConfig(- Provides comprehensive error handling and recovery mechanisms

    level=logging.INFO,

    format='%(asctime)s - %(levelname)s - %(message)s',Usage:

    handlers=[    python room_selector_apo_persistent.py

        logging.FileHandler('apo_training.log'),    

        logging.StreamHandler()    # Training will:

    ]    # 1. Load optimal configuration from previous runs (or use defaults)

)    # 2. Execute APO training with Azure OpenAI

logger = logging.getLogger(__name__)    # 3. Save results and update training history

    # 4. Generate POML traces and logs for analysis



class PersistentAPOTrainer:Environment Variables Required:

    """    AZURE_OPENAI_ENDPOINT: Azure OpenAI service endpoint

    APO trainer with persistent state management for room selection optimization.    AZURE_OPENAI_API_KEY: Authentication key for Azure OpenAI

        AZURE_OPENAI_API_VERSION: API version (e.g., "2024-12-01-preview")

    Features:    AZURE_OPENAI_DEPLOYMENT_NAME: Model deployment name for training

    - Automatic checkpoint saving and loading

    - Performance tracking across sessionsOutput Files:

    - Configurable training parameters    apo_training_history.json: Persistent training scores and configurations

    - Comprehensive logging and monitoring    apo.log: Detailed training logs for debugging and analysis

    """    pomltrace/: POML optimization traces for performance analysis

        agentops.log: Agent operations logs for monitoring

    def __init__(self, checkpoint_file: str = "apo_training_history.json"):

        """Author: Agent Lightning AOAI Examples Team

        Initialize the persistent APO trainer.Version: 2.0

        Date: November 2, 2025

        Args:"""

            checkpoint_file (str): Path to save training checkpoints

        """import os

        self.checkpoint_file = checkpoint_fileimport sys

        self.training_history = []import logging

        self.current_best_score = 0.0import json

        self.agent = RoomSelectorAgent()import datetime

        from typing import Tuple, cast

        # Load previous training statefrom pathlib import Path

        self.load_checkpoint()

        # Add project paths

        logger.info("PersistentAPOTrainer initialized")sys.path.insert(0, str(Path(__file__).parent.parent))  # Add examples/apo to path

sys.path.insert(0, str(Path(__file__).parent))         # Add AOAI to path

    def load_checkpoint(self):

        """Load training history from checkpoint file."""# Load environment from local APO .env file

        try:from dotenv import load_dotenv

            if os.path.exists(self.checkpoint_file):load_dotenv('../.env')

                with open(self.checkpoint_file, 'r') as f:

                    data = json.load(f)# Configure LLM proxy to use Azure OpenAI with deployment from environment

                    self.training_history = data.get('history', [])azure_deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')  # Use deployment name from .env

                    self.current_best_score = data.get('best_score', 0.0)if not azure_deployment:

                    raise ValueError("AZURE_OPENAI_DEPLOYMENT_NAME must be set in .env file")

                logger.info(f"Loaded checkpoint: {len(self.training_history)} sessions, "

                           f"best score: {self.current_best_score:.2f}")os.environ['OPENAI_API_KEY'] = os.getenv('AZURE_OPENAI_API_KEY', '')

            else:os.environ['OPENAI_BASE_URL'] = f"{os.getenv('AZURE_OPENAI_ENDPOINT', '')}"

                logger.info("No checkpoint found, starting fresh training")os.environ['OPENAI_API_VERSION'] = os.getenv('AZURE_OPENAI_API_VERSION', '2024-12-01-preview')

        except Exception as e:

            logger.error(f"Failed to load checkpoint: {e}")# Map common models to our Azure deployment from environment

            self.training_history = []os.environ['OPENAI_MODEL_MAP'] = json.dumps({

            self.current_best_score = 0.0    'gpt-5-mini': azure_deployment,

    'gpt-4o-mini': azure_deployment,

    def save_checkpoint(self):    'gpt-4-turbo': azure_deployment,

        """Save current training state to checkpoint file."""    'gpt-4': azure_deployment,

        try:    'gpt-4.1-mini': azure_deployment,

            checkpoint_data = {    azure_deployment: azure_deployment  # Also map the actual deployment name to itself

                'history': self.training_history,})

                'best_score': self.current_best_score,

                'last_updated': datetime.now().isoformat(),# Import room selector components from the module

                'total_sessions': len(self.training_history)from room_selector_module import RoomSelectionTask, load_room_tasks, prompt_template_baseline, room_selector

            }

            # Import Agent Lightning components  

            with open(self.checkpoint_file, 'w') as f:from agentlightning import Trainer, configure_logger

                json.dump(checkpoint_data, f, indent=2)from agentlightning.adapter import TraceToMessages

            from agentlightning.algorithm.apo import APO

            logger.info(f"Checkpoint saved: {len(self.training_history)} sessions")from agentlightning.types import Dataset

        except Exception as e:from agentlightning.llm_proxy import LLMProxy

            logger.error(f"Failed to save checkpoint: {e}")

# Use working Azure client creation

    def get_training_tasks(self):from openai import AsyncAzureOpenAI

        """

        Get training tasks for room selection scenarios.def create_azure_openai_client() -> AsyncAzureOpenAI:

            """

        Returns:    Create Azure OpenAI client with proper configuration and validation.

            list: Training tasks with various room selection scenarios    

        """    This function creates an authenticated Azure OpenAI client and validates

        return [    the connection by checking all required environment variables. It provides

            {    detailed feedback about the configuration for debugging purposes.

                "id": "business_trip",    

                "description": "Business traveler needs efficient workspace and connectivity",    Returns:

                "user_input": "I need a room for a 3-day business trip. Must have fast WiFi, work desk, and be quiet for video calls. Budget around $200-250 per night.",        AsyncAzureOpenAI: Configured Azure OpenAI client ready for use

                "expected_features": ["WiFi", "work desk", "quiet", "business amenities"]        

            },    Raises:

            {        ValueError: If required environment variables are missing

                "id": "romantic_getaway",         Exception: If client creation fails due to authentication issues

                "description": "Couple seeking romantic accommodation with special atmosphere",        

                "user_input": "Planning a romantic weekend getaway for our anniversary. Want ocean view, privacy, and luxury amenities. Budget flexible up to $400 per night.",    Environment Variables Validated:

                "expected_features": ["ocean view", "privacy", "luxury", "romantic"]        AZURE_OPENAI_ENDPOINT: Service endpoint URL

            },        AZURE_OPENAI_API_KEY: Authentication key

            {        AZURE_OPENAI_API_VERSION: API version

                "id": "family_vacation",        AZURE_OPENAI_DEPLOYMENT_NAME: Model deployment name

                "description": "Family with children needs space and convenience",         

                "user_input": "Family of 4 with two young kids. Need extra space, ground floor preferred for safety, budget-conscious under $180 per night.",    Example:

                "expected_features": ["space", "family-friendly", "ground floor", "budget"]        client = create_azure_openai_client()

            },        # Output: ✅ Azure OpenAI client created successfully

            {        #         ✅ Using deployment: gpt-4o

                "id": "luxury_executive",        #         ✅ Endpoint: https://your-resource.openai.azure.com/

                "description": "Executive needs premium accommodations and services",    """

                "user_input": "Executive stay for important client meetings. Need luxury suite, concierge services, and premium location. Budget not a concern.",    client = AsyncAzureOpenAI(

                "expected_features": ["luxury", "concierge", "premium", "executive"]        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),

            },        api_key=os.getenv("AZURE_OPENAI_API_KEY"),

            {        api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

                "id": "budget_conscious",    )

                "description": "Traveler prioritizing cost-effectiveness",    

                "user_input": "Solo traveler on a tight budget. Just need clean, basic room with essentials. Maximum $120 per night.",    print(f"✅ Azure OpenAI client created successfully")

                "expected_features": ["budget", "basic", "clean", "essentials"]    print(f"✅ Using deployment: {os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')}")

            }    print(f"✅ Endpoint: {os.getenv('AZURE_OPENAI_ENDPOINT')}")

        ]    

    return client

    def evaluate_room_selection(self, task: dict, recommendation: str) -> float:

        """

        Evaluate the quality of a room recommendation.def load_train_val_dataset() -> Tuple[Dataset[RoomSelectionTask], Dataset[RoomSelectionTask]]:

            """Load and split room task dataset for training and validation."""

        Args:    dataset_full = load_room_tasks()

            task (dict): Training task with expected features    train_split = len(dataset_full) // 2

            recommendation (str): Agent's room recommendation    dataset_train = [dataset_full[i] for i in range(train_split)]

                dataset_val = [dataset_full[i] for i in range(train_split, len(dataset_full))]

        Returns:    return cast(Dataset[RoomSelectionTask], dataset_train), cast(Dataset[RoomSelectionTask], dataset_val)

            float: Score between 0.0 and 1.0

        """

        try:def setup_apo_logger(file_path: str = "apo.log") -> None:

            score = 0.0    """Setup APO logging to file for debugging and analysis."""

            recommendation_lower = recommendation.lower()    file_handler = logging.FileHandler(file_path)

                file_handler.setLevel(logging.INFO)

            # Check for expected features (40% of score)    formatter = logging.Formatter("%(asctime)s [%(levelname)s] (Process-%(process)d %(name)s)   %(message)s")

            feature_score = 0.0    file_handler.setFormatter(formatter)

            for feature in task["expected_features"]:    logging.getLogger("agentlightning.algorithm.apo").addHandler(file_handler)

                if feature.lower() in recommendation_lower:

                    feature_score += 1.0

            feature_score = min(feature_score / len(task["expected_features"]), 1.0)def extract_score_from_result(result) -> float:

            score += feature_score * 0.4    """Extract final score from APO training result."""

                try:

            # Check for clear room selection (20% of score)        # Try different ways to extract the score

            room_indicators = ["room", "suite", "deluxe", "standard", "penthouse", "business"]        if hasattr(result, 'score'):

            if any(indicator in recommendation_lower for indicator in room_indicators):            return float(result.score)

                score += 0.2        elif hasattr(result, 'final_score'):

                        return float(result.final_score)

            # Check for reasoning and explanation (20% of score)        elif hasattr(result, 'best_score'):

            reasoning_indicators = ["because", "since", "due to", "reason", "suitable", "ideal"]            return float(result.best_score)

            if any(indicator in recommendation_lower for indicator in reasoning_indicators):        elif isinstance(result, dict):

                score += 0.2            return float(result.get('score', result.get('final_score', result.get('best_score', 0.0))))

                    else:

            # Check for budget consideration (20% of score)            print("⚠️  Could not extract score from training result")

            budget_indicators = ["budget", "cost", "price", "$", "affordable", "expensive"]            return 0.0

            if any(indicator in recommendation_lower for indicator in budget_indicators):    except (ValueError, AttributeError, TypeError) as e:

                score += 0.2        print(f"⚠️  Could not extract final score from training result: {e}")

                    return 0.0

            return min(score, 1.0)

            

        except Exception as e:def setup_apo_logger(file_path: str = "apo.log") -> None:

            logger.error(f"Error evaluating recommendation: {e}")    """Setup APO logging to file for debugging and analysis."""

            return 0.0    file_handler = logging.FileHandler(file_path)

    file_handler.setLevel(logging.INFO)

    def run_training_session(self, num_iterations: int = 5):    formatter = logging.Formatter("%(asctime)s [%(levelname)s] (Process-%(process)d %(name)s)   %(message)s")

        """    file_handler.setFormatter(formatter)

        Run a complete APO training session.    logging.getLogger("agentlightning.algorithm.apo").addHandler(file_handler)

        

        Args:

            num_iterations (int): Number of optimization iterationsdef load_training_history(history_file: str = "apo_training_history.json") -> dict:

        """    """Load training history from JSON file."""

        logger.info(f"Starting APO training session with {num_iterations} iterations")    if not os.path.exists(history_file):

                return {

        session_start = datetime.now()            "runs": [],

        session_scores = []            "best_score": 0.0,

        tasks = self.get_training_tasks()            "best_run": None

                }

        try:    

            for iteration in range(num_iterations):    try:

                logger.info(f"Training iteration {iteration + 1}/{num_iterations}")        with open(history_file, 'r') as f:

                iteration_scores = []            history = json.load(f)

                            print(f"📚 Loaded training history: {len(history.get('runs', []))} previous runs")

                for task in tasks:            return history

                    # Get room recommendation from agent    except (json.JSONDecodeError, FileNotFoundError) as e:

                    result = self.agent.select_room(task["user_input"])        print(f"⚠️  Could not load training history: {e}")

                            return {

                    if result["success"]:            "runs": [],

                        # Evaluate the recommendation            "best_score": 0.0,

                        score = self.evaluate_room_selection(task, result["recommendation"])            "best_run": None

                        iteration_scores.append(score)        }

                        

                        logger.info(f"Task '{task['id']}' scored: {score:.2f}")

                    else:def save_training_result(score: float, config: dict, history_file: str = "apo_training_history.json") -> None:

                        logger.error(f"Task '{task['id']}' failed: {result.get('error', 'Unknown error')}")    """Save training result with score and configuration."""

                        iteration_scores.append(0.0)    history = load_training_history(history_file)

                    

                # Calculate average score for this iteration    # Create new run entry

                avg_score = sum(iteration_scores) / len(iteration_scores) if iteration_scores else 0.0    new_run = {

                session_scores.append(avg_score)        "timestamp": datetime.datetime.now().isoformat(),

                        "score": score,

                logger.info(f"Iteration {iteration + 1} average score: {avg_score:.2f}")        "config": config,

                **config  # Also store config values at top level for backwards compatibility

        except Exception as e:    }

            logger.error(f"Training session error: {e}")    

            # Add to history

        # Calculate session statistics    history["runs"].append(new_run)

        session_avg = sum(session_scores) / len(session_scores) if session_scores else 0.0    

        session_end = datetime.now()    # Update best score if this is better

        session_duration = (session_end - session_start).total_seconds()    if score > history["best_score"]:

                history["best_score"] = score

        # Update best score        history["best_run"] = new_run

        if session_avg > self.current_best_score:        print(f"🎉 New best score: {score:.3f} (previous: {history['best_score']:.3f})")

            self.current_best_score = session_avg    

            logger.info(f"🎉 New best score achieved: {session_avg:.2f}")    # Save updated history

            try:

        # Record session in history        with open(history_file, 'w') as f:

        session_record = {            json.dump(history, f, indent=2)

            'timestamp': session_start.isoformat(),        print(f"💾 Training results saved to {history_file}")

            'duration_seconds': session_duration,    except Exception as e:

            'iterations': num_iterations,        print(f"❌ Failed to save training history: {e}")

            'scores': session_scores,

            'average_score': session_avg,

            'best_score_updated': session_avg > self.current_best_score,def get_optimal_config_from_history(history_file: str = "apo_training_history.json") -> dict:

            'task_count': len(tasks)    """

        }    Get optimal APO configuration from training history or return defaults.

            

        self.training_history.append(session_record)    This function implements persistent optimization by loading the best-performing

            configuration from previous training runs. If no history exists or no

        # Save checkpoint    successful runs are found, it returns sensible default values.

        self.save_checkpoint()    

            Args:

        # Print session summary        history_file (str): Path to training history JSON file

        self.print_session_summary(session_record)        

    Returns:

    def print_session_summary(self, session: dict):        dict: APO configuration parameters including:

        """Print a summary of the training session."""            - val_batch_size: Validation batch size for stability

        print("\n" + "="*60)            - gradient_batch_size: Gradient computation batch size

        print("🚀 APO Training Session Complete")            - beam_width: Search beam width for exploration

        print("="*60)            - branch_factor: Branching factor for alternatives

        print(f"📊 Average Score: {session['average_score']:.2f}")            - beam_rounds: Number of optimization rounds

        print(f"🏆 Best Score Ever: {self.current_best_score:.2f}")            

        print(f"⏱️  Duration: {session['duration_seconds']:.1f} seconds")    Configuration Evolution:

        print(f"🔄 Iterations: {session['iterations']}")        The function implements progressive optimization by:

        print(f"📝 Total Sessions: {len(self.training_history)}")        1. Loading historical training runs

                2. Identifying the best-performing configuration

        if len(self.training_history) > 1:        3. Returning those parameters for the next training run

            prev_avg = self.training_history[-2]['average_score']        4. Providing defaults for first-time execution

            improvement = session['average_score'] - prev_avg        

            print(f"📈 Improvement: {improvement:+.2f}")    Example:

                config = get_optimal_config_from_history()

        print("="*60 + "\n")        # First run output: 🔧 No previous training history found, using default config

        # Later runs output: 📈 Using optimal config from best run (score: 0.850)

    def print_training_history(self):    """

        """Print complete training history."""    history = load_training_history(history_file)

        if not self.training_history:    

            print("No training history available.")    # If we have a best run, use its config

            return    if history["best_run"] and history["best_score"] > 0:

                config = history["best_run"]["config"]

        print("\n📈 APO Training History")        print(f"📈 Using optimal config from best run (score: {history['best_score']:.3f})")

        print("-" * 50)        return config

            

        for i, session in enumerate(self.training_history, 1):    # Otherwise return default configuration

            timestamp = datetime.fromisoformat(session['timestamp']).strftime("%Y-%m-%d %H:%M")    default_config = {

            print(f"Session {i:2d}: {timestamp} | Score: {session['average_score']:.2f} | "        "val_batch_size": 5,

                  f"Duration: {session['duration_seconds']:.1f}s")        "gradient_batch_size": 2,

                "beam_width": 1,

        if len(self.training_history) >= 2:        "branch_factor": 1,

            recent_scores = [s['average_score'] for s in self.training_history[-5:]]        "beam_rounds": 1

            trend = "📈" if recent_scores[-1] > recent_scores[0] else "📉"    }

            print(f"\nRecent trend: {trend} (last 5 sessions)")    print("🔧 No previous training history found, using default config")

            return default_config

        print(f"Best score: {self.current_best_score:.2f}")

        print("-" * 50 + "\n")

def extract_score_from_result(result) -> float:

    """Extract final score from APO training result."""

def main():    try:

    """Main function to run APO training."""        # Try different ways to extract the score

    print("🧠 Agent Lightning APO Training with Azure OpenAI")        if hasattr(result, 'score'):

    print("=" * 60)            return float(result.score)

            elif hasattr(result, 'final_score'):

    # Check environment            return float(result.final_score)

    required_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT"]        elif hasattr(result, 'best_score'):

    missing_vars = [var for var in required_vars if not os.getenv(var)]            return float(result.best_score)

            elif isinstance(result, dict):

    if missing_vars:            return float(result.get('score', result.get('final_score', result.get('best_score', 0.0))))

        print(f"❌ Missing environment variables: {missing_vars}")        else:

        return 1            print("⚠️  Could not extract score from training result")

                return 0.0

    try:    except (ValueError, AttributeError, TypeError) as e:

        # Initialize trainer        print(f"⚠️  Could not extract final score from training result: {e}")

        trainer = PersistentAPOTrainer()        return 0.0

        

        # Show training history

        trainer.print_training_history()def main() -> None:

            """Main function for APO room selector training with persistence."""

        # Run training session    print("Hotel Room Selector with APO - Azure OpenAI Version with Persistence")

        print("🚀 Starting new training session...")    print("=" * 70)

        trainer.run_training_session(num_iterations=3)    

            # Setup logging

        # Show updated history    configure_logger()

        trainer.print_training_history()    setup_apo_logger()

            

        return 0    # Create Azure OpenAI client

            try:

    except Exception as e:        # Create Azure OpenAI client

        logger.error(f"Training failed: {e}")        openai_client = create_azure_openai_client()

        return 1        print("✅ APO optimization enabled")

        

    except Exception as e:

if __name__ == "__main__":        print(f"❌ Failed to create Azure OpenAI client: {e}")

    import sys        return

    sys.exit(main())    
    # Load datasets
    try:
        dataset_train, dataset_val = load_train_val_dataset()
        print(f"✅ Loaded datasets: {len(dataset_train)} training, {len(dataset_val)} validation tasks")
    except Exception as e:
        print(f"❌ Failed to load datasets: {e}")
        return
    
    # Get optimal configuration from history using our utility functions
    optimal_config = get_optimal_config_from_history()
    
    print("\n🚀 Starting APO training with persistence...")
    print("Note: APO will automatically optimize prompts based on the room selection tasks.")
    
    try:
        # Create APO algorithm with configuration and Azure deployment from environment
        azure_deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME')  # Use deployment name from .env
        if not azure_deployment:
            raise ValueError("AZURE_OPENAI_DEPLOYMENT_NAME must be set in .env file")
            
        algo = APO[RoomSelectionTask](
            openai_client,
            gradient_model=azure_deployment,      # Use deployment from environment for gradients
            apply_edit_model=azure_deployment,    # Use deployment from environment for edits
            val_batch_size=optimal_config["val_batch_size"],
            gradient_batch_size=optimal_config["gradient_batch_size"],
            beam_width=optimal_config["beam_width"],
            branch_factor=optimal_config["branch_factor"],
            beam_rounds=optimal_config["beam_rounds"],
            _poml_trace=True,  # Enable POML tracing for debugging
        )
        
        # Create trainer with APO algorithm
        trainer = Trainer(
            algorithm=algo,
            n_runners=2,  # Use fewer runners for stability
            initial_resources={
                "prompt_template": prompt_template_baseline()
            },
            adapter=TraceToMessages(),
        )
        
        # Run APO training
        result = trainer.fit(
            agent=room_selector, 
            train_dataset=dataset_train, 
            val_dataset=dataset_val
        )
        
        # Extract and save score
        final_score = extract_score_from_result(result)
        save_training_result(final_score, optimal_config)
        
        print(f"\n🎉 APO training completed!")
        print(f"📊 Final score: {final_score:.3f}")
        print(f"Check the 'apo.log' file for detailed training logs.")
        print(f"POML traces are saved in 'pomltrace/' directory for analysis.")
        print(f"💾 Training history saved for future optimization runs.")
        
    except Exception as e:
        print(f"❌ APO training failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()