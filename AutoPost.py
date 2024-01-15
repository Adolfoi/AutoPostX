import pyautogui
import pyperclip
import random
import time

# texts.txtから文章を読み込み、セミコロンで区切ってリストに格納
with open("texts.txt", "r", encoding="utf-8") as file:
    sentences = file.read().split(';')

def main():
    while True:
        # 1分待機
        time.sleep(10)

        # 文章をランダムに選択して、リストから削除
        sentence = random.choice(sentences)
        sentences.remove(sentence)

        # ブラウザの操作（ポストボタンのアクティブ化とクリック）
        pyautogui.click(400, 840)

        # 2秒から3秒の間でランダムな待機時間を生成
        wait_time = random.randint(1, 2)
        time.sleep(wait_time)

        # クリップボードに文章をセット
        pyperclip.copy(sentence)
        time.sleep(wait_time)

        # ブラウザの操作（投稿ウィンドウをアクティブ化）
        pyautogui.click(900, 310)
        time.sleep(wait_time)

        # ペースト操作（Macの場合）
        pyautogui.hotkey('command', 'v')
        print(sentence)
        time.sleep(wait_time)

        # ブラウザの操作（ポスト投稿）
        pyautogui.click(1170, 350)

        # リストから文章がなくなったら終了
        if not sentences:
            print("すべての文章が使用されました。")
            break

if __name__ == "__main__":
    main()
