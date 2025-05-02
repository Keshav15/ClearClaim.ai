# Auto-generate the modular project structure for ClearClaim.AI
# Run this script in your VS Code terminal: python init_structure.py

import os

# Define the desired directory structure
PROJECT_NAME = "clearclaim_ai"
MODULES = {
    "agents": [
        "eligibility",
        "evidence",
        "filing",
        "monitor",
        "denial_analyzer",
        "appeal"
    ],
    "core": [],
    "utils": [],
    "config": [],
    "models": [],
    "logs": [],
    "dashboard": [],
    "scripts": []
}

# Files to create at the project root
ROOT_FILES = [
    "README.md",
    "requirements.txt",
    "main.py",
    ".gitignore"
]

# Function to create directories and __init__.py

def create_structure(root: str):
    os.makedirs(root, exist_ok=True)

    # Create root-level files
    for fname in ROOT_FILES:
        fpath = os.path.join(root, fname)
        if not os.path.exists(fpath):
            open(fpath, "w").close()

    # Create modules and submodules
    for module, submodules in MODULES.items():
        module_path = os.path.join(root, module)
        os.makedirs(module_path, exist_ok=True)

        # __init__.py for module
        open(os.path.join(module_path, "__init__.py"), "w").close()

        # Submodules directories
        for sub in submodules:
            sub_path = os.path.join(module_path, sub)
            os.makedirs(sub_path, exist_ok=True)
            open(os.path.join(sub_path, "__init__.py"), "w").close()
            # create placeholder agent file
            if module == "agents":
                agent_file = sub + "_agent.py"
                with open(os.path.join(sub_path, agent_file), "w") as f:
                    f.write(f"# {sub.title().replace('_', ' ')} Agent module\n")

# Entry point
if __name__ == "__main__":
    create_structure(PROJECT_NAME)
    print(f"Project structure for '{PROJECT_NAME}' created successfully.")
