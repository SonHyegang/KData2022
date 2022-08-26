# EDA

***NOTE: 데이터 EDA를 위하여 어종의 체중-체장 데이터를 R로 분석한 결과의 일부입니다. 자세한 결과들은 EDA 폴더의 파일에서 확인하실 수 있습니다.***

![image](https://user-images.githubusercontent.com/53131824/186838055-01277091-5410-4bf5-8494-a9a578bf7c43.png)

> `어류 5종의 산점도 그래프는 모두 양의 상관관계를 보이고 있다. 모두 일정한 패턴을 보여주고
있으며 잠재적인 이상치 값을 판별하기 어렵다. 특히 전갱이, 눈볼대의 경우 밀집도가 두드러진다.
다음은 어류 14종(고등어, 전갱이, 참돔, 성대, 눈볼대, 붉은 메기, 황돔, 보구치, 덕대, 주둥치, 샛멸,
밴댕이, 황아귀, 멸치) 데이터 중에서 참돔의 데이터로 그려낸 box plot과 histogram이다.`



![image](https://user-images.githubusercontent.com/53131824/186838104-3808ade6-eb61-4c68-8319-70290bc317bf.png)

> `Graph 2와 3을 보면, 참돔의 TL(Total length, 총길이(cm)) box plot에서 제3사분위수와
제1사분위수의 간격이 10 이상 차이 나는 것을 확인할 수 있다. 최댓값과 최솟값의 간극에서
중앙값이 다소 왼쪽으로 치우쳐져 있으므로 참돔의 관측값은 20을 중심으로 몰려있을 것이다.
실제로 왼쪽 아래의 TL histogram에서 참돔의 관측값은 20보다 작고 가까운 구간에 많은 도수가
있음을 확인할 수 있다. 또한, 참돔의 WW(Wet-weight, 습중량(g)) Box plot에서 이상치를
확인했다. 참돔의 WW histogram은 TL histogram보다 양의 치우침 정도가 크게 그려졌고, 오른쪽
꼬리에서 이상치로 판단되는 값들을 확인했다.`



![image](https://user-images.githubusercontent.com/53131824/186838223-c439a07b-9523-4e3d-980e-2ee227cb82ae.png)


> `Graph 4는 회귀분석을 실시하기 전, 회귀분석 가정에 대한 검증을 위해 그린 그래프이다. 왼쪽
상단에 있는 잔차도 그래프에서 잔차가 기울기 0을 중심으로 일정 구간 내에 고르게 분포되어
있어야 한다. Q-Q 그래프에서 직선을 벗어나지 않은 이상치 값이 존재하지 않으면 잔차가 평균이
0인 정규분포를 따르는 정규성 가정을 만족한다고 본다. Scale-Location 그래프에서 추세선의
기울기가 0에 가까우며 직선을 벗어나지 않는 점, 즉 이상점일 가능성이 높은 점들이 적을수록 좋다.
마지막 Residual vs Leverage 그래프에서 Cook’s distance에 가까운 점, 이는 회귀직선의 기울기와
절편에 큰 영향을 미칠 수 있는 점이다.`



![image](https://user-images.githubusercontent.com/53131824/186838283-6024fff6-319b-4410-913d-68661bfcf4a1.png)

> `Graph 5는 회귀분석으로 어류 6종, 총 4,904개체의 값을 체장-체중 관계식에 기초하여 log를 취한
뒤 그려낸 결과이다. 어류 5종의 회귀분석 그래프는 모두 선형성을 보이고 있으며, b의 값이 3과
유의한 차이가 있는지 확인하기 위해 t-test로 검정한 결과, 아래 Table 1과 같았다.`



![image](https://user-images.githubusercontent.com/53131824/186838387-61c1c1ec-d974-4ad1-900f-b079d0da5269.png)


> `b는 2.8에서 3.2 사이에 존재했고 그 결과는 table 1로 나타났다. 따라서 양의 상대 성장을 하는
어류는 고등어(Scomber japonicus), 전갱이(Trichiurus japonicus), 음의 상대 성장을 하는 어류는
성대(Chelidonichthys spinosus), 눈볼대(Doederleinia berycoides), 참돔(Pagrus major)이다.`





### Reference

Han Ju Kim, Yeonghye Kim, Jeong-Hoon Lee and Sang Chul Yoon. 2019. Length-weight Relationships for 27 Fish Species from Southern Sea in Korea. Korean J Fish Aquat Sci
53(5), 790-793, https://doi.org/10.5657/KFAS.2020.0790

Ren, Shaoqing, et al. "Faster r-cnn: Towards real-time object detection with region proposal networks." Advances in neural information processing systems 28 (2015).

Henderson, Paul, and Vittorio Ferrari. "End-to-end training of object class detectors for mean average precision." Asian Conference on Computer Vision. Springer, Cham, 2016.

Elijah Migiro Kembenya, Erick Ochieng Ogello, Cecilia Githukia, Callen Nyaboke Aerad. 2014. Seasonal Changes of Length -Weight Relationship and Condition Factor of Five Fish Species in Lake Baringo, Kenya.
