#インストールしたモジュールをインポートする
import streamlit as st
import requests

#APIキーの入力

#チャットのやり取りを記録するリスト定義する
chat_logs = []
#Webアプリのタイトル
st.title("チャットボット")
#subheader関数でヘッダーにテキストを表示する
st.subheader("メッセージを入力してから送信をタップしてください")
#text_input関数でテキスト入力ウィンドウを設置する
message = st.text_input("メッセージ")

#send_pya3rt関数でチャットボットAPIを呼び出す
#APIキーとWebアプリ上で受け取るテキストをパラメーターとしてAPIに送信し、レスポンスとして返答文を受けとる
def send_pya3rt(endpoint, apikey, text, callback):
    params = {'apikey': apikey,
              'query': text,
             }
    if callback is not None:
        params['callback'] = callback

    response = requests.post(endpoint, params)

    return response.json()

#ボタンが押されたときに呼び出される関数を定義する
def generate_response():
    #send_pya3rt関数で入力されたwテキストとAPIキーを送信し、レスポンスをJson形式で受け取る
    ans_json = send_pya3rt('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
                       apikey, message, None)
    #返信文を取り出し送信文と返信文をchat_logsリストに追加する
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        #write関数でWebアプリ画面に表示させる
        st.write(chat_log)

#テキスト送信ボタンをbutton関数で設置する
#ボタンが押されたときにのみ実行する
if st.button("送信"):
    generate_response()