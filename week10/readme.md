# Flask 기반 웹 프로젝트 (EC2 + Docker, 또는 로컬)
이 저장소는 Flask 기반 웹 프로젝트의 소개 페이지와 API를 제공합니다.

---

## 1. 작품주제(Subject)
-  제목:  데스크톱 음성채팅 애플리케이션
-  요약:  서로 다른 사용자와 통화 및 채팅

---

## 2. 실용적 근거(Rationale)
-   전세계 게이머 증가
-   게이밍·커뮤니티 사용자 증가, 관심사 기반 커뮤니티 형성
   기대 가치:  쉬운 의사소통

---

## 3. 핵심기능(Features)
- 기능 1:  음성 및 통화 기능
- 기능 2:  친구 기능
- 기능 3:  통화방 만들기

---

## 4. 구현환경(Environment)
- Front-End (프론트엔드):  Electron, React
- Back-End (백엔드): Node.js
- Database (데이터베이스):  PostgreSQL
- Runtime (런타임): Render

---

## 5. 팀원 구성 및 역할(Team)
| 이름 | 역할 |
|------|------|
| 류영현 | 백엔드 |
| 정종하 | 백엔드 |
| 김병수 | 프론트엔드 |

---

## 6. 실행 방법(Run)

```bash
# 1. Docker 이미지 빌드 및 실행
sudo docker build -t week11 .
sudo docker run -d -p 5000:80 week11

# 2. 웹 접속
http://localhost:5000
