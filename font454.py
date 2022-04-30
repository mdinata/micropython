from micropython import const
import time


_FONT = (
    b'{{{{{{wws{w{HY{{{{YDYDY{sUtGU{H[wyH{uHgHE{ws{{{{vyxyv{g[K[g{{]f]{{{wDw{{'
    b'{{{wy{{{D{{{{{{{w{K_w}x{VHHHe{wuwww{`KfyD{UKgKU{w}HDK{DxTKT{VxUHU{D[wyx{'
    b'UHfHU{UHEKe{{w{w{{{w{wy{KwxwK{{D{D{{xwKwx{eKg{w{VIHyB{fYH@H{dHdHd{FyxyF{'
    b'`XHX`{DxtxD{Dxtxx{FyxIF{HHDHH{wwwww{KKKHU{HXpXH{xxxxD{Y@DLH{IL@LX{fYHYf{'
    b'`HH`x{fYHIF{`HH`H{UxUKU{Dwwww{HHHIR{HHH]w{HHLD@{HYsYH{HYbww{D[wyD{txxxt{'
    b'x}w_K{GKKKG{wLY{{{{{{{{Dxs{{{{{BIIB{x`XX`{{ByyB{KBIIB{{WIpF{OwUwww{`YB[`'
    b'x`XHH{w{vwC{K{OKHUxHpXH{vwws_{{dD@H{{`XHH{{fYYf{{`XX`x{bYIBK{Ipxx{{B}_d{'
    b'wUws_{{HHIV{{HH]s{{HLD@{{HbbH{{HHV[a{D_}D{Cw|wC{wwwwwwpwOwp{uxfKW{@YYY@{'
)
_SALT = const(132)


def text(buffer, string, x0=0, y0=0, color=0xffff, bgcolor=0, colors=None):
    font = memoryview(_FONT)
    if colors is None:
        colors = (color, color, bgcolor, bgcolor)
    x = x0
    for c in string:
        if c == '\n':
            y0 += 6
            x = x0
            continue
        index = min(95, ord(c) - 0x20)
        if index < 0:
            continue
        row = y0
        index *= 6
        for byte in font[index:index + 6]:
            unsalted = byte ^ _SALT
            for col in range(x, x + 4):
                color = colors[unsalted & 0x03]
                if color is not None:
                    buffer.pixel(col, row, color)
                unsalted >>= 2
            row += 1
        x += 4
        
def scroll_left(buffer,string,delay=0.05):
    for c in range(len(string)*4):
        buffer.fill(0)
        text(buffer,string,-c,0)
        buffer.show()
        time.sleep(delay)
