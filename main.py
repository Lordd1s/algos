def solution(roman_numeral):
    """Returns the rome number to normal number"""
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    decimal_value = 0
    prev_value = 0

    for char in reversed(roman_numeral):
        value = roman_dict[char]
        if value < prev_value:
            decimal_value -= value
        else:
            decimal_value += value
        prev_value = value

    return decimal_value


def narcissistic(number):
    """Check if a number is Narcissistic!"""
    res = " ".join(str(number))
    num_len = len(res.split(" "))
    # print(num_len)
    var = 0
    for i in res.split(" "):
        # print("i: ", i)
        var += int(i) ** num_len
    if var == number:
        return True
    else:
        return False


def alphabet_to_int(string):
    """Converts a string"""
    alphabet = "".join("abcdefghijklmnopqrstuvwxyz")
    result_dict = {}
    result_string = " "
    var = 1
    for i in alphabet:
        result_dict[i] = var
        var += 1

    for j in string.lower():
        if j not in result_dict:
            continue
        else:
            result_string += str(result_dict[j]) + " "
    print(result_dict)
    return result_string


def snail_sort(array):
    result = []
    while array:
        # Извлекаем верхнюю строку
        result += array[0]
        array = array[1:]

        if array and array[0]:  # Проверяем, что остались строки и первая строка не пуста

            # Извлекаем крайний правый столбец
            for row in array:
                result.append(row.pop())

        if array:  # Проверяем, что остались строки

            # Извлекаем нижнюю строку в обратном порядке
            result += array.pop()[::-1]

        if array and array[0]:  # Проверяем, что остались строки и первая строка не пуста

            # Извлекаем крайний левый столбец в обратном порядке
            for row in array[::-1]:
                result.append(row.pop(0))

    return result


def trim(phrase, size):
    """
    :param phrase: take string
    :param size: take int which must take to cut
    :return: cutted string
    """
    if size < 3:
        return phrase[:size] + "..."
    elif len(phrase) > size:
        return phrase[:size - 3] + "..."

    return phrase


def solution_text(text: str, ending: str):
    """Return True if the given text ends with parameters: ending"""
    res = text[: len(text) - len(ending) - 1: -1]
    print(res)
    return True if res[::-1] == ending or text == ending else False


def is_square(n):
    val = n // 2
    print(val)
    if n < 0:
        return False
    elif n == (val ** 2):
        return True
    else:
        return False


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        sorted_price = sorted(prices)
        money_decreament = money
        buyed = []
        for i in sorted_price:
            if i <= money_decreament:
                money_decreament -= i
                buyed.append(i)
            if len(buyed) >= 2:
                return money_decreament
        return money

    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        original_num = x

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original_num == reversed_num

# TwoSum

class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if nums[0] + nums[-1] == target:
            return [0, ]
        for idx, elem in enumerate(nums):
            if elem + nums[idx + 1] == target:
                return [nums.index(elem), idx + 1]


class AddTwoNumbers:
    def add_two_numbers(self, l1: list[int], l2: list[int]) -> list[int]:
        all_list = [l1, l2]
        result = []
        final = []
        while len(all_list[0]) > 0 and len(all_list[1]) > 0:
            summ = all_list[0][-1] + all_list[1][-1]
            result.insert(0, summ)
            all_list[0].pop(-1)
            all_list[1].pop(-1)
        for idx, el in enumerate(result):
            if el >= 10:
                el = 0
                result[idx + 1] += 1
            final.append(el)
        return final


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral
    

if __name__ == "__main__":
    # print(solution("IV"))
    # print(narcissistic(4338281769391370))
    # print(alphabet_to_int("The sunset sets at twelve o'clock."))
    # print(snail_sort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(trim("he", 1))
    # print(solution_text("samurai", "ai"))
    # print(is_square(25))
    # print(Solution().buyChoco(prices=[98, 54, 6, 34, 66, 63, 52, 39], money=62))
    # print(TwoSum().twoSum(nums=[3, 2, 3], target=6))
    # print(AddTwoNumbers().add_two_numbers(l1=[2, 4, 3], l2=[5, 6, 4]))
    # print(Solution().isPalindrome(121))
    print(int_to_roman(3549))
