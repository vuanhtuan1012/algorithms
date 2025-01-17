# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-01-17 05:42:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-01-17 05:44:48

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
- questionCorrection("this is not a relevant question , is it???") = "This is not a relevant question, is it?"
- questionCorrection("who are you,,???") = "Who are you?"
"""