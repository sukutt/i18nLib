from i18nLib import i18nLib

inputPath = input("경로를 입력하세요: ")
oldCSV = input("기존 CSV 파일을 입력하세요: ")
newCSV = input("새로운 CSV 파일을 입력하세요: ")
ext = input("확장자를 입력하세요: ")
i18nLib.change(inputPath, oldCSV, newCSV, ext)


