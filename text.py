##### PROMPT TEXT #####

import sys
import time

def prompt_text(prompt):
    for character in prompt:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.01)
    #print(prompt)