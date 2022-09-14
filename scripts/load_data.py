import pandas as pd
import logging
import dvc.api

logging.basicConfig(filename='./logfile.log', filemode='a',
                    encoding='utf-8', level=logging.DEBUG)

def load_excel_file(path: str, repo: str, version: str):
    path = path
    repo = repo
    version = version

    data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)

    try:
        df = pd.read_excel(data_url)
    except BaseException:
        logging.warning('file not found or wrong file format')
    return df




