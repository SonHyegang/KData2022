speciesinfo = {
'C' : ['참돔 : Pagrus major', '정보1','정보2','정보3'],
'G' : ['고등어 : Scomber Japonicus', '태평양 (한국 남부, 일본에서 마이크로네시아, 호주 북부), 인도양',
'몸 등쪽은 짙은 청색을 띠며 중앙에서부터 밝아져 배쪽은 은백색을 띤다.\
주새개골의 끝에는 검은색 얼룩 점이 있다. 모든 지느러미는 희거나 무색투명하며, 꼬리지느러미만 어두운 갈색을 띤다.',
'1. 고등어 조림 \
2. 고갈비 \
3. 고등어 강정 \
4. 고등어 샌드위치  \
5. 고등어 찌개  \
6. 깐풍 고등어 \
7. 고등어 된장구이 초밥'],
'J' : ['전갱이 : Trachurus Japonucus', '정보1','정보2','정보3'],
'S' : ['성대 : Chelidonichthys spinosus', '정보1','정보2','정보3'],
'N' : ['눈볼대(금태) : Doederleinia berycoiders', '정보1','정보2','정보3'],
'K' : ['광어', '정보1','정보2','정보3'],
'O' : ['오징어', '정보1','정보2','정보3']
}
weighttable = {
      'C' : [0.027, 2.819],
      #a = 0.005270342 / b = 3.12579
      'G' : [0.005270342, 3.12579],
      'J' : [0.007, 3.058],
      'S' : [0.017, 2.792],
      'N' : [0.016, 2.928],
      'K' : [],
      'O' : []
    }

def cal_fishTL(fishIL, bongIT):
  fishTL  = int(fishIL) * 2.1 / bongIT #fishTL : bongIL = 실제 fishTL : 2.1
  return fishTL

def cal_weight(species, fishTL):
  weight = weighttable[species][0]*float(fishTL)**weighttable[species][1] if weighttable[species] is not None else '무게 예측 불가'
  return weight