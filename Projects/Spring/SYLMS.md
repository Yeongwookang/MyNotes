## SYLMS (대학교 학사관리 프로그램)

실제 대학 학사관리 프로그램을 참고하여 만들어 졌으며, 프로젝트 기간은 2022.10.31 ~ 2022.11.18 입니다.
<br>[https://github.com/ssj946/SYLMS](https://github.com/ssj946/SYLMS)

## 기술스택

#### Back-end
<img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white"> 

#### Front-end
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">

#### DB
<img src="https://img.shields.io/badge/oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white"> 

#### WAS
<img src="https://img.shields.io/badge/apache tomcat-F8DC75?style=for-the-badge&logo=apachetomcat&logoColor=white">

#### ETC
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/fontawesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white">


<br>
<br>

## 개요

대학교 학사관리 프로그램에는 교수자(교수)와 학습자(학생), 관리자(조교) 가 존재합니다. 

실제로 대학생활중 조교활동을 해봤던 경험이 사용자 입장에서 더 편한 프로그램을 만드는데 도움이 되었습니다.

학생의 등록은 학교 측에서 학번을 ID로 부여하고 초기 비밀번호를 바꾸는 방식을 채택했습니다.

전체적인 레이아웃은 DashBoard의 형태로 왼쪽 사이드바와 상단 로그인 및 커뮤니티 바로 구성되었습니다.

<br>
<br>

## 작성 코드

단순 CRUD 작업에 대한 설명은 생략하고, 본인이 작성한 코드에 대한 내용만 기재하였습니다.

<br>

### 메인

오른쪽 사이드바에는 할 일이라는 마감이 다가오는 과제나 신청을 보여줍니다.

이번학기 강의는 해당학기의 수강신청된 강의실로 연결되며, 출석을 바로 진행 할 수 있습니다.

강의 History에서는 역대 수강한 강의실 기록을 볼 수 있으며, 학년/학기별로 조회가 가능합니다.

<br>

### 강의실

강의실에서는 오른쪽 사이드바가 아이콘만 남고 간소화 됩니다.

개별 강의실로 연결되는 방식은 GET방식을 통해 DB에서 과목정보를 받아와서 강의실 타이틀을 구성했습니다.

해당 수업을 듣지 않는 사람이 강의실에 접근하면 경고창과 함께 메인페이지로 redirection 했습니다.

강좌 개요를 통해 강의실 홈, 수업계획서, 공지사항, 성적/출석관리, 학습활동, 커뮤니티로 이동이 가능합니다.

<br>

#### 강의실 홈

    강의실 홈에는 이번 주 강의, 주차별 학습활동으로 구성되어있으며, 
    이번주 강의는 해당일자에 수강이 가능한 강의를 띄워주고,
    주차별 학습활동은 전체 강의에 대한 복습 및 강의자료를 제공합니다.
    BootStrap을 활용하여 화면을 디자인했으며, 해당 페이지 내에서 바로 강의 및 자료를 등록할 수 있습니다.

#### 강의 / 강의자료

    강의를 클릭하게되면 동영상이 바로 보이게되며, 해당 페이지에서 강의에 대한 수정삭제가 가능합니다.
    파일첨부가 가능하며, 댓글은 작성할 수 없습니다.

#### 과제

    과제는 교수자가 과제를 등록일과 마감일을 설정하여 등록하면, 학생들에게 보이는 방식입니다.
    학생들은 교수자가 공개하기 전에는 과제를 볼 수 없으며, 마감일을 지나서 과제를 제출할 수 없습니다.

#### 출석

    출석은 교수자가 출석하기 버튼을 통해 출석을 만들면,
    5분동안 출석이 가능하며, 학생들은 지정된 시간내에 출석을 해야합니다.
    아래의 check, x, run 버튼을 통해 자신의 출석기록과 횟수를 알 수 있습니다.


<br>
<br>

## 프로젝트를 마무리하며

#### 소감 및 성취

    DB의 구조와 쿼리의 중요성을 느끼게 되었습니다. 
    OUTER JOIN 과 여러테이블을 한번에 Update, DELETE 하는 방법을 익히게 되었고, 
    트랜젝션 단위를 어디까지로 지정해야 하는지에 대한 이해가 ERD작성에도 영향을 준다는 것을 알게되었습니다.
    PreparedState 문을 반복쿼리에 대해 batch를 활용하여 작성해보았습니다.
    ajax를 통한 비동기식 데이터처리를 처음 해보았고, 유명한 사이트들은 비동기식 처리를 할수 있는것이 많은데
    어떤 프레임워크를 통해서 할 수 있는지에 대해 의문이 생겼습니다.
