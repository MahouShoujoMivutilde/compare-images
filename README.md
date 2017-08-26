## ssim.py

Крохотный скрипт для получения ssim двух изображений с помощью `ffmpeg`.

Написан ввиду нежелания автора устанавливать махину scikit-image со всеми её зависимостями ради одной столь банальной функции.

#### Требования
* `python 3.4+ `
* `ffmpeg` в `PATH`

#### Использование
```
> ssim.py -ref source.png -c modified.jpg
SSIM: 0.975639
```
или
```
from ssim import get_ssim

ref = r'path\to\my\ref.png'
cmp = r'path\to\modified\image.jpg'

ssim_value = get_ssim(ref, cmp)
```