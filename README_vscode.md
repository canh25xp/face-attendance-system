# Setup for VScode
## 1. Clone projects and submodule
```bash
git clone https://github.com/canh25xp/face-attendance-system -b video --depth 1
cd face-attendance-system
git submodule update --init
```
## 2. Add Silent-Face-Anti-Spoofing to PYTHONPATH in launch.json
```bash
touch .vscode/launch.json
```
Add the following lines to the created file
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Custom",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/Silent-Face-Anti-Spoofing"
            },
        }
    ]
}
```
## 3. Open the main.py file and launch the `Python: Custom` configurations.
```
Ctrl+F5
```