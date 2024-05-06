import os
import colorama
from colorama import Fore, Back

colorama.init()

if not os.path.exists('./download'):
    os.mkdir('./download')

def download_urls(urls: list) -> None:
    import urllib.request

    for url in urls:
        filename = url.split('/')[-1]
        filename = filename.replace('&dl=1', '')
        filename = filename.replace('?p=%2F', '')
        
        print(Fore.BLUE + f'文件名: {filename}' + Fore.RESET)
        filepath = os.path.join('./download', filename)
        urllib.request.urlretrieve(url, filepath)
        print(Fore.WHITE + Back.GREEN + f' {filename} 下载完成 ' + Fore.RESET + Back.RESET)