import rpn_calc

def test_add_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.add(stack)
  assert stack == [2.0, 7.0]

def test_add_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.add(stack)
  assert stack == [2.0]

def test_subtract_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.subtract(stack)
  assert stack == [2.0, -1.0]

def test_subtract_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.subtract(stack)
  assert stack == [2.0]

def test_multiply_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.multiply(stack)
  assert stack == [2.0, 12.0]

def test_multiply_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.multiply(stack)
  assert stack == [2.0]

def test_divide_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.divide(stack)
  assert stack == [2.0, 0.75]

def test_divide_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.divide(stack)
  assert stack == [2.0]

def test_divide_by_zero():
  stack = [2.0, 3.0, 0.0]
  rpn_calc.divide(stack)
  assert stack == [2.0, 3.0, 0.0]

def test_exponent_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.exponent(stack)
  assert stack == [2.0, 81]

def test_exponent_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.exponent(stack)
  assert stack == [2.0]

def test_inverse_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.inverse(stack)
  assert stack == [2.0, 3.0, 0.25]

def test_inverse_with_fewer_args_than_needed():
  stack = []
  rpn_calc.inverse(stack)
  assert stack == []

def test_swap_with_more_args_than_needed():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.swap(stack)
  assert stack == [2.0, 4.0, 3.0]

def test_swap_with_fewer_args_than_needed():
  stack = [2.0]
  rpn_calc.swap(stack)
  assert stack == [2.0]

def test_clear_with_populated_stack():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.clear(stack)
  assert stack == []

def test_clear_with_empty_stack():
  stack = []
  rpn_calc.swap(stack)
  assert stack == []

def test_drop_with_populated_stack():
  stack = [2.0, 3.0, 4.0]
  rpn_calc.drop(stack)
  assert stack == [2.0, 3.0]

def test_drop_with_empty_stack():
  stack = []
  rpn_calc.drop(stack)
  assert stack == []
