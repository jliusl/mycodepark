import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt

# 定义一个简单的全连接网络，用于 MNIST 手写数字识别
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # 输入层：28*28=784 维像素 → 64 维隐藏层
        self.fc1 = torch.nn.Linear(28*28, 64)
        # 两个隐藏层，保持 64 维
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc3 = torch.nn.Linear(64, 64)
        # 输出层：64 维 → 10 维（对应 0-9 十个类别）
        self.fc4 = torch.nn.Linear(64, 10)

    def forward(self, x):
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))
        # 使用 log_softmax 输出概率对数，方便后续 NLLLoss
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1)
        return x

# 获取训练或测试数据加载器
def get_data_loader(is_train):
    # 将图像转为 [0,1] 的 Tensor
    to_tensor = transforms.Compose([transforms.ToTensor()])
    data_set = MNIST("", is_train, transform=to_tensor, download=True)
    # batch_size=15：每次训练取 15 张图片
    return DataLoader(data_set, batch_size=15, shuffle=True)

# 在测试集上评估模型准确率
def evaluate(test_data, net):
    n_correct = 0
    n_total = 0
    with torch.no_grad():  # 关闭梯度计算，加速推理
        for (x, y) in test_data:
            # 将 28×28 图像展平为 784 维向量
            outputs = net.forward(x.view(-1, 28*28))
            for i, output in enumerate(outputs):
                if torch.argmax(output) == y[i]:
                    n_correct += 1
                n_total += 1
    return n_correct / n_total  # 返回准确率

def main():
    train_data = get_data_loader(is_train=True)
    test_data = get_data_loader(is_train=False)
    net = Net()

    print("initial accuracy: ", evaluate(test_data, net))
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

    # 训练 2 个 epoch
    for epoch in range(2):
        for (x, y) in train_data:
            net.zero_grad()  # 清零梯度
            output = net.forward(x.view(-1, 28*28))
            # NLLLoss 与 log_softmax 配套使用
            loss = torch.nn.functional.nll_loss(output, y)
            loss.backward()
            optimizer.step()
        print("epoch: ", epoch, "accuracy: ", evaluate(test_data, net))

    # 展示前 4 张测试图片及其预测结果
    for (n, (x, _)) in enumerate(test_data):
        if n > 3:
            break
        predict = torch.argmax(net.forward(x[0].view(-1, 28*28)))
        plt.figure(n)
        plt.imshow(x[0].view(28, 28))
        plt.title("prediction: " + str(int(predict)))

    plt.show()

if __name__ == '__main__':
    main()