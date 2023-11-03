#!/usr/bin/env python3

# Reverse Polish Notation (RPN) calculator
# N.B. the FILO stack is a list, so we operate on the last (-1) elements

import os
import time

stack = []

def print_stack(stack):
  os.system('cls')
  print("RPN Calc")
  for i in stack:
    print(i)

def print_error(error_string):
  print(error_string)
  time.sleep(1.5)

def is_min_size(stack, size):
  if len(stack) < size:
    print_error("ERROR: Too few arguments")
    return False
  else:
    return True
  
def add(stack):
  if is_min_size(stack, 2):
    result = stack.pop(-2) + stack.pop()
    stack.append(result)

def subtract(stack):
  if is_min_size(stack, 2):
    result = stack.pop(-2) - stack.pop()
    stack.append(result)

def multiply(stack):
  if is_min_size(stack, 2):
    result = stack.pop(-2) * stack.pop()
    stack.append(result)

def divide(stack):
  if is_min_size(stack, 2):
    if(stack[-1] == 0.0):
      print_error("ERROR: Divide by zero")
    else:
      result = stack.pop(-2) / stack.pop()
      stack.append(result)

def exponent(stack):
  if is_min_size(stack, 2):
    result = stack.pop(-2) ** stack.pop()
    stack.append(result)

def inverse(stack):
  if is_min_size(stack, 1):
    result = 1 / stack.pop()
    stack.append(result)

def swap(stack):
  if is_min_size(stack, 2):
    result = stack.pop(-2)
    stack.append(result)

def clear(stack):
  stack.clear()

def drop(stack):
  if is_min_size(stack, 1):
    stack.pop()

# Dictionary of supported operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "exp": exponent,
  "inv": inverse,
  "swp": swap,
  "clr": clear,
  "drp": drop,
}

if __name__ == "__main__":
  print_stack(stack)

  while True:
    user_input = input("> ")
    if user_input == "":
      break

    try: #convert input to float
      stack.append(float(user_input))
    except ValueError: 
      try: #if not a float, see if it is a supported operation
        operations[user_input](stack)
      except KeyError: #if not, print error
        print_error("ERROR: Invalid input")

    print_stack(stack)
