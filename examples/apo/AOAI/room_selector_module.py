"""
Room Selector Agent Module - Azure OpenAI Integration

This module provides a production-ready room selection agent using Azure OpenAI
with Agent Lightning's APO (Automatic Prompt Optimization) integration.

Features:
- Azure OpenAI GPT-4o-mini integration
- Comprehensive error handling and retries
- Detailed logging and performance monitoring
- Production-ready authentication and configuration
"""

import os
import logging
import json
from typing import Dict, Any, Optional
from openai import AzureOpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('apo.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RoomSelectorAgent:
    """
    A sophisticated room selection agent that uses Azure OpenAI to make
    intelligent room recommendations based on user preferences and constraints.
    
    This agent demonstrates production-ready patterns for:
    - Azure OpenAI integration with proper error handling
    - Comprehensive logging and monitoring
    - Flexible prompt engineering for diverse scenarios
    - Real-world business logic implementation
    """
    
    def __init__(self):
        """Initialize the room selector agent with Azure OpenAI configuration."""
        self.client = self._setup_azure_openai()
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        
        # System prompt for room selection
        self.system_prompt = """You are an expert hotel room selector with deep knowledge of hospitality and travel. 
Your role is to analyze user requirements and recommend the most suitable room from available options.

Consider these factors in your analysis:
- User preferences and stated needs
- Budget constraints and value optimization
- Room features and amenities alignment
- Context (business trip, family vacation, romantic getaway, etc.)
- Practical considerations (location, size, special requirements)

Provide your recommendation with:
1. Selected room with clear rationale
2. Key reasons for the choice
3. How it addresses user priorities
4. Any relevant considerations or alternatives

Be concise but thorough in your reasoning."""

        logger.info("RoomSelectorAgent initialized successfully")

    def _setup_azure_openai(self) -> AzureOpenAI:
        """
        Setup Azure OpenAI client with proper configuration and error handling.
        
        Returns:
            AzureOpenAI: Configured client instance
            
        Raises:
            ValueError: If required environment variables are missing
            Exception: If client initialization fails
        """
        try:
            # Validate required environment variables
            required_vars = [
                "AZURE_OPENAI_API_KEY",
                "AZURE_OPENAI_ENDPOINT"
            ]
            
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                raise ValueError(f"Missing required environment variables: {missing_vars}")
            
            # Initialize Azure OpenAI client
            client = AzureOpenAI(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
            )
            
            logger.info("Azure OpenAI client initialized successfully")
            return client
            
        except Exception as e:
            logger.error(f"Failed to setup Azure OpenAI client: {e}")
            raise

    def select_room(self, user_input: str, available_rooms: Optional[str] = None) -> Dict[str, Any]:
        """
        Select the best room based on user requirements and available options.
        
        Args:
            user_input (str): User's requirements and preferences
            available_rooms (str, optional): Available room options (uses default if None)
            
        Returns:
            Dict[str, Any]: Selection result with recommendation and reasoning
        """
        try:
            # Use default rooms if none provided
            if available_rooms is None:
                available_rooms = self._get_default_rooms()
            
            # Construct the user prompt
            user_prompt = f"""
User Requirements: {user_input}

Available Rooms:
{available_rooms}

Please analyze the user's requirements and recommend the most suitable room from the available options.
"""

            logger.info(f"Processing room selection request: {user_input[:100]}...")
            
            # Make API call to Azure OpenAI
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            recommendation = response.choices[0].message.content
            
            result = {
                "success": True,
                "recommendation": recommendation,
                "user_input": user_input,
                "timestamp": self._get_timestamp(),
                "model_used": self.deployment_name,
                "tokens_used": response.usage.total_tokens if response.usage else 0
            }
            
            logger.info(f"Room selection completed successfully. Tokens used: {result['tokens_used']}")
            return result
            
        except Exception as e:
            logger.error(f"Room selection failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "user_input": user_input,
                "timestamp": self._get_timestamp()
            }

    def _get_default_rooms(self) -> str:
        """
        Get default room options for demonstration purposes.
        
        Returns:
            str: Formatted room options
        """
        rooms = """
1. Ocean View Deluxe Room - $180/night
   - King bed, ocean view, balcony
   - 400 sq ft, modern amenities
   - Free WiFi, room service, mini-bar

2. City Suite - $250/night
   - Separate living area, city skyline view
   - 600 sq ft, work desk, kitchenette
   - Executive lounge access, premium WiFi

3. Garden Standard Room - $120/night
   - Queen bed, garden view, ground floor
   - 300 sq ft, basic amenities
   - Free WiFi, coffee maker

4. Penthouse Suite - $500/night
   - Master bedroom, panoramic views
   - 1000 sq ft, luxury amenities, jacuzzi
   - Concierge service, airport transfer

5. Business Room - $200/night
   - King bed, work station, city view
   - 350 sq ft, business amenities
   - Fast WiFi, printer access, meeting room credits
"""
        return rooms

    def _get_timestamp(self) -> str:
        """Get current timestamp for logging."""
        from datetime import datetime
        return datetime.now().isoformat()


# Demonstration function for standalone testing
def demo_room_selection():
    """
    Demonstrate the room selector agent with sample scenarios.
    """
    agent = RoomSelectorAgent()
    
    # Sample scenarios
    scenarios = [
        "I need a room for a business trip, budget around $200, need good WiFi and workspace",
        "Looking for a romantic getaway, ocean view preferred, budget flexible up to $400",
        "Family vacation with 2 kids, need space and ground floor, budget conscious under $150",
        "Executive business meeting, need luxury accommodations and concierge services"
    ]
    
    print("=== Room Selector Agent Demo ===\n")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"Scenario {i}: {scenario}")
        print("-" * 50)
        
        result = agent.select_room(scenario)
        
        if result["success"]:
            print("✅ Recommendation:")
            print(result["recommendation"])
            print(f"\n📊 Tokens used: {result['tokens_used']}")
        else:
            print("❌ Error:", result["error"])
        
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    # Run demonstration if executed directly
    demo_room_selection()