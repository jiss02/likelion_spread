  <h3 align="center">2019 1학기 멋쟁이 사자처럼 블로그 프로젝트</h3>
  <p align="center">
    블로그, 사진첩, 댓글 CRUD 기능 구현하기 <br/>
  </p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [Details](#details) 
  * [Deploy](#deploy)
  * [Links](#links)
  * [Demo](#demo)
 * [Contanct](#contact)

&nbsp;
<!-- ABOUT THE PROJECT -->

## About The Project

<div align="center">
<br/>
멋쟁이 사자처럼 2019년도 1학기 마지막 과제 <br/>
    <b>간단한 블로그 프로젝트를 만들어보자</b>
</div>


&nbsp;
### Built With

* Python Django
* HTML5 + CSS3
* SQLite3

&nbsp;
<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

* virtualenv
```bash
$ python -m venv venv
$ . venv/Scripts/activate
```

* Django
```bash
$ pip install django
```


&nbsp;
### Requirements
```
dj-database-url==0.5.0
Django==2.1.8
django-bootstrap4==0.0.8
gunicorn==19.9.0
Pillow==6.0.0
psycopg2-binary==2.8.2
pytz==2019.1
whitenoise==4.1.2
```
&nbsp;
### Installation

1. Clone the repo
```sh
$ git clone https://github.com/jiss02/Django-Blog-Project.git
```
2. Migrate Database
```sh
$ python manage.py migrate
```
4. Run server
```
$ python manage.py runserver
```
&nbsp;
## Details 

### Deploy
* Heroku
&nbsp;
### Links
* Project Link: https://github.com/jiss02/Django-Blog-Project.git
* Website Link: [https://firstspread.herokuapp.com](https://firstspread.herokuapp.com)
&nbsp;
### Demo
<div align="center">
  
| main page |
| :---: |
| <img width="800" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70205225-b9d3f400-1766-11ea-9484-84668cf06d21.png"> |
| detail | 
| <img width="800" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70205226-ba6c8a80-1766-11ea-98b1-a9445104f3b0.png"> | 
| photo write | 
| <img width="800" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70205227-ba6c8a80-1766-11ea-83a5-663690d8e7d6.png"> | 
| diary write | 
| <img width="800" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70205228-ba6c8a80-1766-11ea-931c-7ce3be36fb95.png"> | 
 

</div>


