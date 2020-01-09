
import os
import shutil
import pytest

from git import Repo

TESTS_FOLDER = './test_repos'

@pytest.fixture(scope='session')
def clone_curl(request):
    """Clone the repository of curl for the tests.
    """
    git_url = 'https://github.com/curl/curl.git'
    repo_dir = os.path.join(TESTS_FOLDER, 'curl')
    repo = Repo.clone_from(url=git_url, to_path=repo_dir)
    #repo.heads['curl-7_67_0'].checkout()

    def teardown():
        shutil.rmtree(repo_dir)

    request.addfinalizer(teardown)

    return repo_dir

def pytest_unconfigure(config):
    """Teardown after all tests.
    """
    shutil.rmtree(TESTS_FOLDER)
