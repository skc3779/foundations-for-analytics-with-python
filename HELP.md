파이션 학습
=====================  

파이션 도큐먼트 : https://docs.python.org/ko/3/index.html    
자습서 : https://docs.python.org/ko/3/tutorial/index.html      

파이션 설치
=====================  

```shell
# pip 업그레이드 가상 환경에서 pip를 최신 버전으로 업그레이드
python -m pip install --upgrade pip

# 패키지 재설치 pip를 사용하여 requirements.txt에 있는 모든 패키지를 강제로 재설치
pip install -r requirements.txt --force-reinstall

# 캐시 제거 pip 캐시를 제거한 후 패키지를 다시 설치
pip cache purge
pip install -r requirements.txt
```