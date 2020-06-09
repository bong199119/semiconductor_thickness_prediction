# -*- coding: utf-8 -*-

import modeling
import load_split
import torch
import torch.optim as optim

"""# 경로, 디바이스, 설정초기화"""
def init():
    # data_path -> train data 경로
    data_path = '../semiconductor_train.csv'

    # weight_path -> 가중치파일 경로
    weight_path = 'test_model_new.pth'
    # gpu사용여부확인
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    use_cuda = torch.cuda.is_available()

    # 로그인터벌, 학습률, epoch 설정
    learning_rate = 1e-3
    epochs = 1000
    return epochs, learning_rate, use_cuda, device, weight_path, data_path

# mae함수
def mae(trn_pred, trn_y):
    abs_value = abs(trn_pred - trn_y)
    return abs_value

# training 함수
def training(use_cuda, learning_rate, epochs , model , trn_loader, val_loader ):
    # 옵티마이저 설정
    optimizer = optim.RMSprop(model.parameters(), lr=learning_rate)

    batches = len(trn_loader)

    trn_loss_list = []
    val_loss_list = []

    for epoch in range(epochs):
        trn_loss_summary = 0.0
        for i, trn in enumerate(trn_loader):
            trn_X, trn_y = trn['X'], trn['y']   # cpu 사용시
            if use_cuda:
                trn_X, trn_y = trn_X.cuda(), trn_y.cuda() # gpu 사용시

            # 역전파 단계 전에 갱신할 변수들에 대한 모든 변화도를 0으로 만듭니다. 이렇게 하는 이유는
            # 기본적으로 .backward()를 호출할 때마다 변화도가 버퍼(buffer)에 (덮어쓰지 않고)누적되기 때문
            optimizer.zero_grad()

            trn_pred = model(trn_X.float())  # 모델에 train데이터 넣기
            trn_loss = mae(trn_pred.double(), trn_y.double())  # mae함수(평가방식)로 train loss계산

            # autograd를 사용하여 역전파 단계를 계산합니다.
            trn_loss.sum().backward()
            optimizer.step()

            trn_loss_summary += trn_loss.sum()

            # 15번째마다 val_loss 찍어주기
            if (i + 1) % 15 == 0:
                # gradiant를 무시하고 가중치 조절
                with torch.no_grad():
                    val_loss_summary = 0.0
                    # validation으로 학습정도 평가 -> 학습에는 반영되지 않음
                    for j, val in enumerate(val_loader):
                        val_X, val_y = val['X'], val['y']
                        if use_cuda:
                            val_X, val_y = val_X.cuda(), val_y.cuda()
                        val_pred = model(val_X.float())
                        val_loss = mae(val_pred.double(), val_y.double())
                        val_loss_summary += val_loss.sum()

                print("epoch: {}/{} | step: {}/{} | trn_loss: {:.4f} | val_loss: {:.4f}".format(
                    epoch + 1, epochs, i + 1, batches, (trn_loss_summary / 15) ** (1 / 2),
                    (val_loss_summary / len(val_loader)) ** (1 / 2)
                ))


                trn_loss_list.append((trn_loss_summary / 15) ** (1 / 2))
                val_loss_list.append((val_loss_summary / len(val_loader)) ** (1 / 2))
                trn_loss_summary = 0.0

            savePath = "test_model_new.pth"

            # 가중치 저장
            torch.save(model.state_dict(), savePath)

    print("finish Training")

    return savePath


def main() :
    """# 설정 초기화"""
    epochs, learning_rate, use_cuda, device, weight_path, data_path = init()

    """# 데이터 로드, 스플릿"""
    load_splitter = load_split.load_splitter(data_path)
    trn, val, trn_X, trn_y, val_X, val_y, trn_loader, val_loader  =  load_splitter

    """# 모델생성"""
    model = modeling.make_model(device, weight_path)

    """# 학습"""
    savePath = training(use_cuda, learning_rate, epochs, model, trn_loader, val_loader )


"""# main 실행"""
if __name__ == "__main__":
    main()
