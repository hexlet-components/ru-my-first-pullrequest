from collections import Counter
from pathlib import Path
import subprocess

PATTERNS = {
    "hello / привет": ("hello", "privet", "привет", "hola", "hi"),
    "first / первый": ("first", "1st", "первый", "ферст"),
    "test / тест": ("test", "тест", "proba", "проба"),
    "hexlet": ("hexlet", "хекслет"),
    "мемы": ("1337", "42", "cat", "кот", "bababui"),
}


def human_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}"
        n /= 1024


def bar(part, total, width=20):
    filled = round(width * part / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def commits_count(root):
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-list", "--count", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None


def main():
    root = next(
        (p for p in Path(__file__).resolve().parents if (p / ".git").exists()),
        Path.cwd(),
    )

    files = []
    exts = Counter()
    folklore = Counter()
    dirs = 0
    total_size = 0

    for p in root.rglob("*"):
        if ".git" in p.parts:
            continue
        if p.is_dir():
            dirs += 1
            continue
        if not p.is_file():
            continue

        size = p.stat().st_size
        rel = p.relative_to(root)
        total_size += size
        files.append((size, rel))
        exts[p.suffix.lower() or "<no ext>"] += 1

        name = str(rel).lower()
        for label, words in PATTERNS.items():
            if any(w in name for w in words):
                folklore[label] += 1

    total = len(files)
    commits = commits_count(root)

    print(f"\n=== {root.name} ===")
    summary = f"Папок: {dirs} | Файлов: {total} | Размер: {human_size(total_size)}"
    if commits:
        summary += f" | Коммитов: {commits}"
    print(summary)

    print("\nТоп расширений:")
    for ext, count in exts.most_common(8):
        pct = count / total * 100 if total else 0
        print(f"  {ext:<12} {bar(count, total)} {count:>5} ({pct:4.1f}%)")

    print("\nФольклор в названиях:")
    for label in PATTERNS:
        count = folklore[label]
        print(f"  {label:<20} {bar(count, total)} {count:>5}")

    print("\nСамые тяжёлые файлы:")
    for size, rel in sorted(files, reverse=True)[:5]:
        print(f"  {human_size(size):>9}  {rel}")
    print()


if __name__ == "__main__":
    main()
