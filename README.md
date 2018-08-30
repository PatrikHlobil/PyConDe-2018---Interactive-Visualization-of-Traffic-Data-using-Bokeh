# PyConDe 2018 - Interactive Visualization of Traffic Data using Bokeh

## Set Up
For this tutorial, you will need a setup with some additional Python packages. On my machine, I had issues with installing a Python3 environment with GeoPandas, therefore I used Python2. If you use Anaconda, you can use the Anaconda bash shell to setup an environment with name **Python27_TrafficVisualization** and all necessary dependencies via:

1. Download or clone the content of this repository to your local machine.

2. Change your working directory to the folder of the cloned repository:

            cd /path/to/your/directory

3. Open the (Anaconda) Terminal and create virtual environment via:

            conda env create -f requirements.yml

4. Activate environment via:
    
            conda activate Python27_TrafficVisualization
    
5. Start Jupyter Notebook Server via:

            jupyter notebook
                    
                    
                   
                   
## Download necessary Data

To download the data that we will process, just run the command in your *Python27_TrafficVisualization* environment (working directory has to be set to the repository folder again, see above):

            python "Download Data.py"
