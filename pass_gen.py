#!/usr/bin/env python3
"""Generate secure random passwords."""
import sys, secrets, string

def generate(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special: chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length, special = 16, True
    for a in sys.argv[1:]:
        if a.startswith('--length='): length = int(a.split('=')[1])
        elif a == '--no-special': special = False
    print(generate(length, special))
