#장고는 모델을 사용하여 DB처리 수행
#즉, SQL쿼리문을 사용하지 않고도 처리 가능


#점프 투 장고
#파이썬 설치 시 반드시 add to path 체크하기
#안하면 고급시스템 설정에 들어가 환경변수, path에서 직접 경로를 추가해주어야 한다.

#파이썬 가상 환경 설정하기
#1.명령프롬프트cmd 접속
#2.cd \(상위 디렉토리로 이동)> mkdir venvs(디렉토리 생성) > cd venvs(생성한 디렉토리로 이동)
#3.python -m venv 가상환경이름(가상환경 생성)
#4.cd \venvs\가상환경이름\Scripts (가상환경 진입)
#5.activate (가상환경 활성화)

#가상환경에 장고 설치
#가상환경 활성화 상태에서
#pip install django==3.1.3 입력(경고 메시지 출력)
#python -m pip install --upgrade pip (최신 버전 pip설치)

#프로젝트 디렉터리 생성하기
#1.cd\ (가장 상위로 이동)>mkdir projects (프로젝트 디렉토리 생성)>cd projects(생성한 디렉토리로 이동)
#2.C:\venvs\가상환경이름\Scripts\activate
#3.mkdir mysite(앞서 생성한 가상환경과 이름은 같으나, 장고 프로젝트를 담을 하위 디렉토리다)
#4.cd mysite
#5.django-admin startproject config .(장고 프로젝트 생성)
#6.python manage.py runserver 명령어로 개발 서버 구동
#개발 서버 종료하려면 컨트롤 씨
#127.0.0.1:8000으로 접속 혹은 localhost:8000

#파이참과 연결하기
#파이참 프로젝트 생성하고
#file->settings-->python interpreter에서 add를 눌러 mysite안에 들어있는 python exe구동
#setting.py에서 laguage code를 ko-kr로, time_zone을 Asia/Seoul로 수정한다
#>> 장고 연결 화면이 한글로 바뀌어 뜬다

#예시
#질문/답변을 수행하는 기능 구현
#SQL
#질문 모델이 가져야 할 속성: 제목(subject)/ 내용(content)/ 작성일시(create_date) 등
#답변 모델이 가져야 할 속성: 제목(question)/답변내용(content)/ 답변 작성일시(create_date)

#질문/답변 모델을 pybo/models.py로 정의


#관리자 모드
