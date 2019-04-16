# CMPUT 501 Final Project
## Motivation
The main goal of this study is to find the effect of team size on the productivity of the development team. The reason for conducting this study is to give some insight to project managers as at the beginning of any projects there are many different factors to be considered by the project managers and choosing the correct combination is a daunting task. One of these factors is the size of the development team were choosing a small number may result in the high pressure of workload on the development team and choosing a large team can result in having many developers without enough task and result in the waste of money of the company and the developers' time. So, the project managers want to select a team size which leads to an increase in the team productivity and revenue of the company. After selecting the number of team members, the project managers need to choose the project language where there are a wide variety of languages available. This study tries to find if there is any relation between team size and the language of the project. Consequently, there are two main research questions for this study as follows:<br/>

 * **RQ1** What is the relation between team size and productivity of the development team?<br/>
 * **RQ2** What is the relation between team size and the language of the project?
 
 More information regarding this study can be found in (documantation)[]

## Data
In this project we are using data from TravisTorrent dataset.

Beller M, Gousios G, Zaidman A. (2017) TravisTorrent: Synthesizing Travis CI and GitHub for Full-Stack Research on Continuous Integration

## Requirments
1. Python 3.7.3
2. Jupyter Notebook (Only in case you want to see the files in ipython format and check the results)
3. [travistorrent_8_2_2017.csv.gz](https://travistorrent.testroots.org/page_access/)
4. Python Libraries
    * Numpy 1.16.2
    * Pandas 0.24.2
    * Seaborn 
    * Scipy
    * Matplotlib

## Steps to Reproduce
The following steps represent how to reproduce this workon Ubuntu [18.04](http://releases.ubuntu.com/18.04/) environment.
1. Install Python3 (You can skip this step if you already have Python3 installed)
    ```
    sudo apt-get install python3
    ```
2. Install the required libraries by the following command.
    ```
    pip3 install -r requirements.txt
    ```
3. Clone this repository on your local machine
4. Download the [travistorrent_8_2_2017.csv.gz](https://travistorrent.testroots.org/page_access/) and extract it in the directory of this project.
5. Open the terminal in the directory of this project
6. Run the following command
    ```
    Python3 main.py
    ```
