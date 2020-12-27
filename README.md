# 我的家

## 前言
越來越接近新年了，各樣的親戚都有各自的稱謂，是否很怕叫做稱呼，不知道該如何稱呼眼前的親戚？使用此line bot 以便利的方式瞭解親戚的稱呼

## 構想
主要提供三樣功能，第一是按照一等親以内（包括父親、母親、哥哥、弟弟、姊姊、妹妹、男兒（即兒子）、女兒、丈夫、妻子）的親戚關係，以問答的方式給與該親戚的稱呼、自稱等資訊，二是以查詢的方式，科普該分類下的稱呼。第三則是建立資料庫，記錄親戚的名字和稱呼。

## 環境
- Windows 10
- python 3.7.6

# 技術
- postgresql
    - Heroku-Postgres: 數據庫

## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 從`.env.sample`產生出一個`.env`，並填入以下四個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN

4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```

## 使用說明
- 基本操作
    - 所有用到英文的指令大小寫皆可
    - 隨時輸入任何字若沒觸發到都會有提示
    - 謹一個指令皆可隨時輸入
        - `結束`
            - 重新開始
- 架構圖
    1. 輸入`請告訴我`開始問答
        a. 輸入要查詢的親戚 -> `<一等親>`的`<小分類>`
        b. 不清楚可供查詢的一等親有哪些可輸入`一等親`
        c. 不清楚某一等親下有哪些可查詢的親戚可先輸入`<一等親>的`,如`父親的`
        d.若輸入成功，將會提供欲查詢之親戚的*尊稱*、*自稱*、*對他人稱其家族中人*、*對他人稱自己家族中人*四類資訊
    2. 輸入`尊稱`開始查詢科普
        a. 輸入後會開始有選擇引導使用者到欲查詢對象的分類列表，下面以列表方式列出：
        - `長輩`
            - `祖輩`
            - `父母`
                - `父母`
                - `父母的親戚`
        - `同輩`
            - `兄弟姊妹`
                - `兄弟`
                - `姊妹`
            - `夫妻`    
                - `夫妻`
                - `夫妻的親戚`
        - `晚輩`（即子女）
    
    b. 到了最終分類後，點選或輸入`列表`會列出可查詢的親戚稱呼，輸入正確的話會回復該稱呼的科普
    
    c. 隨時輸入`回上一層`以回到上一層狀態

    3. 輸入`登記`開始記錄親戚的名字與稱呼
        
        a. 輸入後可以輸入四種指令
        
        - `存入`：以“<名字><空格><稱呼>”的格式記錄親戚的資訊     
        - `查詢`：提供三種查詢方式，提供該方式所需要的資訊以查詢資料庫裏的親戚資訊
            
            - `名字` 
            - `稱呼`
            - `全部`
        - `更新`：提供兩種查詢方式（即名字或稱呼），符合要求的親戚資料可以更改其名字或稱呼
        - `刪除`：提供兩種查詢方式（即名字或稱呼），符合要求的親戚資料可以刪除其名字或稱呼，又或者直接輸入`全部`以刪除所有資料也是可以的        

## 使用示範
### `請告訴我`
![](https://i.imgur.com/EOFlNvM.png)
![](https://i.imgur.com/83nWKt7.png)
![](https://i.imgur.com/gIPUlED.png)
### 尊稱
![](https://i.imgur.com/PAhe99o.jpg)
![](https://i.imgur.com/YYbevfS.png)
![](https://i.imgur.com/6z9Jqev.png)
![](https://i.imgur.com/0fCwe4V.png)
![](https://i.imgur.com/6mVHgXG.png)
![](https://i.imgur.com/bEC1Uz2.png)
### 登記
![](https://i.imgur.com/pS6uWLH.png)
![](https://i.imgur.com/rH6p1Ob.png)
![](https://i.imgur.com/7ttFFWR.png)
![](https://i.imgur.com/n9wTMwp.png)
![](https://i.imgur.com/RKdil3L.png)

### FSM
![](https://i.imgur.com/T8D6y5G.png)

## FSM
![](https://i.imgur.com/1zgGqaR.jpg)




### state說明
- user: 輸入`請告訴我`使用詢問功能；`尊稱`使用查詢功能；`fsm`回復fsm的圖檔
- question: 輸入`<一等親>的<親戚>`來查詢
- qing: 回復親戚的稱呼等資訊
- qing_list: 回復可查詢的一等親列表 
- honor: 選擇尊稱-分類1
- honor_e: 選擇尊稱-長輩
- honor_g: 選擇尊稱-祖輩
- honor_g_list: 回復祖輩中可提供查詢的列表
- honor_pa: 選擇尊稱-父母
- honor_par: 選擇尊稱-父母的親戚
- honor_par_list: 回復父母的親戚中可提供查詢的列表
- honor_panr: 選擇尊稱-父母
- honor_panr_list: 回復父母中可提供查詢的列表
- honor_pp: 選擇尊稱-同輩
- honor_s: 選擇尊稱-兄弟姊妹
- honor_bro: 選擇尊稱-兄弟
- honor_bro_list: 回復兄弟中可提供查詢的列表
- honor_sis: 選擇尊稱-姊妹
- honor_sis_list: 回復姊妹中可提供查詢的列表
- honor_mc: 選擇尊稱-夫妻
- honor_mcr: 選擇尊稱-夫妻的親戚
- honor_mcr_list: 回復夫妻的親戚中可提供查詢的列表
- honor_mcnr: 選擇尊稱-夫妻
- honor_mcnr_list: 回復夫妻中可提供查詢的列表
- honor_ch: 選擇尊稱-晚輩
- honor_ch_list: 回復晚輩中可提供查詢的列表
- fsm: 畫出fsm圖
- log: 進入記錄親戚資訊功能
- log_name: 輸入需記錄的親戚的資訊
- log_ins_pro: 將親戚資訊存入資料庫
- log_select: 選擇查詢的方法
- log_sel: 根據上一層選擇的方法（名字或稱呼）提供查詢内容
- log_sel_pro: 處理查詢要求
- log_sel_all_pro: 列出所有資料庫所含有的資料
- log_update: 選擇更新資料的指定方法
- log_upd: 輸入需更新資料的指定内容
- log_upd_col: 輸入需更新資料的更新欄位（名字或稱呼）
- log_upd_key: 輸入需更新資料的更新内容
- log_upd_pro: 處理更新要求
- log_delete: 選擇欲刪除資料的指定方法
- log_del: 輸入欲刪除資料的指定内容
- log_del_pro: 處理刪除指令
- log_del_all_pro: 刪除資料庫中所有的資料

## Deploy in Heroku
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
    heroku config:set APP_KEY=your_olami_APP_KEY
    heroku config:set APP_SECRET=your_olami_APP_SECRET
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```
