# torchcraft-py

Python wrapper for [TorchCraft](https://github.com/TorchCraft/TorchCraft), a bridge between Torch and StarCraft for AI research.

## Installation

1. Install [TorchCraft](https://github.com/TorchCraft/TorchCraft) and its dependencies. You can skip the Torch client part. 

2. Install the package itself:
    ```
    git clone https://github.com/deepcraft/torchcraft-py.git
    cd torchcraft-py
    pip install -e .
    ```

## Usage
1. Start StarCraft server with BWAPI by Chaoslauncher.

2. Run examples:

    ```
    cd examples
    python attack_weakest.py --ip $server_ip --port $server_port
    ```
    
    The `$server_ip` and `$server_port` are the ip and port of the server running StarCraft.