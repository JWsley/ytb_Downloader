import pytube as pyt
import time
import os
from colorama import Fore,Back,Style
from tqdm import tqdm as tq
from colorama import just_fix_windows_console
just_fix_windows_console()



def clear():
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


def videoDown():
    url = input(Fore.YELLOW + 'Insira a URL do video do youtube desejado:')
    time.sleep(1)
    clear()
    print('Aguarde um momento...')
    yt = pyt.YouTube(url)
    
    for i in tq(yt.streams.get_highest_resolution().download()):
        time.sleep(.1)
        clear()
        print(Fore.YELLOW+Style.BRIGHT +f'DOWNLOADING...')
        
    title = yt.title
    print(Fore.GREEN+f'O video de: {title} foi instalado com sucesso!!')
    #    print(Fore.RED+Style.BRIGHT+f'Ocorreu algum erro com a url: "{url}" verifique se a url está incorreta ou alguma restrição de acesso!!! ')



def musicdown():
    url = input(Fore.YELLOW+'Insira a URL da musica do youtube desejada:')
    time.sleep(1)
    clear()
    print('Aguarde um momento...')
    yt = pyt.YouTube(url)

   
    title = yt.title
    
    
    for i in tq(yt.streams.filter(only_audio=True).first().download()):
       time.sleep(.1)
       clear()
       print(Fore.YELLOW+Style.BRIGHT +f'DOWNLOADING...')
    print(Fore.GREEN+f'A musica : {title} foi instalada com sucesso!!')
   
    # print(Fore.RED+Style.BRIGHT+f'Ocorreu algum erro com a url: "{url}" verifique se a url está incorreta ou alguma restrição de acesso!!! ')


# https://www.youtube.com/watch?v=Wrp8QJp4P7E
def menu():
    print(Fore.WHITE+Style.BRIGHT+'==============================')
    print(Fore.WHITE+Style.BRIGHT+'       Y O U' +Fore.RED+Style.BRIGHT+' T U B E           ')
    print(Fore.RED+Style.BRIGHT+'    D O W N'+Fore.WHITE+Style.BRIGHT+ ' L O A D E R     ')
    print(Fore.RED+Style.BRIGHT+ '==============================')
    print(Fore.RED+Style.BRIGHT+ f'\nEscolha uma das opções abaixo:')
    print(Fore.WHITE+Style.BRIGHT+f'\n [0] - video  [1]- Audio MP3  ')
    print(Fore.RED+'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    resp = input(Fore.WHITE+Style.BRIGHT+'Digite aqui: ')


    if resp != '0' and resp != '1':
        clear()
        print('Insira somente 0 ou 1 !!')
        menu()

    else:
        if resp == '0':
          videoDown()
          
          time.sleep(2)
          print('Deseja baixar mais alguma coisa? [S/N]')
          r = input('Escolha:')
          reset = r.lower()
          while reset != 's' and reset != 'n':
             clear()
             print('Escolha apenas entre S ou N:')
             print('Deseja baixar mais alguma coisa? [S/N]')
             r = input('Escolha:')
             reset = r.lower()
            
          if reset == 's':
             clear()
             menu() 
          elif reset == 'n':
             time.sleep(1)
             clear()
             print('Encerrando programa...')
             time.sleep(2)  
        elif resp == '1':
          musicdown()
          
         
          time.sleep(2)
          print('Deseja baixar mais alguma coisa? [S/N]')
          r = input('Escolha:')
          reset = r.lower()
          while reset != 's' and reset != 'n':
             clear()
             print('Escolha apenas entre S ou N:')
             print('Deseja baixar mais alguma coisa? [S/N]')
            
            
          if reset == 's':
             clear()
             menu() 
          elif reset == 'n':
             time.sleep(1)
             clear()
             print('Encerrando programa...')
             time.sleep(2)  



menu()

