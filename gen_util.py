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

def prep_env():
    '''
    Installs the required dependencies
    rscript, rbase, pandas, scipy, 
    R: sfsmisc
    '''
    pass
