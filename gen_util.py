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
    if not os.path.isdir(os.path.join(os.getcwd(), 'tristan_curators')):
        print "Cloning tristan_curators"
        git.Git().clone("https://github.com/tristantao/tristan_curators")
    else:
        print "tristan_curators folder already exists, pulling instead"
        curators_repo = git.cmd.Git('tristan_curators')
        curators_repo.pull()
        print "tristan_curators pull complete"

    #grab the other util code and load it.
    os.system("cp tristan_curators/curate_util.py .")
    import curate_util as CU

def curate():
    '''
    Begins the curation process.
    '''
    print "Begining raw curation"
    retcode = os.system("cd tristan_curators/; python curate.py")
    if retcode != 0:
        print "Raw Curation failed with code %s" % retcode
    else:
        print "Raw Curation complete"
    return retcode

    '''
    #Now, turn the RawCleanData into DataFrame used by the MDA code.
    retcode2 = os.system("Rscript CleanDataWithRealTime.R %s %s" % (os.path.join(HOME_DIR, "tristan_curators/RawCleanData.csv"), os.path.join(HOME_DIR, "tristan_quakers/ScaledMDA/DataFrame.csv")))
    if retcode2 != 0:
        print "DataFrame creation failed with code %s" % retcode
    else:
        print "DataFrame created"
    
    return retcode + retcode2
    ''' 


def prep_env():
    '''
    new ipython (jinja2)
    Installs the required dependencies
    rscript, rbase, pandas, scipy, 
    R: sfsmisc
    '''
    pass
