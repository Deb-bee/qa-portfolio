testcase_id = "TC-001"
num_of_steps = 5
passed = True

print(f"{testcase_id} has {num_of_steps} steps and passed: {passed}")
codes = [200, 201, 404, 500, 200, 403, 301]

for code in codes:
    if 200 <= code <= 299:
        print(f"OK: {code}")          # Remember the f-string!
    elif 400 <= code <= 499:
        print(f"CLIENT ERROR: {code}")
    elif 500 <= code <= 599:
        print(f"SERVER ERROR: {code}")
    else:
        print(f"OTHER: {code}")