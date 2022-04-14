import sys


def repl(text):
    temp = text.replace("0", " .")
    temp = temp.replace("1", " #")
    return temp


def replrev(text):
    temp = text.replace(" ?", "0")
    temp = temp.replace(" .", "0")
    temp = temp.replace(" #", "1")
    return temp


logichome = sys.argv[1]

logichome_list = []
with open(logichome, "r", encoding="utf-8") as f:
    for line in f:
        if line == "\n":
            line = line.replace("\n", "")
        else:
            logichome_list.append(line.rstrip())

# rstrip 오류 방지 - 리스트에서 빈 요소 삭제
logichome_list = [i for i in logichome_list if i]


# 파일 - txt to griddler
if logichome[-3:] == "txt":
    width = int(logichome_list[1])
    height = int(logichome_list[2])
    logic = str(logichome_list[3])
    divided_logic = [logic[i : i + width] for i in range(0, len(logic), width)]
    for i in range(len(divided_logic)):
        divided_logic[i] = repl(divided_logic[i])

    with open(logichome[:-3] + "griddler", "w", encoding="utf-8") as f:
        f.write("MK Version 3.0\n")
        f.write("\n")
        f.write(f"{width} {height}\n")
        for i in range(len(divided_logic)):
            f.write("\n")
            f.write(f"{divided_logic[i]}")
    print("txt -> griddler 변환작업 완료!")
    input("엔터를 누르면 종료됩니다.")

# 파일 - griddler to txt
elif logichome[-3:] == "ler":
    width = logichome_list[1].split(" ")[0]
    height = logichome_list[1].split(" ")[1]
    return_list = []
    for i in range(2, len(logichome_list)):
        logichome_list[i] = replrev(logichome_list[i])
    del logichome_list[1]
    del logichome_list[0]
    logichome_list = "".join(logichome_list)
    with open(logichome[:-8] + "txt", "w", encoding="utf-8") as f:
        f.write("www.logichome.org\n")
        f.write(f"{width}\n")
        f.write(f"{height}\n")
        f.write(f"{logichome_list}")
        f.write("\n")
        f.write("\n")
    print("griddler -> txt 변환작업 완료!")
    input("엔터를 누르면 종료됩니다.")

else:
    print("파일 확장자 오류!")
    input("엔터를 누르면 종료됩니다.")
