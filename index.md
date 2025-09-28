# Machine Learning Activity: R & RStudio Setup Guide
## BF2223 FinTech for Investment Management (NTU)

Welcome! 🎓  
Before our ML activity, please make sure you have **R**, **RStudio**, and the required R packages installed on your computer.  
Follow the instructions below based on your operating system.  

---

## 1. Install R

R is the programming language we will use. Please download the latest version.

- **Windows:**  
  [Download R for Windows](https://cran.r-project.org/bin/windows/base/)  

- **macOS:**  
  [Download R for macOS](https://cran.r-project.org/bin/macosx/)  

👉 After downloading, run the installer and follow the default installation steps.

---

## 2. Install RStudio

RStudio is the integrated development environment (IDE) we’ll use for R.  

- **Download RStudio (latest version, free):**  
  [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)  

👉 Install RStudio after installing R.  
When you open RStudio, it should automatically detect your R installation.

---

## 3. Update R and RStudio (if already installed)

If you already have R or RStudio, please update to the latest versions to avoid compatibility issues.

- **Update R:**  
  - Windows: Download and install the newest version from [CRAN for Windows](https://cran.r-project.org/bin/windows/base/).  
  - macOS: Download and install the newest version from [CRAN for macOS](https://cran.r-project.org/bin/macosx/).  
  - You can have multiple R versions installed; RStudio will detect the latest automatically.  

- **Update RStudio:**  
  - Download and install the newest version from [RStudio Desktop](https://posit.co/download/rstudio-desktop/).  
  - The installer will overwrite the old version, keeping your settings and projects.  

👉 Tip: You can check your current versions in RStudio under **Help → About RStudio** and in the Console by typing:
R.version.string

---

## 4. Update R and RStudio (if already installed)

Once R and RStudio are installed or updated, open RStudio and run the following code in the Console:

- **Install core packages:**  
  - install.packages(c("quantmod", "pROC", "ggplot2", "dplyr", "tidyverse", "zoo", "caret"))

- **Optional: check if installation was successful**
  - library(quantmod)
  - library(pROC)
  - library(ggplot2)
  - library(dplyr)
  - library(tidyverse)
  - library(zoo)
  - library(caret)

---

## 5. Download R Script

The R script is a file with extension .r and contains the code to execute the program. 

- **Download script:**
  - You can download the R script [here](linreg.r).
  - Alternatively, download the R script from NTULearn. 

- **Execute program:**
  - Save the R script in a folder on your computer. 
  - In RStudio, set the working directory to the folder where you saved your script. You can do this by typing the following command in the Console, replacing "[pathname]" with the actual path to your folder:
    - setwd("path/to/your/folder")
  - Try running the R script by typing the following command in the Console:
    - source("linreg.r") 

END










