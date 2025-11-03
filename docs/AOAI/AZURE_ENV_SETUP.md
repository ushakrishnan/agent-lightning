# Azure OpenAI Environment Setup Guide````markdown

# Azure OpenAI Environment Setup for Agent Lightning

This guide provides comprehensive instructions for configuring your Azure OpenAI environment for use with Agent Lightning, covering everything from Azure resource creation to local development setup.

This guide provides comprehensive instructions for configuring Azure OpenAI environment variables with Agent Lightning, including best practices and troubleshooting.

## 🎯 Overview

## Quick Setup (TL;DR)

This setup enables:

- **Azure OpenAI Service** configuration with proper security and access controls```bash

- **Environment variable management** for secure credential handling# 1. Copy example environment file

- **Development workflow optimization** with proper tooling and configurationcp examples/apo/.env.example .env

- **Production-ready patterns** with monitoring, logging, and error handling

# 2. Edit with your Azure OpenAI credentials

## 🏗️ Azure OpenAI Service Setupnano .env



### Step 1: Azure Subscription and Access# 3. Test the setup

uv run python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✅ Environment loaded')"

#### Check Azure OpenAI Availability```

```bash

# List available regions for Azure OpenAI## Required Environment Variables

az cognitiveservices account list-skus \

  --kind OpenAI \### Core Azure OpenAI Variables

  --query "[].{Name:name, Locations:locations[0]}" \

  --output table```bash

```# Your Azure OpenAI endpoint URL (include full path)

AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/

#### Request Access (If Needed)

1. **Navigate** to [Azure OpenAI Access Request](https://aka.ms/oai/access)# Your Azure OpenAI API key

2. **Complete Application** with your use case detailsAZURE_OPENAI_API_KEY=your_actual_api_key_here

3. **Wait for Approval** (typically 1-3 business days)

4. **Verify Access** in Azure Portal# API version (recommended: latest stable)

AZURE_OPENAI_API_VERSION=2024-08-01-preview

### Step 2: Create Azure OpenAI Resource

# Deployment name for your model (e.g., gpt-4, gpt-35-turbo)

#### Using Azure PortalAZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

1. **Sign in** to [Azure Portal](https://portal.azure.com)```

2. **Create Resource** → Search "OpenAI" → Select "Azure OpenAI"

3. **Configure Resource**:### Optional Azure Variables (for advanced features)

   ```

   Subscription: Your Azure subscription```bash

   Resource Group: Create new "rg-agentlightning-dev"# Your Azure subscription ID (for resource management)

   Region: East US (or closest supported region)AZURE_SUBSCRIPTION_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx

   Name: "aoai-agentlightning-dev" (must be globally unique)

   Pricing Tier: Standard S0# Resource group containing your Azure OpenAI service

   ```AZURE_RESOURCE_GROUP=your_resource_group_name

4. **Review + Create** → Wait for deployment completion

# Azure OpenAI service name

#### Using Azure CLIAZURE_RESOURCE_NAME=your_aoai_service_name

```bash```

# Set variables

RESOURCE_GROUP="rg-agentlightning-dev"### Alternative Format (OpenAI-compatible)

LOCATION="eastus"

AOAI_NAME="aoai-agentlightning-dev"For compatibility with examples that use standard OpenAI format:



# Create resource group```bash

az group create --name $RESOURCE_GROUP --location $LOCATION# OpenAI-compatible format (some examples prefer this)

OPENAI_API_KEY=your_azure_api_key_here

# Create Azure OpenAI resourceOPENAI_BASE_URL=https://your-resource-name.openai.azure.com/

az cognitiveservices account create \OPENAI_API_VERSION=2024-08-01-preview

  --name $AOAI_NAME \```

  --resource-group $RESOURCE_GROUP \

  --location $LOCATION \## Setup Methods

  --kind OpenAI \

  --sku S0 \### Method 1: Project-Specific .env File (Recommended)

  --custom-domain $AOAI_NAME

```Create a `.env` file in your project root:



### Step 3: Model Deployment```bash

# Navigate to your project directory

#### Deploy gpt-4o-mini (Recommended)cd /path/to/your/project

1. **Navigate** to your Azure OpenAI resource

2. **Model Deployments** → Click "Create"# Create .env file

3. **Configure Deployment**:cat > .env << EOF

   ```# Azure OpenAI Configuration

   Model: gpt-4o-miniAZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/

   Model version: Latest availableAZURE_OPENAI_API_KEY=your_actual_api_key

   Deployment name: gpt-4o-miniAZURE_OPENAI_API_VERSION=2024-08-01-preview

   Deployment type: StandardAZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

   Tokens per minute rate limit: 50K (adjust as needed)

   Content filter: Default# Optional: OpenAI-compatible format

   ```OPENAI_API_KEY=your_actual_api_key

OPENAI_BASE_URL=https://your-resource-name.openai.azure.com/

#### Deploy Additional Models (Optional)OPENAI_API_VERSION=2024-08-01-preview

```bashEOF

# Using Azure CLI to deploy models

az cognitiveservices account deployment create \# Test environment loading

  --name $AOAI_NAME \uv run python -c "

  --resource-group $RESOURCE_GROUP \from dotenv import load_dotenv

  --deployment-name "gpt-4o-mini" \import os

  --model-name "gpt-4o-mini" \load_dotenv()

  --model-version "2024-07-18" \print('✅ AZURE_OPENAI_ENDPOINT:', os.getenv('AZURE_OPENAI_ENDPOINT'))

  --model-format "OpenAI" \print('✅ API Key loaded:', bool(os.getenv('AZURE_OPENAI_API_KEY')))

  --scale-type "Standard""

``````



### Step 4: Configure Access and Security### Method 2: Shell Export (Session-specific)



#### Get Connection Details```bash

```bash# Export environment variables for current session

# Get endpointexport AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"

az cognitiveservices account show \export AZURE_OPENAI_API_KEY="your_actual_api_key"

  --name $AOAI_NAME \export AZURE_OPENAI_API_VERSION="2024-08-01-preview"

  --resource-group $RESOURCE_GROUP \export AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o"

  --query "properties.endpoint" \

  --output tsv# Verify exports

echo "Endpoint: $AZURE_OPENAI_ENDPOINT"

# Get API keysecho "API Key set: $([ -n "$AZURE_OPENAI_API_KEY" ] && echo "Yes" || echo "No")"

az cognitiveservices account keys list \```

  --name $AOAI_NAME \

  --resource-group $RESOURCE_GROUP \### Method 3: System-wide Setup (Not Recommended)

  --query "key1" \

  --output tsv```bash

```# Add to ~/.bashrc or ~/.bash_profile (use with caution)

echo 'export AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"' >> ~/.bashrc

#### Configure Network Accessecho 'export AZURE_OPENAI_API_KEY="your_actual_api_key"' >> ~/.bashrc

```bashsource ~/.bashrc

# Restrict access to specific IP ranges (optional)```

az cognitiveservices account network-rule add \

  --name $AOAI_NAME \## Configuration Strategy

  --resource-group $RESOURCE_GROUP \

  --ip-address "YOUR_IP_ADDRESS"### For Multiple Projects



# Enable private endpoints (production)**Recommended Pattern**: Local `.env` files per project

az cognitiveservices account update \

  --name $AOAI_NAME \```

  --resource-group $RESOURCE_GROUP \project1/

  --public-network-access Disabled├── .env                    # Project-specific Azure config

```├── examples/

└── scripts/

## 🔐 Environment Configuration

project2/  

### Step 1: Local Environment Setup├── .env                    # Different Azure config

├── examples/

#### Create Environment File└── scripts/

```bash```

# Navigate to your project directory

cd /path/to/agent-lightning**Benefits**:

- ✅ Project isolation

# Create .env file- ✅ Different API keys/endpoints per project

cat > .env << 'EOF'- ✅ Version control friendly (add `.env` to `.gitignore`)

# =============================================================================- ✅ No global environment pollution

# Azure OpenAI Configuration

# =============================================================================### Environment File Hierarchy



# Primary connection settingsAgent Lightning automatically loads environment variables in this order:

AZURE_OPENAI_API_KEY=your_api_key_here

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/1. **System environment variables** (highest priority)

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini2. **Local `.env` file** (project root)

AZURE_OPENAI_API_VERSION=2024-02-15-preview3. **Parent directory `.env` files** (searches upward)

4. **Default values** (lowest priority)

# Optional: Secondary key for failover

AZURE_OPENAI_API_KEY_SECONDARY=your_secondary_key_here## Integration with Agent Lightning



# =============================================================================### How Agent Lightning Uses Environment Variables

# Performance and Rate Limiting

# =============================================================================Agent Lightning uses **LiteLLM** as its core infrastructure, which means:



# Token limits and timeouts```python

AZURE_OPENAI_MAX_TOKENS=2000# Agent Lightning automatically handles environment variables

AZURE_OPENAI_TEMPERATURE=0.7from agentlightning import LLM

AZURE_OPENAI_TIMEOUT_SECONDS=60

AZURE_OPENAI_MAX_RETRIES=3# This automatically uses your AZURE_OPENAI_* variables

llm = LLM(

# Rate limiting    endpoint="azure/gpt-4o",  # LiteLLM format

AZURE_OPENAI_REQUESTS_PER_MINUTE=60    model="gpt-4o"

AZURE_OPENAI_TOKENS_PER_MINUTE=50000)



# =============================================================================# Or use OpenAI client directly with your variables

# Agent Lightning Configuration  import openai

# =============================================================================from dotenv import load_dotenv

load_dotenv()

# APO training parameters

APO_ITERATIONS_PER_SESSION=5client = openai.OpenAI(

APO_MAX_SESSIONS=50    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),

APO_CONVERGENCE_THRESHOLD=0.90    api_key=os.getenv("AZURE_OPENAI_API_KEY"),

APO_CHECKPOINT_FILE=apo_training_history.json    default_headers={"api-version": os.getenv("AZURE_OPENAI_API_VERSION")}

)

# Logging configuration```

LOG_LEVEL=INFO

ENABLE_TRACE_LOGGING=true### Environment Variable Formats

LOG_FILE_PREFIX=agent_lightning

**Azure Format** (Recommended for new projects):

# =============================================================================```bash

# Optional: AgentOps IntegrationAZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# =============================================================================AZURE_OPENAI_API_KEY=your_key

AZURE_OPENAI_API_VERSION=2024-08-01-preview

# AgentOps monitoring (get key from agentops.ai)```

AGENTOPS_API_KEY=your_agentops_key_here

AGENTOPS_ENABLED=true**OpenAI Format** (For compatibility):

AGENTOPS_AUTO_START_SESSION=true```bash

AGENTOPS_TAGS=azure-openai,apo-trainingOPENAI_API_KEY=your_key

OPENAI_BASE_URL=https://your-resource.openai.azure.com/

# =============================================================================OPENAI_API_VERSION=2024-08-01-preview

# Development Settings```

# =============================================================================

**Both formats work** due to LiteLLM's flexible environment variable handling.

# Development mode settings

DEVELOPMENT_MODE=true## Testing Your Setup

ENABLE_DEBUG_LOGGING=false

CACHE_RESPONSES=true### Basic Connectivity Test

CACHE_TTL_SECONDS=3600

```bash

# Testing configuration# Test Azure OpenAI connection

TEST_MODE=falseuv run python -c "

MOCK_AZURE_RESPONSES=falseimport openai

EOFimport os

```from dotenv import load_dotenv



#### Secure the Environment Fileload_dotenv()

```bash

# Set restrictive permissionsclient = openai.OpenAI(

chmod 600 .env    base_url=os.getenv('AZURE_OPENAI_ENDPOINT'),

    api_key=os.getenv('AZURE_OPENAI_API_KEY'),

# Add to .gitignore to prevent accidental commits    default_headers={'api-version': os.getenv('AZURE_OPENAI_API_VERSION')}

echo ".env" >> .gitignore)

echo "*.log" >> .gitignore

echo "apo_training_history.json" >> .gitignoretry:

echo "pomltrace/" >> .gitignore    response = client.chat.completions.create(

echo "__pycache__/" >> .gitignore        model=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o'),

```        messages=[{'role': 'user', 'content': 'Hello, Azure OpenAI!'}],

        max_tokens=10

### Step 2: Environment Variable Loading    )

    print('✅ Azure OpenAI connection successful!')

#### Option A: Using python-dotenv    print(f'Response: {response.choices[0].message.content}')

```pythonexcept Exception as e:

# config.py    print(f'❌ Connection failed: {e}')

import os"

from dotenv import load_dotenv```



def load_config():### Agent Lightning Integration Test

    """Load configuration from environment variables."""

    # Load .env file```bash

    load_dotenv()# Test Agent Lightning with Azure OpenAI

    uv run python -c "

    # Validate required variablesfrom agentlightning import LLM

    required_vars = [from dotenv import load_dotenv

        "AZURE_OPENAI_API_KEY",import os

        "AZURE_OPENAI_ENDPOINT",

        "AZURE_OPENAI_DEPLOYMENT_NAME"load_dotenv()

    ]

    try:

    missing_vars = [var for var in required_vars if not os.getenv(var)]    llm = LLM(

    if missing_vars:        endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),

        raise ValueError(f"Missing required environment variables: {missing_vars}")        model=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o')

        )

    return {    print('✅ Agent Lightning LLM created successfully!')

        'api_key': os.getenv('AZURE_OPENAI_API_KEY'),except Exception as e:

        'endpoint': os.getenv('AZURE_OPENAI_ENDPOINT'),    print(f'❌ Agent Lightning integration failed: {e}')

        'deployment_name': os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),"

        'api_version': os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-15-preview'),```

        'max_tokens': int(os.getenv('AZURE_OPENAI_MAX_TOKENS', '2000')),

        'temperature': float(os.getenv('AZURE_OPENAI_TEMPERATURE', '0.7')),## Troubleshooting

        'timeout': int(os.getenv('AZURE_OPENAI_TIMEOUT_SECONDS', '60'))

    }### Common Issues



# Install python-dotenv#### 1. "Authentication failed"

pip install python-dotenv**Problem**: Invalid API key or endpoint

```

**Solution**:

#### Option B: Shell Script Loading```bash

```bash# Verify your environment variables

# load_env.shecho "Endpoint: $AZURE_OPENAI_ENDPOINT"

#!/bin/bashecho "API Key (first 10 chars): ${AZURE_OPENAI_API_KEY:0:10}..."



# Load environment variables from .env file# Check if .env file is being loaded

if [ -f .env ]; thenuv run python -c "

    export $(cat .env | sed 's/#.*//g' | xargs)from dotenv import load_dotenv

    echo "✅ Environment variables loaded from .env"import os

elseload_dotenv()

    echo "❌ .env file not found"print('Variables loaded:', bool(os.getenv('AZURE_OPENAI_API_KEY')))

    exit 1"

fi```



# Validate required variables#### 2. "Model not found"

required_vars=("AZURE_OPENAI_API_KEY" "AZURE_OPENAI_ENDPOINT" "AZURE_OPENAI_DEPLOYMENT_NAME")**Problem**: Deployment name mismatch



for var in "${required_vars[@]}"; do**Solution**:

    if [ -z "${!var}" ]; then```bash

        echo "❌ Missing required environment variable: $var"# List your Azure OpenAI deployments

        exit 1az cognitiveservices account deployment list \

    fi    --name your-resource-name \

done    --resource-group your-resource-group \

    --query "[].{name:name,model:properties.model.name}" -o table

echo "✅ All required environment variables are set"

# Update AZURE_OPENAI_DEPLOYMENT_NAME to match

# Usage: source load_env.sh```

```

#### 3. "Environment variables not loading"

### Step 3: Configuration Validation**Problem**: `.env` file not found or not loaded



#### Validation Script**Solution**:

```python```bash

# validate_config.py# Check if .env file exists

import osls -la .env

import sys

from openai import AzureOpenAI# Verify .env file content

from typing import Dict, Listcat .env



def validate_environment() -> Dict[str, bool]:# Force reload environment

    """Validate all environment variables and connections."""uv run python -c "

    results = {}from dotenv import load_dotenv

    load_dotenv('.env', override=True)

    # Check required environment variablesimport os

    required_vars = [print('Loaded variables:', [k for k in os.environ.keys() if 'AZURE' in k])

        "AZURE_OPENAI_API_KEY","

        "AZURE_OPENAI_ENDPOINT", ```

        "AZURE_OPENAI_DEPLOYMENT_NAME",

        "AZURE_OPENAI_API_VERSION"#### 4. "API version not supported"

    ]**Problem**: Outdated API version

    

    print("🔍 Validating Environment Variables...")**Solution**:

    for var in required_vars:```bash

        value = os.getenv(var)# Update to latest stable API version

        results[f"env_{var}"] = bool(value)# Edit .env file and change:

        status = "✅" if value else "❌"AZURE_OPENAI_API_VERSION=2024-08-01-preview

        print(f"  {status} {var}: {'Set' if value else 'Missing'}")```

    

    # Validate endpoint format### Debug Commands

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")

    valid_endpoint = endpoint.startswith("https://") and ".openai.azure.com" in endpoint```bash

    results["endpoint_format"] = valid_endpoint# Check all Azure-related environment variables

    print(f"  {'✅' if valid_endpoint else '❌'} Endpoint format: {'Valid' if valid_endpoint else 'Invalid'}")env | grep -i azure

    

    # Test Azure OpenAI connection# Test .env file loading

    print("\n🔗 Testing Azure OpenAI Connection...")uv run python -c "

    try:from dotenv import load_dotenv

        client = AzureOpenAI(import os

            api_key=os.getenv("AZURE_OPENAI_API_KEY"),load_dotenv()

            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),azure_vars = {k: v for k, v in os.environ.items() if 'AZURE' in k.upper()}

            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")for k, v in azure_vars.items():

        )    print(f'{k}: {v[:20]}...' if len(v) > 20 else f'{k}: {v}')

        "

        # Test with simple completion

        response = client.chat.completions.create(# Validate environment file format

            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),uv run python -c "

            messages=[{"role": "user", "content": "Hello"}],from dotenv import dotenv_values

            max_tokens=10config = dotenv_values('.env')

        )required = ['AZURE_OPENAI_ENDPOINT', 'AZURE_OPENAI_API_KEY']

        missing = [var for var in required if not config.get(var)]

        results["azure_connection"] = Trueif missing:

        print("  ✅ Azure OpenAI connection successful")    print(f'❌ Missing variables: {missing}')

        print(f"  📊 Test response: {response.choices[0].message.content.strip()}")else:

            print('✅ All required variables present')

    except Exception as e:"

        results["azure_connection"] = False```

        print(f"  ❌ Azure OpenAI connection failed: {str(e)}")

    ## Security Best Practices

    # Check Agent Lightning installation

    print("\n📦 Validating Agent Lightning Installation...")### 1. Protect API Keys

    try:

        import agentlightning```bash

        from agentlightning.algorithm.apo import APO# Add .env to .gitignore

        results["agentlightning"] = Trueecho ".env" >> .gitignore

        print(f"  ✅ Agent Lightning {agentlightning.__version__} installed")

        print("  ✅ APO algorithm available")# Set proper file permissions

    except ImportError as e:chmod 600 .env

        results["agentlightning"] = False

        print(f"  ❌ Agent Lightning installation issue: {e}")# Never commit API keys to version control

    git check-ignore .env  # Should output: .env

    # Check optional dependencies```

    print("\n🔧 Checking Optional Components...")

    ### 2. Use Environment-Specific Keys

    # AgentOps

    agentops_key = os.getenv("AGENTOPS_API_KEY")```bash

    results["agentops"] = bool(agentops_key)# Development environment

    print(f"  {'✅' if agentops_key else '⚠️'} AgentOps: {'Configured' if agentops_key else 'Not configured (optional)'}")AZURE_OPENAI_API_KEY=dev_key_here

    

    return results# Production environment  

AZURE_OPENAI_API_KEY=prod_key_here

def print_summary(results: Dict[str, bool]):```

    """Print validation summary."""

    total_checks = len(results)### 3. Rotate Keys Regularly

    passed_checks = sum(results.values())

    ```bash

    print(f"\n📋 Validation Summary: {passed_checks}/{total_checks} checks passed")# Update API keys in Azure portal

    # Update .env file with new keys

    if passed_checks == total_checks:# Test connectivity after rotation

        print("🎉 All validations passed! Your environment is ready.")```

        return 0

    else:## Advanced Configuration

        print("⚠️ Some validations failed. Please review the issues above.")

        ### Multiple Azure OpenAI Resources

        # Critical vs non-critical failures

        critical_failures = [```bash

            key for key, passed in results.items() # Primary resource

            if not passed and key in ["azure_connection", "agentlightning"]AZURE_OPENAI_ENDPOINT=https://primary-resource.openai.azure.com/

        ]AZURE_OPENAI_API_KEY=primary_key

        

        if critical_failures:# Secondary resource (for failover)

            print("❌ Critical failures detected. Please fix these before proceeding.")AZURE_OPENAI_ENDPOINT_SECONDARY=https://secondary-resource.openai.azure.com/

            return 1AZURE_OPENAI_API_KEY_SECONDARY=secondary_key

        else:```

            print("ℹ️ Only non-critical issues detected. You can proceed with caution.")

            return 0### Model-Specific Deployments



if __name__ == "__main__":```bash

    # Load environment if .env file exists# Different deployments for different models

    try:AZURE_OPENAI_GPT4_DEPLOYMENT=gpt-4o-deployment

        from dotenv import load_dotenvAZURE_OPENAI_GPT35_DEPLOYMENT=gpt-35-turbo-deployment

        load_dotenv()AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002

    except ImportError:```

        pass

    ### Region-Specific Configuration

    results = validate_environment()

    exit_code = print_summary(results)```bash

    sys.exit(exit_code)# US East deployment

```AZURE_OPENAI_ENDPOINT_US=https://us-east-resource.openai.azure.com/

AZURE_OPENAI_API_KEY_US=us_key

```bash

# Run validation# Europe deployment

python validate_config.pyAZURE_OPENAI_ENDPOINT_EU=https://eu-west-resource.openai.azure.com/

```AZURE_OPENAI_API_KEY_EU=eu_key

```

## 🚀 Production Configuration

## Integration Examples

### Step 1: Azure Key Vault Integration

### Example 1: APO Training with Azure OpenAI

#### Create Key Vault

```bash```bash

# Create Key Vault# Create .env for APO training

KEY_VAULT_NAME="kv-agentlightning-prod"cat > .env << EOF

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

az keyvault create \AZURE_OPENAI_API_KEY=your_key

  --name $KEY_VAULT_NAME \AZURE_OPENAI_API_VERSION=2024-08-01-preview

  --resource-group $RESOURCE_GROUP \AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

  --location $LOCATION \EOF

  --sku standard

# Run APO training

# Store secretsuv run python examples/apo/room_selector_apo_persistent.py

az keyvault secret set \```

  --vault-name $KEY_VAULT_NAME \

  --name "azure-openai-api-key" \### Example 2: Multi-Environment Setup

  --value "your_api_key_here"

```bash

az keyvault secret set \# Development environment (.env.dev)

  --vault-name $KEY_VAULT_NAME \cat > .env.dev << EOF

  --name "azure-openai-endpoint" \AZURE_OPENAI_ENDPOINT=https://dev-resource.openai.azure.com/

  --value "https://your-resource.openai.azure.com/"AZURE_OPENAI_API_KEY=dev_key

```AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo

EOF

#### Use Key Vault in Application

```python# Production environment (.env.prod)  

# key_vault_config.pycat > .env.prod << EOF

from azure.keyvault.secrets import SecretClientAZURE_OPENAI_ENDPOINT=https://prod-resource.openai.azure.com/

from azure.identity import DefaultAzureCredentialAZURE_OPENAI_API_KEY=prod_key

import osAZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

EOF

def load_config_from_keyvault():

    """Load configuration from Azure Key Vault."""# Load specific environment

    key_vault_name = os.getenv("KEY_VAULT_NAME")uv run python -c "

    if not key_vault_name:from dotenv import load_dotenv

        raise ValueError("KEY_VAULT_NAME environment variable required")load_dotenv('.env.prod')  # or .env.dev

    # Your code here

    # Initialize Key Vault client"

    credential = DefaultAzureCredential()```

    client = SecretClient(

        vault_url=f"https://{key_vault_name}.vault.azure.net/",## See Also

        credential=credential

    )- `INSTALLATION_GUIDE.md` - Complete installation instructions

    - `examples/apo/AOAI/docs/APO_PERSISTENCE.md` - APO training with Azure OpenAI

    # Retrieve secrets- `WSL_SETUP_GUIDE.md` - Windows Subsystem for Linux setup

    config = {````
        'api_key': client.get_secret("azure-openai-api-key").value,
        'endpoint': client.get_secret("azure-openai-endpoint").value,
        'deployment_name': client.get_secret("azure-openai-deployment-name").value
    }
    
    return config
```

### Step 2: Managed Identity Setup

#### Create Managed Identity
```bash
# Create user-assigned managed identity
IDENTITY_NAME="id-agentlightning-prod"

az identity create \
  --name $IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP

# Get identity client ID
IDENTITY_CLIENT_ID=$(az identity show \
  --name $IDENTITY_NAME \
  --resource-group $RESOURCE_GROUP \
  --query clientId \
  --output tsv)

# Assign role to Azure OpenAI
az role assignment create \
  --assignee $IDENTITY_CLIENT_ID \
  --role "Cognitive Services OpenAI User" \
  --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.CognitiveServices/accounts/$AOAI_NAME"
```

#### Configure Application for Managed Identity
```python
# managed_identity_config.py
from azure.identity import ManagedIdentityCredential
from openai import AzureOpenAI
import os

def create_azure_client_with_managed_identity():
    """Create Azure OpenAI client using managed identity."""
    
    # Use managed identity for authentication
    credential = ManagedIdentityCredential(
        client_id=os.getenv("AZURE_CLIENT_ID")  # Optional: specify client ID
    )
    
    # Get access token
    token = credential.get_token("https://cognitiveservices.azure.com/.default")
    
    # Create client with token
    client = AzureOpenAI(
        api_key=f"Bearer {token.token}",
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    
    return client
```

### Step 3: Monitoring and Alerting

#### Application Insights Integration
```python
# monitoring_config.py
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os

def setup_monitoring():
    """Configure Application Insights monitoring."""
    
    # Get instrumentation key
    instrumentation_key = os.getenv("APPINSIGHTS_INSTRUMENTATION_KEY")
    if not instrumentation_key:
        return
    
    # Configure Azure Log Handler
    logger = logging.getLogger(__name__)
    logger.addHandler(AzureLogHandler(
        connection_string=f"InstrumentationKey={instrumentation_key}"
    ))
    
    # Custom telemetry
    from opencensus.ext.azure.trace_exporter import AzureExporter
    from opencensus.trace.samplers import ProbabilitySampler
    from opencensus.trace.tracer import Tracer
    
    tracer = Tracer(
        exporter=AzureExporter(
            connection_string=f"InstrumentationKey={instrumentation_key}"
        ),
        sampler=ProbabilitySampler(1.0)
    )
    
    return tracer
```

## 🚨 Troubleshooting

### Common Configuration Issues

#### Invalid Endpoint Format
**Problem**: Endpoint URL format errors
**Solution**:
```bash
# Correct format
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# Common mistakes to avoid
# ❌ Missing https://
# ❌ Wrong domain (.azure.com instead of .openai.azure.com)
# ❌ Extra paths or parameters
```

#### Deployment Name Mismatch
**Problem**: Model deployment not found
**Solution**:
```bash
# List deployments
az cognitiveservices account deployment list \
  --name $AOAI_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "[].name" \
  --output table

# Verify deployment name matches environment variable
echo $AZURE_OPENAI_DEPLOYMENT_NAME
```

#### API Key Issues
**Problem**: Authentication failures
**Solutions**:
1. **Regenerate Keys**: Use Azure Portal to regenerate API keys
2. **Check Permissions**: Ensure proper role assignments
3. **Verify Scope**: Check if keys are scoped correctly

#### Rate Limiting
**Problem**: 429 Too Many Requests errors
**Solutions**:
```python
# Implement exponential backoff
import time
import random

def api_call_with_backoff(client, **kwargs):
    max_retries = 3
    base_delay = 1
    
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
            raise e
```

### Environment-Specific Issues

#### WSL File Permissions
```bash
# Fix WSL file permission issues
chmod 600 .env
sudo chown $USER:$USER .env
```

#### Path Resolution
```bash
# Use absolute paths in WSL
cd /mnt/c/path/to/project
# Not: cd C:\path\to\project
```

#### Network Connectivity
```bash
# Test connectivity to Azure
curl -I https://your-resource.openai.azure.com/
nslookup your-resource.openai.azure.com
```

## 📚 Best Practices

### Security
1. **Never commit API keys** to version control
2. **Use Key Vault** for production secrets
3. **Implement managed identity** for Azure resources
4. **Rotate keys regularly** (quarterly recommended)
5. **Monitor access patterns** for anomalies

### Performance
1. **Cache responses** when appropriate
2. **Implement connection pooling** for high-volume applications
3. **Use appropriate token limits** to control costs
4. **Monitor rate limits** and implement backoff strategies

### Monitoring
1. **Enable Application Insights** for production workloads
2. **Set up alerts** for errors and performance issues
3. **Track token usage** for cost management
4. **Monitor model performance** and accuracy

### Development
1. **Use environment-specific configurations** (dev/staging/prod)
2. **Implement comprehensive logging** at appropriate levels
3. **Validate configurations** before deployment
4. **Test failover scenarios** with secondary keys

---

*This environment setup guide provides comprehensive Azure OpenAI configuration for production-ready Agent Lightning applications with proper security, monitoring, and performance optimization.*