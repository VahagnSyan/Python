"""
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է
տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ:
Օրինակ
մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Արդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
"""


def test_mix_nested_lists():
    input_list1 = [["a", "b"], ["c", "d"]]
    assert mix_nested_lists(input_list1) == ["a", "b", "c", "d"]

    input_list2 = [[1, 2, 3], [4, 5, 6]]
    assert mix_nested_lists(input_list2) == [1, 2, 3, 4, 5, 6]

    input_list3 = [["x", "y"], ["z"]]
    assert mix_nested_lists(input_list3) == ["x", "y", "z"]

    input_list4 = [[]]
    assert mix_nested_lists(input_list4) == []

    input_list5 = []
    assert mix_nested_lists(input_list5) == []

    print("All test cases passed!")


def mix_nested_lists(list):
    merged_list = []

    for sublist in list:
        # Adds every element of subarray to merged_list
        merged_list.extend(sublist)

    return merged_list


test_mix_nested_lists()
