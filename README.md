# torchcraft-py

Python wrapper for [TorchCraft](https://github.com/TorchCraft/TorchCraft), a bridge between Torch and StarCraft for AI research.

## Installation

1. Install [TorchCraft](https://github.com/TorchCraft/TorchCraft) and its dependencies. You can skip the Torch client part. 

2. Install the package itself:
    ```
    git clone http://gitlab.alibaba-inc.com/cogcom/torchcraft-py.git
    cd torchcraft-py
    pip install -e .
    ```

## Usage
1. Start starcraft with BWAPI by Chaoslauncher.
2. Run

    ```
    cd examples
    python attack_weakest.py -s $server_ip
    ```
    
    The `$server_ip` is the ip address of the machine running StarCraft.