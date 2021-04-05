N = int(raw_input())
for _ in range(N):
    line = raw_input().strip()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', line, re.I)]
    for code in codes:
        print code