# 데이터: 객관적 사실, 실제 값
# 정보: 데이터를 가공처리하여 의사결정에 활용하도록 조직한 결과물
# 생성된 정보는 정보 시스템을 통해 다른 사용자의 입력 데이터로 활용되기도 함
#
# 정보시스템
# 현실세계<->데이터->처리->정보--->업무담당자/의사결정자
#             데이터베이스
#
# 데이터베이스:데이터 종속성 문제를 공통의 데이터 모델과 표준 데이터 언어를 사용하여 해결/
#             데이터 중복성 문제를 통합 저장소를 이용하여 해결
#             데이터베이스 접근을 DBMS가 제공
# 데이터언어 SQL: 사용자와 응용 프로그램은 모두 DBMS를 통해서만 데이터베이스에 접근 가능. DBMS에 요청 내용을 전달하기 위한 도구
# Structured Query Language
#   데이터 정의어(DDL)/데이터 조작어(DML)/데이터 제어어(DCL)로 나뉨
# Data Definition Language/ Data Manipulation Language / Data Control Language

# DDL: DB구조 정의, DB객체 생성/수정/삭제
# DML: DB데이터 관리, 입력/수정/삭제/검색
# DCL: DB관리 및 통제, DB백업/복원, 사용자 등록/권한 관리


# 데이터 모델: 현실 세계의 데이터를 명세하는 고유한 표현 방식이자 데이터 모델링을 위한 도구
# 데이터 구조/연산/제약조건
#
# 관계형 데이터 모델: 테이블 형태의 릴레이션을 통해 데이터를 저장하고 데이터 간의 관련성도 표현
# 릴레이션/관계대수/무결성 제약 조건
# 릴레이션(relation):특별한 의미를 갖는 테이블
#     속성(attribute)테이블의 열, 데이터를 표현하는 가장 작은 단위, 의미적으로 더 이상 분해할 수 없는 원자값 사용
#     튜플(tuple)테이블의 각 행, 현실세계의 개체 표현, 각 속성 값들의 조합으로 구성
#     도메인(domain)각 속성이 취할 수 있는 모든 값들의 집합 정의한 것, 데이터 값들의 유형과 크기/범위를 정의
#     카디널리티(cardinality)릴레이션 안의 전체 튜플의 개수, 입력/수정/삭제 등을 통해 계속 변화,동적 특성
#     차수(degree)릴레이션을 구성하는 전체 속성의 개수, 각 튜플이 가지는 속성 값의 개수는 릴레이션의 차수와 같음, 정적 특성
# 릴레이션
# 릴레이션 스키마(schema)
#     특정 릴레이션의 논리적 구조를 의미
#     릴레이션의 이름과 릴레이션 안에 포함된 모든 속성의 이름들로 정의
#     테이블의 첫 번째 행인 헤더 부분에 표현
#     릴레이션 내포(intension)라고도 함
#     시간이 경과해도 좀처럼 변경되지 않는 정적인 특성
#     릴레이션 이름(속성이름1,속성이름2,...,속성이름n) key는 밑줄로 표시
# 릴레이션 인스턴스(instance)
#     어느 한 시점에 릴레이션에 존재하는 튜플들의 집합
#     보통 테이블의 첫 번째 행인 헤더 부분 제외한 나머지 모든 행들의 집합
#     릴레이션 외연(extension)이라고도 함
#     시간에 따라 변하는 동적인 특성
#     {< >,< >,< >}
# 데이터베이스 스키마>릴레이션 스키마
# 데이터베이스 인스턴스>릴레이션 인스턴스

#튜플
#유일성(릴레이션 안 같은 튜플 존재x)(모든 튜플은 다른 튜플과 구별되는 유일한 속성 값 있어야함)
#무순서성(순서에 의미 없다)

#속성
#무순서성(순서로 참조x 이름으로 참조o)
#원자성(다중 값 허용x 복합속성x 더 쪼갤 수 없어야 함)

#키(key)
#튜플을 식별하게 해주는 하나 이상의 속성 집합
#후보키/슈퍼키/기본키/대체키/외래키
#후보키는 유일성 & 최소성 갖출 것 슈퍼키는 유일성만
#기본키는 후보키 중 정적이고/null값 못가지고/속성 개수가 적으며/속성 값 크기가 작은 것
#대체키는 기본키 아닌 후보키들
#외래키는 기본키를 참조하는 집합

#무결성 제약 조건:데이터 일관성 & 정확성에 손상 없을 것

