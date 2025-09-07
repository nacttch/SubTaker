from termcolor import colored as term_colored

def print_banner():
    banner = r"""
    
.▄▄ · ▄• ▄▌▄▄▄▄· ▄▄▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
▐█ ▀. █▪██▌▐█ ▀█▪•██  ▐█ ▀█ █▌▄▌▪▀▄.▀·▀▄ █·
▄▀▀▀█▄█▌▐█▌▐█▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█▄█▌██▄▪▐█ ▐█▌·▐█▪ ▐▌▐█.█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀ .▀  ▀

           SubTaker - by Nactch
    """
    print(term_colored(banner, "magenta"))

def colored(text, color):
    try:
        return term_colored(text, color)
    except Exception:
        return text
