# Cloning_toolkit

## Requirements:
- python3.6 
    - PyQt5 
## Usage (Mac) :
1. Miniconda3をインストールする。https://conda.io/miniconda.html  
   このサイト内のMac OS X, Python3.6, 64-bitの物をダウンロード
2. Miniconda3のインストールを行う。ターミナルを開き以下を入力する。（"$"は入力する必要なし）  
   $ cd Downloads  
   $ sudo ./Miniconda3-latest-MacOSX-x86_64.sh 
   パスワード（ログインするときと同じものを入力。文字を打っても何も出ないが、実際は入力されている。エンターキーを押して入力)
   エンターキーを長押し
   指示に従ってインストールを行う。途中Miniconda3をPathに追加するかどうかと聞かれるところをyesにする。
3. ターミナルを再起動して、
   $ which python 
   /Users/owner/miniconda3/bin/python3　のように返されることを確認
4. $ sudo pip install pyqt5
5. Cloning_toolkitをGithibからダウンロード。"cd ダウンロードした場所"でCloning_toolkitをダウンロードした場所へ移動。以下例  
   $ cd Downloads/Cloning_toolkit-master/CloningPy/
6. $ python CloningPy_developing.py  
   これで立ち上がるかどうか確認。
7. $ cd 
8. $ 
   
   
   
2. $ /usr/bin/python3 Cloning_developing.py

## Usage (Windows10) :
1. まずpython3.6.6をダウンロード。https://www.python.org/downloads/release/python-366/  
   画面下のほうにあるWindows x86-64 executable installerをダウンロード  
2. python3.6.6をインストールする。ダウンロードしたファイルをクリックしてインストールを進める。  
   途中PythonをPathに追加しますか？というチェックボックスがあるので、そこをチェックしてインストールを進める。  
3. python3.6.6がインストールされたかを確認する。コマンドプロンプトにて  
   python  
   と入力して、インストールされているかを確認  
   quit()  
   でpythonから抜ける。  
4. PyQt5をダウンロードする。コマンドプロンプトにて  
   python -m pip install --trusted-host files.pythonhosted.org pyqt5  
   と入力してSuccessfully installed pyqt5 と出るのを確認する。  
5. GitからCloning_toolkitをダウンロードしてzipを解凍する。  
6. コマンドプロンプトを開き、ダウンロードした場所に"cd ディレクトリのパス"で移動する 以下例  
   cd C:\Users\DAIYA OHARA\Desktop\CloningPy  
7. コマンドプロンプトにて以下で起動。  
   python CloningPy_developing.py  
   

## Result : 
3000bp,100ng/ulのVector及び800bp,30ng/ulのInsert（ゲル抽出産物)をライゲーションするとする。  
最終的なDNA混合物のvolumeを7.5ulとしたとき、Vector:Insertのモル比が1:8になるようにするにはそれぞれを何ul入れればよいかを計算。  
  
![CloningPy Ligation example](https://user-images.githubusercontent.com/28255294/42268856-8c6f4796-7fb7-11e8-8cf8-2db9aede4af1.PNG)
