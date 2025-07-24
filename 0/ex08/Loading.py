import sys
import time

def ft_tqdm(lst: range):
    total = len(lst)

    for i, item in enumerate(lst, 1):
        # Progress bar
        progress = int(50 * i / total)
        bar = '=' * progress + '>' + '.' * (49 - progress)
        percent = int(100 * i / total)

        sys.stdout.write(f'\r{percent}%|[{bar}] {i}/{total}')
        sys.stdout.flush()
        yield item
    print()  # Newline after completion
