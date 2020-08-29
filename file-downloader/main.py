import os, sys, requests
from scrape import get_page_download_links

def make_folder_at_dir(target_dir, name):
    try:
        path = os.path.join(target_dir, name)
        os.mkdir(path)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        return path

def remove_apostrophes(str):
  return str.replace("‘", '').replace("’", '').replace("'", '')


def str_to_file_name(str):
  str_arr = (str.lower() + '.pdf').split(' ')
  return remove_apostrophes('_'.join(str_arr))

def download_link(file_name, link, directory):
    content = requests.get(link).content

    with open(f'{directory}/{file_name}', 'wb') as f:
      f.write(content)
    

def main():
  # links = get_page_download_links('https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/')
  # outer_dir = '/'.join(os.getcwd().split('/')[:-1])
  # directory = make_folder_at_dir(outer_dir, 'Beginner Python Cheat Sheets')

  # for name, link in links.items():
  #   file_name = str_to_file_name(name)
  #   download_link(file_name, link, directory)
  
  print('Download Completed')


main()
