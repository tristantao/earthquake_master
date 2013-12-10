import git
import os

HOME_DIR = os.getcwd()

def setup_repos():
    '''
    Clones the required repos if they don't exist.
    Pulls if they do exist.
    '''
    if not os.path.isdir(os.path.join(os.getcwd(), 'tristan_quakers')):
        print "Cloning tristan_quakers"
        git.Git().clone("https://github.com/tristantao/tristan_quakers")
    else:
        print "TheQuakers folder already exists, pulling instead"
        quakers_repo = git.cmd.Git('tristan_quakers')
        quakers_repo.pull()
        print "tristan_quakers pull complete"
    print "\n.....\n"
    if not os.path.isdir(os.path.join(os.getcwd(), 'data-curators')):
        print "Cloning data-curators"
        git.Git().clone("https://github.com/stat157/data-curators")
    else:
        print "data-curators folder already exists, pulling instead"
        curators_repo = git.cmd.Git('data-curators')
        curators_repo.pull()
        print "data-curators pull complete"

    #grab the other util code and load it.
    os.system("cp data-curators/curate_util.py .")
    import curate_util as CU

def curate():
    '''
    Begins the curation process.
    '''
    print "Begining curation"
    retcode = os.system("cd data-curators; python curate.py")
    if retcode != 0:
        print "Suration failed with code %s" % retcode
    else:
        print "Curation complete"
    return retcode

def generate_ecdf_plots():
    '''
    Utilizes the ECDF/ecdf.R to genrate the ecdf plots.
    '''
    retcode = os.system("cd tristan_quakers/ECDF; Rscript ecdf.R " + os.path.join(HOME_DIR, 'tristan_quakers/ECDF/'))
    #print os.getcwd()
    if retcode == 0:
        print "ECDF generated!"
    else:
        print "ECDF generation failed with code %s" % retcode
    return retcode


def show_plot():
    import Image
    image = Image.open(os.path.join(HOME_DIR, 'tristan_quakers/ECDF/plot.png' ))
    image.show()

##########################
####Important Functions###
##########################
setup_repos()
#curate
generate_ecdf_plots()
show_plot()


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




