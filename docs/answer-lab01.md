# Lab 01: Câu trả lời thảo luận

## 1. Vì sao dùng git mv?
`git mv` vừa di chuyển file vừa đưa thay đổi vào staging. Git không lưu
"đổi tên" như một thao tác riêng mà tự nhận ra file giống nhau về nội dung,
nên lịch sử vẫn theo dõi được bằng `git log --follow`, và PR hiển thị
"renamed" thay vì xóa file cũ rồi thêm file mới.

## 2. release/lab01 có phải baseline không?
Có. Nó được tạo từ master sau khi mọi thay đổi đã qua Pull Request, là
phiên bản đã thống nhất và chỉ thay đổi qua quy trình. Tuy nhiên nhánh có
thể bị di chuyển, nên về sau (Lab 04) cần gắn tag để định danh chính xác.

## 3. Vì sao không commit thẳng master dù làm một mình?
Master là nhánh tích hợp, mọi thứ nên qua PR để có điểm review, lịch sử rõ
ràng, dễ revert một thay đổi và để tập đúng quy trình làm việc nhóm. Branch
protection cũng chặn push trực tiếp nên không ai lỡ tay làm hỏng master.