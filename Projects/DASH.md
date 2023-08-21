
## DASH (서울시 지하철 인원 정보를 활용한 공유 모빌리티 이송 계획 시스템)

프로젝트 기간은 2022.12.26 ~ 2023.01.27 입니다. 팀장으로서 주도적으로 프로젝트를 진행했습니다.
<br> 같은 폴더내에 DASH.pdf가 프로젝트 상세 문서입니다.
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

Tiles3를 적용하여 레이아웃에 대한 중복요소 제거했습니다. 

각 페이지는 반응형웹이고, 상단 sticky-top 바를 갖습니다.

출/퇴근, 연차, 공지사항, 진행중인 결재, 일정, 커뮤니티, 우측 사이드바로 구성되어있습니다.

<br>

#### 출/퇴근
    출근을 눌러 해당 시간으로 출근시각이 찍히면, 
    퇴근 가능한 시간을 계산하여 해당 시간 이후에 퇴근버튼이 활성화 됩니다.
    출퇴근 현황 버튼을 통해 자신의 출퇴근 기록을 볼 수 있습니다.
    
#### 연차
    자신의 연차/특별휴가로 나누어 총 사용량을 퍼센트로 알수 있고, 연차 사용 기록을 볼 수 있습니다.
    
#### 우측 사이드바
    jquery를 활용하여 항상 오른쪽에서 똑같은 위치에 따라가도록 구현하였습니다.
<br>

### 결재
결재는 일반적인 결재를 최대한 구현하려고 노력했습니다.

기안자는 session에 저장된 정보를 가져오며, 참조기능으로 다른 사람을 참조시킬수 있습니다.

프로젝트 단위로 문서를 묶을수 있는 타임라인 기능을 통해 결재를 관리하기 편하게 하였습니다.
<br>

#### 결재
    결제 메인 페이지는 진행중인 결재와, 자신이 작성한 결재를 볼 수 있습니다.
    결재를 작성하게되면 타임라인과 참조를 모달창을 통해 검색 및 적용이 가능합니다.(비동기)
    파일첨부가 가능합니다.
<br>

#### 타임라인
    타임라인은 프로젝트 단위로 묶어서 결재를 관리하는 것으로 정의하였고, 
    타임라인을 관리하는 별도의 페이지를 구성하였습니다.
    타임라인을 불러오는 것은 ajax를 통해 비동기식으로 처리하였고 각 결재로 이동이 가능합니다.
<br>

### 추천
서울시 데이터 광장상의 지하철 인원정보에 따른 이용율 높은 상위 20개 역의 정보를 가져와서 

QGIS를 통해 해당 역 주변 100m, 200m, 300m 반경원을 만들고, 도로 및 건물을 제외하여 

실제로 주차가 가능한 구역을 나타냅니다.
<br>

#### 추천
    추천은 메인 기능으로서 leaflet.js를 사용하여 만들었습니다. 초기 화면은 서울 중심으로 지도가 띄워집니다.
    필터기능을 통해 서울시 지하철 역 반경 100m, 200m, 300m 내 도로및 건물을 제외한 주차가능 구역을 띄워줍니다.

<br>

## 프로젝트를 마무리하며

#### 소감 및 성취

    많은 부분을 Spring Framework가 자동으로 처리해주어 불필요한 코드의 중복이 상당히 줄어들었고, 
    의존성 주입을 통해 tiles3, spring security를 활용하게 되어 편했다.
    레거시코드에서 logback과 slf4j를 활용하고 AOP단계를 조정하여 콘솔창에 너무 많은 내용이 나오지 않게 하였다.
    JavaScript 부분에서는 leaflet.js로 마커, 화면구성, 다각형 띄우기 등을 원문 사이트를 통해 학습하여 처리했고,
    geojson으로 만들어주는 프로그램인 QGIS를 활용하여 shp파일 여러개를 하나의 geojson파일로 변경하였다.
    이 과정에서 shp 파일의 공간좌표계등의 별도의 공부가 필요했지만, 
    원래 공학을 하던 입장에서 필요한 것을 새로 배워서 적용하는것에 대한 부담이 적었다.
