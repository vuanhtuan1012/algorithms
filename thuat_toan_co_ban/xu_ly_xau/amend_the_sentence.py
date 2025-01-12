# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-12 12:05:51
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-12 12:15:19

"""
Cho một xâu kí tự s gồm nhiều từ. Trong đó mỗi từ sẽ được bắt đầu bởi một kí tự in hoa.
Vì một lí do gì đó, người ta quên chèn các khoảng trắng giữa các từ.

Hãy viết chương trình sửa lại xâu kí tự đó theo yêu cầu sau:
- Tách các từ, và thêm 1 kí tự cách (space) giữa 2 từ liên tiếp
- Chuyển đổi các kí tự in hoa thành kí tự in thường

Ví dụ:
- amendTheSentence("CodelearnIsAwesome") = "codelearn is awesome"
- amendTheSentence("Hello") = "hello"
"""


def amend_the_sentence(sentence: str) -> str:
    """
    Returns the sentence amended
    """
    amended_sentence = ""
    for char in sentence:
        if char.islower():
            amended_sentence += char
        else:
            amended_sentence += f" {char.lower()}"
    return amended_sentence.strip()


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        ("CodesignalIsAwesome", "codesignal is awesome"),
        ("Hello", "hello"),
        (
            "vSKwWDjwIerQKMgVaAniorRJlerbKpDgvyKBLPNwSRWtylqKewNFtERNuUBBHAsGkTSSfdhQHJYvAighAdeG",
            (
                "v s kw w djw ier q k mg va anior r jlerb kp dgvy k b l p nw"
                " s r wtylq kew n ft e r nu u b b h as gk t s sfdh q h j yv aigh ade g"
            ),
        ),
        (
            (
                "iFvFAxtViLJDuWWXJesppOcLVdRAJZwBobdczkkWSPHzFLf"
                "yvmJYPdqYqRKKvLGYLwEFXcJiyYWLqjBvHjeqE"
            ),
            (
                "i fv f axt vi l j du w w x jespp oc l vd r a j zw bobdczkk"
                " w s p hz f lfyvm j y pdq yq r k kv l g y lw e f xc jiy y w lqj bv hjeq e"
            ),
        ),
        ("iEiMCyKAdsfGMPa", "i ei m cy k adsf g m pa"),
    ]
    for sentence, ground_truth in test_cases:
        result = amend_the_sentence(sentence)
        print(f"amend_the_sentence({sentence}) = {result}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
