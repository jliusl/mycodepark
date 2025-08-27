import pytest
import time
from count_days import count_days


# @pytest.fixture(scope="function", autouse=False, params=[x for x in range(5)], name="t")
# def timing(request):
#     print(f"\n用例前置操作, 第{request.param + 1}次")
#     start = time.time()
#     yield request.param
#     end = time.time()
#     print(f"\n用例后置操作, 耗时: {end - start:.2f}s")

@pytest.mark.parametrize("t, start_date, end_date, expected", [
    (0, '2023.01.01', '2023.01.02', 1),
    (1, '2023.01.01', '2023.01.01', 0),
    (2, '2023.01.01', '2024.01.01', 365),
], indirect=["t"])  # indirect表示 "t" 是fixture的名称



@pytest.mark.smoke
def test_count_days(t, start_date, end_date, expected):

    print("用例执行")
    print(t, start_date, end_date, expected)
    time.sleep(1)
    assert count_days(start_date, end_date) == expected
