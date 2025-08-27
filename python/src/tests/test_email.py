# test_email_sender.py
import pytest
from email_sender import send_email

def test_send_email_success(monkeypatch):
    """测试邮件发送成功的情况"""

    # 创建一个模拟的 SMTP 类
    class MockSMTP:
        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.sent_messages = []

        def starttls(self):
            pass  # 模拟启用 TLS

        def login(self, user, password):
            pass  # 模拟登录

        def send_message(self, msg):
            # 可以记录发送的消息，用于断言
            self.sent_messages.append(msg)
            return True


        def quit(self):
            pass  # 模拟关闭连接

    # 使用 monkeypatch 替换 smtplib.SMTP
    monkeypatch.setattr("smtplib.SMTP", MockSMTP)

    # 调用被测试函数
    result = send_email("测试主题", "测试内容", "to@example.com")

    # 断言发送成功
    assert result is True


def test_send_email_failure(monkeypatch):
    """测试邮件发送失败的情况（抛出异常）"""

    # 模拟 SMTP 抛出异常
    class MockSMTP:
        def __init__(self, host, port):
            raise Exception("网络连接失败")

        def starttls(self):
            pass

        def login(self, user, password):
            pass

        def send_message(self, msg):
            pass

        def quit(self):
            pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)

    result = send_email("测试主题", "测试内容", "to@example.com")

    assert result is False


def test_verify_smtp_called_with_correct_args(monkeypatch):
    """测试 SMTP 是否使用了正确的参数初始化"""

    called_args = None

    class MockSMTP:
        def __init__(self, host, port):
            nonlocal called_args
            called_args = (host, port)

        def starttls(self):
            pass

        def login(self, user, password):
            pass

        def send_message(self, msg):
            pass

        def quit(self):
            pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)

    send_email("测试", "内容", "to@example.com")

    assert called_args == ('smtp.example.com', 587)