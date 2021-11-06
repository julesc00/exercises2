
def compile_something(source: "something definition here",
                      filename: "something else",
                      mode: "what are you talking about here?"):
    my_source = source
    my_file = filename
    my_mode = mode


def solution(a: list) -> int:

    def check_if_even(number: int) -> bool:
        return bool(number % 2)

    def check_if_odd(number: int) -> bool:
        return not check_if_even(number)

    even_max = max(list(filter(
        check_if_even, a
    )) + [0])

    odd_max = max(list(filter(
        check_if_odd, a
    )) + [0])

    return even_max + odd_max


print(solution([20, 37]))

