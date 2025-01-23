# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-17 05:42:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-23 16:26:17

"""
Một hệ thống hỏi đáp trực tuyến cần chuẩn hóa câu hỏi của người dùng.
Một câu hỏi đã được chuẩn hóa cần tuân thủ các luật sau:

- Luật chung: Câu hỏi chỉ chứa kí tự chữ cái (a-zA-Z), chữ số (0-9), dấu phẩy (,),
  dấu cách (' '), dấu hỏi (?). Các kí tự khác đều được thay thế bằng dấu cách
- Luật dấu cách: Không có dấu cách ở đầu hay ở cuối câu.
  Giữa các từ chỉ có 1 dấu cách duy nhất. Sau mỗi dấu cách là 1 chữ cái hoặc chữ số?
- Luật dấu phẩy: Trước dấu phẩy luôn là 1 chữ cái hoặc chữ số. Sau dấu phẩy luôn là một dấu cách
  Trường hợp đứng trước dấu phẩy là dấu cách, hãy xóa dấu cách này đi.
- Luật chữ hoa/chữ thường: Chữ cái bắt đầu câu luôn được viết hoa. Các chữ cái khác đều viết thường
- Luật dấu hỏi: Luôn có 1 dấu ? kết thúc câu. Trước dấu ? luôn là kí tự chữ cái hoặc chữ số
  Trường hợp có các dấu ? xuất hiện khi chưa kết thúc câu, hãy thay thế nó bằng dấu cách
  Trường hợp trước dấu cách là dấu phẩy và dấu cách, hãy xóa dấu cách và dấu phẩy

Ví dụ:
- questionCorrection("this is not a relevant question , is it???")
  = "This is not a relevant question, is it?"
- questionCorrection("who are you,,???") = "Who are you?"
"""

import re


def correct_question(question: str) -> str:
    """
    Returns the standardized question
    """
    # common rule
    standardized_question = re.sub(r"[^a-zA-Z0-9, \?]", " ", question)

    # space rule
    standardized_question = re.sub(r"^\s+", "", standardized_question)
    standardized_question = re.sub(r"\s+$", "", standardized_question)
    standardized_question = re.sub(r"\s{2,}", " ", standardized_question)

    # comma rule
    standardized_question = re.sub(r"[^a-zA-Z0-9],+", ",", standardized_question)
    standardized_question = re.sub(r",([^ ])", ", \\g<1>", standardized_question)

    # upper/lower case rule
    standardized_question = re.sub(
        r"^([a-z])", lambda match: match.group(1).upper(), standardized_question
    )
    standardized_question = re.sub(
        r"(?<!^)[A-Z]", lambda match: match.group(0).lower(), standardized_question
    )

    # question mark rule
    standardized_question = re.sub(r"[^a-zA-Z0-9]+\?+", "?", standardized_question)
    standardized_question = re.sub(r"\?(?=[^$])", "", standardized_question)
    standardized_question = re.sub(r"([^\?])$", "\\g<1>?", standardized_question)

    return standardized_question


def dry_tests():
    """
    Dry tests
    """
    test_cases = [
        (
            " this  is not   a     relevant question , is it??? ",
            "This is not a relevant question, is it?",
        ),
        ("Is this answer correct?", "Is this answer correct?"),
        ("                                      s.", "S?"),
        ("z?", "Z?"),
        ("z", "Z?"),
        (
            " what is the value? of Sin theta into cos theta ,?",
            "What is the value of sin theta into cos theta?",
        ),
    ]
    for i, (question, ground_truth) in enumerate(test_cases):
        result = correct_question(question)
        print(f"Test case {i+1}: {result == ground_truth}")


if __name__ == "__main__":
    dry_tests()
