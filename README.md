# Quantifying Visual Informativeness for AVSR in Noisy Conditions: Insights from AV-HuBERT and MaFI Matrics

## Introduction

This project provides a collection of Python scripts designed for comprehensive data analysis and visualization tasks, particularly focusing on MaFI (Mouth and Facial Informativeness) scores and Individual Word Error Rate (IWER) metrics in multimodal speech recognition experiments.

## Project Structure

### Main Directories and Files:
- av_hubert: Files sourced from the official AV-HuBERT repository (https://github.com/facebookresearch/av_hubert).
* MaFI: Files sourced from the official AV-HuBERT dataset (https://osf.io/mna8j/).
+ Project: Scripts and data used for analysis, processing, and experimentation within this project.

### Python Scripts Description in Project:
- BoxPlot_Bootstrapping file:
    - Generates boxplots illustrating the distribution of IWER across different MaFI levels.

    - Employs bootstrapping to assess the variability and robustness of the observed trends.
* Pearson file:
    * Calculates the Pearson correlation coefficient between MaFI scores and IWER.

    * Visualizes correlation values across varying Signal-to-Noise Ratio (SNR) conditions.
+ SNR_Gain file:
    + Visualizes the SNR gain across different datasets, highlighting improvements in multimodal speech recognition performance under varied acoustic conditions.
- TCD-TIMIT file:
    - Identifies common words between professionally trained lip speakers and general volunteers.
    
    - Analyzes differences in IWER performance between these two groups
* Analysis file:
    * Contains additional scripts used for supplementary analyses relevant to the project's experiments.

## Environment Setup
The environment for executing these scripts should follow the official guidelines from the AV-HuBERT repository. Additional dependencies specific to this project are listed in `requirements.txt`.
To set up the environment:

```sh
pip install -r requirements.txt
```

## Usage
Run the Python scripts individually according to your analysis needs. Example:
```sh
python resample.py
python LRS3Test_PearsonPlot.py
python SLRS3Test_SNR_Gain.py
```
Ensure data files are correctly placed within the directories as referenced in each script.

