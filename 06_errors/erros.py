#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASk Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()  # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")