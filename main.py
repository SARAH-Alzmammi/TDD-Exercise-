import re


class Calculator:

    def add(self, numbers: str) -> int:
        delimiter = ','
        if numbers.startswith('//'):
            delimiter = numbers[numbers.find('//') + len('//'):numbers.rfind('\n')]
            numbers: str = numbers.removeprefix(f"//{delimiter}\n").strip()

            if numbers.count(delimiter) * 2 != len(re.findall(r'[0-9]+', numbers)):
                unexpected_delimiter = ''.join([i for i in numbers.replace('delimiter', '') if not i.isdigit()])
                raise Exception(
                    f"'{delimiter}' expected but ‘{unexpected_delimiter[0]}’ found at position {numbers.find(unexpected_delimiter[0])}.")

        else:
            numbers = numbers.replace('\n', delimiter)

        numbers: list = numbers.split(delimiter)

        if numbers[-1] == '' and len(numbers) > 1:
            raise Exception('The string must not end with a delimiter')

        final_res = 0
        for i in numbers:
            final_res += int(i if i.isdigit() else 0)
        return final_res