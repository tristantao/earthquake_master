import git
import os
import Image

HOME_DIR = os.getcwd()

def generate_data_frame():
    '''
    Uses the curation code and generate a dataframe for MDA plot.
    Not currently used.
    '''
    retcode = os.system("Rscript CleanDataWithRealTime.R tristan_curatprs/RawCleanData.csv " + os.path.join(HOME_DIR, 'tristan_quakers/ScaledMDA/DataFrame.csv'))
    if retcode == 0:
        print "MDA DataFrame generated!"
    else:
        print "MDA DataFrame generation failed with code %s" % retcode
    return retcode


def generate_MDA_plots():
    '''
    Utilizes the tristan_quakers/ScaledMDA/ScaledMDA-Presentation.R to genrate the ecdf plots.
    '''
    retcode = os.system("cd tristan_quakers/ScaledMDA/; Rscript ScaledMDA-Presentation.R " + os.path.join(HOME_DIR, 'tristan_curators/RawCleanData.csv'))
    if retcode == 0:
        print "MDA plots generated!"
    else:
        print "MDA plots generation failed with code %s" % retcode
    return retcode

def show_MDAdiv_plot():
    '''
    Shows the MDA Div error plot
    '''
    image = Image.open(os.path.join(HOME_DIR, 'tristan_quakers/ScaledMDA/ErrorSMDADiv.jpeg'))
    image.show()

def show_MDAsub_plot():
    '''
    Shows the MDA Sub error plot
    '''
    image = Image.open(os.path.join(HOME_DIR, 'tristan_quakers/ScaledMDA/ErrorSMDAsub.jpeg'))
    image.show()


'''
q_o = quakers_repo.remote.origin
g = git.cmd.Git(git_dir)
g.pull()

catalog_dict = CU.grab_data_dict(1999,1999, 'data-curators/clean_data/')
#data_frame  = CU.grab_data_frame(catalog_dict)
#rows = random.sample(data_frame.index, 250)
#df_250 = data_frame.ix[rows]
#df_250.to_csv(os.path.join(os.getcwd(), "250.csv"), index = False)

'''




