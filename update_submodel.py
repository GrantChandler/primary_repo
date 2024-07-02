import os


def update_git_submodels(path: str):
    os.chdir(path)
    os.system('git pull')
    os.system('git submodule update --init --recursive')


path = "data2"
update_git_submodels(path)