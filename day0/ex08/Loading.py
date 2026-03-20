import os


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """

    if not lst or len(lst) == 0:
        print("0it [00:00, ?it/s]")
        return
    total = len(lst)
    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80

    min_bar = 3
    start = os.times().elapsed

    for i, item in enumerate(lst, 1):
        elapsed = os.times().elapsed - start
        rate = i / elapsed if elapsed > 0 else 0.0
        remaining = (total - i) / rate if rate > 0 else 0.0

        percent = int(i * 100 / total)

        elapsed_str = f"{int(elapsed//60):02d}:{int(elapsed%60):02d}"
        remain_str = f"{int(remaining//60):02d}:{int(remaining%60):02d}"

        left = f"\r{percent:3d}%|"
        right = f"| {i}/{total} [{elapsed_str}<{remain_str}, {rate:6.2f}it/s]"

        bar_width = term_width - (len(left) + len(right) - 1)
        if bar_width < min_bar:
            bar_width = min_bar

        filled = int(bar_width * i / total)
        bar = "█" * filled + " " * (bar_width - filled)

        print(left + bar + right, end="", flush=True)
        yield item
