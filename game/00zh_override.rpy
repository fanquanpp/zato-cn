## Z.A.T.O. 汉化补丁 - 字体与字号覆盖
## 原版使用 cour.ttf（Courier），不含中文字形。
## 中文界面改用思源黑体（Source Han Sans，SIL OFL 开源协议），
## 随补丁分发于 game/tl/chinese/fonts/ 目录。
##
## 本文件必须在 init -1 优先级、且按文件名排序位于 screens.rpy 之前执行，
## 确保 screens.rpy 中的 style 语句构建样式时读取到覆盖后的 gui 变量。
## 注意 gui.button_text_font / gui.choice_button_text_font 等是 define 时的值拷贝，
## 需要一并覆盖。

init -1 python:
    _ZH_FONT = "tl/chinese/fonts/SourceHanSansLite.ttf"

    ## 思源黑体精简版不含西里尔字母（片尾致谢与隐藏讯息中的俄文），
    ## 用 FontGroup 把西里尔区间回退到 Ren'Py 内置的 DejaVuSans。
    def _zh_build_font():
        g = renpy.text.font.FontGroup()
        g.add(_ZH_FONT, None, None)
        g.add("DejaVuSans.ttf", 0x0400, 0x052F)
        g.add("DejaVuSans.ttf", 0x1C80, 0x1C8F)
        return g

    gui.text_font = _zh_build_font()
    gui.name_text_font = gui.text_font
    gui.interface_text_font = gui.text_font
    gui.button_text_font = gui.text_font
    gui.choice_button_text_font = gui.text_font

    ## 中文字号相对英文等宽字体略作调整，保证阅读舒适度
    gui.text_size = 24
    gui.name_text_size = 28
    gui.interface_text_size = 23
    gui.label_text_size = 25
    gui.button_text_size = 23
    gui.choice_button_text_size = 24

    del _ZH_FONT
    del _zh_build_font
