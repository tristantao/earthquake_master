import git
import os
import Image

HOME_DIR = os.getcwd()

def generate_quantile_plots():
    '''
    Utilizes the tristan_quakers/Quantile-Method/Quantile-final.R to genrate the ecdf plots.
    '''
    print "Starting Quantile plot generation via Quantile-final.R"
    retcode = os.system("cd tristan_quakers/Quantile-Method/; Rscript Quantile-final.R " + os.path.join(HOME_DIR, 'tristan_curators/RawCleanData.csv'))
    if retcode == 0:
        print "Quantile plots generated!"
    else:
        print "Quantile plots generation failed with code %s" % retcode
    return retcode

def show__plot():
    '''
    Shows the Quantile Div error plot
    '''
    image = Image.open(os.path.join(HOME_DIR, 'tristan_quakers/Quantile-Method/XXXXXXXXXXXX.png'))
    image.show()



