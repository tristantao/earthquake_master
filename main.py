import git
import os

HOME_DIR = os.getcwd()

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


#copy over the util file and import
os.system("cp data-curators/curate_util.py .")
import curate_util as CU

print "="*10
print "Begining curation"
#retcode = os.system("cd data-curators; python curate.py")


catalog_dict = CU.grab_data_dict(1999,1999, 'data-curators/clean_data/')
#data_frame  = CU.grab_data_frame(catalog_dict)
#rows = random.sample(data_frame.index, 250)
#df_250 = data_frame.ix[rows]
#df_250.to_csv(os.path.join(os.getcwd(), "250.csv"), index = False)

retcode = os.system("cd tristan_quakers/ECDF; Rscript ecdf.R " + os.path.join(os.getcwd(), 'tristan_quakers/ECDF/'))
#print os.getcwd()
print retcode
print "DONE!"

'''
q_o = quakers_repo.remote.origin
g = git.cmd.Git(git_dir)
g.pull()
'''




