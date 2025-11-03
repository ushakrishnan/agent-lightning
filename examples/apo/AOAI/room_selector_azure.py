#!/usr/bin/env python3#!/usr/bin/env python3

""""""

Room Selector Azure OpenAI DemoAzure Room Selector - Executable Script



This script demonstrates the Azure OpenAI room selector agent withThis script provides a command-line interface for testing the Azure OpenAI room selector.

interactive testing capabilities.It can run individual room selection tasks, perform connection tests, or run demo scenarios.



Usage:Usage:

    python room_selector_azure.py    python room_selector_azure.py                    # Run demo with sample tasks

    python room_selector_azure.py --test-connection  # Test Azure connection only

Requirements:    python room_selector_azure.py --single-task     # Run single task interactively

    - Azure OpenAI credentials configured in environment

    - Agent Lightning with APO extras installedAuthor: Agent Lightning AOAI Examples Team

"""Version: 1.0

Date: November 2, 2025

import os"""

import sys

from room_selector_module import RoomSelectorAgentimport argparse

import asyncio

import sys

def main():from typing import List

    """Main function to run the room selector demo."""

    print("🏨 Azure OpenAI Room Selector Agent")from rich.console import Console

    print("=" * 50)from rich.panel import Panel

    from rich.table import Table

    # Check environment configuration

    required_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT"]# Import the module components

    missing_vars = [var for var in required_vars if not os.getenv(var)]from room_selector_module import (

        RoomSelectionTask,

    if missing_vars:    create_azure_client,

        print(f"❌ Missing environment variables: {missing_vars}")    load_room_tasks,

        print("\nPlease set the following environment variables:")    prompt_template_baseline,

        for var in missing_vars:    room_selector,

            print(f"  export {var}=your_value_here")    judge_room_selection,

        print("\nSee docs/AOAI/AZURE_ENV_SETUP.md for detailed setup instructions.")    AZURE_DEPLOYMENT

        return 1)

    

    try:console = Console()

        # Initialize the agent

        print("🚀 Initializing Room Selector Agent...")

        agent = RoomSelectorAgent()async def test_azure_connection() -> bool:

        print("✅ Agent initialized successfully!\n")    """Test Azure OpenAI connection."""

            try:

        # Interactive mode        console.print("🔧 Testing Azure OpenAI connection...", style="yellow")

        print("💬 Interactive Mode (type 'quit' to exit)")        client = create_azure_client()

        print("Enter your room selection requirements:\n")        

                # Test with a simple completion

        while True:        response = await client.chat.completions.create(

            try:            model=AZURE_DEPLOYMENT,

                user_input = input("Your requirements: ").strip()            messages=[{"role": "user", "content": "Hello! Just testing the connection."}],

                            max_tokens=10,

                if user_input.lower() in ['quit', 'exit', 'q']:            temperature=0.0

                    print("👋 Goodbye!")        )

                    break        

                        console.print("✅ Azure OpenAI connection successful!", style="green")

                if not user_input:        console.print(f"📡 Endpoint: {client._azure_endpoint}")

                    continue        console.print(f"🤖 Model: {AZURE_DEPLOYMENT}")

                        console.print(f"💬 Test response: {response.choices[0].message.content.strip()}")

                print("\n🤔 Analyzing your requirements...")        return True

                result = agent.select_room(user_input)        

                    except Exception as e:

                if result["success"]:        console.print(f"❌ Azure OpenAI connection failed: {e}", style="red")

                    print("✅ Room Recommendation:")        return False

                    print("-" * 30)

                    print(result["recommendation"])

                    print(f"\n📊 Tokens used: {result['tokens_used']}")async def run_single_task_interactive() -> None:

                else:    """Run a single room selection task interactively."""

                    print(f"❌ Error: {result['error']}")    console.print("🎯 Interactive Room Selection", style="bold cyan")

                    console.print("Enter task details (press Enter for default values):")

                print("\n" + "="*60 + "\n")    

                    # Get user input

            except KeyboardInterrupt:    date = input("Date (YYYY-MM-DD) [2025-10-13]: ").strip() or "2025-10-13"

                print("\n\n👋 Goodbye!")    time = input("Time (HH:MM) [11:00]: ").strip() or "11:00"

                break    duration = int(input("Duration in minutes [60]: ").strip() or "60")

            except Exception as e:    attendees = int(input("Number of attendees [4]: ").strip() or "4")

                print(f"❌ Unexpected error: {e}")    needs_input = input("Needs (comma-separated) [WiFi]: ").strip() or "WiFi"

                continue    needs = [need.strip() for need in needs_input.split(",")]

            accessible = input("Accessibility required? (y/n) [n]: ").strip().lower() == 'y'

        return 0    

            # Create task

    except Exception as e:    task = RoomSelectionTask(

        print(f"❌ Failed to initialize agent: {e}")        date=date,

        return 1        time=time,

        duration_min=duration,

        attendees=attendees,

if __name__ == "__main__":        needs=needs,

    sys.exit(main())        accessible=accessible
    )
    
    console.print("\n🏨 Running room selection...", style="yellow")
    
    # Run the task
    try:
        template = prompt_template_baseline()
        score = await room_selector(task, template)
        
        console.print(f"\n✅ Task completed with score: {score:.3f}", style="green")
        
    except Exception as e:
        console.print(f"❌ Task failed: {e}", style="red")


async def run_demo() -> None:
    """Run demo with multiple sample tasks."""
    console.print("🏨 Azure Room Selector Demo", style="bold cyan")
    console.print("=" * 50)
    
    # Load tasks
    try:
        tasks = load_room_tasks()
        console.print(f"📋 Loaded {len(tasks)} sample tasks", style="green")
    except Exception as e:
        console.print(f"❌ Failed to load tasks: {e}", style="red")
        return
    
    # Test Azure connection first
    if not await test_azure_connection():
        console.print("🔌 Please check your Azure OpenAI configuration in .env file", style="yellow")
        return
    
    console.print("\n🚀 Running room selection on sample tasks...", style="yellow")
    
    # Run tasks
    scores = []
    template = prompt_template_baseline()
    
    for i, task in enumerate(tasks[:4]):  # Run first 4 tasks for demo
        try:
            console.print(f"\n📝 Task {i+1}/{min(4, len(tasks))}: {task.date} at {task.time}")
            console.print(f"   👥 {task.attendees} attendees, needs: {task.needs}")
            
            score = await room_selector(task, template)
            scores.append(score)
            
            console.print(f"   ✅ Score: {score:.3f}")
            
        except Exception as e:
            console.print(f"   ❌ Failed: {e}", style="red")
            scores.append(0.0)
    
    # Show summary
    if scores:
        console.print("\n" + "="*50)
        
        # Create summary table
        table = Table(title="📊 Demo Results Summary", border_style="cyan")
        table.add_column("Metric", style="bold")
        table.add_column("Value", style="green")
        
        table.add_row("Tasks Completed", f"{len(scores)}")
        table.add_row("Average Score", f"{sum(scores)/len(scores):.3f}")
        table.add_row("Best Score", f"{max(scores):.3f}")
        table.add_row("Worst Score", f"{min(scores):.3f}")
        table.add_row("Success Rate", f"{len([s for s in scores if s >= 0.6]) / len(scores) * 100:.1f}% (score ≥ 0.6)")
        
        console.print(table)
        
        console.print(Panel(
            "✅ Demo completed successfully!\n\n"
            "The room selector is working with Azure OpenAI and can intelligently "
            "match room requirements with available options. Scores above 0.6 indicate "
            "good matches, while perfect scores (1.0) indicate optimal selections.",
            title="🎯 Summary",
            border_style="green"
        ))


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Azure Room Selector Demo")
    parser.add_argument("--test-connection", action="store_true", 
                      help="Test Azure OpenAI connection only")
    parser.add_argument("--single-task", action="store_true",
                      help="Run single task interactively")
    
    args = parser.parse_args()
    
    try:
        if args.test_connection:
            # Test connection only
            result = asyncio.run(test_azure_connection())
            sys.exit(0 if result else 1)
        elif args.single_task:
            # Run single interactive task
            asyncio.run(run_single_task_interactive())
        else:
            # Run full demo
            asyncio.run(run_demo())
            
    except KeyboardInterrupt:
        console.print("\n👋 Demo interrupted by user", style="yellow")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n❌ Unexpected error: {e}", style="red")
        sys.exit(1)


if __name__ == "__main__":
    main()
