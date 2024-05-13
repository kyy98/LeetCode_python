# 로그의 가장 앞 부분은 식별자
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 식별자는 순서에 영향을 끼치지 않지만 문자가 동일한 경우 식별자 순으로 한다
# 숫자 로그는 입력 순서대로 한
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits=[], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))   #sort 기준 순서대로
        return letters+digits
        