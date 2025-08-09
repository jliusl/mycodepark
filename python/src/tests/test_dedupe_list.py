from dedupe_list import dedupe

# def setup_function():
#     print("\n用例前置操作")

# def teardown_function():
#     print("\n用例后置操作")

def test_dedupe():
    print("用例执行")
    a = [3, 2, 3, 5, 7, 9, 20, 9, 7, 31]
    assert dedupe(a) == [3, 2, 5, 7, 9, 20, 31]