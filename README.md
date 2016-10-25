# Solitaire UTF-8
支持UTF-8版的卡牌加密算法

# 例子
```python
instance = solitaire_utf8()
deck = [30, 35, 16, 47, 49, 43, 25, 8, 17, 50, 22, 36, 51, 32, 52, 27, 2, 48, 1, 37, 29, 42, 23, 38, 4, 41, 44, 34, 9, 14, 26, 5, 15, 13, 46, 31, 40, 18, 45, 28, 12, 33, 19, 7, 11, 3, 21, 10, 39, 20, 24, 6]

instance.init_deck(deck)
instance.init_joker(51,52)

encrypted_jp = instance.encrypt("作品の制作過程は、大きく分けると3つの工程に別れている。")
encrypted_cn = instance.encrypt("汉语，又称中国语（日本、韩国等），其他名称有汉文、中文、华文、唐文（书写）、唐话、中国话（语言）等[注 1]，是属汉藏语系的分析语，具有声调。")
decrypted_jp = instance.decrypt(encrypted_jp)
decrypted_cn = instance.decrypt(encrypted_cn)
```

加密卡牌组合（密码）：
```python
[30, 35, 16, 47, 49, 43, 25, 8, 17, 50, 22, 36, 51, 32, 52, 27, 2, 48, 1, 37, 29, 42, 23, 38, 4, 41, 44, 34, 9, 14, 26, 5, 15, 13, 46, 31, 40, 18, 45, 28, 12, 33, 19, 7, 11, 3, 21, 10, 39, 20, 24, 6]
```
日文原句：
```
作品の制作過程は、大きく分けると3つの工程に別れている。
```
中文原句：
```
汉语，又称中国语（日本、韩国等），其他名称有汉文、中文、华文、唐文（书写）、唐话、中国话（语言）等[注 1]，是属汉藏语系的分析语，具有声调。
```
日文加密后：
```
F22E197B158AED0E6F0AA5524A70B06B254B30C38836BE00C7E2D8609A6604164B860A3817F7A4E9CB8840BB209325AB5AB5DCAFF17441A06FE5CCA13E5A949475CF193F344D85EEF99EBD33B0DE91B28E13
```
中文加密后：
```
F422067E21A6E9394D0AAC244D6AD4665C6A3EB6BA3BDC0EC31EDF618D6407216A86093A1B0EC7EBD5A444D62E9F508C068ED7E093A987764E2575869A1EC3DF2CC05A0D3BA738E4363BBD9385F9FC65857426A5A308CCB6E4CC7A3785EBFEBADA60F063047FEB8559B9221CD48282C4F275A9003200A7B5E5F5941A6CCDBB01397BEA5ECEBCFB1E31CCEBE9F008FC29C9DD5F6E6251E041D59C101A6D38FA3C608C626A3969E4C378C40DE89C7DC6C20E9BD5E302A7BACA821086DB24A6E6A7DDF2165E1F259CE7192B0DBEB0
```
