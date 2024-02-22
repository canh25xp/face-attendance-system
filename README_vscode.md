# Setup for VScode
## 1. Clone projects and submodule
```bash
git clone https://github.com/canh25xp/face-attendance-system -b video --depth 1
cd face-attendance-system
git submodule update --init
```

## Create venv and install requirements
TODO : Add instruction for creating venv
```bash
pip install -r Silent-Face-Anti-Spoofing/requirements.txt
pip install cmake
pip install -r requirements.txt
```

## Install dlib
```bash
git clone https://github.com/z-mahmud22/Dlib_Windows_Python3.x
cd Dlib_Windows_Python3.x
python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
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