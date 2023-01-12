import pytube as pt
from time import time
from colorama import Fore as fc
from getDownloadPath import getDownloadPath

class videoDownloader():
    _url = ''
    _selectedVideo = ''
    _title = ''
    _videoObject = ''


    def __init__(self, url):
        while True:
            try:
                self._url = pt.YouTube(url)
            except:
                print(f'{fc.RED}Link Inválido...{fc.RESET}')
                break

            try:
                self._selectedVideo = self._url.streams.filter(file_extension = 'mp4').get_highest_resolution()
                self._title = self._selectedVideo.title
                self._videoObject = {
                    'Url' : self._url,
                    'itag': self._selectedVideo.itag,
                    'Title' : self._title
                }
            except:
                print(fc.RED + 'Erro')
            finally:
                break


    def __del__(self):
        print(f'{fc.CYAN}Rotina de downloads finalizada...{fc.RESET}')
        time.sleep(5)


    def startDownload(self):
        while True:
            ans = input(f'{fc.MAGENTA}Confirmar dowload de: {fc.GREEN}{self._videoObject.get("Title")}{fc.MAGENTA} - [s] ou [n]:{fc.YELLOW} ')
            ans = ans.lower().strip()
            if ans == 's':
                isConfirmed = True
                break
            elif ans == 'n':
                isConfirmed = False
                print(f'{fc.CYAN}Download cancelado...{fc.RESET}')
                break

        if isConfirmed:
            try:
                self._selectedVideo.download(getDownloadPath())
                print(f'{fc.GREEN}Download Iniciado...')
                print(f'Video..............: {self._videoObject.get("Title")}\n')
            except:
                print(f'{fc.RED}Download falhou...{fc.RESET}')


def main():
    url = input(f'{fc.MAGENTA}Insira o link do video:{fc.YELLOW} ')
    video = videoDownloader(url)
    video.startDownload()

if __name__ == '__main__':
    main()