def run_tests():
  from main import Solution
  solution = Solution()

  # First we'll do the test case shown in the task description so that will be the one shown to people first if their code isn't working.  If that passes then we'll do other test cases.
  test_cases = [{
    'input': [5, [
      [0, 1],
      [1, 2],
      [3, 4],
    ]],
    'output': 2
  }, {
    'input': [0, []],
    'output': 0
  }, {
    'input': [1, []],
    'output': 1
  }, {
    'input': [2, []],
    'output': 2
  }, {
    'input': [3, []],
    'output': 3
  }, {
    'input': [2, [
      [0, 1],
    ]],
    'output': 1
  }, {
    'input': [3, [
      [0, 1],
    ]],
    'output': 2
  }, {
    'input': [3, [
      [1, 2],
    ]],
    'output': 2
  }, {
    'input': [3, [
      [0, 1],
      [1, 2],
    ]],
    'output': 1
  }]

  for test_case in test_cases:
    input = test_case['input']
    expected_output = test_case['output']
    actual_output = solution.countComponents(*input)
    if not actual_output == expected_output:
      print('Test case failed.\nInput: {}\nExpected: {}\nGot: {}\n'.format(
        input, expected_output, actual_output))
      return
  print("All test cases passed!")
