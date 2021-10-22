# EMI Toolkit
## Date : 23/10/2021

# Team: 
    1. Arjun Panicker
    2. Clariza Look
    3. Deepakraj Sugumaran
    4. Harper Wu
    5. Kiet Hoang

## Project Sub-Team:
    A. EMI Toolkit - [ Arjun Panicker , Deepakraj]
    B. Python Websever  - [Clariza Look, Harper Wu, Kiet Hoang]

# EMI Toolkit

### EMI Toolkit - Requirements

    1. [Required] Python 3.7.3 and above
    2. [Required] PySerial 3.5 and above
    3. [Required] PyNMEA-2 1.18 and above

### Prerequisites - Install Dependent Packages
    1. Download and install anaconda https://www.anaconda.com/
    2. Download or Clone this repo.
    
 
### 3. Open terminal [Linux/MacOS] or Open Anaconda Terminal [Windows] and navigate to Prerequisites/
    cd Prerequisites/

### 4. Use the following command to create a conda environment

    conda env create -f precision-farming-emitoolkit.yml
    
### 5. Activate the environment by,

    conda activate emitoolkit

## EMI Toolkit - Running the GUI
### 1. Navigate to EMI-Toolkit Folder
    
    cd ..
    cd EMI-Toolkit/
### 2. Run the main program by,

    python3 main.py



## Web Application

### Home Page
From home page of this applicaiton, users could use map or history button to view avaiable maps and history data collection record.  

### Map page
In map page, there are a list of maps of different map which could be use to perform data collection and visualization.  
Choose the fild map would like to use to process to viem map and start tracking

### Tracking page
In tracking page, the map selected in previous page would be shown with location coordinate and hardware status informaiton on top and operation button on th bottom.

