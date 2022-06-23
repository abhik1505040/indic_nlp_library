# 
#  Copyright (c) 2013-present, Anoop Kunchukuttan
#  All rights reserved.
#  
#  This source code is licensed under the MIT license found in the
#  LICENSE file in the root directory of this source tree.
# 

import os

"""
Path to the Indic NLP Resources directory
"""
INDIC_RESOURCES_PATH = ''
GIT_URL = "https://github.com/anoopkunchukuttan/indic_nlp_resources"

def init():
    """
    Initialize the module. The following actions are performed:

    - Checks of INDIC_RESOURCES_PATH variable is set. If not, checks if it can beb initialized from 
        INDIC_RESOURCES_PATH environment variable. If that fails, an exception is raised
    """
    global INDIC_RESOURCES_PATH 
    if INDIC_RESOURCES_PATH == '':
        INDIC_RESOURCES_PATH = os.environ.get('INDIC_RESOURCES_PATH', "")
    
    if not os.path.isdir(INDIC_RESOURCES_PATH):
        cache_dir = os.path.expanduser(
            os.path.join('~/.cache', 'indic_nlp_resources')
        )
        
        os.makedirs(
            os.path.dirname(cache_dir), 
            exist_ok=True
        )
        
        if not os.path.isdir(cache_dir):
            from git import Repo, RemoteProgress
            from tqdm import tqdm

            class CloneProgress(RemoteProgress):
                def __init__(self):
                    super().__init__()
                    self.pbar = tqdm()

                def update(self, op_code, cur_count, max_count=None, message=''):
                    self.pbar.total = max_count
                    self.pbar.n = cur_count
                    self.pbar.refresh()

            Repo.clone_from(GIT_URL, cache_dir, progress=CloneProgress())

        INDIC_RESOURCES_PATH = cache_dir

def get_resources_path(): 
    """
        Get the path to the Indic NLP Resources directory
    """
    return INDIC_RESOURCES_PATH

def set_resources_path(resources_path): 
    """
        Set the path to the Indic NLP Resources directory
    """
    global INDIC_RESOURCES_PATH 
    INDIC_RESOURCES_PATH=resources_path

class IndicNlpException(Exception):
    """
        Exceptions thrown by Indic NLP Library components are instances of this class.  
        'msg' attribute contains exception details.
    """
    def __init__(self, msg):
        self.msg = msg 

    def __str__(self):
        return repr(self.msg)

