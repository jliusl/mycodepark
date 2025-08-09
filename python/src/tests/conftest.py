import pytest
import time

@pytest.fixture(scope="function", autouse=True, params=[x for x in range(3)], name="t")
def timing(request):
    print(f"\n用例前置操作, 第{request.param + 1}次")
    start = time.time()
    yield request.param
    end = time.time()
    print(f"\n用例后置操作, 耗时: {end - start:.2f}s")