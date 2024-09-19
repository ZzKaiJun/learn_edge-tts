import edge_tts
import asyncio

## edge-tts --list-voices  配音員列表

# zh-CN-XiaoxiaoNeural           甜女
# zh-CN-XiaoyiNeural             甜女2
# zh-CN-YunjianNeural            成男
# zh-CN-YunxiNeural              注意看這個男人
# zh-CN-YunxiaNeural             小孩
# zh-CN-YunyangNeural            男
# zh-CN-liaoning-XiaobeiNeural   女
# zh-CN-shaanxi-XiaoniNeural     female?

# zh-TW-HsiaoChenNeural    山道猴女友
# zh-TW-HsiaoYuNeural      媽媽
# zh-TW-YunJheNeural       山道猴

TEXT = "我這裡有塊麵包，我還不餓，來!請你們吃"
VOICE = "zh-TW-HsiaoChenNeural"
OUTPUT_FILE="test.mp3"

async def amain() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

asyncio.run(amain())