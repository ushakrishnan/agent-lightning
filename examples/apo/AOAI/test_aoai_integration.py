#!/usr/bin/env python3
"""
Azure OpenAI APO Integration - Comprehensive Test Suite

This script validates the complete Azure OpenAI APO integration including:
- Environment setup verification
- Azure OpenAI connectivity
- Module imports and initialization
- APO training functionality
- Persistence system validation

Usage:
    python test_aoai_integration.py

Requirements:
    - Active conda environment with Agent Lightning
    - Azure OpenAI credentials configured
    - All required dependencies installed
"""

import os
import sys
import json
import tempfile
from datetime import datetime
from typing import Dict, List, Any


def print_header(title: str):
    """Print formatted test section header."""
    print(f"\n{'='*60}")
    print(f"🧪 {title}")
    print(f"{'='*60}")


def print_result(test_name: str, success: bool, details: str = ""):
    """Print formatted test result."""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} {test_name}")
    if details:
        print(f"    {details}")


def test_environment_setup() -> Dict[str, Any]:
    """Test basic environment setup and dependencies."""
    print_header("Environment Setup Validation")
    results = {}
    
    # Test Python version
    python_version = sys.version_info
    python_ok = python_version >= (3, 8)
    print_result(
        "Python Version", 
        python_ok, 
        f"Python {python_version.major}.{python_version.minor}.{python_version.micro}"
    )
    results["python_version"] = python_ok
    
    # Test Agent Lightning import
    try:
        import agentlightning
        version = agentlightning.__version__
        print_result("Agent Lightning Import", True, f"Version {version}")
        results["agentlightning"] = True
    except ImportError as e:
        print_result("Agent Lightning Import", False, str(e))
        results["agentlightning"] = False
    
    # Test APO algorithm import
    try:
        from agentlightning.algorithm.apo import APO
        print_result("APO Algorithm Import", True)
        results["apo_algorithm"] = True
    except ImportError as e:
        print_result("APO Algorithm Import", False, str(e))
        results["apo_algorithm"] = False
    
    # Test Azure OpenAI SDK
    try:
        from openai import AzureOpenAI
        print_result("Azure OpenAI SDK Import", True)
        results["azure_openai_sdk"] = True
    except ImportError as e:
        print_result("Azure OpenAI SDK Import", False, str(e))
        results["azure_openai_sdk"] = False
    
    # Test PyTorch
    try:
        import torch
        print_result("PyTorch Import", True, f"Version {torch.__version__}")
        results["pytorch"] = True
    except ImportError as e:
        print_result("PyTorch Import", False, str(e))
        results["pytorch"] = False
    
    return results


def test_environment_variables() -> Dict[str, Any]:
    """Test Azure OpenAI environment variables."""
    print_header("Environment Variables Validation")
    results = {}
    
    required_vars = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT", 
        "AZURE_OPENAI_DEPLOYMENT_NAME"
    ]
    
    for var in required_vars:
        value = os.getenv(var)
        has_value = bool(value and value.strip())
        print_result(
            f"{var}", 
            has_value,
            "Set" if has_value else "Missing or empty"
        )
        results[var.lower()] = has_value
    
    # Test endpoint format
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    valid_endpoint = endpoint.startswith("https://") and ".openai.azure.com" in endpoint
    print_result(
        "Endpoint Format",
        valid_endpoint,
        "Valid Azure OpenAI endpoint" if valid_endpoint else "Invalid format"
    )
    results["endpoint_format"] = valid_endpoint
    
    return results


def test_azure_openai_connection() -> Dict[str, Any]:
    """Test Azure OpenAI service connectivity."""
    print_header("Azure OpenAI Connection Test")
    results = {}
    
    try:
        from openai import AzureOpenAI
        
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        # Test API call
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini"),
            messages=[{"role": "user", "content": "Hello Azure OpenAI! Respond with just 'Connected.'"}],
            max_tokens=10,
            temperature=0
        )
        
        response_text = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens if response.usage else 0
        
        print_result("API Connection", True, f"Response: '{response_text}', Tokens: {tokens_used}")
        results["connection"] = True
        results["tokens_used"] = tokens_used
        
    except Exception as e:
        print_result("API Connection", False, str(e))
        results["connection"] = False
    
    return results


def test_module_imports() -> Dict[str, Any]:
    """Test room selector module imports and initialization."""
    print_header("Module Import and Initialization")
    results = {}
    
    # Test room selector module import
    try:
        from room_selector_module import RoomSelectorAgent
        print_result("Room Selector Module Import", True)
        results["module_import"] = True
        
        # Test agent initialization
        agent = RoomSelectorAgent()
        print_result("Room Selector Agent Init", True)
        results["agent_init"] = True
        
    except Exception as e:
        print_result("Room Selector Module", False, str(e))
        results["module_import"] = False
        results["agent_init"] = False
    
    # Test APO trainer import
    try:
        from room_selector_apo_persistent import PersistentAPOTrainer
        print_result("APO Trainer Module Import", True)
        results["apo_trainer_import"] = True
        
        # Test trainer initialization
        trainer = PersistentAPOTrainer(f"test_checkpoint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        print_result("APO Trainer Init", True, f"History: {len(trainer.training_history)} sessions")
        results["apo_trainer_init"] = True
        
    except Exception as e:
        print_result("APO Trainer Module", False, str(e))
        results["apo_trainer_import"] = False
        results["apo_trainer_init"] = False
    
    return results


def test_room_selection_functionality() -> Dict[str, Any]:
    """Test basic room selection functionality."""
    print_header("Room Selection Functionality")
    results = {}
    
    try:
        from room_selector_module import RoomSelectorAgent
        agent = RoomSelectorAgent()
        
        # Test room selection
        test_input = "I need a room for business travel with good WiFi and workspace, budget around $200"
        result = agent.select_room(test_input)
        
        success = result.get("success", False)
        if success:
            recommendation = result.get("recommendation", "")
            tokens = result.get("tokens_used", 0)
            print_result(
                "Room Selection", 
                True, 
                f"Generated recommendation ({tokens} tokens)"
            )
            print(f"    Sample: {recommendation[:100]}...")
        else:
            error = result.get("error", "Unknown error")
            print_result("Room Selection", False, error)
        
        results["room_selection"] = success
        
    except Exception as e:
        print_result("Room Selection", False, str(e))
        results["room_selection"] = False
    
    return results


def test_apo_scoring_system() -> Dict[str, Any]:
    """Test APO scoring system."""
    print_header("APO Scoring System")
    results = {}
    
    try:
        from room_selector_apo_persistent import PersistentAPOTrainer
        trainer = PersistentAPOTrainer()
        
        # Test scoring with good recommendation
        good_task = {
            "id": "test_business",
            "expected_features": ["wifi", "workspace", "budget"]
        }
        good_recommendation = "I recommend the Business Room ($200/night) because it offers excellent WiFi, dedicated workspace, and fits perfectly within your budget."
        
        good_score = trainer.evaluate_room_selection(good_task, good_recommendation)
        print_result(
            "Good Recommendation Scoring",
            good_score > 0.7,
            f"Score: {good_score:.2f} (expected >0.7)"
        )
        
        # Test scoring with poor recommendation
        poor_recommendation = "There are rooms available."
        poor_score = trainer.evaluate_room_selection(good_task, poor_recommendation)
        print_result(
            "Poor Recommendation Scoring",
            poor_score < 0.5,
            f"Score: {poor_score:.2f} (expected <0.5)"
        )
        
        results["scoring_good"] = good_score > 0.7
        results["scoring_poor"] = poor_score < 0.5
        results["scoring_differential"] = good_score > poor_score
        
    except Exception as e:
        print_result("APO Scoring System", False, str(e))
        results["scoring_good"] = False
        results["scoring_poor"] = False
        results["scoring_differential"] = False
    
    return results


def test_persistence_system() -> Dict[str, Any]:
    """Test APO persistence system."""
    print_header("APO Persistence System")
    results = {}
    
    try:
        from room_selector_apo_persistent import PersistentAPOTrainer
        
        # Create temporary checkpoint file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            checkpoint_file = f.name
        
        try:
            # Test checkpoint creation and saving
            trainer = PersistentAPOTrainer(checkpoint_file)
            trainer.training_history = [
                {
                    "timestamp": datetime.now().isoformat(),
                    "average_score": 0.85,
                    "iterations": 3
                }
            ]
            trainer.current_best_score = 0.85
            trainer.save_checkpoint()
            
            print_result("Checkpoint Save", True)
            
            # Test checkpoint loading
            trainer2 = PersistentAPOTrainer(checkpoint_file)
            loaded_history = len(trainer2.training_history)
            loaded_score = trainer2.current_best_score
            
            print_result(
                "Checkpoint Load",
                loaded_history > 0 and loaded_score == 0.85,
                f"Loaded {loaded_history} sessions, best score: {loaded_score}"
            )
            
            results["persistence_save"] = True
            results["persistence_load"] = loaded_history > 0 and loaded_score == 0.85
            
        finally:
            # Cleanup
            if os.path.exists(checkpoint_file):
                os.unlink(checkpoint_file)
                
    except Exception as e:
        print_result("Persistence System", False, str(e))
        results["persistence_save"] = False
        results["persistence_load"] = False
    
    return results


def print_summary(all_results: Dict[str, Dict[str, Any]]):
    """Print comprehensive test summary."""
    print_header("Test Summary")
    
    total_tests = 0
    passed_tests = 0
    
    for category, results in all_results.items():
        category_passed = sum(1 for r in results.values() if r is True)
        category_total = len(results)
        total_tests += category_total
        passed_tests += category_passed
        
        status = "✅" if category_passed == category_total else "⚠️" if category_passed > 0 else "❌"
        print(f"{status} {category.replace('_', ' ').title()}: {category_passed}/{category_total}")
    
    print(f"\n📊 Overall: {passed_tests}/{total_tests} tests passed ({passed_tests/total_tests*100:.1f}%)")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Your Azure OpenAI APO integration is ready to use.")
        return 0
    elif passed_tests > total_tests * 0.7:
        print("⚠️ Most tests passed. Review failures above and fix any critical issues.")
        return 1
    else:
        print("❌ Multiple test failures. Please review your setup and configuration.")
        return 2


def main():
    """Run comprehensive test suite."""
    print("🧪 Azure OpenAI APO Integration Test Suite")
    print(f"Timestamp: {datetime.now().isoformat()}")
    
    all_results = {}
    
    # Run all test categories
    all_results["environment_setup"] = test_environment_setup()
    all_results["environment_variables"] = test_environment_variables()
    all_results["azure_connection"] = test_azure_openai_connection()
    all_results["module_imports"] = test_module_imports()
    all_results["room_selection"] = test_room_selection_functionality()
    all_results["apo_scoring"] = test_apo_scoring_system()
    all_results["persistence"] = test_persistence_system()
    
    # Print summary and return exit code
    exit_code = print_summary(all_results)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())