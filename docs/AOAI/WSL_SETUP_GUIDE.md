# WSL Setup Guide for Agent Lightning and Azure OpenAI# Windows Subsystem for Linux (WSL) Setup Guide



This comprehensive guide walks you through setting up Windows Subsystem for Linux (WSL2) for optimal development with Agent Lightning and Azure OpenAI integration.This guide provides comprehensive instructions for setting up WSL2 with Ubuntu for optimal Agent Lightning development.



## 🎯 Overview## Prerequisites



WSL2 provides the best development experience for Agent Lightning on Windows by offering:- **Windows 11** (recommended) or **Windows 10** version 2004 or higher

- **Native Linux environment** with full Python ecosystem support- **Administrator access** on Windows machine

- **Excellent performance** with native file system access- **At least 8GB RAM** for comfortable development

- **Seamless integration** with VS Code and development tools

- **Docker support** for containerized deployments## WSL2 Installation

- **Git integration** with proper line ending handling

### 1. Enable WSL and Virtual Machine Platform

## 📋 Prerequisites

Open PowerShell as Administrator and run:

### System Requirements

- **Windows 11** or **Windows 10** version 2004 and higher (Build 19041 and higher)```powershell

- **64-bit processor** with virtualization capabilities# Enable WSL feature

- **4GB RAM minimum** (8GB+ recommended for optimal performance)dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

- **Virtualization enabled** in BIOS/UEFI settings

- **Administrator privileges** for initial setup# Enable Virtual Machine Platform

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

### Check Windows Version

```powershell# Restart Windows

# Run in PowerShellshutdown /r /t 0

winver```



# Or check build number### 2. Set WSL 2 as Default

[System.Environment]::OSVersion.Version

```After restart, open PowerShell as Administrator:



## 🚀 WSL2 Installation```powershell

# Set WSL 2 as default version

### Step 1: Enable Required Windows Featureswsl --set-default-version 2



#### Option A: Using PowerShell (Recommended)# Update WSL kernel (if needed)

```powershellwsl --update

# Run PowerShell as Administrator```

# Enable WSL and Virtual Machine Platform

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart### 3. Install Ubuntu 22.04 LTS

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

```powershell

# Restart required# Install Ubuntu 22.04 LTS from Microsoft Store or command line

Restart-Computerwsl --install -d Ubuntu-22.04

```

# Or download and install manually

#### Option B: Using Windows Features GUI# Visit Microsoft Store and search for "Ubuntu 22.04 LTS"

1. **Open Windows Features**: Press `Win + R`, type `optionalfeatures`, press Enter```

2. **Enable Features**:

   - ☑️ Windows Subsystem for Linux### 4. Initial Ubuntu Setup

   - ☑️ Virtual Machine Platform

3. **Restart** your computerWhen Ubuntu first launches:



### Step 2: Install WSL21. **Create user account** (enter username and password)

2. **Update system packages**:

#### Download and Install WSL2 Kernel Update

1. **Download**: [WSL2 Linux kernel update package](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)```bash

2. **Install**: Run the downloaded MSI filesudo apt update && sudo apt upgrade -y

3. **Verify**: Installation should complete without errors```



#### Set WSL2 as Default Version## Development Environment Setup

```powershell

# Set WSL2 as default version### 1. Install Essential Tools

wsl --set-default-version 2

```bash

# Verify WSL installation# Install build essentials

wsl --statussudo apt install -y build-essential curl wget git vim

```

# Install Python development dependencies

### Step 3: Install Ubuntu 22.04 LTSsudo apt install -y python3-dev python3-pip python3-venv



#### Option A: Using Microsoft Store (Recommended)# Install additional utilities

1. **Open Microsoft Store**sudo apt install -y htop tree unzip

2. **Search** for "Ubuntu 22.04 LTS"```

3. **Install** the application

4. **Launch** Ubuntu from Start Menu### 2. Install Miniconda



#### Option B: Using Command Line```bash

```powershell# Download Miniconda

# List available distributionswget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

wsl --list --online

# Install Miniconda

# Install Ubuntu 22.04bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3

wsl --install -d Ubuntu-22.04

```# Initialize conda

$HOME/miniconda3/bin/conda init bash

### Step 4: Initial Ubuntu Configuration

# Restart shell or reload bashrc

#### First Launch Setupsource ~/.bashrc

```bash

# Ubuntu will prompt for user creation# Verify installation

# Enter your preferred username (lowercase, no spaces)conda --version

# Set a strong password (you'll need this for sudo)```



# Example:### 3. Configure Git

Username: yourusername

Password: [your secure password]```bash

```# Set up Git credentials

git config --global user.name "Your Name"

#### Update System Packagesgit config --global user.email "your.email@example.com"

```bash

# Update package lists and upgrade system# Configure line endings for cross-platform development

sudo apt update && sudo apt upgrade -ygit config --global core.autocrlf input

```

# Install essential development tools

sudo apt install -y \## Agent Lightning Specific Setup

    curl \

    wget \### 1. Create Conda Environment

    git \

    build-essential \```bash

    software-properties-common \# Create dedicated environment for Agent Lightning

    apt-transport-https \conda create -n agentlightning python=3.10 -y

    ca-certificates \conda activate agentlightning

    gnupg \

    lsb-release# Verify Python version

```python --version  # Should show Python 3.10.x

```

## 🐍 Python Development Environment Setup

### 2. Install PyTorch (CPU Version)

### Step 1: Install Python 3.11+

```bash

#### Using deadsnakes PPA (Recommended)# Install CPU-only PyTorch for WSL compatibility

```bashpip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Add deadsnakes PPA for latest Python versions

sudo add-apt-repository ppa:deadsnakes/ppa -y# Verify PyTorch installation

sudo apt updatepython -c "import torch; print(f'PyTorch {torch.__version__} installed successfully')"

```

# Install Python 3.11 and development packages

sudo apt install -y \### 3. Clone and Setup Agent Lightning

    python3.11 \

    python3.11-dev \```bash

    python3.11-venv \# Navigate to a suitable directory (e.g., Windows drive mount)

    python3.11-distutils \cd /mnt/c/Users/YourUsername/Projects

    python3-pip

# Clone agent-lightning repository

# Set Python 3.11 as defaultgit clone https://github.com/ushakrishnan/agent-lightning.git

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1cd agent-lightning

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Install in development mode with all extras

# Verify installationpip install -e .[apo,verl,dev,agents]

python --version

python3 --version# Install additional Azure OpenAI dependencies

```pip install openai python-dotenv

```

#### Install pip and setuptools

```bash## WSL2 Optimization

# Download and install pip

curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11### 1. Configure WSL Memory Usage



# Upgrade pip and install essential packagesCreate or edit `%UserProfile%\.wslconfig` on Windows:

python -m pip install --upgrade pip setuptools wheel

``````ini

[wsl2]

### Step 2: Install UV Package Managermemory=6GB

processors=4

```bashswap=2GB

# Install UV package manager (fast Python package installer)localhostForwarding=true

curl -LsSf https://astral.sh/uv/install.sh | sh```



# Add UV to PATH### 2. Enable Systemd (Optional)

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

source ~/.bashrcIn Ubuntu, edit `/etc/wsl.conf`:



# Verify installation```bash

uv --versionsudo nano /etc/wsl.conf

``````



### Step 3: Install Conda (Optional but Recommended)Add:

```ini

#### Download and Install Miniconda[boot]

```bashsystemd=true

# Download Miniconda installer```

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Restart WSL:

# Install Miniconda```powershell

bash Miniconda3-latest-Linux-x86_64.sh# In Windows PowerShell

wsl --shutdown

# Follow the installer prompts:wsl

# - Accept license terms```

# - Choose installation location (default: /home/username/miniconda3)

# - Allow installer to initialize conda### 3. File System Performance



# Restart shell or source bashrc- **Use Linux file system** (`/home/`) for better performance

source ~/.bashrc- **Avoid Windows drives** (`/mnt/c/`) for intensive operations

- **Use symbolic links** if you need to access files from Windows

# Verify installation

conda --version```bash

```# Create symlink from Windows to Linux filesystem

ln -s /mnt/c/Users/YourUsername/Projects ~/projects-windows

#### Configure Conda```

```bash

# Update conda## VS Code Integration

conda update -n base -c defaults conda

### 1. Install VS Code Extensions

# Configure conda channels

conda config --add channels conda-forgeIn VS Code on Windows, install:

conda config --set channel_priority strict- **WSL** extension

- **Python** extension

# Create environment for Agent Lightning- **Remote - WSL** extension

conda create -n agentlightning python=3.11 -y

conda activate agentlightning### 2. Open Project in WSL

```

```bash

## 🛠️ Development Tools Configuration# From WSL terminal, open VS Code in current directory

code .

### Step 1: Git Configuration

# Or open specific project

#### Install and Configure Gitcode /path/to/agent-lightning

```bash```

# Git should already be installed, but verify

git --version### 3. Configure Python Interpreter



# Configure Git (replace with your information)In VS Code:

git config --global user.name "Your Name"1. Press `Ctrl+Shift+P`

git config --global user.email "your.email@example.com"2. Type "Python: Select Interpreter"

3. Choose the conda environment: `/home/username/miniconda3/envs/agentlightning/bin/python`

# Configure line endings for cross-platform compatibility

git config --global core.autocrlf input## Testing Installation

git config --global core.eol lf

### 1. Verify Environment

# Configure default branch name

git config --global init.defaultBranch main```bash

# Activate conda environment

# Optional: Configure credential helperconda activate agentlightning

git config --global credential.helper store

```# Check installations

python -c "import agentlightning; print('✅ Agent Lightning')"

#### SSH Key Setup (Recommended)python -c "import torch; print(f'✅ PyTorch {torch.__version__}')"

```bashpython -c "import openai; print('✅ OpenAI SDK')"

# Generate SSH key for GitHub/Azure DevOps

ssh-keygen -t ed25519 -C "your.email@example.com"# Check conda environment

conda info --envs

# Start SSH agent and add key```

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519### 2. Run Agent Lightning Tests



# Display public key to add to your Git provider```bash

cat ~/.ssh/id_ed25519.pub# Navigate to examples directory

```cd examples/apo



### Step 2: VS Code Integration# Test APO functionality

uv run python room_selector_apo_persistent.py

#### Install VS Code (Windows)```

1. **Download**: [VS Code for Windows](https://code.visualstudio.com/)

2. **Install** with default settingsExpected output:

3. **Launch** VS Code```

🔧 Loading optimal configuration from training history...

#### Install WSL Extension🎯 Starting APO training with Azure OpenAI

```bash✅ APO training completed successfully

# In VS Code, install the WSL extension```

# Or use command palette: Ctrl+Shift+P -> "Extensions: Install Extensions"

# Search for "WSL" and install the official Microsoft extension## Common Issues and Solutions

```

### PyTorch Import Hangs

#### Connect to WSL

```bash**Problem**: PyTorch hangs during import in WSL2

# From WSL terminal, open current directory in VS Code

code .**Solution**:

```bash

# Or from VS Code, use Ctrl+Shift+P -> "WSL: Connect to WSL"# Uninstall current PyTorch

```pip uninstall torch torchvision torchaudio



#### Recommended VS Code Extensions for WSL# Reinstall CPU-only version

```bashpip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install extensions from WSL terminal```

code --install-extension ms-python.python

code --install-extension ms-python.flake8### Memory Issues

code --install-extension ms-python.black-formatter

code --install-extension ms-toolsai.jupyter**Problem**: WSL runs out of memory during training

code --install-extension ms-vscode.azure-account

code --install-extension GitHub.copilot**Solution**:

```1. Increase WSL memory limit in `.wslconfig`

2. Restart WSL: `wsl --shutdown` then `wsl`

### Step 3: Docker Support (Optional)3. Use smaller batch sizes in training



#### Install Docker Engine### File Permission Issues

```bash

# Add Docker GPG key**Problem**: Permission denied errors when accessing Windows files

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

**Solution**:

# Add Docker repository```bash

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null# Fix file permissions

sudo chmod +x /path/to/file

# Install Docker

sudo apt update# Or work within Linux filesystem

sudo apt install -y docker-ce docker-ce-cli containerd.iocp /mnt/c/path/to/project ~/project-copy

```

# Add user to docker group

sudo usermod -aG docker $USER### Conda Environment Issues



# Start Docker service**Problem**: Conda environments not activating properly

sudo systemctl enable docker

sudo systemctl start docker**Solution**:

```bash

# Verify installation (may need to restart WSL)# Reinitialize conda

docker --versionconda init bash

```source ~/.bashrc



## 🏗️ Agent Lightning Environment Setup# Recreate environment if needed

conda env remove -n agentlightning

### Step 1: Create Project Structureconda create -n agentlightning python=3.10 -y

```

```bash

# Create development directory## Performance Tips

mkdir -p ~/development/agentlightning

cd ~/development/agentlightning### 1. File System Location



# Clone Agent Lightning repository- **Store projects** in Linux filesystem (`/home/`) for better I/O performance

git clone https://github.com/ushakrishnan/agent-lightning.git- **Use Windows filesystem** (`/mnt/c/`) only for file sharing

cd agent-lightning

```### 2. Memory Management



### Step 2: Set Up Python Environment- **Monitor memory usage** with `htop`

- **Close unnecessary applications** in Windows

#### Using UV (Recommended)- **Use swap file** for large training jobs

```bash

# Create virtual environment with UV### 3. Network Configuration

uv venv --python 3.11

source .venv/bin/activate- **Use localhost forwarding** for web applications

- **Configure firewall** if needed for external access

# Install Agent Lightning with APO support- **Test connectivity** with Azure OpenAI endpoints

uv add "agentlightning[apo]==0.2.2"

## Advanced Configuration

# Install additional dependencies

uv add python-dotenv azure-identity azure-keyvault-secrets### 1. Custom Shell Setup

```

Add to `~/.bashrc`:

#### Using Conda```bash

```bash# Auto-activate conda environment

# Create conda environmentconda activate agentlightning

conda create -n agentlightning python=3.11 -y

conda activate agentlightning# Useful aliases

alias ll='ls -la'

# Install Agent Lightningalias la='ls -la'

pip install "agentlightning[apo]==0.2.2"alias ..='cd ..'

alias agl='cd ~/agent-lightning'

# Install additional dependencies

pip install python-dotenv azure-identity azure-keyvault-secrets# Set environment variables

```export EDITOR=vim

export PYTHONPATH="${PYTHONPATH}:/home/username/agent-lightning"

### Step 3: Configure Environment Variables```



```bash### 2. Development Shortcuts

# Create .env file for Azure OpenAI configuration

cat > .env << 'EOF'Create useful scripts in `~/bin/`:

# Azure OpenAI Configuration```bash

AZURE_OPENAI_API_KEY=your_api_key_here#!/bin/bash

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/# ~/bin/apo-test

AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-minicd ~/agent-lightning/examples/apo

AZURE_OPENAI_API_VERSION=2024-02-15-previewconda activate agentlightning

uv run python room_selector_apo_persistent.py

# Development Settings```

LOG_LEVEL=INFO

DEVELOPMENT_MODE=trueMake executable:

EOF```bash

chmod +x ~/bin/apo-test

# Secure the environment file```

chmod 600 .env

```### 3. Backup and Sync



### Step 4: Verify Installation```bash

# Create backup script

```bash#!/bin/bash

# Test Python and Agent Lightning# Backup conda environments and project files

python -c "tar -czf backup-$(date +%Y%m%d).tar.gz ~/miniconda3/envs ~/agent-lightning

import agentlightning```

print(f'Agent Lightning version: {agentlightning.__version__}')

## Troubleshooting Resources

from agentlightning.algorithm.apo import APO

print('APO algorithm available')### WSL Issues



from openai import AzureOpenAI1. **Check WSL status**: `wsl --status`

print('Azure OpenAI SDK available')2. **View running distributions**: `wsl --list --running`

3. **Restart WSL**: `wsl --shutdown` then `wsl`

print('✅ All components installed successfully')

"### Agent Lightning Issues

```

1. **Check environment**: `conda info --envs`

## 🚀 Performance Optimization2. **Verify installations**: Run test suite

3. **Review logs**: Check `apo.log` and terminal output

### Step 1: WSL Configuration

### Getting Help

#### Configure WSL Memory and CPU Limits

```bash- **WSL Documentation**: [Microsoft WSL Docs](https://docs.microsoft.com/en-us/windows/wsl/)

# Create or edit .wslconfig file in Windows user directory- **Agent Lightning Issues**: [GitHub Issues](https://github.com/microsoft/agent-lightning/issues)

# From WSL, access Windows user directory- **Conda Documentation**: [Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)

cd /mnt/c/Users/$(whoami)

## See Also

# Create .wslconfig file

cat > .wslconfig << 'EOF'- `INSTALLATION_GUIDE.md` - Agent Lightning installation steps

[wsl2]- `AZURE_ENV_SETUP.md` - Azure OpenAI environment configuration

# Limit memory usage (adjust based on your system)- `examples/apo/AOAI/docs/APO_PERSISTENCE.md` - APO training and optimization guide
memory=8GB

# Limit CPU usage
processors=4

# Enable swap file
swap=2GB

# Disable page reporting
pageReporting=false

# Disable nested virtualization
nestedVirtualization=false
EOF
```

#### Restart WSL to Apply Changes
```powershell
# From PowerShell (Windows)
wsl --shutdown

# Restart your WSL distribution
wsl -d Ubuntu-22.04
```

### Step 2: File System Optimization

#### Use WSL File System for Development
```bash
# Always work in WSL file system (/home/username) for best performance
# Avoid using Windows file system (/mnt/c/) for active development

# Good: /home/username/development/agentlightning
# Avoid: /mnt/c/Users/username/development/agentlightning

# Move existing projects if needed
mv /mnt/c/path/to/project ~/development/
```

#### Configure Git for Performance
```bash
# Optimize Git for large repositories
git config --global core.preloadindex true
git config --global core.fscache true
git config --global gc.auto 256

# Configure file system monitoring
git config --global core.fsmonitor true
```

### Step 3: Python Performance Tuning

#### Configure pip for Speed
```bash
# Create pip configuration
mkdir -p ~/.config/pip
cat > ~/.config/pip/pip.conf << 'EOF'
[global]
cache-dir = ~/.cache/pip
disable-pip-version-check = true
timeout = 60

[install]
compile = false
use-pep517 = true
EOF
```

#### Optimize Python Startup
```bash
# Add to ~/.bashrc for faster Python startup
echo 'export PYTHONDONTWRITEBYTECODE=1' >> ~/.bashrc
echo 'export PYTHONUNBUFFERED=1' >> ~/.bashrc
source ~/.bashrc
```

## 🚨 Troubleshooting

### Common WSL Issues

#### WSL Installation Fails
**Problem**: "WSL 2 requires an update to its kernel component"
**Solution**:
1. Download and install the [WSL2 kernel update](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
2. Restart your computer
3. Try the installation again

#### Ubuntu Fails to Launch
**Problem**: "The attempted operation is not supported for the type of object referenced"
**Solution**:
```powershell
# Enable required Windows features
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

# Restart and try again
```

#### Permission Denied Errors
**Problem**: Permission errors when accessing files
**Solution**:
```bash
# Fix file permissions
sudo chown -R $USER:$USER ~/development
chmod -R 755 ~/development

# For specific files
chmod 600 .env
chmod +x scripts/*.sh
```

### Performance Issues

#### Slow File Operations
**Problem**: File operations are slow when working with Windows file system
**Solution**:
```bash
# Move your project to WSL file system
mv /mnt/c/path/to/project ~/development/

# Always use WSL paths for development
cd ~/development/agentlightning
```

#### High Memory Usage
**Problem**: WSL uses too much memory
**Solution**:
```bash
# Edit .wslconfig to limit memory usage
# (See Performance Optimization section above)

# Or temporarily free memory
echo 1 | sudo tee /proc/sys/vm/drop_caches
```

#### Network Connectivity Issues
**Problem**: Cannot reach external services
**Solution**:
```bash
# Check DNS resolution
nslookup google.com

# If DNS issues, configure nameservers
sudo nano /etc/resolv.conf
# Add: nameserver 8.8.8.8

# Restart WSL networking
sudo service networking restart
```

### Agent Lightning Specific Issues

#### Import Errors
**Problem**: Cannot import agentlightning modules
**Solution**:
```bash
# Verify you're in the correct environment
which python
pip list | grep agentlightning

# Reinstall if necessary
pip uninstall agentlightning
pip install "agentlightning[apo]==0.2.2"
```

#### Azure OpenAI Connection Issues
**Problem**: Cannot connect to Azure OpenAI from WSL
**Solution**:
```bash
# Test connectivity
curl -I https://your-resource.openai.azure.com/

# Check environment variables
env | grep AZURE_OPENAI

# Verify SSL certificates
python -c "import ssl; print(ssl.get_default_verify_paths())"
```

## 📚 Best Practices

### Development Workflow
1. **Use WSL file system** for all development work
2. **Keep projects organized** in ~/development/ directory
3. **Use virtual environments** for each project
4. **Configure VS Code** to work seamlessly with WSL
5. **Regular backups** of important work

### Security
1. **Secure environment files** with restrictive permissions
2. **Use SSH keys** for Git authentication
3. **Keep system updated** with regular apt upgrades
4. **Avoid storing secrets** in version control

### Performance
1. **Limit WSL resource usage** based on your system
2. **Use WSL file system** for active development
3. **Configure caching** for package managers
4. **Monitor resource usage** with htop or similar tools

### Maintenance
1. **Regular system updates**: `sudo apt update && sudo apt upgrade`
2. **Clean package caches**: `sudo apt autoremove && sudo apt autoclean`
3. **Monitor disk usage**: `df -h` and `du -sh ~/`
4. **Backup important configurations**: ~/.bashrc, .env files, etc.

## 🎯 Next Steps

After completing this WSL setup:

1. **Follow the [Installation Guide](INSTALLATION_GUIDE.md)** to set up Agent Lightning
2. **Configure Azure OpenAI** using the [Azure Environment Setup](AZURE_ENV_SETUP.md)
3. **Run the examples** in `examples/apo/AOAI/` to verify everything works
4. **Start developing** your own Agent Lightning applications

## 📖 Additional Resources

### Documentation
- [WSL Documentation](https://docs.microsoft.com/windows/wsl/)
- [VS Code WSL Tutorial](https://docs.microsoft.com/windows/wsl/tutorials/wsl-vscode)
- [Python Development in WSL](https://docs.microsoft.com/windows/python/web-frameworks)

### Tools and Utilities
- [Windows Terminal](https://docs.microsoft.com/windows/terminal/) - Enhanced terminal experience
- [Oh My Zsh](https://ohmyz.sh/) - Enhanced shell with themes and plugins
- [Homebrew for Linux](https://brew.sh/) - Package manager alternative

---

*This WSL setup guide provides a comprehensive foundation for Agent Lightning development on Windows with optimal performance, security, and developer experience.*