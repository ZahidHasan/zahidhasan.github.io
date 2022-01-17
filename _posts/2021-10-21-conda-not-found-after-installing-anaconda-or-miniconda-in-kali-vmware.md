---
published: true
key: '22'
title: 'conda not found after installing Anaconda/Miniconda in Kali '
tags:
  - Linux
  - Kali
  - Python
  - conda
---
## conda not found

You download anaconda/miniconda distribution, install them following on-screen instructions but at the end what you get is 'conda not found'.

### Open .bashrc file in your home directory (hidden) and copy 

```ps

>>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/kali/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kali/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kali/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kali/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

### Now open .zshrc file in home and paste the coppied code at the end.

Thats it! conda now found
