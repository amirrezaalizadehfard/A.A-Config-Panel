# content_filter.py
# فیلتر محتوای بزرگسال (Adult Content Filter)
# ══════════════════════════════════════════════════════════════════════════════
# منطق ساده و سبک: قبل از باز شدن تانل TCP به مقصد، نام دامنه‌ی درخواستی
# (که از هدر VLESS استخراج می‌شه) با یک لیست از دامنه‌های شناخته‌شده و
# چند کلیدواژه‌ی رایج مقایسه می‌شه. این چک فقط روی SNI/Hostname مقصد انجام
# می‌شه (نه IP خام) و هزینه‌ی محاسباتی تقریباً صفر داره، پس روی throughput
# ریله تاثیری نمی‌ذاره.
#
# نکته: این یک فیلتر «best effort» بر پایه‌ی نام دامنه‌ست، نه یک فایروال
# در سطح DPI. برای اکثر کاربردهای خانگی/شخصی (جلوگیری از دسترسی راحت روی
# یک کانفیگ خاص) کافیه، اما تضمین ۱۰۰٪ نمی‌ده (مثلاً وقتی مقصد یک IP خام
# بدون SNI باشه قابل تشخیص نیست).
# ══════════════════════════════════════════════════════════════════════════════

import os
import re
from pathlib import Path

DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
EXTRA_BLOCKLIST_FILE = DATA_DIR / "adult_blocklist_extra.txt"

# دامنه‌های شناخته‌شده‌ی پرمخاطب (بررسی با تطبیق suffix، یعنی زیردامنه‌ها هم پوشش داده می‌شن)
KNOWN_ADULT_DOMAINS: set[str] = {
    "pornhub.com", "xvideos.com", "xnxx.com", "xhamster.com", "redtube.com",
    "youporn.com", "youjizz.com", "tube8.com", "spankbang.com", "beeg.com",
    "brazzers.com", "onlyfans.com", "chaturbate.com", "livejasmin.com",
    "cam4.com", "stripchat.com", "bongacams.com", "myfreecams.com",
    "motherless.com", "porn.com", "sex.com", "eporner.com", "hqporner.com",
    "porntrex.com", "thumbzilla.com", "txxx.com", "camsoda.com",
    "adultfriendfinder.com", "ashemaletube.com", "efukt.com", "fapdu.com",
    "hclips.com", "hentaihaven.xxx", "nhentai.net", "rule34.xxx",
    "e-hentai.org", "sankakucomplex.com", "javhd.com", "javfinder.com",
    "javlibrary.com", "missav.com", "pornone.com", "porndig.com",
    "vporn.com", "xmoviesforyou.com", "camwhores.tv", "4tube.com",
    "drtuber.com", "tnaflix.com", "xxxbunker.com", "porndoe.com",
    "chaturbate.global", "manyvids.com", "clips4sale.com", "fetlife.com",
}

# کلیدواژه‌هایی که اگر به‌صورت توکن مستقل در نام دامنه دیده بشن، مسدود می‌شن
# (توکن‌سازی با جدا کردن روی نقطه/خط‌تیره انجام می‌شه، پس مثلاً "sextant.com"
# به اشتباه مسدود نمی‌شه چون توکنش "sextant" هست نه "sex")
ADULT_KEYWORDS: set[str] = {
    "porn", "porno", "pornhub", "xxx", "xvideos", "xnxx", "xhamster",
    "hentai", "nsfw", "camgirl", "camgirls", "sextube", "fuckbook",
    "brazzers", "chaturbate", "livejasmin", "redtube", "youporn",
    "spankbang", "onlyfans", "javhd", "adultfriendfinder", "escort",
    "camwhores", "fapdu", "javfinder",
}

_TOKEN_RE = re.compile(r"[a-z0-9]+")
_IP_RE = re.compile(r"^[\d.]+$")

_extra_domains: set[str] = set()


def _load_extra() -> None:
    """لیست تکمیلی دامنه‌های مسدود که خودِ ادمین می‌تونه در
    /data/adult_blocklist_extra.txt (هر دامنه در یک خط) اضافه کنه."""
    global _extra_domains
    try:
        if EXTRA_BLOCKLIST_FILE.exists():
            lines = EXTRA_BLOCKLIST_FILE.read_text(encoding="utf-8").splitlines()
            _extra_domains = {
                ln.strip().lower() for ln in lines
                if ln.strip() and not ln.strip().startswith("#")
            }
    except Exception:
        _extra_domains = set()


_load_extra()


def reload_extra_blocklist() -> int:
    """رفرش دستی لیست تکمیلی (مثلاً بعد از ویرایش فایل از پنل). تعداد آیتم‌ها رو برمی‌گردونه."""
    _load_extra()
    return len(_extra_domains)


def _suffix_match(host: str, domains: set[str]) -> bool:
    for d in domains:
        if host == d or host.endswith("." + d):
            return True
    return False


def is_adult_domain(host: str | None) -> bool:
    """بررسی می‌کنه آیا دامنه‌ی مقصد مربوط به محتوای بزرگسال شناخته‌شده است."""
    if not host:
        return False
    host_l = host.strip().lower().rstrip(".")
    if not host_l:
        return False
    # روی IP خام (بدون نام دامنه) نمی‌شه بر اساس اسم چک کرد؛ از فیلتر رد می‌شه.
    if _IP_RE.match(host_l) or ":" in host_l:
        return False
    if _suffix_match(host_l, KNOWN_ADULT_DOMAINS):
        return True
    if _extra_domains and _suffix_match(host_l, _extra_domains):
        return True
    tokens = set(_TOKEN_RE.findall(host_l))
    if tokens & ADULT_KEYWORDS:
        return True
    return False
