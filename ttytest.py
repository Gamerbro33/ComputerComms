import sys
import termios
import tty

import sys
import termios
import tty

fd = sys.stdin.fileno()
# Save original settings to restore them later
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(fd, when=termios.TCSAFLUSH)
    print("Press any key to continue...", end="", flush=True)
    # Reads exactly 1 byte immediately
    char = sys.stdin.read(1)
finally:
    # Always restore original terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

print(f"\nYou pressed: {char}")
