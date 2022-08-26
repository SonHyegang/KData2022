# Fishchecker
**2022 데이터 청년 캠퍼스 고려대학교 빅데이터 기반의 지능정보시스템 개발 : Team 11**
- [Fishchecker](#fishchecker)
    + [Development Environment](#development-environment)
  * [How to use](#how-to-use)
    + [Colab](#colab)
    + [PyQt5 UI](#pyqt5-ui)
  * [Results for some Test cases](#results-for-some-test-cases)
    + [Colab test version](#colab-test-version)
    + [PyQt5 UI](#pyqt5-ui-1)
  * [EDA](#eda)
  * [Algorithm](#algorithm)
  * [Team members](#team-members)
  * [도움주신 분들](#-------)

<br>
<br>


![image](https://user-images.githubusercontent.com/53131824/186707022-956ff170-4047-4f2d-b739-3f7a295451d1.png)



> `The problems to be solved in this project are as follows. Fish with the camera function of the mobile
when the picture was taken,`

1️⃣ **Classify the fish in the picture**<br>
2️⃣ **Predict the weight of a fish based on an existing data set**<br>
3️⃣ **Provide meaningful information to users.**

>   `This project provides meaningful information to users based on fish species classification and weight prediction functions. Based on the mobile application service, users can conveniently Its purpose is to make it possible to obtain information.`

<br>
<br>


### Development Environment
- [ ] EDA : R Studio
- [ ] System : VSCode, Colab PRO

<br>
<br>


## How to use
### Colab
***NOTE: PyQt5 UI는 사용환경에 따라 실행시간에 차이가 클 수 있습니다. 또한 영상실행 단계에서 코덱 issue가 발생할 수 있어 fishChcker algorithm 결과를 어떤 사용환경에서도 확인해보실 수 있도록 Colab test version를 지원하고 있습니다.***

1. Download the ZIP file from the link below

   https://drive.google.com/file/d/1ixf9Td-opkCBDDwDRdwEQicY2Ljvy700/view?usp=sharing 

2. Unzip the downloaded file and upload it to My Drive in Google Drive.
![image](https://user-images.githubusercontent.com/53131824/186811130-f654b789-4300-46c5-be22-9e97bd15c3e5.png)

3. For faster execution, change the runtime type to GPU and run all shells


<br><br>


### PyQt5 UI
1. Install the codec from the link below for smooth execution in the video execution stage of the UI

   https://codecguide.com/download_kl.htm 

2. Download the EXE file and run it

   ***NOTE: Please make sure that all paths do not contain Korean characters.***

3. If you want to directly create and run the executable file or run main.py directly from the shell, please match the versions of the packages you need.
```
python -m pip install -r requirements.txt
```

<br><br>

## Results for some Test cases
### Colab test version


https://user-images.githubusercontent.com/53131824/186845531-4f5c8a3e-c8f8-413a-a236-5a4ba2719c58.mp4

![image](https://user-images.githubusercontent.com/53131824/186847162-3b6b54e1-217e-47d0-9c85-26ad55dc215f.png)


<br><br>

### PyQt5 UI


https://user-images.githubusercontent.com/53131824/186846835-744303e4-cb83-41a8-9b1f-6f26fbbb896c.mp4

![1](https://user-images.githubusercontent.com/53131824/186847252-fd7714b1-4983-489b-bf6f-22da0507f2d9.png)
![2](https://user-images.githubusercontent.com/53131824/186847271-7b9dbe93-06b5-41c4-8009-df8edd7c97ef.png)

<br><br>

## EDA
![image](https://user-images.githubusercontent.com/53131824/186893196-5a534f1d-a19a-4c5f-ac2f-46b75450e85c.png)
![image](https://user-images.githubusercontent.com/53131824/186893248-5531fbf5-27f0-4e59-9518-966768af952c.png)


***NOTE: EDA에 대한 detail은 https://github.com/SonHyegang/KData2022_Fishchecker/tree/main/EDA
에서 확인하실 수 있습니다***

<br><br>

## Algorithm
![image](https://user-images.githubusercontent.com/109898791/186849435-10d466fe-e003-473a-8ab8-bccb6d83bc4a.png)




***NOTE: Algorithm에 대한 detail은 https://github.com/SonHyegang/KData2022_Fishchecker/tree/main/Fishchecker%20Colab 에서 확인하실 수 있습니다***



<br><br>

## Team members
|Member|Contributions|Contact|
|:-:|-------|-|
|김지나|||
|손혜강|||
|윤세정|||
|임정아|||
|황영석|||

**최종 시연을 위한 v16_best.pt, bong_v5_best.pt file외 중간산출물과 raw data들은 장시간 data 수집과 training, tuning의 결과물이란 점, 용량제한 문제점으로 인해 Github repository에서 공개하고 있지 않습니다. 필요하신 분들은 Team members table의 contact mail로 연락주시기 바랍니다.**

<br>

## 도움주신 분들
한국수산회 수산정책연구소 소장님
해양수산부 운영지원과 관계자
노량진수산물도매시장 경영기획부 관계자


![image](https://user-images.githubusercontent.com/53131824/186621158-785481bb-8d06-4c23-9b98-653a00c0f562.png)
