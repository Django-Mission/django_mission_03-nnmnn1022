# django_mission_03-nnmnn1022

## Basic
- 고객센터(`support`) 앱의 자주묻는질문(`Faq`), 1:1문의(`Inquiry`), 답변(`Answer`) 관리자 페이지 등록
    - 자주묻는질문(`Faq`)
        - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
        - 검색 필드 : 제목
        - 필터 필드 : 카테고리
    - 1:1문의(`Inquiry`)
        - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
        - 검색 필드 : 제목, 이메일, 전화번호
        - 필터 필드 : 카테고리
        - 인라인모델 : 답변(`Answer`)
    - 답변(`Answer`)
        - 1:1문의 모델에 인라인모델로 추가

https://user-images.githubusercontent.com/41253926/166137694-11f9667c-4038-47c1-8acd-f9d7d7a556b1.mp4

## Challenge
- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력
        
        ※ action을 추가 학습을 위한 목적으로 실제 문자, 메일은 발송하지 않습니다.
        
        기능의 목표가 고객센터 담당자 업무 효율을 위한 사용성 개선이었기 때문에
        답변 완료된 내용 중 알림을 보낸 항목들은 `알림 완료`로 상태를 변경하도록 하는 코드도 추가함.



https://user-images.githubusercontent.com/41253926/166139532-f9d71b32-3740-46e7-b816-0ea3b61355f4.mp4

