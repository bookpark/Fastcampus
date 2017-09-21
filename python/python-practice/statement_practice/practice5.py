l = ['%d x %d = %d' % (x, y, x * y) for x in range(2, 10) for y in range(1, 10)]

# 현재 출력중인 결과가 구구단 중 '몇'단에 해당하는지의 index
gugu_index = 2
# 전체 구구단 결과 리스트 중 몇 번째를 순회하고 있는지의 index
list_index = 0
for item in l:
    # 전체 구구단 리스트의 아이템 중 9번째마다 실행
    if list_index % 9 == 0:
        print('== %s단 ==' % gugu_index)
        # 한 번 '몇'단인지 출력 후에는 다음 단의 index를 저장
        gugu_index += 1

    # 전체 구구단 결과 리스트 중 몇 번째를 순회하는중인지 업데이트
    list_index += 1
    # 전체 구구단 결과 중 현재 순회중인 item을 출력
    print(item)


# enumerate내장함수를 사용, index를 생략
for list_index, item in enumerate(l):
    if list_index % 9 == 0:
        print('== %s단 ==' % gugu_index)
        gugu_index += 1
    print(item)


# dict를 사용해서 gugu_index를 구구단 자료구조내에 포함

# List comprehension으로 단순 리스트를 만드는것이 아니라 dict의 리스트를 생성
'''
[
    {
        'title': '2단',
        'items': [
            '2 x 1 = 2',
            '2 x 2 = 4',
        ]
    },
    {
        'title': '3단',
        'items': [
            ..
            ...
        }
    }
]
'''

# for문으로 순회 시, 리스트의 순회항목이 dict가 되도록 한다(기존에는 단순한 문자열)
# 각 dict는 자신이 '몇단'인지의 정보와 9개의 결과 리스트를 갖는다
gugu_list = [
        {
            'title': '%d단' % x,
            'items': ['%d x %d = %d' % (x, y, x * y) for y in range(1, 10)]
        }
        for x in range(2, 10)
]

gugu_list = [{'title': '%d단' % x, 'items': ['%d x %d = %d' % (x, y, x * y) for y in range(1, 10)]} for x in range(2, 10)]

for gugu in gugu_list:
    print(gugu['title'])
    for item in gugu['items']:
        print(item)
    print('')

