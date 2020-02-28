# Welcome to Coral Wavefront

This is a repository to detect wavefronts with a coral edge TPU dev board.
The wavefronts are created with a deformable mirror.

## Overview

│   .gitignore                          │  
│   README.md   						│  
│   server_ip_input.py					│-> Sets server IP  
│   									│  
├───client								│  
│   │   socket_connector.py				│-> Connects TPU to PC  
│           							│  
├───secret								│  
│       ip_config.txt					│-> IP config  
│       								│  
├───server								│  
│   │   snap.png						│-> Snapshot  
│   │   socket_connector_to_board.ipynb	│-> Starts server  
│           							│  
└───tensorflow							│  
    │   createTestModel.ipynb			│-> Converts TF Model to TF Lite  
    │       							│  
    └───models							│-> Trained models  


### Markdown

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).  

### Jekyll Themes

This Pages site usees the layout and styles from Jekyll.  
