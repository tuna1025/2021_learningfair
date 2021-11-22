from PIL import Image
import time
import random

# 편리한 기능
def hgj(sentence, timesl = 0.1):
    for i in range(len(sentence)):
        print(sentence[i], end = "")
        time.sleep(timesl)

def b (sentence, timesl=0.5): 
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)

def red(world):
    hgj("\x1b[31m" + world + "\x1b[0m")

def magenta(world):
    hgj("\x1b[35m" + world + "\x1b[0m")

def green(world):
    hgj("\x1b[32m" + world + "\x1b[0m")

# 이다솔
def next_stage(): #다음스테이지로 이동하는 함수
        green("다음 스테이지로 이동합니다. \n")
        hgj("해치웠다. 하지만 홀가분하지는 않았다. \n")
        hgj("정말 괴물이 한 마리밖에 없었을까? \n")
        hgj("앞에 엘리베이터가 있으니 일단 저걸로 6층으로 이동해야겠다. \n")
        img = Image.open('elevator.gif')
        img.show()
        hgj("엘레베이터를 타고 올라가며 생각했다. 살아남자. \n")
        hgj("괴물과의 전쟁은 이미 시작됐다. \n")

def floor_1(): #1층 메인함수
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[1층]")
        hgj("대체 이 아파트에 무슨 일이 생긴 걸까. \n")
        hgj("제길, 하나도 안 보이네. \n")
        hgj("그래도 일단은 앞으로 가보는 수밖에 없나? \n")
        b("...\n")
        hgj("1층 입구 앞에 도착했다. \n")
        hgj("일단 들어가야 할 것 같은데 망설여지네... \n")
        hgj("주위가 음산한게 금방이라도 무언가 튀어나올 것 같다. \n")
        hgj("꼭 이 주위를 한 번쯤은 둘러봐야할 것처럼. \n")
        hgj("입구의 손잡이를 두 손으로 꽉 붙든 채 고민했다. \n")
        hgj("들어갈까? 아니면 주위를 둘러볼까? \n")
        green("!Tip 무기가 어디 떨어져있을지 모릅니다. \n")
        answer3 = int(input("1. 들어간다. 2. 주위를 둘러본다. \n"))
        while answer3 != 1 and answer3 != 2:
            answer3 = int(input("선택지를 잘못 입력하셨습니다.\n"))
        if answer3 == 2:
            b("...\n")
            hgj("주위를 둘려보던 중 바닥에서 이상한 물건들을 발견했다. \n")
            img = Image.open('칼.jpg')
            img.show()
            hgj("어? 이게 다 뭐야? \n")
            hgj("자세히 보니 무기들인 것 같다. \n")
            hgj("웬 무기..? 누가 싸우려고 하다 흘린 것들인가...? \n")
            hgj("근데 대체 뭐랑 싸우려고 한 거지...? \n")
            hgj("이상한 점이 한 둘이 아니다. 하지만 일단은 가지고 다니는게 좋으려나? \n")
            answer4 = int(input("1. 줍는다 2. 줍지 않는다 \n"))
            while answer4 != 1 and answer4 != 2:
                answer4 = int(input("선택지를 잘못 입력하셨습니다.\n"))
            if answer4 == 1:
                green("!Tip 무기는 단 하나만 고를 수 있습니다. 선택에 신중하세요. \n")
                answer5 = int(input("1. 야구 배트. 2. 권총. 3. 칼. 4. 화염병. \n"))
                while answer5 != 1 and answer5 != 2 and answer5 != 3 and answer5 != 4:
                    answer5 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                hgj("최대한 신중하게 무기를 선택했다. \n")
                hgj("뭐가 어떻게 돌아가고 있는지 잘 모르겠지만 도움이 됐으면 좋겠네. \n")
                green("아이템을 획득 후 1층 안으로 진입합니다. \n")
            elif answer4 == 2:
                hgj("지나치고 1층 안으로 진입합니다. \n")
        elif answer3 == 1:
            hgj("1층 안으로 진입합니다. \n")
        b("...\n\n")
        hgj("부스럭... 바스락... 끼익... \n")
        hgj("누군가와 마주쳤다. 누구지? 이 아파트 사람인가? \n")
        hgj("남자가 내게 말을 걸어온다. \n")
        b("...\n")
        img = Image.open('JJH.jpg')
        img.show()
        magenta("남자: 안녕하세요. 저는 정재헌이라고 합니다. \n")
        hgj("남자의 이름은 정재헌, 이 아파트에 살던 사람같다. \n")
        magenta("정재헌: 이 아파트에는 괴물이 가득해요. 많은 사람들이 죽고 다쳤습니다. \n")
        hgj("이게 다 괴물 때문이라고? 영화 속에서나 일어날 법한 이야기가 사실이라니. \n")
        hgj("하지만 지금 아파트 상황을 보면 신빙성이 아예 없는 이야기도 아니다. \n")
        hgj("나: 그럼 이제 어떻게 해야 하죠? \n")
        magenta("정재헌: 힘을 합쳐 괴물을 무찌르는 수밖에 없겠죠. \n")
        magenta("정재헌: 그러기 위해 사람들을 모으고 있습니다. 저희와 함께 해주시겠습니까? \n")
        green("!Tip 정재헌 님은 칼을 소지하고 있습니다. \n")
        green("이와 동행 하시겠습니까? \n")
        answer6 = int(input("1. 동행한다. 2. 동행하지 않는다. \n"))
        while answer6 != 1 and answer6 != 2:
            answer6 = int(input("선택지를 잘못 입력하셨습니다.\n"))
        if answer6 == 1:
            magenta("정재헌: 앞으로 잘 부탁드립니다. \n")
            magenta("정재헌: 괴물들로부터 살아 남아보자고요. \n")
            hgj("그래, 살아남는 수밖에 없다. 그게 내가 이 말도 안 되는 상황에 내린 결론이다. \n")
        elif answer6 == 2:
            magenta("정재헌: 함께 할 수 있었다면 좋았을텐데 아쉽군요... \n")
            magenta("정재헌: 꼭 살아남으시길 바랍니다. \n")
        b("...\n\n")
        hgj("일단 앞으로 가봐야할 것 같다. \n")
        hgj("띵-. 샤악. \n")
        hgj("갑자기 엘리베이터 문이 열렸다. \n")
        red("드드드득, 드드드득, 위잉, 드드드득, 드드드드득, 위잉 \n")
        img = Image.open('경비.jpg')
        img.show()
        red("생, 선, ㅆ...ㄱ...은...ㅅ...ㅐ..ㅇ..ㅅㅓ..ㄴ \n")
        hgj("엘리베이터 안에서 튀어나온 건 괴물이었다. \n")
        hgj("그리고 괴물의 손엔 잡초를 깎는 기계가 들려있었다. \n")
        hgj("제길, 까딱하면 죽겠는데. \n")
        hgj("일단 공격해봐야 하나? \n")
        green("!Tip 괴물을 공격하지 않으면 괴물로부터 공격 받을 수 있습니다. \n")
        answer7 = int(input("1. 공격한다. 2. 공격하지 않는다. \n"))
        while answer7 != 1 and answer7 != 2:
            answer7 = int(input("선택지를 잘못 입력하셨습니다.\n"))
        if answer7 == 2:
            hgj("녀석이 나를 발견했다. \n")
            red("카앙!! 위잉, 드드드득, 위잉, 드드드득, 드드드득 \n")
            img = Image.open('경비2.jpg')
            img.show()
            hgj("녀석이 굉음과 함께 내게 돌진한다. \n")
            green("경비원 괴물이 당신을 향해 공격합니다. \n")
            game_over = True
        elif answer7 == 1:
            if answer3 == 1:
                hgj("공격하겠다고 했지만 공격할 수 있는 무기가 없다. \n")
                hgj("제길, 어떻게 해야하지? 당하는 수밖에 없나? \n")
                if answer6 == 1:
                    green("동행인 정재헌 님이 당신의 앞에 무기를 든 채 서있습니다.")
                    hgj("설마 ... \n")
                    magenta("정재헌: 물러나세요. 제가 처리하겠습니다. \n")
                    hgj("나: 미쳤어요? 혼자서 저 괴물을 어떻게 처리해요? \n")
                    magenta("정재헌: 이게 최선입니다. 현재 당신은 무기가 없으니까요. \n")
                    hgj("제길, 틀림없는 내 불찰이다. \n")
                    red("캉, 치잉, 캉, 드르르륵, 캉, 위잉, 치잉, 드드르륵, 캉 \n")
                    hgj("정재헌 씨의 팔 한 쪽이 날라가더니 정재헌 씨가 괴물과 함께 엘리베이터 안으로 들어갔다. \n")
                    img = Image.open('JJH_in_ele.jpg')
                    img.show()
                    magenta("정재헌: 당신은, 꼭 살아남기를 바랍니다. \n")
                    hgj("띵-. 샤악. \n")
                    hgj("엘리베이터 문이 닫혔다. \n")
                    green("정재헌 님의 희생 덕분에 경비원 괴물이 처치되었습니다. \n")
                    next_stage()
                    floor_over = True
                elif answer6 == 2:
                    hgj("녀석이 나를 발견했다. \n")
                    red("카앙!! 위잉, 드드드득, 위잉, 드드드득, 드드드득 \n")
                    img = Image.open('경비2.jpg')
                    img.show()
                    hgj("녀석이 굉음과 함께 내게 돌진한다. \n")
                    green("경비원 괴물이 당신을 향해 공격합니다. \n")
                    game_over = True
            elif answer3 == 2:
                hgj("분명 녀석의 약점이 있을 것이다. \n")
                hgj("거기를 공격해야 하는데 어디를 공격해야 하지? \n")
                green("!Tip 녀석의 약점을 공격하거나 일부 부분을 많은 횟수로 공격해야 처치가 가능합니다. \n")
                answer8 = int(input("1. 머리. 2. 팔. 3. 다리. 4. 배. \n"))
                while answer8 != 1 and answer8 != 2 and answer8 != 3 and answer8 != 4:
                    answer8 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                if answer5 == 1 or answer5 == 3:
                    hgj("공격할 곳은 정했고, 이제 몇번이나 공격하냐의 차이인데 ... \n")
                    hgj("몇 번이나 공격해야 하나. \n")
                    answer9 = int(input("1. 1번. 2. 2번. 3. 3번. 4. 4번 이상. \n"))
                    while answer9 != 1 and answer9 != 2 and answer9 != 3 and answer9 != 4:
                        answer9 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                    hgj("정신을 붙잡고 괴물을 향해 공격했다. \n")
                    while answer9 < 3:
                        red("쾅, 크아아악!!, 위잉, 드드드륵 \n")
                        hgj("저 괴물자식 죽지를 않는다. \n")
                        hgj("다시 공격해야 하나? \n")
                        answer10 = int(input("1. 다시 공격한다. 2. 공격하지 않는다. \n"))
                        while answer10 != 1 and answer10 != 2:
                            answer10 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                        if answer10 == 1:
                            hgj("몇 번이나 더 공격해야 하지? \n")
                            answer9 = int(input("1. 1번. 2. 2번. 3. 3번. 4. 4번 이상. \n"))
                            while answer9 != 1 and answer9 != 2 and answer9 != 3 and answer9 != 4:
                                answer9 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                            continue
                        elif answer10 == 2:
                            red("카앙!! 위잉, 드드드득, 위잉, 드드드득, 드드드득 \n")
                            img = Image.open('경비2.jpg')
                            img.show()
                            hgj("녀석이 굉음과 함께 내게 돌진한다. \n")
                            green("경비원 괴물이 당신을 향해 공격합니다. \n")
                            game_over = True
                    green("경비원 괴물이 처지되었습니다. \n")
                    next_stage()
                    floor_over = True
                elif answer5 == 2:
                    if answer8 == 2 or answer8 == 3 or answer8 == 4:
                        while answer8 != 1:
                            red("쾅, 크아아악!!, 위잉, 드드드륵 \n")
                            hgj("저 괴물자식 죽지를 않는다. \n")
                            hgj("다시 공격해야 하나? \n")
                            answer10 = int(input("1. 다시 공격한다. 2. 공격하지 않는다. \n"))
                            while answer10 != 1 and answer10 != 2:
                                answer10 = int(input("선택지를 잘못 입력하셨습니다.\n"))
                            if answer10 == 1:
                                print("이번에는 어디를 공격해야 하지? \n")
                                answer8 = int(input("1. 머리. 2. 팔. 3. 다리. 4. 배. \n"))
                                continue
                            elif answer10 == 2:
                                red("카앙!! 위잉, 드드드득, 위잉, 드드드득, 드드드득 \n")
                                img = Image.open('경비2.jpg')
                                img.show()
                                hgj("녀석이 굉음과 함께 내게 돌진한다. \n")
                                green("경비원 괴물이 당신을 향해 공격합니다. \n")
                                game_over = True                          
                    if answer8 == 1:
                        hgj("탕-. \n")
                        hgj("괴물의 머리를 저격했다. \n")
                        hgj("괴물이 움직이지 않는다. 성공한 건가? \n")
                        green("경비원 괴물이 머리가 파괴된 채 처치되었습니다. \n")
                        next_stage()
                        floor_over = True
                elif answer5 == 4:
                    hgj("슈욱-. \n")
                    hgj("괴물을 향해 화염병을 던졌다. \n")
                    red("크아아아아악!!!!! \n")
                    hgj("괴물이 불에 타 괴로워하더니 조용해졌다. 성공한 건가? \n")
                    hgj("경비원 괴물이 불에 타 처지되었습니다. \n")
                    next_stage()
                    floor_over = True

# 유용주
def start():
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        choice1 = int(input("1. 시작, 2. 스토리 설명, 3. 게임 설명\n"))
        while choice1 != 1 and choice1 != 2 and choice1 != 3:
            choice1 = int(input("선택지를 잘못 입력하셨습니다."))
        if choice1 == 1:
            hgj("게임을 시작합니다...\n\n")
            floor_over = True
        elif choice1 == 2:
            hgj("불특정 다수의 사람들이 하나 둘 씩 괴물로 변해가기 시작했다.\n원인은 알 수 없지만 사람들의 욕망이 겉으로 발현되는 순간 괴물로 변하는 것 같다.\n괴물들은 각자의 욕망에 따라 다른 형태와 능력을 가지게된다.\n이들과의 의사소통이 불가능하지만 특정 단어를 지속적으로 반복한다.\n주인공은 1층에 살고 있으며 살아남기 위해 옥상으로 올라간다.\n")   
        else:
            hgj("<SOS(Save Our Souls)>는 원작 <스위트홈>을 각색하여 만들어진 게임입니다.\n이 게임은 당신의 선택에 따라서 앞으로의 이야기가 달라집니다.\n선택하는 곳에 숫자만을 적어주세요.\n")

def floor_5(): # 무전기 에피소드
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[5층]")
        hgj("(덜커덩)\n젠장...엘레베이터가 고장났잖아..\n위에가 막힌 것 같아..\n일단 내려서 계단으로 이동하든지 해야겠어...\n한 시라도 이 지긋지긋한 곳을 벗어나고 싶어\n바깥 상황이라도 알 수 있다면 좋을 텐데...\n저거는 무전기잖아..? 누가 도망치다가 흘렸나보네.\n고치면 다시 사용할 수 있을 것 같아!\n")
        while floor_over != True:
                hgj("(치직)....(치)...(치직)..들리...(치직)십니까?..?\n")
                hgj("여보세요? 누구신가요..?\n저..(치직)는 군인..(치지직)입니다. 생존...(치직)자를 찾고 있었습니다. (치직)그..곳은 어..디..(치칙)인가요?\n그린홈 103동이에요\n(치직) 알겠습..(치직)니다. 헬기..(치직)를 보내드릴테니 옥상으로 오세..(치직)요.\n(무전기가 끊겼다.)\n그래 옥상으로 올라가서 헬기를 타고 탈출하자!\n")
                floor_over = True

def floor_6(): # 거미 괴물 에피소드
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[6층]")
        hgj("드디어 6층인가...\n뭐야 이곳은...사방이 거미줄이잖아\n아파트 문들이 종이처럼 찢겨있어..\n분명히 이곳에 다른 괴물이 있는 것이 분명해...\n")
        red("쉬이이이이이이이이익\n")
        hgj("크 괴물 녀석의 비명소리 때문에 귀가 따가워...\n어떡하지..?\n")
        choice1 = int(input("1. 소화전에 들어가서 숨는다, 2. 괴물을 기다린다\n"))
        while choice1 != 1 and choice1 != 2:
            choice1 = int(input("선택지를 잘못 입력하셨습니다."))
        if choice1 == 1:
            hgj("그래 아직 괴물이 얼마나 센지 모르잖아.\n소화전에서 괴물이 지나가도록 기다려야겠어\n")
            red("쉬이이이이이익\n")
            hgj("제발... 빨리 지나쳐줘...\n(.....)\n괴물이 지나간 것 같은데 문을 열어볼까?\n")
            while floor_over != True:
                choice2 = int(input("1. 소화전을 연다, 2. 소화전을 열지 않는다\n"))
                while choice2 != 1 and choice2 != 2:
                    choice2 = int(input("선택지를 잘못 입력하셨습니다."))
                if choice2 == 1:
                    img = Image.open("spider1.jpg")
                    img.show()
                    hgj("어라..왜 아직도 있는거야...\n아까 간 것이 아니었던 거야?\n")
                    red("쉬이이이이이이익\n")
                    hgj("안돼...!\n")
                    floor_over = True
                    game_over = True
                else:
                    hgj("(덜커덩)\n(쉬이이이이이이익)\n후 다행히 문을 안 열기를 잘한 것 같아\n괴물은 물건이 떨어지는 소리에 반응해서 다른 곳으로 간 것 같아.\n괴물이 눈치채기 전에 어서 빨리 다음 층으로 이동해야겠어\n")
                    floor_over = True
        else:
            hgj("그래 이왕 이렇게 된 거 빨리 싸우자 괴물아!\n")
            red("쉬이이이이익\n")
            hgj("빨리 주변에서 괴물과 싸울 만한 무기를 집어야겠어\n")
            choice3 = int(input("1. 전기모기채를 잡는다, 2. 식칼을 잡는다\n"))
            while choice3 != 1 and choice3 != 2:
                choice3 = int(input("선택지를 잘못 입력하셨습니다."))
            if choice3 == 1:
                img = Image.open("spide2.jpg")
                img.show()
                hgj("전기모기채를 가지고 무엇을 할 수 있을까..? 그래도 뭐라도 해야 내가 살 수 있어..!\n")
                red("쉬이이이익\n")
                hgj("받아라!!!\n")
                red("끼이이이이이익!!!\n")
                hgj("어라..? 전기모기채에 닿은 부분이 녹고 있잖아? 혹시 이 괴물의 약점은 전기이지 않을까?\n지금이 이길 수 있는 유일한 기회야\n다시 받아라!!\n")
                red("끼이이이이이이익\n")
                hgj("(괴물이 쓰러졌다.)\n내가 해냈어!!! 내가 해냈다고...!\n전기모기채는 배터리가 다 나갔나..아쉽지만 버리고 가야겠어\n어서 빨리 다음 층으로 올라가자..!\n")
                floor_over = True
            else:
                img = Image.open("spide2.jpg")
                img.show()
                hgj("그래 식칼이면 괴물에게도 위협적일거야\n")
                red("쉬이이이익\n")
                hgj("받아라!!!\n(탕)\n(끼이이이이이이익!)\n녀석의 피부가 너무 단단해서 식칼이 부서졌잖아..\n오히려 녀석을 화나게 한 것 같아\n")
                red("끼이이이이이이익\n")
                hgj(".....! 안돼!\n")
                floor_over = True
                game_over = True

def floor_7(): # 음식 에피소드
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[7층]")
        hgj("정말 아슬아슬했어\n잘못했다가는 거미 괴물에게 죽었을 거야...\n(꼬르륵)\n쉴 틈 없이 올라오다보니 배고픈지도 몰랐네\n7층에서 뭐라도 먹을 것을 찾아야겠어\n젠장..7층의 모든 문들도 거미 괴물이 부셨잖아 특히 703호와 704호는 고칠 수도 없을 것 같아..\n내가 집에서 챙긴 도구로는 한 곳 밖에 들어갈 수 없을 텐데 어쩌지..\n")
        while floor_over != True:
            choice1 = int(input("1. 701호에 들어간다, 2. 702호에 들어간다\n"))
            while choice1 != 1 and choice1 != 2:
                choice1 = int(input("선택지를 잘못 입력하셨습니다."))
            if choice1 == 1:
                hgj("(킁킁)\n흠...이게 무슨 냄새지\n(식탁에는 빵이 보인다.)\n굶어죽지는 말라는 신의 계시인가..먹어도 되는 걸까?\n")
                choice2 = int(input("1. 빵을 집어먹는다, 2. 빵을 먹지 않는다\n"))
                while choice2 != 1 and choice2 != 2:
                    choice2 = int(input("선택지를 잘못 입력하셨습니다."))
                if choice2 == 1:
                    hgj("이 빵 맛이 이상한걸...?\n...!\n우우웨엑...뭐야 이 빵 맛이 이상하잖아\n(빵 뒷면을 보니 곰팡이가 피었다.)\n배가 너무 아파... 약도 없는데...\n(눈 앞이 아득해진다.)\n")
                    floor_over = True
                    game_over = True
                else:
                    hgj("자세히 보니 빵 뒷면에 곰팡이가 피었잖아\n후 안 먹길 잘한 것 같아...이런 일은 다시는 없어야 할 것 같아..\n다른 곳에서 찾아야겠어..어서 빨리 다음 층으로 올라가자..!\n")
                    floor_over = True
            else:
                hgj("제발 이 방에는 음식이 있기를....그동안 난 너무 굶었다고...\n(뒤적뒤적)\n어..! 라면이잖아!\n끓여먹을 여유가 없는게 아쉽지만 그래도 이 정도면 탈출할 때까지는 버틸 수 있을거야!\n어서 빨리 다음 층으로 올라가자..!\n")
                floor_over = True

def floor_8():
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[8층]")
        hgj("드디어 8층이다..\n괴물에게 죽지않고 올라오다보니 이 정도까지 올라온건가?\n뭐지 저거는...으윽 바퀴벌레다...\n역시 이 아파트 오래됐어...\n여기서는 못잘 것 같아..다음 층에서 자든지 해야겠어...\n")
        floor_over = True

def floor_9(): # 화재 에피소드
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[9층]")
        hgj("9층으로 올라왔다..\n이곳은 층간소음이 자주 일어난다고 엘레베이터에서 본 적이 있지..\n주위를 보니 소음이 들리기는커녕 쥐 죽은 듯이 조용하네\n나도 조용히 하고 오늘 밤은 여기서 보내야겠어.\n(킁킁)\n어라 이게 무슨 냄새지? 이상한 냄새가 나는걸?\n밤이라 아무것도 안보여\n전등 불을 켜야하나?\n")
        while floor_over != True:
            choice1 = int(input("1. 스위치를 켠다, 2. 그대로 있는다\n"))
            while choice1 != 1 and choice1 != 2:
                choice1 = int(input("선택지를 잘못 입력하셨습니다."))
            if choice1 == 1:
                hgj("스위치를 켜서 이게 무슨 냄새인지 알아야겠어!\n(스위치를 킨다.)\n(콰과쾅)\n(전기의 스파크와 가스가 만나 폭발했다.)\n")
                floor_over = True
                game_over = True
            else:
                hgj("잠깐만 이 냄새는 가스 냄새 아니야..?\n스위치를 켰으면 집이 폭발했을지도 몰라\n어서 빨리 창문을 열어 환기를 시켜줘야겠어\n")
                floor_over = True

def floor_10(): # 샤워 이벤트
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[10층]")
        hgj("10층으로 올라왔다..\n(킁킁)\n어디서 쉰내가 나는데...이런..! 내 냄새잖아!\n안되겠어 이번 층에서 샤워라도 해야겠어...\n1003호가 그나마 화장실이 깨끗하네...그리고 물티슈도 있어\n잠깐만..아직 물이 나오잖아..?\n물티슈로 닦을까..? 아니면 물로 씻을까..?\n")
        while floor_over != True:
            choice1 = int(input("1. 물티슈로 닦는다, 2. 물로 샤워한다\n"))
            while choice1 != 1 and choice1 != 2:
                choice1 = int(input("선택지를 잘못 입력하셨습니다."))
            if choice1 == 1:
                hgj("그래 물이 오염됐을 수도 있어..일단 물티슈로 몸을 닦자..\n(물티슈로 몸을 닦는다.)\n그래 이정도가 어디야..빨리 밖으로 나가서 씻든가 해야지..\n")
                floor_over = True
            else:
                hgj("(옷을 벗는다.)\n그럼 오랜만에 물로 샤워를 해볼까?\n(수도꼭지를 튼다.)\n...! 뭐야 이 물 흙탕물이잖아..!\n젠장... 몸만 더럽히고 나왔네...기분 나쁘네...\n빨리 밖으로 나가서 몸을 씻든가 해야겠어\n")
                floor_over = True

def Game_over():
    global floor_over, game_over
    while game_over == True:
        print("[GAME OVER]")
        choice1 = int(input("1. 재시작, 2. 종료\n"))
        while choice1 != 1 and choice1 != 2:
            choice1 = int(input("선택지를 잘못 입력하셨습니다."))
        if choice1 == 1:
            game_over = False
            break
        else:
            game_over = True
            break

# 윤성훈
def scene_1():
    while (True):
        print("[11층]")
        hgj("간신히 10층을 뚫고 올라온 11층 복도. 다음 층으로 가려면 이 복도를 지나가야한다.\n")
        img = Image.open('monstre.jpg')
        img.show()
        hgj("그런데 그 중간에 머리가 코부분으로 잘린 괴물이 가로막고 있다 어떻게 해야할까..\n")
        print("1. 저 괴물녀석 눈이 잘렸어... 우릴 보지 못할거야 천천히 지나가자")
        print("2. 아니야.. 그래도 혹시 몰라 그냥 가까이 가지 않는게 좋겠어 내려가서 다른 길을 찾아보자..")
        f_select = int(input("선택: "))
        while f_select != 1 and f_select != 2:
            f_select = int(input("선택: "))
        if f_select == 1 or f_select == 2 :
            return f_select

def scene_2_1():
    while (True):
        print("1. 1101호") #소화기 - 소용없음
        print("2. 1102호") #블루투스 스피커
        print("3. 1103호") #작동 되는 휴대폰
        print("4. 1104호") #초코맛 단백질 
        print("5. 아니야.. 이건 불법이야.. 그냥 지나간다.") #그냥 보스전 다이렉트
        f_select = int(input("선택: "))
        while f_select != 1 and f_select != 2 and f_select != 3 and f_select != 4 and f_select != 5:
            f_select = int(input("선택: "))
        if f_select == 1 or f_select == 2 or f_select == 3 or f_select == 4 or f_select == 5:
            return f_select

def scene_2_1_1():
    while (True):
        print("1. 1101호") #소화기 - 소용없음
        print("2. 1102호") #블루투스 스피커
        print("3. 1103호") #작동 되는 휴대폰
        print("4. 1104호") #초코맛 단백질 
        print("5. 이제 그만 가도 될 것 같다.")
        f_select = int(input("선택: "))
        while f_select != 1 and f_select != 2 and f_select != 3 and f_select != 4 and f_select != 5:
            f_select = int(input("선택: "))
        if f_select == 1 or f_select == 2 or f_select == 3 or f_select == 4 or f_select == 5:
            return f_select

def scene_2_2():
    img = Image.open('door.jpg')
    img.show()
    print("(까이익.. 철컥)")
    img = Image.open('monstre1.jpg')
    img.show()
    hgj("어..? 내려왔는데 괴물이 있다..\n")
    hgj("아까 내려오면서 낸 소리에 괴물이 따라온듯하다.\n")
    hgj("역시 다시 올라가서 그냥 지나가는게 좋겠어..\n")
    print("(끼이익..)")
    hgj("어..?\n")
    img = Image.open('monstre.jpg')
    img.show()
    hgj("왜.. 이 괴물이 여기에..\n")
    b("...\n")
    print("(콰직!)")
    img = Image.open('blood.jpg')
    img.show()
    return

def func_weapon(n_select, n_item):
    if n_select == 1 and n_item['fire'] == 0:
        hgj("소화기를 얻었습니다.\n")
        n_item['fire'] = 1
        n_item['count'] += 1
        return n_item
    elif n_select == 2 and n_item['bluetooth'] == 0:
        hgj("블루투스 스피커를 얻었습니다.\n")
        n_item['bluetooth'] = 1
        n_item['count'] += 1
        return n_item
    elif n_select == 3 and n_item['phone'] == 0:
        hgj("작동하는 휴대폰을 얻었습니다.\n")
        n_item['phone'] = 1
        n_item['count'] += 1
        return n_item
    elif n_select == 4 and n_item['protin'] == 0:
        hgj("초코맛 프로틴을 얻었습니다.\n")
        n_item['protin'] = 1
        n_item['count'] += 1
        return n_item
    elif n_select == 5:
        n_item['count'] = -1
        return n_item
    else :
        hgj("여기 방은 아무것도 없다.")
        return n_item

def scene_3():
    while (True):
        print("아.. 젠장 아까 봤던 괴물이.. 여기 말고는 길이 없는데 싸울 수 밖에 없나\n")
        print("1.싸운다 2.도망친다")
        f_select = int(input("선택: "))
        if f_select == 1 or f_select == 2 :
            return f_select
        else :
            print("선택지를 잘못 입력하셨습니다.")
            continue
def scene_3_1(n_item): #수정 필요
    hgj("가지고 있는걸 다 써서 저 괴물을 죽여야겠어\n")
    while True:
        if n_item['fire'] == 1 :
            hgj("소화기로 시아를 차단하면 내가 공격할 수 있지 않을까?")
            print("(푸쉬이익)")
            b("...")
            hgj("아.. 맞아 저 자식 눈이 없었지\n")
            n_item['fire'] = 0
            if n_item['bluetooth'] == 0 and n_item['phone'] == 0 and n_item['protin'] == 0:
                hgj("어..")
                return 2
            elif n_item['bluetooth'] == 1 or n_item['phone'] == 1 or n_item['protin'] == 1:
                continue
        elif n_item['bluetooth'] == 1:
            b("...")
            hgj("그럼 스피커로 유인을 해야겠어\n")
            hgj("젠장.. 배터리가 없어..\n")
            n_item['bluetooth'] = 0
            if n_item['phone'] == 0 and n_item['protin'] == 0:
                b("...")
                return 2
            elif n_item['phone'] == 1 or n_item['protin'] == 1:

                continue
        elif n_item['phone'] == 1:
            hgj("이 휴대폰으로 노래를 틀고 던지면 그쪽으로 갈거야\n")
            print("1.노래를 튼다. 2.노래를 틀지 않는다.")
            f_select = int(input("선택: "))
            n_item['phone'] = 0
            if f_select == 1:
                print("(진진자라 지리지리자!)")
                hgj("좋아 이제 이 휴대폰을 다른쪽에 던지면..어?\n")
                return 2
            elif f_select == 2:
                hgj("맞아.. 소리가 들리면 나를 먼저 죽이겠지\n")
                if n_item['protin'] == 0:
                    hgj("이제.. 남아있는게 없어\n")
                    return 3
                elif n_item['protin'] == 1:
                    return 1
        elif n_item['protin'] == 1:
            return 1
        elif n_item['protin'] == 0:
            return 3

def scene_3_2():
    print("(슈우욱!)")
    print("(푹..)")
    hgj("커헉..")
    print("(추욱..)")
    return

def scene_3_3():
    print("(콰직!)\n")
    hgj("어..?\n")
    hgj("머리 짤린 괴물이..\n")
    hgj("죽었어..\n")
    img = Image.open('protin.jpg')
    img.show()
    red("괴물: ㅍ..ㅡ..ㄹ..ㅗ..ㅌ..ㅣ..ㄴ...\n")
    print("(쿵..쿵)\n")
    hgj("뭐야.. 이쪽으로 오는..\n")
    print("(콰직..)\n")
    img = Image.open('blood.jpg')
    img.show()
    return

#메인 11층 함수
def floor_11():
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        f_select_1 = scene_1()
        if f_select_1 == 1 :
            b("(...)")
            img = Image.open('corridor.jpg')
            img.show()
            hgj("휴.. 겨우 복도를 지났다.. 앞에 방이 많다.. 쓸모있는 물건을 얻을 수 있을거 같아.. 한번 들어가 볼까? 어떤 방을 먼저 들어가보지..?\n")
            f_select_2 = scene_2_1()

            item = {'fire': 0, 'bluetooth': 0, 'phone': 0, 'protin': 0, 'count': 0}
            item = func_weapon(f_select_2, item)
            while (True):
                f_select_2 = 0
                if item['count'] >= 3:
                    hgj("이제 필요한 물건은 다 챙긴거 같으니 가보자")
                    break
                elif item['count'] == -1:
                    print("(뚜벅.. 뚜벅..)")
                    break
                f_select_2 = scene_2_1_1()
                if f_select_2 != 0:
                    item = func_weapon(f_select_2, item)
        
            f_select_3 = scene_3()
            if f_select_3 == 1:
                f_select_3_1 = scene_3_1(item)
                if f_select_3_1 == 1:
                    print("(콰직!)\n")
                    hgj("어..?\n")
                    hgj("머리 짤린 괴물이..\n")
                    hgj("죽었어..\n")
                    red("괴물: ㅍㅡㄹㅗ...ㅌㅣㄴ...\n")
                    hgj("프로틴? 혹시 이걸 원하는 건가?\n")
                    img = Image.open('protin.jpg')
                    img.show()
                    hgj("이걸 보고 있는거 같아.\n")
                    print("(쿵..쿵)\n")
                    hgj("이쪽으로 온다.. 에라 모르겠다 에잇!\n")
                    print("(프로틴을 내 뒤쪽으로 던졌다)\n")
                    img = Image.open('protin1.jpg')
                    img.show()
                    print("(쿵.쿵.쿵.쿵)\n")
                    hgj("후..\n")
                    hgj("내 바로 옆을 지나갔어...\n")
                    hgj("좋아 이제 앞으로 갈 수 있겠어\n")
                    floor_over = True
                elif f_select_3_1 == 2:
                    scene_3_2()
                    game_over = True
                elif f_select_3_1 == 3:
                    scene_3_3()
                    game_over = True
            elif f_select_3 == 2:
                scene_3_2()
                game_over = True
        elif f_select_1 == 2 :
            scene_2_2()
            game_over = True

# 이동원
def floor16_18():
    global sohwa, floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        print("[16층]")
        hgj("우여곡절 끝에 16층까지 올라왔다.\n")
        hgj("하지만 위로 올라가는 계단에 반쯤 부숴진 바리케이드가 있었다.\n")
        hgj("잘만 하면 지나갈 수 있을 것 같은데 지나가 볼까?\n\n")
        select = int(input("1. 지나가 본다. 2. 비상구로 나가 16층을 빠져나갈 방법을 찾아본다.\n"))
        print("\n")
        while select != 1 and select != 2:
            select = int(input("선택지를 잘못 입력하셨습니다."))
        print("")
        if select == 1:
            b("...")
            hgj("부스락..바스락..\n")
            hgj("음... 조금 들어가보니 뒤쪽에 가구가 더 쌓여있다.\n아무래도 지나가기 힘들 것 같으니 다른길을 찾아봐야겠다.\n")
        elif select == 2:
            hgj("음...아무래도 지나가기 어려울 것 같다.\n혹시 다른 괴물이 소리를 듣고 찾아 올 수 있으니 괜히 힘들이지 말고 다른길을 찾아봐야겠다.\n")

        hgj("...\n\n")
        hgj("다른 길을 계속 찾아 봤지만 아무것도 없었다.\n엘리베이터를 통해 가야하나?\n")
        hgj("전기가 안들어와 작동은 멈췄겠지만 승강로를 통해 윗층으로 갈 수 있을 것이다.\n")
        print("")
        select = int(input("1. 조금 더 찾아본다. 2. 바로 승강로를 통해 올라간다.\n"))

        while select != 1 and select != 2:
            select = int(input("선택지를 잘못 입력하셨습니다."))

        print("")
        if select == 1:
            b("...!\n")
            hgj("소화기를 찾았다. 둔기로도 쓸 수있고 여차하면 연막으로 쓸 수 있을 것이다.\n")
            sohwa += 1
        elif select == 2:
            print("길을 찾느라 시간이 지체됐다.\n옥상에 너무 늦게 가면 구조헬기가 떠날지도 모른다. 빠르게 올라가야겠다.\n")
        b("...\n")
        hgj("엘레베이터 앞")
        img = Image.open('elevator.gif')
        img.show()#이미지 보여줌
        hgj("승강로가 노후되어 위험해 보인다.\n하지만 길이 없으니 어쩔 수 없다.\n")
        hgj(' "흡!.."\n\n')
        hgj("끼이익...\n")
        hgj("쾅!")
        floor_over = True

def floor19_rooftop():
    global floor_over, game_over, sohwa
    floor_over = False
    while floor_over != True and game_over != True:
        print("[19층]")
        hgj("후..승강로의 끝인 19층까지 올라오는데 성공했지만 잔해가 떨어지면서 큰소리가 났다.\n")
        hgj("아마 근처에 있는 괴물이 접근 할 것이다.\n 앞으로 한 층남았는데 괴물따위에 죽을 수 없다\n")
        b("쿵...쿵..\n")
        hgj("없기를 바랬지만 결국 괴물이 나타났다.\n")
        img = Image.open("1_protein.gif")
        img.show()#이미지 보여줌
        red("'ㅍㅡㄹㅗㅌㅣㄴ..'\n")
        hgj("놈이 막고 있는 길은 옥상으로 향하는 유일한 통로다. 맞서 싸우던가 빠르게 피해 도망가는 수 밖에 없다.\n\n")
        if sohwa == 1:
            print("\n")
            select = int(input("1. 소화기를 분사해 도주한다. 2. 더러운 괴물놈에게 도망칠 수 없다. 맞서싸운다.\n"+"\x1b[32m"+"!Tip소화기를 가지고 있는 경우 근육괴물과 싸워서 이길 확률은 10%입니다."+"\x1b[0m"))

            while select != 1 and select != 2 :
                select = int(input("선택지를 잘못 입력하셨습니다."))

            print("")
            if select == 1:
                hgj("푸쉬익!!")
                b("..!\n")
                red("ㄱㅡㄴㅇㅠㄱ..\n")
                hgj("소화기를 분사해 시야를 가려 녀석이 혼란스러워 하는 사이 무사히 옥상으로 빠져 나와 탈출했다. \n")
                img = Image.open('hel.gif')
                img.show()
                floor_over = True
            elif select == 2:
                n = random.randint(1,100)
                if 1<= n and 10 >=n:
                    b("...")
                    hgj("나는 놈에게 멸치라고 도발해 내가 올라왔던 승강로로 유인했다.\n")
                    hgj("그 후 소화기를 분사해 시야를 가렸고 녀석이 혼란스러워 하는 사이 온몸으로 밀쳐 떨어뜨렸다.\n")
                    hgj("19층 높이이니 괴물이라도 무사하진 못할 것이다.\n")
                    img = Image.open('hel.gif')
                    img.show()
                    floor_over = True
                else:
                    b("...쿵!\n")
                    img = Image.open('protein_2.gif')
                    img.show()
                    hgj("나는 놈에게 멸치라고 도발해 내가 올라왔던 승강로로 유인했다.\n")
                    hgj("그 후 소화기를 분사해 시야를 가리고 온몸으로 밀쳤다.\n")
                    hgj("하지만 놈은 본능적으로 문틀을 잡고 버텼고 나는 고군분투하였지만 한끝차이로 실패했다.")
                    floor_over = True
                    game_over = True
                    
        else:
            print("\n")
            select = int(input("1. 도주한다.  2. 더러운 괴물놈에게 도망칠 수 없다. 맞서싸운다.\n"+"\1xb[32m"+"!Tip맨손일때 괴물에게 도주할 확률은 60%,이길 확률은 1%입니다.\n "+"\1xb[0m \n"))
            n = random.randint(1,100)
            while select != 1 and select != 2  :
                select = int(input("선택지를 잘못 입력하셨습니다."))

            print("")
            if select == 1:
                if n >=1 and n <= 60:
                    b("...")
                    hgj("잔해를 던져 괴물의 주의를 끈 후 죽을 힘을 다해 도주했고 성공했다.\n")
                    img = Image.open('hel.gif')
                    img.show()
                    print("\n")
                    return 1
                    
                else:
                    print("...쿵!\n")
                    img = Image.open('protein_2.gif')
                    img.show()
                    hgj("잔해를 던져 괴물의 주의를 끈 후 죽을 힘을 다해 도주했지만 결국 잡히고 말았다.\n 역시 싸웠어야 했나?\n")
                    game_over = True
            elif select == 2:
                if n == 1:
                    b("...")
                    hgj("더러운 괴물놈에게서 도망칠 수 없다.\n")
                    hgj("무아지경으로 괴물과 싸웠고 정신을 차려보니 녀석은 죽어있었다.\n")
                    hgj("...")
                    hgj("나 또한 괴물이 되어가는 것일까?\n")
                    img = Image.open('hel.gif')
                    img.show()
                    hgj("하지만 달라지는 것은 없다. 다음을 기약하기 위해 탈출 할 뿐이다.\n")
                    floor_over = True
                else:
                    hgj("...해치웠나?")
                    b("..")
                    hgj("쿵!")
                    img = Image.open('protein_2.gif')
                    img.show()
                    hgj("반전은 없었다.\n")
                    game_over = True

def end():
    global floor_over, game_over
    floor_over = False
    while floor_over != True and game_over != True:
        green("주인공은 옥상에서 대기하고 있던 헬기를 타고 탈출했다.\n")
        game_over = True

# 메인코드
floor_over = False
game_over = False
sohwa = 0
while game_over != True:
    start()
    floor_1()    
    floor_5()
    floor_6()
    floor_7()
    floor_8()
    floor_9()
    floor_10()
    floor_11()
    floor16_18()
    floor19_rooftop()
    end()
    Game_over()