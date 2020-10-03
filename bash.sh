# python3 설치
sudo apt-get install python3
sudo apt-get install python3-pip
pip install --upgrade pip

# 크롤러 패키지 설치
pip3 install -r requirements.txt

# tmux, htop, wget 설치
sudo apt-get install tmux
sudo apt-get install htop
sudo apt-get install wget

# 크롬 드라이버 종속파일 설치
sudo apt-get install -y gconf-service libappindicator3-1 libgbm1 libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# 크롬 드라이버 다운로드
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# 크롬 드라이버 추가 종속성 설치
sudo apt --fix-broken install

# 크롬드라이버 설치
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -fy install