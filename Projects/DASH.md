
## DASH (서울시 지하철 인원 정보를 활용한 공유 모빌리티 이송 계획 시스템)

프로젝트 기간은 2022.12.26 ~ 2023.01.27 입니다. 팀장으로서 주도적으로 프로젝트를 진행했습니다.
<br>[https://github.com/Yeongwookang/DASH](https://github.com/Yeongwookang/DASH)

## 기술스택

#### Back-end
<img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white"> <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

#### Front-end
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"> <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">

#### DB
<img src="https://img.shields.io/badge/oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white"> <img src="https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">

#### WAS
<img src="https://img.shields.io/badge/apache tomcat-F8DC75?style=for-the-badge&logo=apachetomcat&logoColor=white">

#### ETC
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/fontawesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white">


<br>
<br>

## 개요
서울시 지하철 인원정보를 유동인구로 해석, 서울 열린 데이터광장과 국토부 자료를 취합하여 연관된 지리데이터를 만들고,

공유 모빌리티를 당시 가장 많은 점유율을 가지고 있던 전동 킥보드로 선정하여,

그룹웨어 + 전동 킥보드 대여소 위치 추천 시스템 (Python, QGIS 활용) 구현

<br>
<br>

## 작성 코드

단순 CRUD 작업에 대한 설명은 생략하고, 본인이 작성한 코드에 대한 내용만 기재하였습니다.
Spring Legacy Project / JSP를 사용하였습니다.

<br>

### 메인 / 레이아웃

Tiles3를 적용하여 레이아웃에 대한 중복요소 제거했습니다. 각 페이지는 반응형웹이고, 상단 sticky-top 바를 갖습니다.

    


<br>

## 프로젝트를 마무리하며

#### 소감 및 성취

    Spring MVC(Model, View, Controller)에서 이전 프로젝트와 달리 많은 부분을 Spring Framework가 자동으로 처리해주어 불필요한 코드의 중복이 상당히 줄어들었고, 
    의존성 주입을 통해 tiles3, spring security를 활용하게 되어 편했다.
    레거시코드에서 logback과 slf4j를 활용하고 AOP단계를 조정하여 콘솔창에 너무 많은 내용이 나오지 않게 하였다.
    JavaScript 부분에서는 처음 사용해본 leaflet으로 마커, 화면구성, 다각형 띄우기 등을 원문 사이트 튜토리얼을 통해 처리했고,
    geojson으로 만들어주는 프로그램인 QGIS에 국토부 자료와 서울시 자료를 합치거나 빼서 만든 다각형을 하는 등의 전처리 과정을 해내었다.
    이 과정에서 공간좌표계등의 별도의 공부가 필요했지만, 원래 공학을 하던 입장에서 필요한 것을 새로 배워서 적용하는것에 대한 부담이 적었다.
    모든 과정이 수학문제를 풀 듯이 해결할 수 있었고, 나름 재미있었다.
