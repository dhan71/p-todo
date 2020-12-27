# p-todo
manage personal todo list

# development evironment
DB : sqlite3
Language : python3
Gui : qtpy(Qt5) or wxPython
version control : git & github

# Toto structure
priority : number(2) - (1 ~ 9) or (High,Mid,Low)
group : varchar(100)
begin date : date
end date : date
title : varchar(500)
contents : varchar(4000)

# App
name : p-todo
license : ?
documents :
  1. help
  2. waht is

# 기능 정리

1. mobile - PC 연동 (부차적인 기능으로 꼭 필요한가?)
2. title & contents 입력 가능
3. todo를 우선순위로 정렬
   - 높은 우선순위를 위에 표시
   - 사용자가 drag&drop 으로 위치를 이동하면 우선순위 변경
   - 새로 입력한 todo는 제일 높은 우선순위 부여
   - 동일 우선순위인 경우 마감 날짜로 정렬
4. 진행todo, 완료todo 로 분리해서 관리
   완료한 todo는 진행 중 todo에서 제거하고 완료 todo로 이동
5. 진행todo, 완료todo 조회 가능
6. 완전 삭제 기능
7. 조회 - title, contents, end date, begin date
8. 검색 - 키워드로 title, contents 검색
   search - search titles, contents with a keyword
9. python이면 windows, linux 모두 지원 가능?
10. 다국어 지원(한국어, 영어)
    multi language(Korean, English)
11. todo grouping 기능


# App view components

No Menu
Toolbar : [new] [quit] [search]
Table
Seq  Priority  End Date    Title       Contents           begin Date
1    5         2020-12-08  make todo   todo management    2020-12-01