# Lab 02: Câu trả lời thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?
Nhánh tính năng được tạo từ master cũ nên thiếu những thay đổi mới. Gộp
master vào nhánh trước giúp phát hiện xung đột và lỗi tích hợp ngay trên
máy mình thay vì lúc gộp PR.

## 2. Khi nào không được rebase?
Khi các commit đã được chia sẻ (đã push, người khác đã dựa vào). Rebase viết
lại lịch sử và sinh SHA mới, làm hỏng nhánh của người khác.

## 3. feature/* khác topic/* ra sao?
feature/* là một tính năng của sản phẩm (cart-print, search-by-title).
topic/* là chủ đề khác không phải tính năng, như tài liệu, template, cấu hình.
