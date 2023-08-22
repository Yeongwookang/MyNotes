## 웹스크래퍼 만들기
Selenium 4.11.2 버전을 import 하여 채용사이트인 indeed를 scrapping 하는 프로젝트를 진행했습니다.

개발기간은 23.08.22 하루입니다.

#### 개발 환경 세팅

    처음에는 replit으로 개발을 진행했는데, replit은 파이썬 3.10을 사용하고 패키지 설치 및 설정이 힘들어서,
    VSCode로 pip 버전을 맞춰서 개발을 진행했습니다.
    Chrome driver는 매번 맞춰서 파일을 넣기가 어려울것 같아서 크롬을 최신업데이트 하고 
    pypi에 있는 webdriver-manager 모듈을 활용하여 자동 최신화하게 했습니다.

#### Selenium

    replit으로 할때는 beautifulsoup를 이용해서 하다가 Selenium의 메소드들을 새로 알아야 했습니다.
    https://www.selenium.dev/documentation/ 공식문서를 참조하면서 해결했습니다.
    
    
