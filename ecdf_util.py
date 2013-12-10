import git
import os

HOME_DIR = os.getcwd()

def generate_ecdf_plots():
    '''
    Utilizes the ECDF/ecdf.R to genrate the ecdf plots.
    '''
    #    retcode = os.system("cd tristan_quakers/ECDF; Rscript ecdf.R " + os.path.join(HOME_DIR, 'tristan_quakers/ECDF/'))
    retcode = os.system("cd tristan_quakers/ECDF; Rscript improved_ecdf.R " + os.path.join(HOME_DIR, 'tristan_quakers/ECDF/'))
    #print os.getcwd()
    if retcode == 0:
        print "ECDF generated!"
    else:
        print "ECDF generation failed with code %s" % retcode
    return retcode

def show_plots():
    import Image
    #from IPython.core.display import Image
    #Image(filename=os.path.join(HOME_DIR, 'tristan_quakers/ECDF/plot.png'))
    image = Image.open(os.path.join(HOME_DIR, 'tristan_quakers/ECDF/plot.png'))
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




