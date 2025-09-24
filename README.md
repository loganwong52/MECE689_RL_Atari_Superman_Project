# MECE689_RL_Atari_Superman_Project

**Author:** Logan Wong
<br>
**Date:** September 24, 2025
<br>
**Course:** MECE 689: Reinforcement Learning
<br>
**Instructor:** Professor Ali Baheri

# Overview
This repository contains implementations of reinforcement learning algorithms, DQN, PPO, A2C, and QR-DQN, applied to the Atari 2600 game Superman using OpenAI Gymnasium and Stable-Baselines3.

## File structure
```
MECE689_RL_Atari_Superman_Project/ 
├── train_baseline.ipynb/
├── train_baseline_action_mask.ipynb/
├── train_baseline.ipynb/
├── eval_baseline.ipynb/
├── PPO_Attempt.ipynb/
├── eval_PPO.ipynb/
├── A2C_Attempt.ipynb/
├── eval_A2C.ipynb/
├── QRDQN_Attempt.ipynb/
├── eval_QRDQN.ipynb/
```

# Installation
git clone https://github.com/loganwong52/MECE689_RL_Atari_Superman_Project
<br>
cd MECE689_RL_Atari_Superman_Project
<br>
conda create -n superman_env python=3.9
<br>
conda activate superman_env
<br>
pip install -r requirements.txt


## What I did to get it set up
cd .\Desktop\college\2nd_year_MS\RL\Project_2\MECE689_RL_Atari_Superman_Project\

conda create -n superman_env python=3.9

conda init powershell

### Close powershell and reopen

conda activate superman_env

pip install stable-baselines3
<br>
pip install sb3_contrib
<br>
pip install "gymnasium==0.28.1"
<br>
pip install "gymnasium[atari,accept-rom-license]" 
<br>
pip install "gymnasium[class_control,box2d]" 
<br>
pip install notebook


# Usage
### Open a 2nd window, and launch Jupyter Notebook by typing:
jupyter notebook

## Training
Run all cells in a file that has "train" in its name.

## Evaluation
Run all cells in a file that has "eval" in its name.

# Results
See models saved in the models folder.
<br>
See metrics printed out in the files with "eval" in their name.





